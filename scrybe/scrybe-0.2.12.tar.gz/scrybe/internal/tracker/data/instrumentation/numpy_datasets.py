import functools
import os
import sys
import warnings

from scrybe.internal.depgraph.nodes import DatasetTrackingNode
from scrybe.internal.depgraph.ops import Operations
from scrybe.internal.depgraph.tracking_graph import TrackingGraph
from scrybe.internal.tracker.data.instrumentation.import_interceptor import ModulePatcher
from scrybe.internal.tracker.data.utils import safe_extract_name_and_path, skip_tracking, \
    set_dataset_node_path, set_dataset_info
from scrybe.internal.util import get_module_name

# FIXME(msachdev): Clean this shit
NDArrayTracker = dict()
ENABLE_VERBOSE_LOGGING = False

SCRYBE_FILE_PATH_ATTR = "scrybe_file_path"
SCRYBE_FILENAME_ATTR = "scrybe_filename"


# FIXME(msachdev): and this too
def aid(arr_obj):
    return arr_obj.__array_interface__['data'][0]


def tracked_ndarray_constructor(mod):
    class TrackedNDArray(mod.ndarray):
        __array_priority__ = 0.1

        def __new__(cls, input_array, reason):
            self = input_array.view(cls)
            self.reason = reason
            return self

        # TODO(msachdev): Remove dead code
        # def __getitem__(self, *args):
        #     out = super().__getitem__(*args)
        #     # In case of IDEs like PyCharm, the repr function is called very frequently, which in case of numpy,
        #     # repeatedly calls __getitem__ -- let's skip these calls
        #     module_name = get_module_name(inspect.currentframe().f_back)
        #     if module_name != 'numpy.core.arrayprint':
        #         if TrackingGraph.has_tracked_obj(obj=out):
        #             out_node: DatasetTrackingNode = TrackingGraph.get_node_for_tracked_object(obj=out)
        #             indexers = list()
        #             indexer_args = args[0] if isinstance(args[0], tuple) else (args[0],)
        #             for arg in indexer_args:
        #                 if isinstance(arg, int):
        #                     indexers.append(dict(type='int', val=arg))
        #                 elif is_int_like(arg):
        #                     int_arg = int(arg)
        #                     indexers.append(dict(type='int', val=int_arg))
        #                 elif isinstance(arg, str):
        #                     indexers.append(dict(type='str', val=arg))
        #                 elif isinstance(arg, slice):
        #                     val = (arg.start, arg.stop, arg.step)
        #                     indexers.append(dict(type='slice', val=str(val)))
        #                 elif isinstance(arg, TrackedNDArray):
        #                     indexer_node = TrackingGraph.get_node_for_tracked_object(obj=arg)
        #                     indexers.append(dict(type='ndarray', val=indexer_node.client_id))
        #                     out_node.add_predecessor(predecessor_node=indexer_node, operations={Operations.INDEXER})
        #                 elif isinstance(arg, list):
        #                     indexer_node = None
        #                     if TrackingGraph.has_tracked_obj(obj=arg):
        #                         indexer_node = TrackingGraph.get_node_for_tracked_object(obj=arg)
        #                         out_node.add_predecessor(predecessor_node=indexer_node, operations={Operations.INDEXER})
        #                     client_id = indexer_node.client_id if indexer_node is not None else ""
        #                     indexers.append(dict(type='list', val=client_id))
        #                 else:
        #                     self.__log_verbose__("Unknown indexer type: ", type(arg))
        #             out_node.set_indexing_info(indexing_info=indexers)
        #     return out

        def __getitem__(self, *args):
            out = super().__getitem__(*args)
            # In case of IDEs like PyCharm, the repr function is called very frequently, which in case of numpy,
            # repeatedly calls __getitem__ -- let's skip these calls
            module_name = get_module_name(sys._getframe().f_back)
            if module_name != 'numpy.core.arrayprint':
                # The output can be a scalar or something else -- need to check if it exists in our graph
                if TrackingGraph.has_tracked_obj(obj=out):
                    out_node = TrackingGraph.get_node_for_tracked_object(obj=out)
                    self_node = TrackingGraph.get_node_for_tracked_object(obj=self)
                    out_node.add_predecessor(predecessor_node=self_node, operations={Operations.ROW_FILTER,
                                                                                     Operations.COLUMN_SELECT})
                    indexer_args = args[0] if isinstance(args[0], tuple) else (args[0],)
                    for arg in indexer_args:
                        if TrackingGraph.has_tracked_obj(obj=arg):
                            indexer_node = TrackingGraph.get_node_for_tracked_object(obj=arg)
                            out_node.add_predecessor(predecessor_node=indexer_node, operations={Operations.INDEXER})
            return out

        def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
            args = list()
            predecessor_nodes = list()
            for i, input_ in enumerate(inputs):
                if isinstance(input_, TrackedNDArray):
                    args.append(input_.view(mod.ndarray))
                    predecessor_nodes.append(TrackingGraph.get_node_for_tracked_object(obj=input_))
                else:
                    args.append(input_)

            outputs = kwargs.pop('out', None)
            if outputs:
                out_args = []
                for j, output in enumerate(outputs):
                    if isinstance(output, TrackedNDArray):
                        out_args.append(output.view(mod.ndarray))
                    else:
                        out_args.append(output)
                kwargs['out'] = tuple(out_args)
            else:
                outputs = (None,) * ufunc.nout

            results = super().__array_ufunc__(ufunc, method, *args, **kwargs)
            if results is NotImplemented:
                return NotImplemented

            if method == 'at':
                return

            if ufunc.nout == 1:
                results = (results,)

            import numpy as np
            final_results = list()
            result_nodes = list()
            for result, output in zip(results, outputs):
                if output is None:
                    if isinstance(result, np.ndarray) and result.shape != ():
                        new_result_obj = result.view(TrackedNDArray)
                        final_results.append(new_result_obj)
                        result_nodes.append(TrackingGraph.get_node_for_tracked_object(obj=new_result_obj))
                    else:
                        final_results.append(result)
                else:
                    final_results.append(output)
                    if isinstance(output, TrackedNDArray):
                        # In this case, it is possible that one of the output objects is one of the input
                        # object itself (e.g. a += b). In such cases, we need to bump the version of the
                        # dataset object and create a new node for it
                        output_node = TrackingGraph.get_node_for_tracked_object(obj=output)
                        for predecessor_node in predecessor_nodes:
                            if predecessor_node is output_node:
                                version = TrackingGraph.get_max_version_of_tracked_object(obj=output)
                                version += 1
                                output_node = DatasetTrackingNode(oid=id(output), version=version,
                                                                  obj_type=DatasetTrackingNode.ObjectType.NUMPY)
                                TrackingGraph.add_tracked_object(obj=output, node=output_node)
                        result_nodes.append(TrackingGraph.get_node_for_tracked_object(obj=output))

            for result_node in result_nodes:
                for predecessor_node in predecessor_nodes:
                    result_node.add_predecessor(predecessor_node=predecessor_node,
                                                operations={Operations.TRANSFORM})

            return final_results[0] if len(final_results) == 1 else final_results

        def __array_function__(self, func, types, *args, **kwargs):
            out = super().__array_function__(func, types, *args, **kwargs)
            if not isinstance(out, TrackedNDArray) and isinstance(out, mod.ndarray) and out.shape != ():
                out = out.view(TrackedNDArray)
            if TrackingGraph.has_tracked_obj(obj=out):
                out_node = TrackingGraph.get_node_for_tracked_object(obj=out)
                input_arrs = args[0]
                if isinstance(input_arrs, tuple) and (isinstance(input_arrs[0], tuple) or
                                                      isinstance(input_arrs[0], list)):
                    input_arrs = input_arrs[0]
                if not isinstance(input_arrs, list) and not isinstance(input_arrs, tuple):
                    input_arrs = (input_arrs,)
                for input_arr in input_arrs:
                    # In some cases (e.g. atleast_*d functions), the output can be one of the inputs itself
                    if TrackingGraph.has_tracked_obj(obj=input_arr) and input_arr is not out:
                        input_arr_node = TrackingGraph.get_node_for_tracked_object(obj=input_arr)
                        out_node.add_predecessor(predecessor_node=input_arr_node, operations={Operations.TRANSFORM})
            return out

        def __array_finalize__(self, obj):
            if TrackingGraph.has_tracked_obj(obj=self):
                # TODO(msachdev): Can this still happen? If so, does it require bumping the version?
                return

            node = DatasetTrackingNode(oid=id(self), version=0, obj_type=DatasetTrackingNode.ObjectType.NUMPY)
            if isinstance(obj, TrackedNDArray):
                # If of is of type TrackedNDArray, it is guaranteed that it is already in NP_ARRAY_GRAPH
                obj_node = TrackingGraph.get_node_for_tracked_object(obj=obj)
                if self.base is obj:
                    if self.__array_interface__['typestr'] != obj.__array_interface__['typestr']:
                        node.add_predecessor(predecessor_node=obj_node, operations={Operations.VIEW})
                    elif self.__array_interface__['shape'] != obj.__array_interface__['shape'] and \
                            self.__array_interface__['data'] == obj.__array_interface__['data']:
                        # This happens in case of reshape
                        node.add_predecessor(predecessor_node=obj_node, operations={Operations.VIEW})
                elif self.base is not None and not isinstance(self.base, TrackedNDArray):
                    # TODO(msachdev): Need to re-evaluate some of these cases now that we have handled UFUNCs
                    # When executing UFUNCs, numpy will first create an ndarray to contain the output and then
                    # will view-cast it to our subclass. In such cases, self.base is the original ndarray and
                    # obj is the input to the UFUNC
                    node.add_predecessor(predecessor_node=obj_node, operations={Operations.TRANSFORM})
                elif self.base is None:
                    node.add_predecessor(predecessor_node=obj_node, operations={Operations.TRANSFORM})
            else:
                pass
                # if self.base is obj:
                #     if obj is None:
                #         pass
                #     elif self.__array_interface__ == obj.__array_interface__:
                #         # This is basically the exact same array type cast from ndarray to TrackedNDArray
                #         # which means this is coming from our __new__ function
                #         pass
                # else:
                #     # This is a finalize after a UFUNC operation
                #     # TODO(msachdev): Handle this case correctly
                #     pass
            TrackingGraph.add_tracked_object(obj=self, node=node)

        def __reduce__(self):
            pickled_state = self.view(mod.ndarray).__reduce__()
            # TODO(msachdev): Need to figure out a way to handle parallel process use case
            # new_state = pickled_state[2] + (id(self),)
            # return pickled_state[0], pickled_state[1], new_state
            return pickled_state

        def __setstate__(self, state):
            prev_oid = state[-1]  # Set the info attribute
            predecessor_node = TrackingGraph.get_node_for_tracked_object_id(obj_id=prev_oid)
            super().__setstate__(state[0:-1])
            node = DatasetTrackingNode(oid=id(self), version=0, obj_type=DatasetTrackingNode.ObjectType.NUMPY)
            TrackingGraph.add_tracked_object(obj=self, node=node)
            if predecessor_node:
                node.add_predecessor(predecessor_node=predecessor_node, operations={Operations.COPY})

        def take(self, indices, *args, **kwargs):
            out = super().take(indices, *args, **kwargs)
            if TrackingGraph.has_tracked_obj(obj=out) and TrackingGraph.has_tracked_obj(obj=indices):
                out_node = TrackingGraph.get_node_for_tracked_object(obj=out)
                indexer_node = TrackingGraph.get_node_for_tracked_object(obj=indices)
                out_node.add_predecessor(predecessor_node=indexer_node, operations={Operations.INDEXER})
            return out

    # We reset the name here to match what is in the Pandas library so that variable inspection looks clean on
    # client code.
    # Technically we can simple use this name above -- I feel more comfortable doing this hack so that anyone reading
    # code should mentally associate our subclass as "TrackedNDArray" rather than Series
    TrackedNDArray.__name__ = "array"
    return TrackedNDArray


def safe_convert_array(arr, module_name: str, function_name: str):
    import numpy as np
    from .numpy_datasets import array as TrackedNDArray
    if skip_tracking(module_name=module_name):
        return arr
    if isinstance(arr, np.ndarray) and not isinstance(arr, TrackedNDArray):
        arr = TrackedNDArray(input_array=arr, reason=function_name)
    return arr


def wrap_ndarray_creator_basic(f, function_name):
    @functools.wraps(f)
    def wrapped_func(*args, **kwargs):
        arr = f(*args, **kwargs)
        module_name = get_module_name(sys._getframe().f_back)
        arr = safe_convert_array(arr=arr, module_name=module_name, function_name=function_name)
        return arr

    return wrapped_func


def wrap_ndarray_creator_from_arraylike(f, function_name):
    @functools.wraps(f)
    def wrapped_func(*args, **kwargs):
        arr = f(*args, **kwargs)
        module_name = get_module_name(sys._getframe().f_back)
        arr = safe_convert_array(arr=arr, module_name=module_name, function_name=function_name)
        # Establish link between this new object and the input
        input_arr = args[0] if len(args) > 0 else kwargs['object']
        # If the input array is a TrackedNDArray and the call is made with copy=False, subok=True then numpy will
        # return the same object as the input so we don't need to establish a link
        if input_arr is not arr:
            if TrackingGraph.has_tracked_obj(obj=arr):
                if TrackingGraph.has_tracked_obj(obj=input_arr):
                    arr_node = TrackingGraph.get_node_for_tracked_object(obj=arr)
                    input_arr_node = TrackingGraph.get_node_for_tracked_object(obj=input_arr)
                    arr_node.add_predecessor(predecessor_node=input_arr_node, operations={Operations.COPY})
                else:
                    def check_h5py_dataset():
                        try:
                            import h5py
                            from h5py import Dataset
                            if isinstance(input_arr, Dataset) and hasattr(input_arr, 'file') and hasattr(input_arr.file,
                                                                                                         'filename'):
                                file_path = input_arr.file.filename
                                if file_path:
                                    set_dataset_node_path(orig_obj=arr, file_path=file_path, created_in_run=False,
                                                          upload=False)
                        except ImportError:
                            pass
                    with warnings.catch_warnings():
                        warnings.simplefilter("ignore")
                        check_h5py_dataset()
        return arr

    return wrapped_func


def wrap_ndarray_creator_from_file(f, function_name):
    @functools.wraps(f)
    def wrapped_func(*args, **kwargs):
        from numpy.lib.npyio import NpzFile
        arr = f(*args, **kwargs)
        module_name = get_module_name(sys._getframe().f_back)
        arr = safe_convert_array(arr=arr, module_name=module_name, function_name=function_name)
        if TrackingGraph.has_tracked_obj(obj=arr):
            filename, file_path = safe_extract_name_and_path(args=args, kwargs=kwargs)
            if len(filename) > 0:
                arr_node = TrackingGraph.get_node_for_tracked_object(obj=arr)
                arr_node.set_node_name(name=filename)
                arr_node.set_data_path(path=file_path)
                arr_node.set_created_in_run(val=False)
                set_dataset_info(dataset_obj=arr)
        elif isinstance(arr, NpzFile):
            filename, file_path = safe_extract_name_and_path(args=args, kwargs=kwargs)
            if len(filename) > 0:
                setattr(arr, SCRYBE_FILE_PATH_ATTR, file_path)
                setattr(arr, SCRYBE_FILENAME_ATTR, filename)

        return arr

    return wrapped_func


def wrap_npzfile_getitem(f):
    @functools.wraps(f)
    def wrapped_func(self, *args):
        arr = f(self, *args)
        module_name = get_module_name(sys._getframe().f_back)
        arr = safe_convert_array(arr=arr, module_name=module_name, function_name="load")
        if hasattr(self, SCRYBE_FILE_PATH_ATTR):
            file_path = getattr(self, SCRYBE_FILE_PATH_ATTR)
            filename = getattr(self, SCRYBE_FILENAME_ATTR)
            arr_node = TrackingGraph.get_node_for_tracked_object(obj=arr)
            arr_node.set_node_name(name=filename)
            arr_node.set_data_path(path=file_path)
        return arr

    return wrapped_func


def wrap_for_warning_suppression(f):
    @functools.wraps(f)
    def wrapped_func(*args, **kwargs):
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            return f(*args, **kwargs)

    return wrapped_func


def track_array_if_possible(array_obj):
    import numpy as np
    from .numpy_datasets import array as TrackedNDArray
    if isinstance(array_obj, np.ndarray):
        return array_obj.view(TrackedNDArray)
    return None


MODULE_PATCHER_MAP = {
    "numpy.core._multiarray_umath": ModulePatcher(
        patch_func_map=dict(
            empty=lambda f: wrap_ndarray_creator_basic(f, function_name="empty"),
            zeros=lambda f: wrap_ndarray_creator_basic(f, function_name="zeros"),
            arange=lambda f: wrap_ndarray_creator_basic(f, function_name="arange"),

            array=lambda f: wrap_ndarray_creator_from_arraylike(f, function_name="array"),
            fromiter=lambda f: wrap_ndarray_creator_from_arraylike(f, function_name="fromiter"),

            fromfile=lambda f: wrap_ndarray_creator_from_file(f, function_name="fromfile")
        ),
        dynamic_class_specs=[
            (tracked_ndarray_constructor,)
        ],
        class_method_patcher_spec=[],
        post_patch_additional_modules=['numpy']
    ),

    "numpy.core._asarray": ModulePatcher(
        patch_func_map=dict(
            asarray=lambda f: wrap_ndarray_creator_from_arraylike(f, function_name="asarray"),
            asanyarray=lambda f: wrap_ndarray_creator_from_arraylike(f, function_name="asanyarray"),
            ascontiguousarray=lambda f: wrap_ndarray_creator_from_arraylike(f, function_name="ascontiguousarray"),
            asfortranarray=lambda f: wrap_ndarray_creator_from_arraylike(f, function_name="asfortranarray"),
            require=lambda f: wrap_ndarray_creator_from_arraylike(f, function_name="require"),
        ),
        dynamic_class_specs=[
        ],
        class_method_patcher_spec=[],
        post_patch_additional_modules=['numpy']
    ),

    "numpy.core.numeric": ModulePatcher(
        patch_func_map=dict(
            identity=lambda f: wrap_ndarray_creator_basic(f, function_name="identity"),
            full=lambda f: wrap_ndarray_creator_basic(f, function_name="full"),
            ones=lambda f: wrap_ndarray_creator_basic(f, function_name="ones"),
        ),
        dynamic_class_specs=[
        ],
        class_method_patcher_spec=[],
        post_patch_additional_modules=['numpy']
    ),

    "numpy.lib.function_base": ModulePatcher(
        patch_func_map=dict(
            copy=lambda f: wrap_ndarray_creator_from_arraylike(f, function_name="copy"),
            asarray_chkfinite=lambda f: wrap_ndarray_creator_from_arraylike(f, function_name="asarray_chkfinite"),
        ),
        dynamic_class_specs=[
        ],
        class_method_patcher_spec=[],
        post_patch_additional_modules=['numpy']
    ),

    "numpy.lib.npyio": ModulePatcher(
        patch_func_map=dict(
            genfromtxt=lambda f: wrap_ndarray_creator_from_file(f, function_name="genfromtxt"),
            loadtxt=lambda f: wrap_ndarray_creator_from_file(f, function_name="loadtxt"),
            load=lambda f: wrap_ndarray_creator_from_file(f, function_name="load")
        ),
        dynamic_class_specs=[
        ],
        class_method_patcher_spec=[
            ('NpzFile', '__getitem__', wrap_npzfile_getitem)
        ],
        post_patch_additional_modules=['numpy']
    ),

    "numpy.lib.twodim_base": ModulePatcher(
        patch_func_map=dict(
            eye=lambda f: wrap_ndarray_creator_basic(f, function_name="eye"),
        ),
        dynamic_class_specs=[
        ],
        class_method_patcher_spec=[],
        post_patch_additional_modules=['numpy']
    ),

    "numpy.core.function_base": ModulePatcher(
        patch_func_map=dict(
            add_newdoc=lambda f: wrap_for_warning_suppression(f),
        ),
        dynamic_class_specs=[
        ],
        class_method_patcher_spec=[],
        post_patch_additional_modules=['numpy']
    )
}

# Need to use __array_function__ which requires NUMPY_EXPERIMENTAL_ARRAY_FUNCTION=1 for numpy v 1.16
# Set it here
os.environ["NUMPY_EXPERIMENTAL_ARRAY_FUNCTION"] = "1"
