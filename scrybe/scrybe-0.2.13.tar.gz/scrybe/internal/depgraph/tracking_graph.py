import logging
import weakref

from typing import Iterable, Dict

from scrybe.internal.depgraph.lineage_graph import LineageGraph
from scrybe.internal.depgraph.nodes import BaseTrackingNode

LOGGER = logging.getLogger("scrybe_logger")


def log_upload_data_to_file(upload_data: Iterable[Dict], func_name: str):
    def default_json(non_serializable_obj):
        try:
            return float(non_serializable_obj)
        except Exception as e:
            return "%s.%s" % (non_serializable_obj.__class__.__module__, non_serializable_obj.__class__.__name__)

    func_name = func_name.replace('-', '_')

    import json
    with open('/tmp/upload_data', 'a') as f:
        LOGGER.debug('%s = [' % func_name, file=f)
        for d in upload_data:
            LOGGER.debug(json.dumps(d, indent=2, default=default_json) + ", ", file=f)
        LOGGER.debug("]", file=f)
        LOGGER.debug("upload_packets(%s)\n" % func_name, file=f)


class TrackingGraph(object):
    class TrackedObject(object):
        def __init__(self, node: BaseTrackingNode):
            self.nodes = [node]

        def get_max_version(self):
            return len(self.nodes) - 1

        def get_node_for_latest_version(self):
            return self.nodes[-1]

        def add_node_for_new_version(self, node):
            self.nodes.append(node)

    # Following is a map from [TrackedObject] -> [object] (which needs to be tracked)
    # This keeps a ref on the TrackedObject object and thereby keeps the graph node object alive
    TRACKER_OBJECT_MAP = weakref.WeakValueDictionary()

    # Following is a map from object's OID -> [TrackedObject]
    # This allows looking up the TrackedObject corresponding to an object which needs tracking
    # This has a cascading delete effect -- when the main object gets collected, it will
    # remove the entry from TRACKER_OBJECT_MAP, thereby losing the ref on the TrackedObject instance,
    # which in-turn will cause the entry to be removed from the below map
    OID_TRACKED_OBJECT_MAP = weakref.WeakValueDictionary()

    @classmethod
    def has_tracked_obj(cls, obj) -> bool:
        return id(obj) in cls.OID_TRACKED_OBJECT_MAP

    @classmethod
    def get_max_version_of_tracked_object(cls, obj) -> int:
        return cls.OID_TRACKED_OBJECT_MAP[id(obj)].get_max_version()

    @classmethod
    def get_node_for_tracked_object(cls, obj) -> BaseTrackingNode:
        #  This function always returns the node corresponding to the latest (i.e. current) version
        #  of the object
        return cls.OID_TRACKED_OBJECT_MAP[id(obj)].get_node_for_latest_version()

    @classmethod
    def get_node_for_tracked_object_id(cls, obj_id) -> BaseTrackingNode:
        #  This function always returns the node corresponding to the latest (i.e. current) version
        #  of the object
        return cls.OID_TRACKED_OBJECT_MAP[obj_id].get_node_for_latest_version() \
            if obj_id in cls.OID_TRACKED_OBJECT_MAP else None

    @classmethod
    def add_tracked_object(cls, obj, node: BaseTrackingNode, replace_existing=False):
        if cls.has_tracked_obj(obj=obj):
            tracked_obj = cls.OID_TRACKED_OBJECT_MAP[id(obj)]
            if not replace_existing:
                tracked_obj.add_node_for_new_version(node=node)
                return
            else:
                cls.TRACKER_OBJECT_MAP.pop(tracked_obj)
        tracked_obj = cls.TrackedObject(node=node)
        cls.TRACKER_OBJECT_MAP[tracked_obj] = obj
        cls.OID_TRACKED_OBJECT_MAP[id(obj)] = tracked_obj

    @classmethod
    def replace_node_reference(cls, orig_obj, new_obj):
        if not TrackingGraph.has_tracked_obj(obj=orig_obj):
            return
        tracked_obj = TrackingGraph.OID_TRACKED_OBJECT_MAP.pop(id(orig_obj))
        cls.OID_TRACKED_OBJECT_MAP[id(new_obj)] = tracked_obj
        cls.TRACKER_OBJECT_MAP[tracked_obj] = new_obj

    @classmethod
    def get_lineage_of_tracked_object(cls, obj) -> LineageGraph:
        if not cls.has_tracked_obj(obj=obj):
            raise ValueError("Given object is not tracked in graph")
        node = cls.get_node_for_tracked_object(obj=obj)
        return node.get_lineage()
