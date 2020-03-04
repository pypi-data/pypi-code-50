import logging
import uuid

from scrybe.internal.const import SCRYBE_GRID_ID_KEY, SCRYBE_GRID_MODEL_INFO_LIST, \
    SCRYBE_GRID_ESTIMATOR, SCRYBE_GRID_ID_KEY_KEYID, SCRYBE_GRID_MODEL_INFO_LIST_KEYID, SCRYBE_GRID_ESTIMATOR_KEYID
from scrybe.internal.depgraph import TrackingGraph
from scrybe.internal.threading_util import *
from scrybe.internal.tracker.data.utils import remove_predecessors
from scrybe.internal.tracker.metrics import create_curve_artifact_associations
from scrybe.internal.tracker.model import is_model_obj, remove_obj_from_pipeline_list, get_or_create_pipeline_node
from scrybe.internal.tracker.tracker_util import predict_handler, create_model_payload, create_pipeline_model_payload, \
    pipeline_transform_handler, get_args_with_tracked_datasets, all_func_enable_patching_decorator, \
    stats_enable_patching_decorator
from scrybe.internal.util import get_func_arg_names, get_func_req_params, get_module_name
from .sklearn_util import CLASSIFICATION_FUNCTIONS, PIPELINE_FUNCTIONS, METRICS_FUNCTIONS, ARTIFACT_FUNCTIONS, \
    PLOT_DATA, get_pipeline_db_parameters, create_db_metric, create_db_artifact, upload_best_estimator_and_metric, \
    is_scrybe_patched_model, FEATURE_UNION_FUNCTIONS

LOGGER = logging.getLogger("scrybe_logger")


def grid_func_before_decorator(metadata_dict, orig_func, *args, **kwargs):
    grid_search_obj = args[0]
    arg_names = get_func_arg_names(orig_func)
    args, kwargs = get_args_with_tracked_datasets([1, 2], arg_names, *args, **kwargs)
    if hasattr(grid_search_obj, "estimator") and is_scrybe_patched_model(model_obj=grid_search_obj.estimator):
        kwargs[SCRYBE_GRID_ID_KEY] = {SCRYBE_GRID_ID_KEY_KEYID: str(uuid.uuid4())}
        kwargs[SCRYBE_GRID_MODEL_INFO_LIST] = {SCRYBE_GRID_MODEL_INFO_LIST_KEYID: list()}
        kwargs[SCRYBE_GRID_ESTIMATOR] = {SCRYBE_GRID_ESTIMATOR_KEYID: grid_search_obj.estimator}
    Config.disable_src_code_tracking()
    return args, kwargs


def grid_func_exception_handler_decorator(metadata_dict, orig_func, self_obj, *args, **kwargs):
    Config.enable_src_code_tracking()
    ThreadLocalVarHandler.stats.enable_patching()


def grid_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    Config.enable_src_code_tracking()
    upload_best_estimator_and_metric(metadata_dict, ret_val, orig_func, *args, **kwargs)


def split_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    cv_id = str(uuid.uuid4())
    for train_index, test_index in ret_val:
        if TrackingGraph.has_tracked_obj(obj=train_index):
            train_index_node = TrackingGraph.get_node_for_tracked_object(obj=train_index)
            train_index_node.set_cv_id(cv_id=cv_id)
        yield train_index, test_index


def plot_data_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    func_name = orig_func.__name__
    arg_names = get_func_arg_names(orig_func)
    y_true, y_pred = get_func_req_params(arg_names, [0, 1], *args, **kwargs)
    y_true_name, y_pred_name = get_func_req_params(arg_names, [0, 1], *arg_obj_names, **kwargs_obj_names)
    local_dict_name = {"y_true": y_true_name, "y_pred": y_pred_name}
    ret_val = create_curve_artifact_associations(ret_val=ret_val, y_true=y_true, y_pred=y_pred,
                                                 local_name_dict=local_dict_name)
    create_db_artifact(arg_obj_names, kwargs_obj_names, ret_val, func_name, arg_names, *args, **kwargs)
    return ret_val


def artifact_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    unset_metric_in_progress()
    func_name = orig_func.__name__
    arg_names = get_func_arg_names(orig_func)
    create_db_artifact(arg_obj_names, kwargs_obj_names, ret_val, func_name, arg_names, *args, **kwargs)


def metric_func_before_decorator(metadata_dict, orig_func, *args, **kwargs):
    if is_metric_in_progress():
        return False
    else:
        set_metric_in_progress()


def metric_func_exception_handler_decorator(metadata_dict, orig_func, ret_val, *args, **kwargs):
    unset_metric_in_progress()


def metric_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    unset_metric_in_progress()
    func_name = orig_func.__name__
    arg_names = get_func_arg_names(orig_func)
    create_db_metric(arg_obj_names, kwargs_obj_names, ret_val, func_name, arg_names, *args, **kwargs)


def pipeline_score_func_before_decorator(metadata_dict, orig_func, *args, **kwargs):
    ThreadLocalVarHandler.stats.disable_patching()


def pipeline_score_func_exception_handler_decorator(metadata_dict, orig_func, self_obj, *args, **kwargs):
    ThreadLocalVarHandler.stats.enable_patching()


@stats_enable_patching_decorator
def pipeline_score_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    # IMP: You cannot call inspect.signature(orig_func) here because it is not a callable
    func_name = orig_func.__name__
    arg_names = ['X', 'y']
    args = args[1:]
    create_db_metric(arg_obj_names, kwargs_obj_names, ret_val, func_name, arg_names, *args, **kwargs)


def predict_func_after_handler(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    if TrackingGraph.has_tracked_obj(obj=ret_val):
        remove_predecessors(ret_val)
    ret_val = predict_handler(arg_obj_names, kwargs_obj_names, ret_val, orig_func, *args, **kwargs)
    return ret_val


@all_func_enable_patching_decorator
def predict_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    return predict_func_after_handler(metadata_dict, ret_val, orig_func, *args, **kwargs)


def class_func_before_decorator(metadata_dict, orig_func, scrybe_orig_fn_frame, *args, **kwargs):
    module_name = get_module_name(scrybe_orig_fn_frame)
    if module_name.startswith('sklearn.ensemble') or module_name.startswith('scrybe'):
        return False
    ThreadLocalVarHandler.all_func.disable_patching()
    return args, kwargs


def class_func_exception_handler_decorator(metadata_dict, orig_func, ret_val, *args, **kwargs):
    ThreadLocalVarHandler.all_func.enable_patching()


@all_func_enable_patching_decorator
def class_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    x_train, y_train = get_func_req_params(get_func_arg_names(orig_func), [1, 2], *args, **kwargs)
    model_name, x_train_name, y_train_name = get_func_req_params(get_func_arg_names(orig_func), [0, 1, 2],
                                                                 *arg_obj_names, **kwargs_obj_names)
    local_name_dict = {"model": model_name, "x_sample": x_train_name, "y_sample": y_train_name}
    create_model_payload(ret_val, x_train, y_train, local_name_dict, metadata_dict)


def pipeline_func_before_decorator(metadata_dict, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    self_obj = args[0]
    # IMP: You cannot call inspect.signature(orig_func) here because it is not a callable
    arg_names = ['self', 'X', 'y']
    x_train, y_train = get_func_req_params(arg_names, [1, 2], *args, **kwargs)
    model_name, x_train_name, y_train_name = get_func_req_params(arg_names, [0, 1, 2], *arg_obj_names,
                                                                 **kwargs_obj_names)
    local_name_dict = {"model": model_name, "x_sample": x_train_name, "y_sample": y_train_name}
    approach, parent_models, hyperparameters = get_pipeline_db_parameters(self_obj)
    architecture = dict()
    pipeline_node = get_or_create_pipeline_node(self_obj, hyperparameters, architecture, x_sample=x_train,
                                                y_sample=y_train, approach=approach, create_new=True,
                                                parent_models=parent_models, is_pipeline_obj=True,
                                                local_name_dict=local_name_dict)
    LOGGER.debug("%s model before call using %s function. client_id=%s" % (approach, orig_func.__name__,
                                                                           pipeline_node.client_id))
    ThreadLocalVarHandler.stats.disable_patching()


def pipeline_func_exception_handler_decorator(metadata_dict, orig_func, self_obj, *args, **kwargs):
    ThreadLocalVarHandler.stats.enable_patching()
    remove_obj_from_pipeline_list(self_obj)


@stats_enable_patching_decorator
def pipeline_fit_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    remove_obj_from_pipeline_list(ret_val)
    if is_model_obj(ret_val):
        x_train, y_train = get_func_req_params(['self', 'X', 'y'], [1, 2], *args, **kwargs)
        create_pipeline_model_payload(model_obj=ret_val, x_train=x_train, y_train=y_train, metadata_dict=metadata_dict)


@stats_enable_patching_decorator
def pipeline_fit_transform_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    model_obj = args[0]
    remove_obj_from_pipeline_list(model_obj)
    if is_model_obj(model_obj):
        x_train, y_train = get_func_req_params(['self', 'X', 'y'], [1, 2], *args, **kwargs)
        create_pipeline_model_payload(model_obj=model_obj, x_train=x_train, y_train=y_train,
                                      metadata_dict=metadata_dict)
        return predict_func_after_handler(metadata_dict, ret_val, orig_func, *args, **kwargs)
    return pipeline_transform_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs)


def pipeline_transform_func_before_decorator(metadata_dict, orig_func, *args, **kwargs):
    ThreadLocalVarHandler.stats.disable_patching()


def pipeline_transform_func_exception_handler_decorator(metadata_dict, orig_func, self_obj, *args, **kwargs):
    ThreadLocalVarHandler.stats.enable_patching()


@stats_enable_patching_decorator
def pipeline_transform_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    model_obj = args[0]
    remove_obj_from_pipeline_list(model_obj)
    if is_model_obj(model_obj):
        return predict_func_after_handler(metadata_dict, ret_val, orig_func, *args, **kwargs)
    if TrackingGraph.has_tracked_obj(obj=ret_val):
        remove_predecessors(ret_val=ret_val)
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    ret_val = pipeline_transform_handler(arg_obj_names, kwargs_obj_names, ret_val, orig_func, *args, **kwargs)
    return ret_val


def patch(patcher_obj):

    # Register the pipeline fit methods
    for module_name, class_name in PIPELINE_FUNCTIONS:
        func_to_patch_list = ['fit', 'fit_transform', 'fit_predict']
        for func_to_patch in func_to_patch_list:
            func_name = class_name + '.' + func_to_patch
            patcher_obj.register_before(module_name, func_name, pipeline_func_before_decorator)
            patcher_obj.register_exception_handler(module_name, func_name, pipeline_func_exception_handler_decorator)
            if func_to_patch == 'fit':
                patcher_obj.register_after(module_name, func_name, pipeline_fit_func_after_decorator)
            else:
                patcher_obj.register_after(module_name, func_name, pipeline_fit_transform_func_after_decorator)
        func_to_patch_list = ['predict', 'predict_proba', 'predict_log_proba', 'decision_function', '_transform',
                              '_inverse_transform']
        for func_to_patch in func_to_patch_list:
            func_name = class_name + '.' + func_to_patch
            patcher_obj.register_before(module_name, func_name, pipeline_transform_func_before_decorator)
            patcher_obj.register_exception_handler(module_name, func_name,
                                                   pipeline_transform_func_exception_handler_decorator)
            patcher_obj.register_after(module_name, func_name, pipeline_transform_func_after_decorator)
        func_name = class_name + '.score'
        patcher_obj.register_before(module_name, func_name, pipeline_score_func_before_decorator)
        patcher_obj.register_exception_handler(module_name, func_name,
                                               pipeline_score_func_exception_handler_decorator)
        patcher_obj.register_after(module_name, func_name, pipeline_score_func_after_decorator)

    for module_name, func_name in FEATURE_UNION_FUNCTIONS:
        patcher_obj.register_before(module_name, func_name, pipeline_transform_func_before_decorator)
        patcher_obj.register_exception_handler(module_name, func_name,
                                               pipeline_transform_func_exception_handler_decorator)
        patcher_obj.register_after(module_name, func_name, pipeline_transform_func_after_decorator)

    # Register the fit methods
    for module_name, function_name in METRICS_FUNCTIONS:
        patcher_obj.register_before(module_name, function_name, metric_func_before_decorator)
        patcher_obj.register_exception_handler(module_name, function_name, metric_func_exception_handler_decorator)
        patcher_obj.register_after(module_name, function_name, metric_func_after_decorator)

    for module_name, class_name in CLASSIFICATION_FUNCTIONS:
        patcher_obj.register_before(module_name, class_name + '.fit', class_func_before_decorator)
        patcher_obj.register_exception_handler(module_name, class_name + '.fit', class_func_exception_handler_decorator)
        patcher_obj.register_after(module_name, class_name + '.fit', class_func_after_decorator)
        patcher_obj.register_before(module_name, class_name + '.predict', class_func_before_decorator)
        patcher_obj.register_exception_handler(module_name, class_name + '.predict',
                                               class_func_exception_handler_decorator)
        patcher_obj.register_after(module_name, class_name + '.predict', predict_func_after_decorator)
        patcher_obj.register_before(module_name, class_name + '.predict_proba', class_func_before_decorator)
        patcher_obj.register_exception_handler(module_name, class_name + '.predict_proba',
                                               class_func_exception_handler_decorator)
        patcher_obj.register_after(module_name, class_name + '.predict_proba', predict_func_after_decorator)

    for module_name, function_name in ARTIFACT_FUNCTIONS:
        patcher_obj.register_before(module_name, function_name, metric_func_before_decorator)
        patcher_obj.register_exception_handler(module_name, function_name, metric_func_exception_handler_decorator)
        patcher_obj.register_after(module_name, function_name, artifact_func_after_decorator)

    for module_name, function_name in PLOT_DATA:
        patcher_obj.register_after(module_name, function_name, plot_data_func_after_decorator)

    patcher_obj.register_before("sklearn.model_selection._search", 'BaseSearchCV.fit', grid_func_before_decorator)
    patcher_obj.register_exception_handler("sklearn.model_selection._search", 'BaseSearchCV.fit',
                                           grid_func_exception_handler_decorator)
    patcher_obj.register_after("sklearn.model_selection._search", 'BaseSearchCV.fit', grid_func_after_decorator)

    patcher_obj.register_after("sklearn.model_selection._split", 'BaseCrossValidator.split', split_func_after_decorator)
