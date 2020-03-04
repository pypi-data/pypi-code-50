from scrybe.internal.config import Config
from scrybe.internal.patcher import get_wrapper
from scrybe.internal.tracker.metrics import get_data_artifact_node
from scrybe.internal.tracker.stats_decorator_func.stats_util import *
from scrybe.internal.tracker.data.utils import set_dataset_info_and_maybe_upload
from scrybe.internal.uploader import DataReceiver
from scrybe.internal.util import get_module_name, is_site_package_caller, get_func_arg_names, get_func_req_params


def create_and_upload_stats(ret_val, dataset_1, dataset_2, stats, artifact_type, artifact_identifier, local_name_dict):
    data_stats_node = get_data_artifact_node(dataset_1=dataset_1, dataset_2=dataset_2, ret_val=ret_val,
                                             object_type=artifact_type, artifact_identifier=artifact_identifier,
                                             local_name_dict=local_name_dict)
    if data_stats_node is None:
        return
    data_stats_node.add_metric(stats)
    set_dataset_info_and_maybe_upload(dataset_obj=dataset_1)
    set_dataset_info_and_maybe_upload(dataset_obj=dataset_2)
    DataReceiver.receive_batch(data_dict_list=data_stats_node.prepare_for_upload())


def stats_func_before_decorator(metadata_dict, orig_func, scrybe_orig_fn_frame, *args, **kwargs):
    module_name = get_module_name(scrybe_orig_fn_frame)
    if module_name.startswith('scrybe') or is_site_package_caller(scrybe_orig_fn_frame):
        return False


def stats_func_calc_metric_and_upload(dataset, ret_val, stats_func_name, axis, local_name_dict):
    metric = get_metric(obj=ret_val, stats_func=stats_func_name, axis=axis)
    if metric is None:
        return
    stats, artifact_type = metric
    artifact_identifier = get_artifact_identifier(artifact_type=artifact_type, stats_type="stats")
    stats = {artifact_identifier: stats}
    create_and_upload_stats(ret_val=ret_val, dataset_1=dataset, dataset_2=None, stats=stats,
                            artifact_type=artifact_type, artifact_identifier=artifact_identifier,
                            local_name_dict=local_name_dict)


def stats_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    arg_names = get_func_arg_names(orig_func)
    dataset = get_func_req_params(arg_names, [0], *args, **kwargs)
    if len(dataset) < Config.get_min_data_rows_for_stats():
        return
    axis = get_param('axis', arg_names, orig_func, *args, **kwargs)
    dataset_name = get_func_req_params(arg_names, [0], *arg_obj_names, **kwargs_obj_names)
    local_name_dict = {"dataset_1": dataset_name}
    stats_func_calc_metric_and_upload(dataset=dataset, ret_val=ret_val, stats_func_name=orig_func.__name__, axis=axis,
                                      local_name_dict=local_name_dict)


def quantile_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    arg_names = get_func_arg_names(orig_func)
    dataset, q = get_func_req_params(arg_names, [0, 1], *args, **kwargs)
    stats_func = str(int(q * 100)) + "%"
    if len(dataset) < Config.get_min_data_rows_for_stats():
        return
    axis = get_param('axis', arg_names, orig_func, *args, **kwargs)
    dataset_name = get_func_req_params(arg_names, [0], *arg_obj_names, **kwargs_obj_names)
    local_name_dict = {"dataset_1": dataset_name}
    stats_func_calc_metric_and_upload(dataset=dataset, ret_val=ret_val, stats_func_name=stats_func, axis=axis,
                                      local_name_dict=local_name_dict)


def ndframe_stats_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    func_to_patch = ret_val
    cls_obj = args[0]
    if not hasattr(cls_obj, '__module__') or not hasattr(cls_obj, '__name__'):
        return
    module_name = cls_obj.__module__
    class_name = cls_obj.__name__
    if not module_name in ['pandas.core.series', 'pandas.core.frame'] or not class_name in ['DataFrame', 'Series']:
        return
    arg_names = get_func_arg_names(orig_func)
    stats_func_name = get_func_req_params(arg_names, [1], *args, **kwargs)
    if stats_func_name not in STATS_FUNCS:
        return
    ret_val = get_wrapper(func_to_patch, before=[stats_func_before_decorator], after=[stats_func_after_decorator],
                          exception_handler=None)
    return ret_val


def values_stats_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_names = get_func_arg_names(orig_func)
    dataset_obj = get_func_req_params(arg_names, [0], *args, **kwargs)
    if len(dataset_obj) < Config.get_min_data_rows_for_stats():
        return
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    dataset_obj_name = get_func_req_params(arg_names, [0], *arg_obj_names, **kwargs_obj_names)
    local_name_dict = {"dataset_1": dataset_obj_name}
    stats = get_values(ret_val, orig_func, *args, **kwargs)
    if stats is None:
        return
    artifact_type = ArtifactType.DATA_VALUES
    artifact_identifier = get_artifact_identifier(artifact_type=artifact_type, stats_type='stats')
    stats = {artifact_identifier: stats}
    create_and_upload_stats(ret_val=ret_val, dataset_1=dataset_obj, dataset_2=None, stats=stats,
                            artifact_type=artifact_type, artifact_identifier=artifact_identifier,
                            local_name_dict=local_name_dict)


def co_with_self_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    if orig_func.__name__.startswith('cov'):
        stats_name = 'covariance'
    elif orig_func.__name__.startswith('corr'):
        stats_name = 'correlation'
    else:
        return
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    arg_names = get_func_arg_names(orig_func)
    dataset = get_func_req_params(arg_names, [0], *args, **kwargs)
    if len(dataset) < Config.get_min_data_rows_for_stats():
        return
    method = get_param('method', arg_names, orig_func, *args, **kwargs)
    dataset_2 = get_param('other', arg_names, orig_func, *args, **kwargs)
    dataset_2_name = None
    if dataset_2 is not None:
        dataset_2_index = arg_names.index('other')
        dataset_2_name = get_func_req_params(arg_names, [dataset_2_index], *arg_obj_names, **kwargs_obj_names)
    if dataset_2 is None:
        dataset_2 = get_param('y', arg_names, orig_func, *args, **kwargs)
        if dataset_2 is not None:
            dataset_2_index = arg_names.index('y')
            dataset_2_name = get_func_req_params(arg_names, [dataset_2_index], *arg_obj_names, **kwargs_obj_names)
    dataset_name = get_func_req_params(arg_names, [0], *arg_obj_names, **kwargs_obj_names)
    local_name_dict = {"dataset_1": dataset_name, "dataset_2": dataset_2_name}
    metric = get_co_stats(obj=ret_val)
    if metric is None:
        return
    if isinstance(metric, tuple):
        stats, artifact_type = metric
    else:
        stats = {orig_func.__name__: metric}
        artifact_type = ArtifactType.STATS_NUMBER
    if method is not None:
        stats = {stats_name: {method: stats}}
    else:
        stats = {stats_name: stats}
    artifact_identifier = stats_name
    create_and_upload_stats(ret_val=ret_val, dataset_1=dataset, dataset_2=dataset_2, stats=stats,
                            artifact_type=artifact_type, artifact_identifier=artifact_identifier,
                            local_name_dict=local_name_dict)


def patch(patcher_obj):
    for module_name, func_name in PANDAS_NUMPY_STATS:
        patcher_obj.register_before(module_name, func_name, stats_func_before_decorator)
        patcher_obj.register_after(module_name, func_name, stats_func_after_decorator)

    for module_name, func_name in NDFRAME_STATS:
        patcher_obj.register_after(module_name, func_name, ndframe_stats_func_after_decorator)

    for module_name, func_name in VALUE_STATS:
        patcher_obj.register_before(module_name, func_name, stats_func_before_decorator)
        patcher_obj.register_after(module_name, func_name, values_stats_func_after_decorator)

    for module_name, func_name in QUANTILE_STATS:
        patcher_obj.register_before(module_name, func_name, stats_func_before_decorator)
        patcher_obj.register_after(module_name, func_name, quantile_func_after_decorator)

    for module_name, func_name in CO_STATS:
        patcher_obj.register_before(module_name, func_name, stats_func_before_decorator)
        patcher_obj.register_after(module_name, func_name, co_with_self_func_after_decorator)
