import ntpath

from scrybe.internal.const import KERAS_APPROACH
from scrybe.internal.depgraph import TrackingGraph
from scrybe.internal.tracker.data.missed_dataset_handler import track_data
from scrybe.internal.tracker.data.utils import safe_extract_name_and_path, is_dataset_obj, set_dataset_node_path
from scrybe.internal.uploader import DataReceiver
from scrybe.internal.util import get_func_arg_names, get_func_req_params
from .model import get_or_create_model_node, is_model_obj
from .nnet_decorator_func.nnet_util import get_architecture, get_keras_hyperparameters
from .sklearn_decorator_func.sklearn_util import maybe_create_model_node_after_deserialization

SAVE_FUNCTIONS = [
    # FIXME(chandra): pickle.dump is not getting patched
    ('pickle', 'dump'),
    ('joblib.numpy_pickle', 'dump'),
    ('pandas.core.generic', 'NDFrame.to_csv'),
    ('pandas.core.generic', 'NDFrame.to_pickle'),
]

LOAD_FUNCTIONS = [
    ('pickle', 'load'),
    ('joblib.numpy_pickle', 'load'),
]

H5PY_DATASET_LOAD = [
    ('h5py._hl.dataset', 'Dataset.__getitem__')
]

H5PY_DATASET_SAVE = [
    ('h5py._hl.group', 'Group.create_dataset')
]


def is_numpy_array(obj):
    try:
        import numpy as np
        if obj is not None and isinstance(obj, np.ndarray):
            return True
    except Exception:
        pass
    return False


def maybe_track_dataset_and_set_path(orig_obj, file_path, upload, created_in_run=True, node_name=None):
    if not is_numpy_array(obj=orig_obj):
        return None
    try:
        if not TrackingGraph.has_tracked_obj(obj=orig_obj):
            # This is a case of missed/bad data tracking -- better patch it up
            orig_obj = track_data(data_obj=orig_obj)
        set_dataset_node_path(orig_obj=orig_obj, file_path=file_path, created_in_run=created_in_run,
                              node_name=node_name, upload=upload)
        return orig_obj
    except Exception:
        # The error has been produced because a weakref cannot be created on this data type
        pass
    return None


def track_h5py_dataset_getitem_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    dataset = args[0]
    file_path = None
    created_in_run = True
    if hasattr(dataset, 'file') and hasattr(dataset.file, 'filename'):
        file_path = dataset.file.filename
        if file_path:
            created_in_run = False
    tracked_obj = maybe_track_dataset_and_set_path(orig_obj=ret_val, file_path=file_path, created_in_run=created_in_run,
                                                   upload=False)
    if tracked_obj is not None:
        ret_val = tracked_obj
    return ret_val


def track_h5py_create_dataset_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_names = get_func_arg_names(orig_func)
    h5_obj, data_obj_name, data_obj = get_func_req_params(arg_names, [0, 1, 4], *args, **kwargs)
    file_path = None
    if hasattr(h5_obj, 'file') and hasattr(h5_obj.file, 'filename'):
        file_path = h5_obj.file.filename
    if not file_path:
        return
    if TrackingGraph.has_tracked_obj(obj=data_obj):
        set_dataset_node_path(orig_obj=data_obj, file_path=file_path, created_in_run=True, node_name=data_obj_name)
    else:
        maybe_track_dataset_and_set_path(orig_obj=data_obj, file_path=file_path, created_in_run=True,
                                         node_name=data_obj_name, upload=True)


def deserialize_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    orig_object = ret_val
    if orig_object is None:
        return
    # TODO(chandra): Associate this filename with s3 path
    if len(args) > 0:
        file_obj = args[0]
    else:
        arg_names = get_func_arg_names(orig_func)
        file_obj = kwargs[arg_names[0]]
    filename, file_path = safe_extract_name_and_path(args=(file_obj,), kwargs=dict())
    tracked_obj = maybe_track_dataset_and_set_path(orig_obj=orig_object, file_path=file_path, created_in_run=False,
                                                   upload=False)
    if tracked_obj is not None:
        return tracked_obj
    maybe_create_model_node_after_deserialization(orig_object, file_path, filename)


def keras_load_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_names = get_func_arg_names(orig_func)
    if ret_val is not None:
        # In case of load()
        orig_model = ret_val
        if len(args) > 0:
            file_path = args[0]
        else:
            file_path = kwargs[arg_names[0]]
    else:
        # In case of load_weights
        orig_model, file_path = get_func_req_params(arg_names, [0, 1], *args, **kwargs)
    # TODO(chandra): Associate this filename with s3 path
    filename, file_path = safe_extract_name_and_path(args=(file_path,), kwargs=dict())
    model_node = get_or_create_model_node(orig_model, approach=KERAS_APPROACH, name=filename, path=file_path,
                                          create_new=True, created_in_run=False)
    model_node.set_architecture(get_architecture(orig_model))
    model_node.set_hyperparams(get_keras_hyperparameters(params={}, model=orig_model))
    DataReceiver.receive_batch(data_dict_list=model_node.prepare_for_upload())
    # log_upload_data_to_file(upload_data=model_node.prepare_for_upload(), func_name=orig_func.__name__)


def save_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_names = get_func_arg_names(orig_func)
    orig_obj, file_obj = get_func_req_params(arg_names, [0, 1], *args, **kwargs)
    filename, file_path = safe_extract_name_and_path(args=(file_obj,), kwargs=dict())
    if not filename:
        return
    if is_model_obj(orig_obj):
        model_node = get_or_create_model_node(orig_obj)
        model_node.set_path(file_path)
        model_node.set_node_name(filename)
        DataReceiver.receive_batch(data_dict_list=model_node.prepare_for_upload())
    elif is_dataset_obj(orig_obj=orig_obj):
        set_dataset_node_path(orig_obj=orig_obj, file_path=file_path, created_in_run=True)
    elif is_numpy_array(obj=orig_obj):
        maybe_track_dataset_and_set_path(orig_obj=orig_obj, file_path=file_path, created_in_run=True, upload=True)


def patch(patcher_obj):
    for module_name, function_name in SAVE_FUNCTIONS:
        patcher_obj.register_after(module_name, function_name, save_func_after_decorator)
    for module_name, function_name in LOAD_FUNCTIONS:
        patcher_obj.register_after(module_name, function_name, deserialize_func_after_decorator)
    for module_name, function_name in H5PY_DATASET_LOAD:
        patcher_obj.register_after(module_name, function_name, track_h5py_dataset_getitem_after_decorator)
    for module_name, function_name in H5PY_DATASET_SAVE:
        patcher_obj.register_after(module_name, function_name, track_h5py_create_dataset_after_decorator)
