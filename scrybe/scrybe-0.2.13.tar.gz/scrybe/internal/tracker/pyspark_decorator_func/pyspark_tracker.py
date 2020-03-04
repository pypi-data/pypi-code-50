from scrybe.internal.depgraph.nodes import UtilityNode
from scrybe.internal.tracker.data.utils import safe_extract_name_and_path, set_dataset_node_path_from_node
from scrybe.internal.tracker.model import remove_obj_from_pipeline_list
from scrybe.internal.util import get_func_req_params, get_func_arg_names
from .pyspark_util import *


def classification_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    if ret_val is None or (hasattr(ret_val, '__module__') and ret_val.__module__ == "pyspark.ml.feature"):
        return
    try:
        from pyspark.ml import PipelineModel
        if isinstance(ret_val, PipelineModel):
            return
    except ImportError:
        pass
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    self_obj, training_data, params = get_func_req_params(get_func_arg_names(orig_func), [0, 1, 2], *args, **kwargs)
    if isinstance(params, (list, tuple)):
        return
    model_name, training_data_name = get_func_req_params(get_func_arg_names(orig_func), [0, 1], *arg_obj_names,
                                                         **kwargs_obj_names)
    local_name_dict = {"model": model_name, "x_sample": training_data_name, "y_sample": training_data_name}
    if isinstance(ret_val, list):
        # This should not happen since we return if params is list or tuple
        for model_obj in ret_val:
            create_model_payload(model_obj=model_obj, training_data=training_data, estimator_obj=self_obj,
                                 local_name_dict=local_name_dict)
    else:
        model_obj = ret_val
        try:
            from pyspark.ml.tuning import CrossValidatorModel, TrainValidationSplitModel
            if isinstance(model_obj, (CrossValidatorModel, TrainValidationSplitModel)):
                handle_grid_search_best_estimator(grid_search_model_obj=ret_val, grid_search_obj=self_obj,
                                                  training_data=training_data)
                return
        except ImportError:
            try:
                create_model_payload(model_obj=model_obj, training_data=training_data, estimator_obj=self_obj,
                                     local_name_dict=local_name_dict)
            except Exception:
                return
        create_model_payload(model_obj=model_obj, training_data=training_data, estimator_obj=self_obj,
                             local_name_dict=local_name_dict)


def pipeline_func_before_decorator(metadata_dict, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    arg_names = get_func_arg_names(orig_func)
    pipeline_obj, training_data, params = get_func_req_params(arg_names, [0, 1, 2], *args, **kwargs)
    if isinstance(params, (list, tuple)):
        return
    model_name, training_data_name = get_func_req_params(arg_names, [0, 1], *arg_obj_names, **kwargs_obj_names)
    local_name_dict = {"model": model_name, "x_sample": training_data_name, "y_sample": training_data_name}
    approach, parent_models, hyperparameters = get_pipeline_estimator_parameters(pipeline_obj=pipeline_obj)
    architecture = dict()
    get_or_create_pipeline_node(pipeline_obj, hyperparameters, architecture, x_sample=training_data,
                                y_sample=training_data, approach=approach, create_new=True,
                                parent_models=parent_models, is_pipeline_obj=True,
                                local_name_dict=local_name_dict)


def pipeline_func_exception_handler_decorator(metadata_dict, orig_func, self_obj, *args, **kwargs):
    remove_obj_from_pipeline_list(self_obj)


def pipeline_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_names = get_func_arg_names(orig_func)
    pipeline_obj, training_data, params = get_func_req_params(arg_names, [0, 1, 2], *args, **kwargs)
    if isinstance(params, (list, tuple)):
        return
    remove_obj_from_pipeline_list(pipeline_obj=pipeline_obj)
    if is_model_obj(pipeline_obj):
        create_pipeline_model_payload(estimator_obj=pipeline_obj, training_data=training_data,
                                      pipeline_model_obj=ret_val)


def metric_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    evaluator_obj, predictions = get_func_req_params(get_func_arg_names(orig_func), [0, 1], *args, **kwargs)
    evaluator_obj_name, predictions_name = get_func_req_params(get_func_arg_names(orig_func), [0, 1], *arg_obj_names,
                                                               **kwargs_obj_names)
    local_name_dict = {"y_true": predictions_name, "y_pred": predictions_name}
    create_metric_payload(evaluator=evaluator_obj, metric_val=ret_val, predictions=predictions,
                          local_name_dict=local_name_dict)


def writer_lineage_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    self_obj, instance_obj = get_func_req_params(get_func_arg_names(orig_func), [0, 1], *args, **kwargs)
    if TrackingGraph.has_tracked_obj(self_obj) or not TrackingGraph.has_tracked_obj(obj=instance_obj):
        return
    node = UtilityNode(oid=id(self_obj), version=0)
    TrackingGraph.add_tracked_object(obj=self_obj, node=node)
    node.add_reference(TrackingGraph.get_node_for_tracked_object(obj=instance_obj))


def save_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_names = get_func_arg_names(orig_func)
    writer_obj, path = get_func_req_params(arg_names, [0, 1], *args, **kwargs)
    if not TrackingGraph.has_tracked_obj(obj=writer_obj):
        return
    writer_node = TrackingGraph.get_node_for_tracked_object(obj=writer_obj)
    if len(writer_node.references) != 1:
        return
    orig_obj_node = writer_node.references[0]
    filename, file_path = safe_extract_name_and_path(args=(path,), kwargs=dict())
    if not file_path:
        return
    if orig_obj_node.node_type == BaseTrackingNode.Type.MODEL:
        model_node = orig_obj_node
        if file_path:
            model_node.set_path(file_path)
        model_node.set_node_name(filename)
        DataReceiver.receive_batch(data_dict_list=model_node.prepare_for_upload())
    elif orig_obj_node.node_type == BaseTrackingNode.Type.DATA:
        filename, file_path = safe_extract_name_and_path(args=(file_path,), kwargs=dict())
        if len(file_path) > 0:
            set_dataset_node_path_from_node(dataset_node=orig_obj_node, filename=filename, file_path=file_path,
                                            created_in_run=True, node_name=None)
            DataReceiver.receive_batch(data_dict_list=orig_obj_node.prepare_for_upload())


def load_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_names = get_func_arg_names(orig_func)
    orig_obj, path = get_func_req_params(arg_names, [0, 1], *args, **kwargs)
    filename, file_path = safe_extract_name_and_path(args=(path,), kwargs=dict())
    if not file_path:
        return
    try:
        from pyspark.ml.base import Model
        if not isinstance(ret_val, Model):
            return
        maybe_create_model_node_after_deserialization(orig_object=ret_val, file_path=file_path, filename=filename)
    except ImportError:
        pass


def patch(patcher_obj):
    for module_name, func_name in CLASSIFICATION_FUNCS:
        patcher_obj.register_after(module_name, func_name, classification_func_after_decorator)
    for module_name, func_name in PIPELINE_FUNCS:
        patcher_obj.register_before(module_name, func_name, pipeline_func_before_decorator)
        patcher_obj.register_exception_handler(module_name, func_name, pipeline_func_exception_handler_decorator)
        patcher_obj.register_after(module_name, func_name, pipeline_func_after_decorator)
    for module_name, func_name in METRIC_FUNCS:
        patcher_obj.register_after(module_name, func_name, metric_func_after_decorator)
    for module_name, func_name in WRITER_LINEAGE_FUNCS:
        patcher_obj.register_after(module_name, func_name, writer_lineage_func_after_decorator)
    for module_name, func_name in WRITER_FUNCS:
        patcher_obj.register_after(module_name, func_name, save_func_after_decorator)
    for module_name, func_name in LOADER_FUNC:
        patcher_obj.register_after(module_name, func_name, load_func_after_decorator)
