from scrybe.internal.const import TRAIN_METRICS_PREFIX, VAL_METRICS_PREFIX
from scrybe.internal.depgraph.nodes import ArtifactType
from scrybe.internal.tracker.metrics import get_train_metric_node, get_eval_metric_node, get_validation_metric_node
from scrybe.internal.tracker.tracker_util import set_support, handle_confusion_matrix, handle_curve
from scrybe.internal.uploader import DataReceiver

XGB_MODULES = [
    ('xgboost.sklearn', 'XGBClassifier'),
    ('xgboost.sklearn', 'XGBRFClassifier'),
    ('xgboost.sklearn', 'XGBRegressor'),
    ('xgboost.sklearn', 'XGBRFRegressor'),
    ('lightgbm.sklearn', 'LGBMClassifier'),
    ('lightgbm.sklearn', 'LGBMRegressor'),
    ('catboost.core', 'CatBoost'),
    ('catboost.core', 'CatBoostClassifier'),
    ('catboost.core', 'CatBoostRegressor'),
]


def handle_artifact(arg_obj_names, kwargs_obj_names, ret_val, func_name, arg_names, *args, **kwargs):
    func_artifact_map = {
        'get_confusion_matrix': (handle_confusion_matrix, ArtifactType.TABLE, 'confusion_matrix'),
        'get_roc_curve': (handle_curve, ArtifactType.PLOT_DATA, 'roc_curve'),
        'get_fpr_curve': (handle_curve, ArtifactType.PLOT_DATA, 'fpr_curve'),
        'get_fnr_curve': (handle_curve, ArtifactType.PLOT_DATA, 'fnr_curve'),
    }
    if func_name in func_artifact_map:
        func_callable, obj_type, metric_name = func_artifact_map[func_name]
        artifact = func_callable(arg_obj_names, kwargs_obj_names, ret_val, metric_name, arg_names, *args, **kwargs)
        return artifact, obj_type
    return None, None


def get_scalar_value(value):
    if isinstance(value, (list, tuple)) and len(value) > 0:
        value = value[-1]
    try:
        if not isinstance(value, str):
            float_value = float(value)
            int_value = int(value)
            if int_value == float_value:
                return int_value
            else:
                return float_value
    except Exception as e:
        return None


def get_eval_metrics(x_eval, key_prefix, evals_result_metrics):
    metrics = dict()
    set_support(dataset=x_eval, metric_dict=metrics, metric_key=key_prefix + 'support')
    for key in evals_result_metrics:
        if key_prefix == '':
            if isinstance(evals_result_metrics[key], list):
                metrics[key] = evals_result_metrics[key][-1]
            else:
                metrics[key] = evals_result_metrics[key]
        else:
            metrics[key_prefix + key] = evals_result_metrics[key]
    return metrics


def get_eval_data(eval_set, index):
    if isinstance(eval_set[index], (tuple, list)):
        x_eval, y_eval = eval_set[index]
    else:
        x_eval = eval_set[index]
        y_eval = None
    return x_eval, y_eval


def set_metrics(model_obj, x_train, y_train, eval_set, local_name_dict):
    if not hasattr(model_obj, 'evals_result_') or model_obj.evals_result_ is None:
        return
    if 'training' in model_obj.evals_result_ or 'learn' in model_obj.evals_result_:
        if 'training' in model_obj.evals_result_:
            evals_result_metrics = model_obj.evals_result_['training']
        else:
            evals_result_metrics = model_obj.evals_result_['learn']
        key_prefix = TRAIN_METRICS_PREFIX
        metrics = dict()
        set_support(dataset=x_train, metric_dict=metrics, metric_key=key_prefix + 'support')
        for key in evals_result_metrics:
            metrics[key_prefix + key] = evals_result_metrics[key]
        metric_node = get_train_metric_node(x_sample=x_train, y_sample=y_train, model=model_obj, ret_val=model_obj,
                                            local_name_dict=local_name_dict)
        if metric_node is None:
            return
        metric_node.add_metric(metrics)
        DataReceiver.receive_batch(data_dict_list=metric_node.prepare_for_upload())
    if eval_set is None:
        return
    if 'validation' in model_obj.evals_result_.keys():
        x_eval, y_eval = get_eval_data(eval_set=eval_set, index=0)
        evals_result_metrics = model_obj.evals_result_["validation"]
        metrics = get_eval_metrics(x_eval=x_eval, key_prefix=VAL_METRICS_PREFIX,
                                   evals_result_metrics=evals_result_metrics)
        metric_node = get_validation_metric_node(x_val=x_eval, y_val=y_eval, model=model_obj, ret_val=model_obj,
                                                 local_name_dict=local_name_dict)
        metric_node.add_metric(metrics)
        DataReceiver.receive_batch(data_dict_list=metric_node.prepare_for_upload())
    validation_index = -1
    for key in model_obj.evals_result_.keys():
        split_key = key.split('_')
        if len(split_key) < 2:
            continue
        try:
            index = int(split_key[-1])
        except Exception:
            continue
        if index > validation_index:
            validation_index = index
    for key in model_obj.evals_result_:
        split_key = key.split('_')
        if len(split_key) < 2:
            continue
        try:
            index = int(split_key[1])
        except Exception:
            continue
        if index >= len(eval_set):
            continue

        x_eval, y_eval = get_eval_data(eval_set=eval_set, index=index)
        evals_result_metrics = model_obj.evals_result_[key]
        key_prefix = ''
        if x_eval is x_train and y_eval is y_train:
            key_prefix = TRAIN_METRICS_PREFIX
        elif index == validation_index:
            key_prefix = VAL_METRICS_PREFIX
        metrics = get_eval_metrics(x_eval=x_eval, key_prefix=key_prefix, evals_result_metrics=evals_result_metrics)
        if key_prefix == TRAIN_METRICS_PREFIX:
            metric_node = get_train_metric_node(x_sample=x_eval, y_sample=y_eval, model=model_obj, ret_val=model_obj,
                                                local_name_dict=local_name_dict)
        elif key_prefix == VAL_METRICS_PREFIX:
            metric_node = get_validation_metric_node(x_val=x_eval, y_val=y_eval, model=model_obj, ret_val=model_obj,
                                                     local_name_dict=local_name_dict)
        else:
            metric_tuple = get_eval_metric_node(y_true=y_eval, x_test=x_eval, ret_val=model_obj, model=model_obj,
                                                metric_names=list(metrics.keys()), local_name_dict=local_name_dict)
            if metric_tuple is None:
                return
            metric_node, metric_seq_dict = metric_tuple
            metrics.update(metric_seq_dict)
        if metric_node is None:
            return
        metric_node.add_metric(metrics)
        DataReceiver.receive_batch(data_dict_list=metric_node.prepare_for_upload())
