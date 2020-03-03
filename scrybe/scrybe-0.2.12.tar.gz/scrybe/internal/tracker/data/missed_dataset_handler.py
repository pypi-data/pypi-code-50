import weakref
from scrybe.internal.depgraph.tracking_graph import TrackingGraph
from scrybe.internal.depgraph.nodes import DatasetTrackingNode


class MissedDatasetTracker(object):
    """
    The following two functions are called in the event where we find a dataset which needs to be tracked
    but was not already automatically tracked. In such cases, to keep the lineage graph complete, we
    have two options:
      - If the untracked object is of a type whose handling we understand (e.g. ndarray), we will create a new
        object of its corresponding sub-class (e.g. TrackedNDArray) to create a graph node
      - If we don't currently handle this type, we can optionally create a dataset graph node with
        UNKNOWN sub type
      In the latter case, the object is not changed so if that same object is encountered again, the oid will
      help us find the node in the graph. However, in the first case, the user might still be referencing
      the object of the base class, and so we might see the object again and create yet another sub-class object.
      To avoid this situation, we need to hold on to the graph node and the new object until the original object
      is collected
    """
    # Following is a map from [TrackedDataObjectHolder] -> [object] where the [object] is the missed data object
    MISSED_OBJECT_MAP = weakref.WeakValueDictionary()

    class TrackedDataObjectHolder(object):
        """
        This class is a holder for the tracked object which was created for missed object (see: track_data_if_possible)
        """
        def __init__(self, tracked_data_obj):
            self.tracked_data_obj = tracked_data_obj

    @classmethod
    def find_data_object(cls, data_obj):
        for tracked_obj_holder, missed_data_obj in cls.MISSED_OBJECT_MAP.items():
            if missed_data_obj is data_obj:
                return tracked_obj_holder.tracked_data_obj
        return None

    @classmethod
    def add_missed_obj_to_tracker(cls, data_obj, tracked_data_obj):
        tracked_obj_holder = cls.TrackedDataObjectHolder(tracked_data_obj=tracked_data_obj)
        cls.MISSED_OBJECT_MAP[tracked_obj_holder] = data_obj


def track_data_if_possible(data_obj):
    out = MissedDatasetTracker.find_data_object(data_obj=data_obj)
    if out is None:
        from scrybe.internal.tracker.data.instrumentation.numpy_datasets import track_array_if_possible
        # FIXME(msachdev): Handle simple lists. pandas
        all_trackers = (track_array_if_possible, )
        for tracker in all_trackers:
            out = tracker(data_obj)
            if out is not None:
                MissedDatasetTracker.add_missed_obj_to_tracker(data_obj=data_obj, tracked_data_obj=out)
                break
    return out


def track_data(data_obj):
    out = track_data_if_possible(data_obj=data_obj)
    if out is None:
        node = DatasetTrackingNode(oid=id(data_obj), version=0, obj_type=DatasetTrackingNode.ObjectType.UNKNOWN)
        TrackingGraph.add_tracked_object(obj=data_obj, node=node)
        out = data_obj
    return out
