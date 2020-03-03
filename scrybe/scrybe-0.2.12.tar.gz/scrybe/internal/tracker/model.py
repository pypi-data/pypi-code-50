import logging
import threading
from typing import Union

from scrybe.internal.depgraph import TrackingGraph
from scrybe.internal.depgraph.nodes import ModelTrackingNode, BaseTrackingNode, PipelineTrackingNode
from scrybe.internal.depgraph.ops import Operations
from scrybe.internal.tracker.custom_model_param import CustomParamManager
from scrybe.internal.tracker.data.basic_iterator_util import get_node_for_simple_iterable, is_simple_iterable, \
    get_iterable_of_tracked_types
from scrybe.internal.tracker.data.missed_dataset_handler import track_data_if_possible
from scrybe.internal.uploader import DataReceiver

LOGGER = logging.getLogger("scrybe_logger")
# TODO(chandra): handle orphan pipeline objects in the case where
# a pipeline model.fit starts but is stopped before completion
PIPELINE_MODEL_LIST = []


def add_to_pipeline_list(pipeline_obj):
    PIPELINE_MODEL_LIST.append((pipeline_obj, threading.currentThread().ident))


def is_model_obj(orig_model):
    if not TrackingGraph.has_tracked_obj(obj=orig_model):
        return False
    model_node = TrackingGraph.get_node_for_tracked_object(obj=orig_model)
    return model_node.node_type == BaseTrackingNode.Type.MODEL


def remove_obj_from_pipeline_list(pipeline_obj):
    item_to_remove = None
    for item in PIPELINE_MODEL_LIST:
        item_pipeline_obj, thread_id = item
        if item_pipeline_obj == pipeline_obj:
            item_to_remove = item
            break
    if item_to_remove is not None:
        PIPELINE_MODEL_LIST.remove(item_to_remove)


def get_model_node_for_pipeline(pipeline_obj) -> Union[ModelTrackingNode, None]:
    if not TrackingGraph.get_node_for_tracked_object(obj=pipeline_obj):
        return None
    pipeline_node = TrackingGraph.get_node_for_tracked_object(obj=pipeline_obj)
    model_node = ModelTrackingNode(oid=id(pipeline_obj), version=0, approach=pipeline_node.approach,
                                   name=pipeline_node.name, path=pipeline_node.path, created_in_run=True)
    for predecessor_node, ops in pipeline_node.predecessors.items():
        model_node.add_predecessor(predecessor_node=predecessor_node, operations=ops)
    for successor_node in pipeline_node.successors:
        model_node.successors.add(successor_node)
    TrackingGraph.add_tracked_object(obj=pipeline_obj, node=model_node, replace_existing=True)
    model_node.set_hyperparams(pipeline_node.hyperparameters)
    model_node.set_architecture(pipeline_node.architecture)
    return model_node


def maybe_add_as_pipeline_parent(parent_model, search_start_index=None):
    if len(PIPELINE_MODEL_LIST) == 0:
        return
    if search_start_index is None:
        search_start_index = len(PIPELINE_MODEL_LIST) - 1
    if search_start_index < 0:
        return
    current_thread = threading.currentThread().ident
    for i in range(search_start_index, -1, -1):
        pipeline_obj, thread_id = PIPELINE_MODEL_LIST[i]
        if parent_model == pipeline_obj:
            continue
        if current_thread == thread_id and TrackingGraph.has_tracked_obj(obj=pipeline_obj):
            converted = False
            if is_model_obj(pipeline_obj):
                pipeline_obj_node = TrackingGraph.get_node_for_tracked_object(obj=pipeline_obj)
            else:
                pipeline_obj_node = get_model_node_for_pipeline(pipeline_obj)
                converted = True
            parent_model_node = TrackingGraph.get_node_for_tracked_object(obj=parent_model)
            parent_model_node.is_created_in_pipeline = True
            pipeline_obj_node.add_predecessor(predecessor_node=parent_model_node, operations={Operations.ENSEMBLE})
            if converted:
                maybe_add_as_pipeline_parent(parent_model=pipeline_obj, search_start_index=i-1)
            return


def add_model_data_predecessor(data_obj, model_node, operation, local_name_ref, local_name_dict):
    if data_obj is None:
        return
    if isinstance(data_obj, list) or isinstance(data_obj, tuple) or isinstance(data_obj, dict):
        data_node = get_node_for_simple_iterable(iterable_obj=data_obj)
        if data_node is None:
            return
        model_node.add_predecessor(predecessor_node=data_node, operations=operation)
    elif TrackingGraph.has_tracked_obj(obj=data_obj):
        data_node = TrackingGraph.get_node_for_tracked_object(obj=data_obj)
        data_node.set_node_name_if_not_final(local_name_dict.get(local_name_ref, None))
        model_node.add_predecessor(predecessor_node=data_node, operations=operation)


def get_or_create_model_node(model, x_sample=None, y_sample=None, approach=None, name=None, path=None,
                             create_new=False, parent_models=None, is_pipeline_obj=False,
                             created_in_run=None, local_name_dict: dict = dict()) -> ModelTrackingNode:
    if created_in_run is None:
        created_in_run = create_new

    # Step 1: Check if this model object is already being tracked
    model_version = 0
    parent_model_nodes = list()
    if TrackingGraph.has_tracked_obj(obj=model):
        tracked_model_node = TrackingGraph.get_node_for_tracked_object(obj=model)
        model_version = TrackingGraph.get_max_version_of_tracked_object(obj=model) + 1
        if not create_new:
            return tracked_model_node
        else:
            parent_model_nodes.append((tracked_model_node, {Operations.TRANSFER_LEARN}))

    # Step 2: Fetch graph nodes of all parent models
    if parent_models is not None and len(parent_model_nodes) == 0:
        for parent_model in parent_models:
            parent_model_node = TrackingGraph.get_node_for_tracked_object(obj=parent_model)
            parent_model_nodes.append((parent_model_node, {Operations.ENSEMBLE}))

    # Step 3: Create tracking node
    model_node = ModelTrackingNode(oid=id(model), version=model_version, approach=approach, name=name, path=path,
                                   created_in_run=created_in_run)
    model_node.set_node_name_if_not_final(local_name_dict.get("model", None))

    # Step 4: Track the model
    TrackingGraph.add_tracked_object(obj=model, node=model_node)

    # Step 5: Add predecessors
    # Step 5.1: Data predecessors
    add_model_data_predecessor(data_obj=x_sample, model_node=model_node, operation={Operations.TRAINING_DATA},
                               local_name_ref="x_sample", local_name_dict=local_name_dict)
    add_model_data_predecessor(data_obj=y_sample, model_node=model_node, operation={Operations.TRAINING_LABELS},
                               local_name_ref="y_sample", local_name_dict=local_name_dict)

    # Step 5.2: Add model predecessors
    for parent_model_node, node_operation in parent_model_nodes:
        model_node.add_predecessor(predecessor_node=parent_model_node, operations=node_operation)

    # FIXME(msachdev): Fix pipelines!
    if is_pipeline_obj:
        add_to_pipeline_list(model)
    maybe_add_as_pipeline_parent(model)

    return model_node


def get_or_create_pipeline_node(pipeline_obj, hyperparameters, architecture, x_sample=None, y_sample=None,
                                approach=None, name=None, path=None, create_new=False, parent_models=None,
                                created_in_run=None, is_pipeline_obj=False,
                                local_name_dict: dict = dict()) -> Union[ModelTrackingNode, PipelineTrackingNode]:
    if is_model_obj(pipeline_obj) or (parent_models is not None and len(parent_models) > 0):
        model_node = get_or_create_model_node(model=pipeline_obj, x_sample=x_sample, y_sample=y_sample, approach=approach,
                                        name=name, path=path, create_new=create_new, parent_models=parent_models,
                                        is_pipeline_obj=is_pipeline_obj, created_in_run=created_in_run,
                                        local_name_dict=local_name_dict)
        if model_node.get_hyperparams() is None:
            model_node.set_hyperparams(hyperparams=hyperparameters)
            model_node.set_architecture(architecture=architecture)
        return model_node
    if TrackingGraph.has_tracked_obj(obj=pipeline_obj):
        return TrackingGraph.get_node_for_tracked_object(obj=pipeline_obj)
    pipeline_node = PipelineTrackingNode(oid=id(pipeline_obj), version=0, approach=approach, name=name, path=path,
                                         hyperparameters=hyperparameters, architecture=architecture)
    pipeline_node.set_node_name_if_not_final(local_name_dict.get("model", None))
    add_model_data_predecessor(data_obj=x_sample, model_node=pipeline_node, operation={Operations.TRAINING_DATA},
                               local_name_ref="x_sample", local_name_dict=local_name_dict)
    add_model_data_predecessor(data_obj=y_sample, model_node=pipeline_node, operation={Operations.TRAINING_LABELS},
                               local_name_ref="y_sample", local_name_dict=local_name_dict)
    TrackingGraph.add_tracked_object(obj=pipeline_obj, node=pipeline_node)

    add_to_pipeline_list(pipeline_obj=pipeline_obj)
    return pipeline_node


def create_prediction_association_for_simple_iterable(x_test, y_pred, model, local_name_dict: dict):
    iterable = get_iterable_of_tracked_types(iterable=y_pred)
    if iterable is None:
        return
    model_node = TrackingGraph.get_node_for_tracked_object(obj=model)
    model_node.set_node_name_if_not_final(local_name_dict.get("model", None))
    if not TrackingGraph.has_tracked_obj(obj=x_test):
        x_test = track_data_if_possible(data_obj=x_test)
    x_test_node = None
    if x_test is not None:
        x_test_node = TrackingGraph.get_node_for_tracked_object(obj=x_test)
        x_test_node.set_node_name_if_not_final(local_name_dict.get("x_test", None))
    for item in iterable:
        item_node = TrackingGraph.get_node_for_tracked_object(obj=item)
        item_node.add_predecessor(predecessor_node=model_node, operations={Operations.PREDICTION})

        # In some cases, the model and/or base testing dataset can get collected. To avoid messing up the graph
        # we let y_pred keep a ref to the tracking node of the model and x_test
        item_node.add_reference(node=model_node)
        if x_test_node is not None:
            item_node.add_predecessor(predecessor_node=x_test_node, operations={Operations.TEST_INPUT})


def create_transformation_association_for_simple_iterable(x_test, y_pred, local_name_dict: dict):
    iterable = get_iterable_of_tracked_types(iterable=y_pred)
    if iterable is None:
        return
    if not TrackingGraph.has_tracked_obj(obj=x_test):
        x_test = track_data_if_possible(data_obj=x_test)
    x_test_node = None
    if x_test is not None:
        x_test_node = TrackingGraph.get_node_for_tracked_object(obj=x_test)
        x_test_node.set_node_name_if_not_final(local_name_dict.get("x_test", None))
    for item in iterable:
        item_node = TrackingGraph.get_node_for_tracked_object(obj=item)
        if x_test_node is not None:
            item_node.add_predecessor(predecessor_node=x_test_node, operations={Operations.TRANSFORM})


def create_prediction_associations(x_test, y_pred, model, local_name_dict: dict):
    if not TrackingGraph.has_tracked_obj(obj=model):
        return

    if is_simple_iterable(obj=y_pred):
        create_prediction_association_for_simple_iterable(x_test=x_test, y_pred=y_pred, model=model,
                                                          local_name_dict=local_name_dict)
        return

    if not TrackingGraph.has_tracked_obj(obj=y_pred):
        return

    y_pred_node = TrackingGraph.get_node_for_tracked_object(obj=y_pred)
    model_node = TrackingGraph.get_node_for_tracked_object(obj=model)
    model_node.set_node_name_if_not_final(local_name_dict.get("model", None))

    y_pred_node.add_predecessor(predecessor_node=model_node, operations={Operations.PREDICTION})

    # In some cases, the model and/or base testing dataset can get collected. To avoid messing up the graph
    # we let y_pred keep a ref to the tracking node of the model and x_test
    y_pred_node.add_reference(node=model_node)

    if not TrackingGraph.has_tracked_obj(obj=x_test):
        x_test = track_data_if_possible(data_obj=x_test)

    if x_test is not None:
        x_test_node = TrackingGraph.get_node_for_tracked_object(obj=x_test)
        x_test_node.set_node_name_if_not_final(local_name_dict.get("x_test", None))
        y_pred_node.add_predecessor(predecessor_node=x_test_node, operations={Operations.TEST_INPUT})


def create_transformation_associations(x_test, y_pred, local_name_dict: dict, operation=Operations.PIPELINE_TRANSFORM):
    if is_simple_iterable(obj=y_pred):
        create_transformation_association_for_simple_iterable(x_test=x_test, y_pred=y_pred,
                                                              local_name_dict=local_name_dict)
        return

    if not TrackingGraph.has_tracked_obj(obj=y_pred):
        return

    y_pred_node = TrackingGraph.get_node_for_tracked_object(obj=y_pred)
    if not TrackingGraph.has_tracked_obj(obj=x_test):
        x_test = track_data_if_possible(data_obj=x_test)

    if x_test is not None:
        x_test_node = TrackingGraph.get_node_for_tracked_object(obj=x_test)
        x_test_node.set_node_name_if_not_final(local_name_dict.get("x_test", None))
        y_pred_node.add_predecessor(predecessor_node=x_test_node, operations={operation})


def add_custom_parameter(model, param_name: str, param_value):
    CustomParamManager.add_tracked_param(model=model, metric={param_name: param_value})


def set_features(model, feature_names: list):
    if not TrackingGraph.has_tracked_obj(obj=model):
        LOGGER.error("Cannot log feature names. Scrybe is unable to track this model object")
        return
    model_node = TrackingGraph.get_node_for_tracked_object(obj=model)
    if model_node.node_type != BaseTrackingNode.Type.MODEL:
        LOGGER.error("Cannot log feature names. The first argument must be a model object")
        return
    model_node.set_features(features=feature_names)
    DataReceiver.receive_batch(data_dict_list=model_node.prepare_for_upload())


def set_feature_importances(model, feature_importances: dict):
    if not TrackingGraph.has_tracked_obj(obj=model):
        LOGGER.error("Cannot log feature importance. Scrybe is unable to track this model object")
        return
    model_node = TrackingGraph.get_node_for_tracked_object(obj=model)
    if model_node.node_type != BaseTrackingNode.Type.MODEL:
        LOGGER.error("Cannot log feature importance. The first argument must be a model object")
        return
    model_node.set_feature_importance(feature_importance=feature_importances)
    DataReceiver.receive_batch(data_dict_list=model_node.prepare_for_upload())


def set_custom_hyperparam(model_node, estimator_obj, hyperparams):
    custom_metric = None
    if CustomParamManager.has_tracked_param(model=estimator_obj):
        custom_metric = CustomParamManager.get_custom_metric_for_model(model=estimator_obj)
    elif hasattr(estimator_obj, "uid"):
        custom_metric = CustomParamManager.get_custom_metric_for_model_uid(uid=estimator_obj.uid)
    if custom_metric is not None:
        if hyperparams is None:
            hyperparams = dict()
        hyperparams.update(custom_metric)
    model_node.set_hyperparams(hyperparams)
