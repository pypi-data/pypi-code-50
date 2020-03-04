import functools
import inspect
import sys

from scrybe.internal.depgraph.nodes import DatasetTrackingNode
from scrybe.internal.depgraph.ops import Operations
from scrybe.internal.depgraph.tracking_graph import TrackingGraph
from scrybe.internal.tracker.data.instrumentation.import_interceptor import ModulePatcher
from scrybe.internal.tracker.data.utils import safe_extract_name_and_path, skip_tracking, \
    set_dataset_info
from scrybe.internal.util import get_module_name, get_func_arg_names, get_func_req_params


def pandas_constructor_wrapper(predecessor, cls, *args, **kwargs):
    self = cls(*args, **kwargs)
    op = Operations.TRANSFORM
    # FIXME(msachdev): What happens if self.values is predecessor.values ?
    if self.index is predecessor.index:
        # FIXME(msachdev): This is too restrictive and misses some cases -- fix it
        if hasattr(self, 'columns') and hasattr(predecessor, 'columns') and self.columns is predecessor.columns:
            op = Operations.VIEW
        else:
            op = Operations.COLUMN_SELECT
    elif hasattr(self, 'columns') and hasattr(predecessor, 'columns') and self.columns is predecessor.columns:
        op = Operations.ROW_FILTER
    predecessor_node = TrackingGraph.get_node_for_tracked_object(obj=predecessor)
    self_node = TrackingGraph.get_node_for_tracked_object(obj=self)
    self_node.add_predecessor(predecessor_node=predecessor_node, operations={op})
    return self


def get_contructor_partial_func(self_obj, module_cls, methods):
    partial_func = functools.partial(pandas_constructor_wrapper, self_obj, module_cls)
    for class_method in methods:
        method = getattr(module_cls, class_method)
        setattr(partial_func, class_method, method)
    return partial_func


def handle_finalize(out, other):
    objs = getattr(other, 'objs', list())

    if TrackingGraph.has_tracked_obj(obj=other):
        objs.append(other)
    if hasattr(other, 'left'):
        objs.append(other.left)
    if hasattr(other, 'right'):
        objs.append(other.right)

    for obj in objs:
        if obj is out:
            continue
        if TrackingGraph.has_tracked_obj(obj=obj):
            out_node = TrackingGraph.get_node_for_tracked_object(obj=out)
            obj_node = TrackingGraph.get_node_for_tracked_object(obj=obj)
            out_node.add_predecessor(predecessor_node=obj_node, operations={Operations.TRANSFORM})


def handle_indexers(result_obj, indexer_args):
    # The output can be a scalar or something else -- need to check if it exists in our graph
    if TrackingGraph.has_tracked_obj(obj=result_obj):
        out_node = TrackingGraph.get_node_for_tracked_object(obj=result_obj)
        for arg in indexer_args:
            if TrackingGraph.has_tracked_obj(obj=arg):
                indexer_node = TrackingGraph.get_node_for_tracked_object(obj=arg)
                out_node.add_predecessor(predecessor_node=indexer_node, operations={Operations.INDEXER})


def wrap_loc_getitem(f):
    @functools.wraps(f)
    def wrapped_func(self, *args):
        out = f(self, *args)
        module_name = get_module_name(sys._getframe().f_back)
        if module_name != 'pandas.io.formats.format':
            indexer_args = args[0] if isinstance(args[0], tuple) else (args[0],)
            handle_indexers(result_obj=out, indexer_args=indexer_args)
        return out
    return wrapped_func


def tracked_series_constructor(mod):
    class TrackedPandasSeries(mod.Series):
        init_arg_names = get_func_arg_names(mod.Series.__init__)
        methods = [x for x, _ in inspect.getmembers(mod.Series, predicate=inspect.ismethod)]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            node = DatasetTrackingNode(oid=id(self), version=0, obj_type=DatasetTrackingNode.ObjectType.PANDAS)
            TrackingGraph.add_tracked_object(obj=self, node=node)
            data = get_func_req_params(self.init_arg_names, [1], *((self,) + args), **kwargs)
            if TrackingGraph.has_tracked_obj(obj=data):
                # TODO(chandra): The operation should be COPY in case of copy argument to constructor is True
                node.add_predecessor(predecessor_node=TrackingGraph.get_node_for_tracked_object(obj=data),
                                     operations={Operations.VIEW})

        @property
        def _constructor(self):
            from .pandas_datasets import Series as TrackedPandasSeries
            return get_contructor_partial_func(self_obj=self, module_cls=TrackedPandasSeries,
                                               methods=TrackedPandasSeries.methods)

        @property
        def _constructor_expanddim(self):
            from .pandas_datasets import DataFrame as TrackedPandasDataFrame
            return get_contructor_partial_func(self_obj=self, module_cls=TrackedPandasDataFrame,
                                               methods=TrackedPandasDataFrame.methods)

        def __getitem__(self, *args):
            out = super().__getitem__(*args)
            # In case of IDEs like PyCharm, the repr function is called very frequently, which in case of numpy,
            # repeatedly calls __getitem__ -- let's skip these calls
            module_name = get_module_name(sys._getframe().f_back)
            if module_name != 'pandas.io.formats.format':
                indexer_args = args[0] if isinstance(args[0], tuple) else (args[0],)
                handle_indexers(result_obj=out, indexer_args=indexer_args)
            return out

        def __reduce__(self):
            pickled_state = super().__reduce__()
            fixed_type_spec = (mod.Series, ) + pickled_state[1][1:]
            new_pickled_state = (pickled_state[0], fixed_type_spec) + pickled_state[2:]
            return new_pickled_state

        def __finalize__(self, other, method=None, **kwargs):
            out = super().__finalize__(other=other, method=method, **kwargs)
            handle_finalize(out=out, other=other)
            return out

        @property
        def values(self):
            from scrybe.internal.tracker.data.instrumentation.numpy_datasets import array as TrackedNDArray
            out = super().values
            module_name = get_module_name(sys._getframe().f_back)
            if not skip_tracking(module_name=module_name):
                if hasattr(out, 'view'):
                    tracked_array = out.view(TrackedNDArray)
                    node = TrackingGraph.get_node_for_tracked_object(obj=self)
                    out_node = TrackingGraph.get_node_for_tracked_object(obj=tracked_array)
                    out_node.add_predecessor(predecessor_node=node, operations={Operations.VIEW})
                    return tracked_array
            return out

        def equals(self, other):
            import pandas as pd
            try:
                pd.testing.assert_series_equal(self, other)
                return True
            except AssertionError:
                return False

    def wrap_new(orig_new):
        @functools.wraps(orig_new)
        def wrapped_new(*args, **kwargs):
            self = orig_new(TrackedPandasSeries)
            return self
        return wrapped_new

    mod.Series.__new__ = wrap_new(orig_new=mod.Series.__new__)

    # We reset the name here to match what is in the Pandas library so that variable inspection looks clean on
    # client code.
    # Technically we can simple use this name above -- I feel more comfortable doing this hack so that anyone reading
    # code should mentally associate our subclass as "TrackedPandasSeries" rather than Series
    TrackedPandasSeries.__name__ = "Series"
    return TrackedPandasSeries


def tracked_dataframe_constructor(mod):
    class TrackedPandasDataFrame(mod.DataFrame):
        init_arg_names = get_func_arg_names(mod.DataFrame.__init__)
        methods = [x for x, _ in inspect.getmembers(mod.DataFrame, predicate=inspect.ismethod)]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            node = DatasetTrackingNode(oid=id(self), version=0, obj_type=DatasetTrackingNode.ObjectType.PANDAS)
            TrackingGraph.add_tracked_object(obj=self, node=node)
            data = get_func_req_params(self.init_arg_names, [1], *((self, ) + args), **kwargs)
            if TrackingGraph.has_tracked_obj(obj=data):
                # TODO(chandra): The operation should be COPY in case of copy argument to constructor is True
                node.add_predecessor(predecessor_node=TrackingGraph.get_node_for_tracked_object(obj=data),
                                     operations={Operations.VIEW})

        def __reduce__(self):
            pickled_state = super().__reduce__()
            fixed_type_spec = (mod.DataFrame, ) + pickled_state[1][1:]
            new_pickled_state = (pickled_state[0], fixed_type_spec) + pickled_state[2:]
            return new_pickled_state

        @property
        def _constructor(self):
            from .pandas_datasets import DataFrame as TrackedPandasDataFrame
            return get_contructor_partial_func(self_obj=self, module_cls=TrackedPandasDataFrame,
                                               methods=TrackedPandasDataFrame.methods)

        @property
        def _constructor_sliced(self):
            from .pandas_datasets import Series as TrackedPandasSeries
            return get_contructor_partial_func(self_obj=self, module_cls=TrackedPandasSeries,
                                               methods=TrackedPandasSeries.methods)

        def __getitem__(self, *args):
            out = super().__getitem__(*args)
            # In case of IDEs like PyCharm, the repr function is called very frequently, which in case of numpy,
            # repeatedly calls __getitem__ -- let's skip these calls
            module_name = get_module_name(sys._getframe().f_back)
            if module_name != 'pandas.io.formats.format':
                indexer_args = args[0] if isinstance(args[0], tuple) else (args[0],)
                handle_indexers(result_obj=out, indexer_args=indexer_args)
            return out

        def __setitem__(self, key, value):
            super().__setitem__(key, value)
            if TrackingGraph.has_tracked_obj(value):
                previous_node = None
                if TrackingGraph.has_tracked_obj(obj=self):
                    previous_node = TrackingGraph.get_node_for_tracked_object(obj=self)
                node = DatasetTrackingNode(oid=id(self), version=0, obj_type=DatasetTrackingNode.ObjectType.PANDAS)
                TrackingGraph.add_tracked_object(obj=self, node=node)
                node.add_predecessor(predecessor_node=TrackingGraph.get_node_for_tracked_object(obj=value),
                                     operations={Operations.TRANSFORM})
                if previous_node is not None:
                    node.add_predecessor(predecessor_node=previous_node, operations={Operations.TRANSFORM})

        def __finalize__(self, other, method=None, **kwargs):
            out = super().__finalize__(other=other, method=method, **kwargs)
            handle_finalize(out=out, other=other)
            return out

        @property
        def values(self):
            from scrybe.internal.tracker.data.instrumentation.numpy_datasets import array as TrackedNDArray
            out = super().values
            module_name = get_module_name(sys._getframe().f_back)
            if not skip_tracking(module_name=module_name):
                if hasattr(out, 'view'):
                    tracked_array = out.view(TrackedNDArray)
                    node = TrackingGraph.get_node_for_tracked_object(obj=self)
                    out_node = TrackingGraph.get_node_for_tracked_object(obj=tracked_array)
                    out_node.add_predecessor(predecessor_node=node, operations={Operations.VIEW})
                    return tracked_array
            return out

        def equals(self, other):
            import pandas as pd
            try:
                pd.testing.assert_frame_equal(self, other)
                return True
            except AssertionError:
                return False

    def wrap_new(orig_new):
        @functools.wraps(orig_new)
        def wrapped_new(*args, **kwargs):
            self = orig_new(TrackedPandasDataFrame)
            return self
        return wrapped_new

    mod.DataFrame.__new__ = wrap_new(orig_new=mod.DataFrame.__new__)

    # We reset the name here to match what is in the Pandas library so that variable inspection looks clean on
    # client code.
    # Technically we can simple use this name above -- I feel more comfortable doing this hack so that anyone reading
    # code should mentally associate our subclass as "TrackedPandasDataFrame" rather than Series
    TrackedPandasDataFrame.__name__ = "DataFrame"
    return TrackedPandasDataFrame


def wrap_dataframe_creator_from_file(f):
    @functools.wraps(f)
    def wrapped_func(*args, **kwargs):
        arr = f(*args, **kwargs)
        if TrackingGraph.has_tracked_obj(obj=arr):
            filename, file_path = safe_extract_name_and_path(args=args, kwargs=kwargs)
            if len(filename) > 0:
                arr_node = TrackingGraph.get_node_for_tracked_object(obj=arr)
                arr_node.set_node_name(name=filename)
                arr_node.set_data_path(path=file_path)
                arr_node.set_created_in_run(val=False)
                set_dataset_info(dataset_obj=arr)

        return arr
    return wrapped_func


MODULE_PATCHER_MAP = {
    "pandas.core.series": ModulePatcher(
        patch_func_map=dict(),
        dynamic_class_specs=[
            (tracked_series_constructor, )
        ],
        class_method_patcher_spec=[],
        post_patch_additional_modules=['pandas']
    ),
    "pandas.core.frame": ModulePatcher(
        patch_func_map=dict(),
        dynamic_class_specs=[
            (tracked_dataframe_constructor, )
        ],
        class_method_patcher_spec=[],
        post_patch_additional_modules=['pandas']
    ),
    "pandas.core.indexing": ModulePatcher(
        patch_func_map=dict(),
        class_method_patcher_spec=[
            ('_LocationIndexer', '__getitem__', wrap_loc_getitem)
        ],
        dynamic_class_specs=[],
        post_patch_additional_modules=[]
    ),
    "pandas.io.parsers": ModulePatcher(
        patch_func_map=dict(
            read_csv=lambda f: wrap_dataframe_creator_from_file(f),
            read_table=lambda f: wrap_dataframe_creator_from_file(f),
            read_fwf=lambda f: wrap_dataframe_creator_from_file(f),
        ),
        class_method_patcher_spec=[],
        dynamic_class_specs=[
        ],
        post_patch_additional_modules=['pandas']
    ),
}
