from scrybe.internal.depgraph import TrackingGraph
from scrybe.internal.depgraph.nodes import DatasetTrackingNode
from scrybe.internal.depgraph.ops import Operations
from scrybe.internal.tracker.data.utils import safe_extract_name_and_path, set_dataset_info_and_upload, set_dataset_info
from scrybe.internal.util import get_func_arg_names, get_func_req_params

POOL_INIT = [
    ('catboost.core', 'Pool.__init__')  # Is dependent on data and labels. Data can be a string which is a file path
]

POOL_FROM_SELF = [
    ('catboost.core', 'Pool.slice'),
]

POOL_SAVE = [
    ('catboost.core', 'Pool.save'),
]


def add_as_parent(node, parent_data_obj, parent_node_name, operation):
    if parent_data_obj is not None and TrackingGraph.has_tracked_obj(obj=parent_data_obj):
        parent_data_node = TrackingGraph.get_node_for_tracked_object(obj=parent_data_obj)
        parent_data_node.set_node_name_if_not_final(name=parent_node_name)
        node.add_predecessor(predecessor_node=parent_data_node, operations={operation})


def pool_init_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    dataset_obj = args[0]
    if TrackingGraph.has_tracked_obj(dataset_obj):
        return
    obj_type = DatasetTrackingNode.ObjectType.CATBOOST_POOL
    node = DatasetTrackingNode(oid=id(dataset_obj), version=0, obj_type=obj_type)
    TrackingGraph.add_tracked_object(obj=dataset_obj, node=node)
    arg_names = get_func_arg_names(orig_func)
    parent_data_obj, label = get_func_req_params(arg_names, [1, 2], *args, **kwargs)
    if isinstance(parent_data_obj, str):
        path = parent_data_obj
        filename, file_path = safe_extract_name_and_path(args=(path,), kwargs=dict())
        if isinstance(file_path, str) and len(file_path) > 0:
            node.set_node_name(name=filename)
            node.set_data_path(path=path)
            node.set_created_in_run(val=True)
            set_dataset_info(dataset_obj=dataset_obj)
    else:
        arg_obj_names = metadata_dict["arg_obj_names"]
        kwargs_obj_names = metadata_dict["kwargs_obj_names"]
        parent_data_name, label_name = get_func_req_params(arg_names, [1, 2], *arg_obj_names, **kwargs_obj_names)
        add_as_parent(node=node, parent_data_obj=parent_data_obj, parent_node_name=parent_data_name,
                      operation=Operations.CONCATENATION)
        add_as_parent(node=node, parent_data_obj=label, parent_node_name=label_name,
                      operation=Operations.CONCATENATION)


def pool_from_self_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    dataset_obj = ret_val
    if not TrackingGraph.has_tracked_obj(dataset_obj):
        obj_type = DatasetTrackingNode.ObjectType.CATBOOST_POOL
        node = DatasetTrackingNode(oid=id(dataset_obj), version=0, obj_type=obj_type)
        TrackingGraph.add_tracked_object(obj=dataset_obj, node=node)
    else:
        node = TrackingGraph.get_node_for_tracked_object(obj=dataset_obj)
    self_obj = args[0]
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    arg_names = get_func_arg_names(orig_func)
    parent_data_name, label_name = get_func_req_params(arg_names, [0], *arg_obj_names, **kwargs_obj_names)
    add_as_parent(node=node, parent_data_obj=self_obj, parent_node_name=parent_data_name,
                  operation=Operations.ROW_FILTER)


def pool_save_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    dataset = args[0]
    if not TrackingGraph.has_tracked_obj(obj=dataset):
        return
    node = TrackingGraph.get_node_for_tracked_object(obj=dataset)
    arg_names = get_func_arg_names(orig_func)
    path = get_func_req_params(arg_names, [1], *args, **kwargs)
    filename, file_path = safe_extract_name_and_path(args=(path,), kwargs=dict())
    if isinstance(file_path, str) and len(file_path) > 0:
        node.set_node_name(name=filename)
        node.set_data_path(path=path)
        node.set_created_in_run(val=True)
        set_dataset_info_and_upload(dataset_obj=dataset)


def patch(patcher_obj):
    for module_name, func_name in POOL_INIT:
        patcher_obj.register_after(module_name, func_name, pool_init_after_decorator)
    for module_name, func_name in POOL_FROM_SELF:
        patcher_obj.register_after(module_name, func_name, pool_from_self_after_decorator)
    for module_name, func_name in POOL_SAVE:
        patcher_obj.register_after(module_name, func_name, pool_save_after_decorator)