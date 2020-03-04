import copy
import io
import ntpath
import pathlib
import weakref

from typing import Tuple

from scrybe.internal.depgraph import TrackingGraph
from scrybe.internal.depgraph.nodes import BaseTrackingNode
from scrybe.internal.tracker.data.missed_dataset_handler import track_data_if_possible
from scrybe.internal.uploader import DataReceiver
from scrybe.internal.util import get_info


def skip_tracking(module_name: str) -> bool:
    modules_to_skip = {'numpy', 'pandas', 'matplotlib'}
    for module_to_skip in modules_to_skip:
        if module_name == module_to_skip or module_name.startswith(module_to_skip + "."):
            return True
    return False


def is_int_like(obj) -> bool:
    try:
        out = int(obj)
    except:
        return False
    return isinstance(out, int)


def safe_extract_name_and_path(args, kwargs) -> Tuple[str, str]:
    file_path = None
    file_arg = args[0] if len(args) > 0 else kwargs['file']

    if isinstance(file_arg, str):
        file_path = file_arg
    elif isinstance(file_arg, io.IOBase):
        file_path = getattr(file_arg, 'name', None)
    elif isinstance(file_arg, pathlib.Path):
        file_path = str(file_arg)

    if file_path:
        head, tail = ntpath.split(file_path)
        full_filename = tail or ntpath.basename(head)
        filename = ntpath.splitext(full_filename)[0]
        return filename, file_path

    return "", ""


def set_dataset_info(dataset_obj):
    if dataset_obj is None or not TrackingGraph.has_tracked_obj(dataset_obj):
        return
    dataset_node = TrackingGraph.get_node_for_tracked_object(obj=dataset_obj)
    if dataset_node.node_type != BaseTrackingNode.Type.DATA:
        return
    if not dataset_node.is_info_set:
        info_str = get_info(obj=dataset_obj)
        dataset_node.update_info(info=info_str)
        return dataset_node


def set_dataset_info_and_maybe_upload(dataset_obj):
    dataset_node = set_dataset_info(dataset_obj=dataset_obj)
    if dataset_node is not None:
        DataReceiver.receive_batch(data_dict_list=dataset_node.prepare_for_upload())


def set_dataset_info_and_upload(dataset_obj):
    if dataset_obj is None or not TrackingGraph.has_tracked_obj(dataset_obj):
        return
    dataset_node = TrackingGraph.get_node_for_tracked_object(obj=dataset_obj)
    if not dataset_node.is_info_set:
        info_str = get_info(obj=dataset_obj)
        dataset_node.update_info(info=info_str)
    DataReceiver.receive_batch(data_dict_list=dataset_node.prepare_for_upload())


def maybe_track_dataset_and_upload_info(dataset, operation, model_node, dataset_name: str = None):
    if dataset is None:
        return
    if not TrackingGraph.has_tracked_obj(obj=dataset):
        dataset = track_data_if_possible(data_obj=dataset)
        if dataset is not None:
            data_node = TrackingGraph.get_node_for_tracked_object(obj=dataset)
            if dataset_name:
                data_node.set_node_name_if_not_final(name=dataset_name)
            model_node.add_predecessor(predecessor_node=data_node, operations={operation})
    set_dataset_info_and_maybe_upload(dataset_obj=dataset)


def is_dataset_obj(orig_obj):
    if not TrackingGraph.has_tracked_obj(obj=orig_obj):
        return False
    dataset_node = TrackingGraph.get_node_for_tracked_object(obj=orig_obj)
    return dataset_node.node_type == BaseTrackingNode.Type.DATA


def set_dataset_node_path_from_node(dataset_node, filename, file_path, created_in_run, node_name):
    if node_name:
        dataset_node.set_node_name(name=node_name)
    else:
        dataset_node.set_node_name(name=filename)
    dataset_node.set_data_path(path=file_path)
    if not created_in_run:
        dataset_node.set_created_in_run(val=False)


def set_dataset_node_path(orig_obj, file_path, created_in_run=True, node_name=None, upload=True):
    filename, file_path = safe_extract_name_and_path(args=(file_path,), kwargs=dict())
    if len(filename) > 0 and TrackingGraph.has_tracked_obj(obj=orig_obj):
        arr_node = TrackingGraph.get_node_for_tracked_object(obj=orig_obj)
        set_dataset_node_path_from_node(arr_node, filename, file_path, created_in_run, node_name)
        if upload:
            set_dataset_info_and_upload(dataset_obj=orig_obj)
        else:
            set_dataset_info(dataset_obj=orig_obj)


def remove_predecessors(ret_val):
    existing_ret_val_node = TrackingGraph.get_node_for_tracked_object(obj=ret_val)
    ret_val_node = copy.copy(existing_ret_val_node)
    ret_val_node.predecessors = weakref.WeakKeyDictionary()
    ret_val_node.successors = weakref.WeakSet()
    ret_val_node.references = list()
    TrackingGraph.add_tracked_object(obj=ret_val, node=ret_val_node, replace_existing=True)
    return ret_val_node
