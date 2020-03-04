from scrybe.internal.depgraph import TrackingGraph
from scrybe.internal.depgraph.nodes import BasicIteratorTrackingNode
from scrybe.internal.tracker.data.missed_dataset_handler import track_data_if_possible


def is_simple_iterable(obj):
    if not (isinstance(obj, list) or isinstance(obj, tuple) or isinstance(obj, dict)):
        return False
    iterable = obj
    if isinstance(obj, dict):
        iterable = obj.values()
    is_numpy_importable = True
    is_pandas_importable = True
    try:
        import numpy
    except ImportError:
        is_numpy_importable = False
    try:
        import pandas
    except ImportError:
        is_pandas_importable = False
    for i in range(len(iterable)):
        # In order to be more efficient we need to stop somewhere
        if i > 1000:
            return False
        item = iterable[i]
        if not ((is_numpy_importable and isinstance(item, numpy.ndarray)) or
                (is_pandas_importable and (isinstance(item, pandas.DataFrame) or isinstance(item, pandas.Series)))):
            return False
    return True


def get_iterable_of_tracked_types(iterable):
    if isinstance(iterable, dict):
        iterable = iterable.values()
    modified_iterable = []
    for item in iterable:
        if TrackingGraph.has_tracked_obj(obj=item):
            modified_iterable.append(item)
        else:
            item = track_data_if_possible(data_obj=item)
            if item is not None:
                modified_iterable.append(item)
    if len(modified_iterable) > 0:
        return modified_iterable
    return None


def get_node_for_simple_iterable(iterable_obj):
    modified_iterable = get_iterable_of_tracked_types(iterable=iterable_obj)
    if modified_iterable is None:
        return None
    iterable_node = BasicIteratorTrackingNode.get_node(oid=id(iterable_obj), obj=modified_iterable)
    return iterable_node
