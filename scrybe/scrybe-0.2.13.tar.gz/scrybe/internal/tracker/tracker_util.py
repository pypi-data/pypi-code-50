import copy
import functools
import logging
from typing import Iterable, Sized

from scrybe.internal.const import SCRYBE_CV_ID_KEY, SCRYBE_GRID_ID_KEY, SCRYBE_GRID_MODEL_INFO_LIST, \
    SCRYBE_GRID_ESTIMATOR, SCRYBE_GRID_ESTIMATOR_KEYID, SCRYBE_GRID_MODEL_INFO_LIST_KEYID, SCRYBE_GRID_ID_KEY_KEYID, \
    TRAIN_METRICS_PREFIX
from scrybe.internal.depgraph.nodes import BaseTrackingNode, ModelTrackingNode
from scrybe.internal.depgraph.ops import Operations
from scrybe.internal.depgraph.tracking_graph import TrackingGraph
from scrybe.internal.threading_util import ThreadLocalVarHandler
from scrybe.internal.tracker.data.missed_dataset_handler import track_data, track_data_if_possible
from scrybe.internal.tracker.data.utils import maybe_track_dataset_and_upload_info
from scrybe.internal.tracker.grid_search import GridModelTrainedInfo
from scrybe.internal.tracker.metrics import get_test_or_train_metric_node
from scrybe.internal.tracker.model import create_prediction_associations, create_transformation_associations, \
    set_custom_hyperparam
from scrybe.internal.tracker.model import get_or_create_model_node
from scrybe.internal.uploader import DataReceiver
from scrybe.internal.util import get_func_arg_names, get_func_req_params, get_default_params, get_hyperparams

LOGGER = logging.getLogger("scrybe_logger")


def warning_suppression_decorator(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            return func(*args, **kwargs)

    return inner


def set_model_features_and_importance(x_train, model_obj, model_node: ModelTrackingNode, grid_best_estimator=False):
    try:
        if hasattr(x_train, 'columns') and x_train.columns is not None and len(x_train.columns) > 0:
            model_node.set_features(list(x_train.columns))
        elif hasattr(x_train, "dtype") and hasattr(x_train.dtype, "names") and x_train.dtype.names is not None and len(
                x_train.dtype.names) > 0:
            model_node.set_features(list(x_train.dtype.names))
        elif hasattr(x_train, "get_feature_names"):
            features = x_train.get_feature_names()
            if features is not None:
                final_features = []
                index = 0
                for feature in features:
                    if not feature:
                        final_features.append("f" + str(index))
                    else:
                        final_features.append(feature)
                    index += 1
                if len(final_features) > 0:
                    model_node.set_features(final_features)
    except ImportError:
        pass

    def calc_feature_importance():
        if hasattr(model_obj, 'feature_importances_') and (
                not (model_node.grid_search_id or model_node.cross_validation_id) or grid_best_estimator):
            try:
                model_node.set_feature_importance(model_obj.feature_importances_)
            except Exception:
                pass
        elif model_node.approach.startswith("Pipeline"):
            num_model_predecessors = 0
            model_node_created_in_pipeline = None
            for predecessor_node, ops in model_node.predecessors.items():
                if predecessor_node.node_type == BaseTrackingNode.Type.MODEL and predecessor_node.is_created_in_pipeline:
                    num_model_predecessors += 1
                    if num_model_predecessors > 1:
                        break
                    model_node_created_in_pipeline = predecessor_node
            if num_model_predecessors == 1:
                predecessor_features = model_node_created_in_pipeline.get_features()
                if predecessor_features is not None and len(predecessor_features) > 0:
                    model_node.set_features(predecessor_features)
                model_node.set_feature_importance(model_node_created_in_pipeline.get_feature_importance())

    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        calc_feature_importance()


def upload_model_and_dataset_info(x_train, y_train, model_obj, model_node: ModelTrackingNode, approach):
    maybe_track_dataset_and_upload_info(dataset=x_train, operation=Operations.TRAINING_DATA, model_node=model_node)
    maybe_track_dataset_and_upload_info(dataset=y_train, operation=Operations.TRAINING_LABELS, model_node=model_node)
    set_model_features_and_importance(x_train=x_train, model_obj=model_obj, model_node=model_node)
    if not model_node.is_created_in_pipeline:
        DataReceiver.receive_batch(data_dict_list=model_node.prepare_for_upload())
        LOGGER.debug("Model of type:%s uploaded. client_id=%s" % (approach, model_node.client_id))


def get_args_with_tracked_datasets(index_list, arg_names, *args, **kwargs):
    datasets = get_func_req_params(arg_names, index_list, *args, **kwargs)
    if datasets is None:
        return args, kwargs
    if not (isinstance(datasets, list) or isinstance(datasets, tuple)):
        datasets = [datasets]
    for i in range(len(datasets)):
        dataset = datasets[i]
        if dataset is None or TrackingGraph.has_tracked_obj(obj=dataset):
            continue
        dataset = track_data_if_possible(data_obj=dataset)
        if dataset is not None:
            index = index_list[i]
            if len(args) > index:
                args = args[:index] + (dataset,) + args[index + 1:]
            else:
                kwargs[arg_names[index]] = dataset
    return args, kwargs


def extract_cv_id(x_train):
    if TrackingGraph.has_tracked_obj(obj=x_train):
        x_train_node = TrackingGraph.get_node_for_tracked_object(obj=x_train)
        indexer_node = x_train_node.find_nearest_node_with_op(op=Operations.INDEXER)
        # indexer_node = x_train_node.get_parent_with_op(op=Operations.INDEXER)
        if indexer_node is not None:
            return indexer_node.cv_id
    return None


def predict_handler(arg_obj_names, kwargs_obj_names, ret_val, orig_func, *args, **kwargs):
    local_name_dict = {}
    model = args[0]
    local_name_dict["model"] = arg_obj_names[0]
    # IMP: You cannot call inspect.signature(orig_func) here because it is not a callable
    if len(args) > 1:
        x_test = args[1]
        local_name_dict["x_test"] = arg_obj_names[0]
    else:
        from scrybe.internal.tracker.sklearn_decorator_func.sklearn_util import is_patched_pipeline_object
        if is_patched_pipeline_object(model):
            arg_names = ['self', 'X']
        else:
            arg_names = get_func_arg_names(orig_func=orig_func)
        x_test = kwargs[arg_names[1]]
        local_name_dict["x_test"] = kwargs_obj_names[arg_names[1]]

    if ret_val is not None and not TrackingGraph.has_tracked_obj(obj=ret_val):
        try:
            # This is a case of missed/bad data tracking -- better patch it up
            ret_val = track_data(data_obj=ret_val)
        except TypeError:
            # The error has been produced because a weakref cannot be created on this data type
            pass
    create_prediction_associations(x_test=x_test, y_pred=ret_val, model=model, local_name_dict=local_name_dict)
    return ret_val


def pipeline_transform_handler(arg_obj_names, kwargs_obj_names, ret_val, orig_func, *args, **kwargs):
    local_name_dict = dict()
    # IMP: You cannot call inspect.signature(orig_func) here because it is not a callable
    if len(args) > 1:
        x_test = args[1]
        local_name_dict["x_test"] = arg_obj_names[0]
    else:
        x_test = kwargs['X']
        local_name_dict["x_test"] = kwargs_obj_names['X']

    if ret_val is not None and not TrackingGraph.has_tracked_obj(obj=ret_val):
        try:
            # This is a case of missed/bad data tracking -- better patch it up
            ret_val = track_data(data_obj=ret_val)
        except TypeError:
            # The error has been produced because a weakref cannot be created on this data type
            pass
    create_transformation_associations(x_test=x_test, y_pred=ret_val, local_name_dict=local_name_dict)
    return ret_val


def create_associations(obj, target_obj_list: list):
    target_nodes = []
    for target_obj, obj_local_name in target_obj_list:
        if TrackingGraph.has_tracked_obj(obj=target_obj):
            target_node = TrackingGraph.get_node_for_tracked_object(obj=target_obj)
            target_node.set_node_name_if_not_final(obj_local_name)
            target_nodes.append(target_node)

    if len(target_nodes) == 0:
        return

    obj_node = TrackingGraph.get_node_for_tracked_object(obj=obj)
    for target_node in target_nodes:
        obj_node.add_predecessor(predecessor_node=target_node, operations={Operations.TRANSFORM})
        # In some cases, the model and/or base testing dataset can get collected. To avoid messing up the graph
        # we let y_pred keep a ref to the tracking node of the model and x_test
        obj_node.add_reference(node=target_node)


def get_cv_id(x_train, metadata_dict, hyperparameters, architecture):
    cv_id = extract_cv_id(x_train=x_train)

    # In case of GridSearch with CV, we need to manually do some grouping here. Basically, all models with
    # the same parameter should have one CV ID, which should be distinct from CV IDs of other models in the
    # search
    if cv_id is not None and SCRYBE_GRID_ID_KEY in metadata_dict and metadata_dict[SCRYBE_GRID_ID_KEY] is not None:
        model_info = GridModelTrainedInfo(architecture=architecture, params=hyperparameters)
        if model_info not in metadata_dict[SCRYBE_GRID_MODEL_INFO_LIST][SCRYBE_GRID_MODEL_INFO_LIST_KEYID]:
            metadata_dict[SCRYBE_GRID_MODEL_INFO_LIST][SCRYBE_GRID_MODEL_INFO_LIST_KEYID].append(model_info)
        model_idx = metadata_dict[SCRYBE_GRID_MODEL_INFO_LIST][SCRYBE_GRID_MODEL_INFO_LIST_KEYID].index(model_info)
        return "%d:%s" % (model_idx, cv_id)
    return cv_id


def handle_cv_grid_and_custom_param(metadata_dict, model_obj, model_node, x_train, hyperparameters):
    if SCRYBE_GRID_ESTIMATOR in metadata_dict and metadata_dict[SCRYBE_GRID_ESTIMATOR] is not None:
        set_custom_hyperparam(model_node=model_node,
                              estimator_obj=metadata_dict[SCRYBE_GRID_ESTIMATOR][SCRYBE_GRID_ESTIMATOR_KEYID],
                              hyperparams=hyperparameters)
    else:
        set_custom_hyperparam(model_node=model_node, estimator_obj=model_obj, hyperparams=hyperparameters)
    metadata_dict[SCRYBE_CV_ID_KEY] = get_cv_id(x_train=x_train, metadata_dict=metadata_dict,
                                                hyperparameters=hyperparameters, architecture=dict())
    model_node.set_cv_and_grid_id_if_possible(metadata_dict=metadata_dict)


def pre_process_params(params):
    our_params = copy.copy(params)
    try:
        if "random_state" in params:
            if our_params["random_state"].__class__.__name__ == "RandomState":
                del our_params["random_state"]
    except Exception as e:
        LOGGER.debug("Unable to remove RandomState from sklearn object. Error:%s" % str(e))
    finally:
        return our_params


@warning_suppression_decorator
def get_classification_model_node_parameters(orig_object, param_getter="get_params"):
    param_method = getattr(orig_object, param_getter)
    params = param_method()
    processed_params = pre_process_params(params)
    req_args, default_dict = get_default_params(orig_object)
    hyperparameters = get_hyperparams(processed_params, default_dict, req_args)
    approach = orig_object.__class__.__name__
    return approach, hyperparameters


def create_model_payload(model_obj, x_train, y_train, local_name_dict: dict, metadata_dict: dict,
                         param_getter="get_params"):
    approach, hyperparameters = get_classification_model_node_parameters(model_obj, param_getter=param_getter)
    model_node = get_or_create_model_node(model=model_obj, x_sample=x_train, y_sample=y_train, approach=approach,
                                          create_new=True, local_name_dict=local_name_dict)
    handle_cv_grid_and_custom_param(metadata_dict=metadata_dict, model_obj=model_obj, model_node=model_node,
                                    x_train=x_train, hyperparameters=hyperparameters)
    upload_model_and_dataset_info(x_train=x_train, y_train=y_train, model_obj=model_obj, model_node=model_node,
                                  approach=approach)


def create_pipeline_model_payload(model_obj, x_train, y_train, metadata_dict: dict):
    model_node = get_or_create_model_node(model_obj)
    hyperparameters = model_node.get_hyperparams()
    if hyperparameters is None:
        hyperparameters = dict()
    handle_cv_grid_and_custom_param(metadata_dict=metadata_dict, model_obj=model_obj, model_node=model_node,
                                    x_train=x_train, hyperparameters=hyperparameters)
    for predecessor_node, ops in model_node.predecessors.items():
        if predecessor_node.node_type == BaseTrackingNode.Type.MODEL and predecessor_node.is_created_in_pipeline:
            predecessor_metadata_dict = copy.deepcopy(metadata_dict)
            for key in predecessor_metadata_dict:
                val = predecessor_metadata_dict[key]
                if val is None:
                    continue
                if key == SCRYBE_GRID_ID_KEY and SCRYBE_GRID_ID_KEY_KEYID in val and isinstance(
                        val[SCRYBE_GRID_ID_KEY_KEYID], str) and len(val[SCRYBE_GRID_ID_KEY_KEYID]) > 0:
                    predecessor_metadata_dict[key][SCRYBE_GRID_ID_KEY_KEYID] = val[SCRYBE_GRID_ID_KEY_KEYID] + \
                                                                               predecessor_node.approach
                    continue
                if isinstance(val, str) and len(val) > 0:
                    predecessor_metadata_dict[key] = val + predecessor_node.approach
            predecessor_node.set_cv_and_grid_id_if_possible(metadata_dict=predecessor_metadata_dict)
    upload_model_and_dataset_info(x_train=x_train, y_train=y_train, model_obj=model_obj, model_node=model_node,
                                  approach='')


def all_func_enable_patching_decorator(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        ret_val = func(*args, **kwargs)
        ThreadLocalVarHandler.all_func.enable_patching()
        return ret_val

    return inner


def stats_enable_patching_decorator(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        ret_val = func(*args, **kwargs)
        ThreadLocalVarHandler.stats.enable_patching()
        return ret_val

    return inner


def bookmark(obj, name: str, msg: str):
    if not TrackingGraph.has_tracked_obj(obj=obj):
        LOGGER.error("Scrybe is unable to track the given object")
        return
    node = TrackingGraph.get_node_for_tracked_object(obj=obj)
    node.set_node_name(name=name)
    node.set_bookmark(msg=msg)
    DataReceiver.receive_batch(data_dict_list=node.prepare_for_upload())


def set_support(dataset, metric_dict, metric_key):
    try:
        support = len(dataset)
        metric_dict[metric_key] = support
    except:
        if hasattr(dataset, "shape") and len(dataset.shape) > 0:
            metric_dict[metric_key] = dataset.shape[0]


def create_db_bulk_metric(arg_obj_names, kwargs_obj_names, ret_val, metrics, arg_names, *args, **kwargs):
    if metrics is None or len(metrics) == 0:
        return
    y_true, y_pred = get_func_req_params(arg_names, [0, 1], *args, **kwargs)
    y_true_name, y_pred_name = get_func_req_params(arg_names, [0, 1], *arg_obj_names, **kwargs_obj_names)
    local_name_dict = {"y_true": y_true_name, "y_pred": y_pred_name}
    if 'support' not in metrics.keys():
        set_support(dataset=y_pred, metric_dict=metrics, metric_key='support')
    metric_tuple = get_test_or_train_metric_node(y_true=y_true, y_pred=y_pred, ret_val=ret_val,
                                                 metric_names=list(metrics.keys()), local_name_dict=local_name_dict)
    if metric_tuple is None:
        return
    metric_node, metric_seq_dict = metric_tuple
    metrics.update(metric_seq_dict)
    if metric_node.node_type == BaseTrackingNode.Type.TRAIN_METRIC:
        train_metrics = dict()
        for key in metrics:
            train_metrics[TRAIN_METRICS_PREFIX + key] = metrics[key]
        metrics = train_metrics
    metric_node.add_metric(metrics)
    DataReceiver.receive_batch(data_dict_list=metric_node.prepare_for_upload())


def get_arg_at_pos(arg_name, arg_index, *args, **kwargs):
    if len(args) >= arg_index + 1:
        arg = args[arg_index]
    elif arg_name in kwargs:
        arg = kwargs[arg_name]
    else:
        arg = None
    return arg


def get_labels(ret_val, arg_index, *args, **kwargs):
    labels = get_arg_at_pos('labels', arg_index, *args, **kwargs)
    if labels is not None:
        return labels
    if isinstance(ret_val, Iterable) or isinstance(ret_val, Sized):
        labels = [str(x) for x in range(len(ret_val))]
        return labels
    return None


def handle_confusion_matrix(arg_obj_names, kwargs_obj_names, ret_val, func_name, arg_names, *args, **kwargs):
    labels = get_labels(ret_val, 2, *args, **kwargs)
    result = dict()
    for i in range(len(labels)):
        result[labels[i]] = dict()
        for j in range(len(labels)):
            result[labels[i]][labels[j]] = ret_val[i][j]
    return {func_name: result}


def handle_curve(arg_obj_names, kwargs_obj_names, ret_val, func_name, arg_names, *args, **kwargs):
    result = dict()
    if len(ret_val) < 2:
        return
    x_axis = list(ret_val[0])
    y_axis = list(ret_val[1])
    if func_name == 'precision_recall_curve':
        result['yaxis_precision'] = x_axis
        result['xaxis_recall'] = y_axis
    elif func_name == 'roc_curve':
        result['xaxis_fpr'] = x_axis
        result['yaxis_tpr'] = y_axis
    elif func_name == 'fpr_curve':
        result['xaxis_thresholds'] = x_axis
        result['yaxis_fpr'] = y_axis
    elif func_name == 'fnr_curve':
        result['xaxis_thresholds'] = x_axis
        result['yaxis_fnr'] = y_axis
    if len(ret_val) == 3:
        result['thresholds'] = list(ret_val[2])
    return {func_name: result}
