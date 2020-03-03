from scrybe.internal.threading_util import *
from scrybe.internal.tracker.metrics import get_model_artifact_node
from scrybe.internal.tracker.save_and_load_tracker import save_func_after_decorator, deserialize_func_after_decorator
from scrybe.internal.tracker.tracker_util import predict_handler, all_func_enable_patching_decorator, \
    create_db_bulk_metric, create_model_payload
from scrybe.internal.tracker.xgb_decorator_func.xgb_util import *
from scrybe.internal.util import get_func_arg_names, get_func_req_params, get_module_name


def artifact_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    func_name = orig_func.__name__
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    arg_names = get_func_arg_names(orig_func)
    metrics_dict, object_type = handle_artifact(arg_obj_names, kwargs_obj_names, ret_val, func_name, arg_names,
                                                *args, **kwargs)
    if metrics_dict is None:
        return
    model_obj, y_true = get_func_req_params(arg_names, [0, 1], *args, **kwargs)
    model_name, y_true_name = get_func_req_params(arg_names, [0, 1], *arg_obj_names, **kwargs_obj_names)
    local_name_dict = {"y_true": y_true_name, "model": model_name}
    artifact_node = get_model_artifact_node(y_true=y_true, model_obj=model_obj, ret_val=ret_val,
                                            object_type=object_type, artifact_identifier=func_name,
                                            local_name_dict=local_name_dict)
    if artifact_node is None:
        return
    artifact_node.add_metric(metrics_dict)
    DataReceiver.receive_batch(data_dict_list=artifact_node.prepare_for_upload())


def metric_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    arg_names = get_func_arg_names(orig_func)
    value = get_scalar_value(ret_val)
    if value is None:
        return
    metric_name = get_func_req_params(arg_names, [2], *args, **kwargs)
    metrics = {metric_name: value}
    create_db_bulk_metric(arg_obj_names, kwargs_obj_names, ret_val, metrics, arg_names, *args, **kwargs)


def evaluate_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    model_obj = args[0]
    model_name = arg_obj_names[0]
    arg_names = get_func_arg_names(orig_func)
    x_test, y_test = get_func_req_params(arg_names, [1, 2], *args, **kwargs)
    if arg_names[2] != "y":
        y_test = x_test
    x_test_name, y_test_name = get_func_req_params(arg_names, [1, 2], *arg_obj_names, **kwargs_obj_names)
    local_name_dict = {"y_true": y_test_name, "x_test": x_test_name, "model": model_name}
    func_name = orig_func.__name__
    metrics = dict()
    if isinstance(ret_val, dict):
        for key, value in ret_val.items():
            value = get_scalar_value(value)
            if value is not None:
                metrics[key] = value
    else:
        value = get_scalar_value(ret_val)
        metrics[func_name] = value
    set_support(dataset=x_test, metric_dict=metrics, metric_key="support")
    metric_tuple = get_eval_metric_node(y_true=y_test, x_test=x_test, ret_val=ret_val, model=model_obj,
                                        metric_names=list(metrics.keys()), local_name_dict=local_name_dict)
    if metric_tuple is None:
        return
    metric_node, metric_seq_dict = metric_tuple
    metrics.update(metric_seq_dict)
    metric_node.add_metric(metrics)
    DataReceiver.receive_batch(data_dict_list=metric_node.prepare_for_upload())


@all_func_enable_patching_decorator
def predict_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    return predict_handler(arg_obj_names, kwargs_obj_names, ret_val, orig_func, *args, **kwargs)


def class_func_before_decorator(metadata_dict, orig_func, scrybe_orig_fn_frame, *args, **kwargs):
    module_name = get_module_name(scrybe_orig_fn_frame)
    if module_name.startswith('xgboost.sklearn') or module_name.startswith(
            'lightgbm.sklearn') or module_name.startswith('scrybe'):
        return False
    ThreadLocalVarHandler.all_func.disable_patching()


def class_func_exception_handler_decorator(metadata_dict, orig_func, ret_val, *args, **kwargs):
    ThreadLocalVarHandler.all_func.enable_patching()


@all_func_enable_patching_decorator
def xgb_class_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    arg_names = get_func_arg_names(orig_func)
    eval_index = arg_names.index('eval_set')
    model_obj, x_train, y_train, eval_set = get_func_req_params(arg_names, [0, 1, 2, eval_index], *args,
                                                                **kwargs)
    model_name, x_train_name, y_train_name = get_func_req_params(arg_names, [0, 1, 2],
                                                                 *arg_obj_names, **kwargs_obj_names)
    local_name_dict = {"model": model_name, "x_sample": x_train_name, "y_sample": y_train_name}
    param_getter = "get_params"
    try:
        from catboost import CatBoost
        if isinstance(model_obj, CatBoost):
            param_getter = "get_all_params"
    except ImportError:
        pass
    create_model_payload(model_obj, x_train, y_train, local_name_dict, metadata_dict, param_getter)
    set_metrics(model_obj=model_obj, x_train=x_train, y_train=y_train, eval_set=eval_set,
                local_name_dict=local_name_dict)


def patch(patcher_obj):
    func_to_patch_list = ['fit', 'predict', 'predict_proba', 'predict_log_proba']
    for module_name, class_prefix in XGB_MODULES:
        for func_to_patch in func_to_patch_list:
            func_name = class_prefix + '.' + func_to_patch
            patcher_obj.register_before(module_name, func_name, class_func_before_decorator)
            patcher_obj.register_exception_handler(module_name, func_name, class_func_exception_handler_decorator)
            if func_to_patch == 'fit':
                patcher_obj.register_after(module_name, func_name, xgb_class_func_after_decorator)
            else:
                patcher_obj.register_after(module_name, func_name, predict_func_after_decorator)
        patcher_obj.register_after(module_name, class_prefix + '.' + 'save_model', save_func_after_decorator)
        patcher_obj.register_after(module_name, class_prefix + '.' + 'load_model', deserialize_func_after_decorator)
        if class_prefix.startswith('CatBoost'):
            patcher_obj.register_after(module_name, class_prefix + '.' + 'score', evaluate_func_after_decorator)
            patcher_obj.register_after(module_name, class_prefix + '.' + 'eval_metrics', evaluate_func_after_decorator)
    patcher_obj.register_after('catboost.utils', 'eval_metric', metric_func_after_decorator)
    artifact_funcs = ['get_confusion_matrix', 'get_roc_curve', 'get_fpr_curve', 'get_fnr_curve']
    for func_to_patch in artifact_funcs:
        patcher_obj.register_after('catboost.utils', func_to_patch, artifact_func_after_decorator)
