import inspect
import sys
from typing import Union, Tuple

from scrybe.internal.tracker.data.basic_iterator_util import is_simple_iterable, \
    get_node_for_simple_iterable
from scrybe.internal.depgraph.nodes import TrainMetricTrackingNode, TestMetricTrackingNode, \
    ValidationMetricTrackingNode, ArtifactTrackingNode, BaseTrackingNode, PlotArtifactTrackingNode, \
    Operations, DataArtifactTrackingNode, ArtifactType, ModelTrackingNode, GhostMetricTrackingNode
from scrybe.internal.depgraph.tracking_graph import TrackingGraph
from scrybe.internal.tracker.data.missed_dataset_handler import track_data
from scrybe.internal.tracker.data.utils import set_dataset_info_and_maybe_upload
from scrybe.internal.tracker.stats_decorator_func.stats_util import get_artifact_identifier
from scrybe.internal.uploader import DataReceiver


def maybe_track_data_and_get_node(obj):
    if obj is None:
        return None
    elif is_simple_iterable(obj=obj):
        return get_node_for_simple_iterable(iterable_obj=obj)
    elif TrackingGraph.has_tracked_obj(obj=obj):
        return TrackingGraph.get_node_for_tracked_object(obj=obj)
    elif not TrackingGraph.has_tracked_obj(obj=obj):
        try:
            obj = track_data(obj)
            return TrackingGraph.get_node_for_tracked_object(obj=obj)
        except TypeError:
            return None
    return None


def get_train_metric_node(x_sample, y_sample, model, ret_val, local_name_dict: dict) -> \
        Union[TrainMetricTrackingNode, None]:
    if not TrackingGraph.has_tracked_obj(obj=model):
        return None

    x_sample_node = maybe_track_data_and_get_node(obj=x_sample)
    if x_sample_node is None:
        return None
    x_sample_node.set_node_name_if_not_final(local_name_dict.get("x_sample", None))

    model_node = TrackingGraph.get_node_for_tracked_object(obj=model)
    model_node.set_node_name_if_not_final(local_name_dict.get("model", None))
    y_sample_node = None
    if TrackingGraph.has_tracked_obj(obj=y_sample):
        y_sample_node = TrackingGraph.get_node_for_tracked_object(obj=y_sample)
        y_sample_node.set_node_name_if_not_final(local_name_dict.get("y_sample", None))

    return TrainMetricTrackingNode.get_node(oid=id(ret_val), x_train_data_node=x_sample_node,
                                            y_train_data_node=y_sample_node, trained_model_node=model_node)


def get_validation_metric_node(x_val, y_val, model, ret_val, local_name_dict: dict) \
        -> Union[ValidationMetricTrackingNode, None]:
    if not TrackingGraph.has_tracked_obj(obj=model):
        return None

    x_val_node = maybe_track_data_and_get_node(obj=x_val)
    if x_val_node is None:
        return None
    x_val_node.set_node_name_if_not_final(local_name_dict.get("x_val", None))

    model_node = TrackingGraph.get_node_for_tracked_object(obj=model)
    model_node.set_node_name_if_not_final(local_name_dict.get("model", None))
    y_validation_node = None
    if TrackingGraph.has_tracked_obj(obj=y_val):
        y_validation_node = TrackingGraph.get_node_for_tracked_object(obj=y_val)
        y_validation_node.set_node_name_if_not_final(local_name_dict.get("y_val", None))

    return ValidationMetricTrackingNode.get_node(oid=id(ret_val), x_val_data_node=x_val_node,
                                                 y_val_data_node=y_validation_node, trained_model_node=model_node)


def get_eval_metric_node(y_true, x_test, ret_val, model, metric_names: list, local_name_dict: dict) -> Union[
    Tuple[TestMetricTrackingNode, dict], None]:
    if not TrackingGraph.has_tracked_obj(obj=model):
        # TODO(chandra): This should be a WARN level log
        return

    x_test_node = maybe_track_data_and_get_node(obj=x_test)
    if x_test_node is None:
        return
    x_test_node.set_node_name_if_not_final(local_name_dict.get("x_test", None))

    y_true_node = maybe_track_data_and_get_node(obj=y_true)
    if y_true_node is None:
        return
    y_true_node.set_node_name_if_not_final(local_name_dict.get("y_true", None))

    model_node = TrackingGraph.get_node_for_tracked_object(obj=model)
    model_node.set_node_name_if_not_final(local_name_dict.get("model", None))

    metric_seq_dict = get_metric_seq_dict(model_node=model_node, metric_names=metric_names)
    metric_node = TestMetricTrackingNode.get_node(oid=id(ret_val), y_test_label_node=y_true_node, model_node=model_node)
    metric_node.add_x_test(x_test_node=x_test_node)
    return metric_node, metric_seq_dict


def get_ghost_metric_node(y_true, x_test, ret_val, server_model_id, metric_names: list, local_name_dict: dict) -> Union[
    Tuple[GhostMetricTrackingNode, dict], None]:
    if isinstance(server_model_id, int):
        server_model_id = str(server_model_id)

    x_test_node = maybe_track_data_and_get_node(obj=x_test)
    if x_test_node is None:
        return
    x_test_node.set_node_name_if_not_final(local_name_dict.get("x_test", None))

    y_true_node = maybe_track_data_and_get_node(obj=y_true)
    if y_true_node is None:
        return
    y_true_node.set_node_name_if_not_final(local_name_dict.get("y_true", None))

    metric_seq_dict = dict()
    for metric_name in metric_names:
        metric_seq_dict[metric_name + ModelTrackingNode.SEQUENCE_NUM_SUFFIX] = 1
    metric_node = GhostMetricTrackingNode.get_node(oid=id(ret_val), y_test_label_node=y_true_node,
                                                   server_model_id=server_model_id)
    metric_node.add_x_test(x_test_node=x_test_node)
    metric_node.set_model_id(server_model_id)
    return metric_node, metric_seq_dict


def get_metric_seq_dict(model_node: ModelTrackingNode, metric_names: list):
    metric_seq_dict = dict()
    for key in metric_names:
        if key not in model_node.metric_seq_num_map:
            model_node.metric_seq_num_map[key] = model_node.FIRST_SEQUENCE_NUM
        metric_seq_dict[key + model_node.SEQUENCE_NUM_SUFFIX] = model_node.metric_seq_num_map[key]
        model_node.metric_seq_num_map[key] += 1
    return metric_seq_dict


def get_test_or_train_metric_node_with_seq_num(model_node, y_true_node, y_pred_node, ret_val, metric_names) -> Tuple[
    Union[TestMetricTrackingNode, TrainMetricTrackingNode], dict]:
    x_sample_node = None
    is_training_data = False
    for predecessor_node, ops in model_node.predecessors.items():
        if Operations.TRAINING_DATA in ops:
            x_sample_node = predecessor_node
        if predecessor_node == y_true_node and Operations.TRAINING_LABELS in ops:
            is_training_data = True
    if is_training_data:
        return TrainMetricTrackingNode.get_node(oid=id(ret_val), x_train_data_node=x_sample_node,
                                                y_train_data_node=y_true_node,
                                                trained_model_node=model_node), dict()
    metric_seq_dict = get_metric_seq_dict(model_node=model_node, metric_names=metric_names)
    return TestMetricTrackingNode.get_node(oid=id(ret_val), y_test_label_node=y_true_node, y_pred_data_node=y_pred_node,
                                           model_node=model_node), metric_seq_dict


def get_test_or_train_metric_node(y_true, y_pred, ret_val, metric_names: list, local_name_dict: dict) -> Union[
    Tuple[Union[TestMetricTrackingNode, TrainMetricTrackingNode], dict], None]:
    if not TrackingGraph.has_tracked_obj(obj=y_pred):
        # TODO(chandra): This should be a WARN level log
        return None

    y_pred_node = TrackingGraph.get_node_for_tracked_object(obj=y_pred)
    y_pred_node.set_node_name_if_not_final(local_name_dict.get("y_pred", None))
    model_node = y_pred_node.find_nearest_node_of_type(node_type=BaseTrackingNode.Type.MODEL)
    if model_node is None:
        return None

    y_true_node = maybe_track_data_and_get_node(obj=y_true)
    if y_true_node is None:
        return
    y_true_node.set_node_name_if_not_final(local_name_dict.get("y_true", None))
    return get_test_or_train_metric_node_with_seq_num(model_node=model_node, y_true_node=y_true_node,
                                                      y_pred_node=y_pred_node, ret_val=ret_val,
                                                      metric_names=metric_names)


def get_artifact_node(y_true, y_pred, ret_val, object_type, artifact_identifier,
                      local_name_dict: dict) -> Union[ArtifactTrackingNode, None]:
    if not TrackingGraph.has_tracked_obj(obj=y_pred):
        # TODO(chandra): This should be a WARN level log
        return None

    y_pred_node = TrackingGraph.get_node_for_tracked_object(obj=y_pred)
    y_pred_node.set_node_name_if_not_final(local_name_dict.get("y_pred", None))
    model_node = y_pred_node.find_nearest_node_of_type(node_type=BaseTrackingNode.Type.MODEL)
    if model_node is None:
        return None

    y_true_node = maybe_track_data_and_get_node(obj=y_true)
    if y_true_node is None:
        return
    y_true_node.set_node_name_if_not_final(local_name_dict.get("y_true", None))

    node = ArtifactTrackingNode.get_node(oid=id(ret_val), y_pred_data_node=y_pred_node, y_test_label_node=y_true_node,
                                         artifact_identifier=artifact_identifier, model_node=model_node)
    node.set_object_type(object_type=object_type)
    return node


def get_model_artifact_node(y_true, model_obj, ret_val, object_type, artifact_identifier,
                            local_name_dict: dict) -> Union[ArtifactTrackingNode, None]:
    if not TrackingGraph.has_tracked_obj(obj=y_true) or not TrackingGraph.has_tracked_obj(obj=model_obj):
        return None

    y_true_node = TrackingGraph.get_node_for_tracked_object(obj=y_true)
    y_true_node.set_node_name_if_not_final(local_name_dict.get("y_true", None))
    model_node = TrackingGraph.get_node_for_tracked_object(obj=model_obj)
    model_node.set_node_name_if_not_final(local_name_dict.get("model", None))

    node = ArtifactTrackingNode.get_node(oid=id(ret_val), y_pred_data_node=y_true_node, y_test_label_node=y_true_node,
                                         artifact_identifier=artifact_identifier, model_node=model_node)
    node.set_object_type(object_type=object_type)
    return node


def get_data_artifact_node(dataset_1, dataset_2, ret_val, object_type, artifact_identifier,
                           local_name_dict: dict) -> Union[DataArtifactTrackingNode, None]:
    dataset_1_node = None
    if dataset_1 is not None and TrackingGraph.has_tracked_obj(obj=dataset_1):
        dataset_1_node = TrackingGraph.get_node_for_tracked_object(obj=dataset_1)
        dataset_1_node.set_node_name_if_not_final(local_name_dict.get("dataset_1", None))
    dataset_2_node = None
    if dataset_2 is not None and TrackingGraph.has_tracked_obj(obj=dataset_2):
        dataset_2_node = TrackingGraph.get_node_for_tracked_object(obj=dataset_2)
        dataset_2_node.set_node_name_if_not_final(local_name_dict.get("dataset_2", None))

    if dataset_1_node is None and dataset_2_node is None:
        return None
    data_artifact_node = DataArtifactTrackingNode.get_node(oid=id(ret_val), dataset_node_1=dataset_1_node,
                                                           dataset_node_2=dataset_2_node,
                                                           artifact_identifier=artifact_identifier)
    data_artifact_node.set_object_type(object_type)
    # noinspection PyTypeChecker
    return data_artifact_node


def get_plot_artifact_node(figure, datasets, dataset_names) -> Union[PlotArtifactTrackingNode, None]:
    dataset_nodes = []
    for i in range(len(datasets)):
        dataset = datasets[i]
        if dataset is None:
            continue
        dataset_name = dataset_names[i]
        dataset_node = None
        if is_simple_iterable(obj=dataset):
            dataset_node = get_node_for_simple_iterable(iterable_obj=dataset)
        elif TrackingGraph.has_tracked_obj(obj=dataset):
            dataset_node = TrackingGraph.get_node_for_tracked_object(obj=dataset)
        if dataset_node is not None:
            dataset_node.set_node_name_if_not_final(dataset_name)
            dataset_nodes.append(dataset_node)
    if TrackingGraph.has_tracked_obj(obj=figure):
        plot_artifact_node = TrackingGraph.get_node_for_tracked_object(obj=figure)
    else:
        plot_artifact_node = PlotArtifactTrackingNode(oid=id(figure), version=0)
        TrackingGraph.add_tracked_object(obj=figure, node=plot_artifact_node)
    for dataset_node in dataset_nodes:
        plot_artifact_node.add_predecessor(predecessor_node=dataset_node, operations={Operations.DATA_PLOT})
    return plot_artifact_node


def create_curve_artifact_associations(ret_val, y_true, y_pred, local_name_dict: dict):
    if not TrackingGraph.has_tracked_obj(obj=y_pred):
        return
    x, y, threshold = ret_val
    if not TrackingGraph.has_tracked_obj(obj=x):
        x = track_data(x)
    if not TrackingGraph.has_tracked_obj(obj=x):
        y = track_data(y)
    if not TrackingGraph.has_tracked_obj(obj=y_true):
        y_true = track_data(y_true)

    y_pred_node = TrackingGraph.get_node_for_tracked_object(obj=y_pred)
    y_pred_node.set_node_name_if_not_final(local_name_dict.get("y_pred", None))
    y_true_node = TrackingGraph.get_node_for_tracked_object(obj=y_true)
    y_true_node.set_node_name_if_not_final(local_name_dict.get("y_true", None))

    x_node = TrackingGraph.get_node_for_tracked_object(obj=x)
    x_node.add_reference(node=y_true_node)
    x_node.add_reference(node=y_pred_node)
    y_node = TrackingGraph.get_node_for_tracked_object(obj=y)
    y_node.add_reference(node=y_true_node)
    y_node.add_reference(node=y_pred_node)
    return x, y, threshold


def get_auc_metric_node(ret_val, x, y, metric_names:list, local_name_dict: dict):
    if not TrackingGraph.has_tracked_obj(obj=x) or not TrackingGraph.has_tracked_obj(obj=y):
        # TODO(chandra): This should be a WARN level log
        return

    x_node = TrackingGraph.get_node_for_tracked_object(obj=x)
    x_node.set_node_name_if_not_final(local_name_dict.get("x", None))
    y_node = TrackingGraph.get_node_for_tracked_object(obj=y)
    y_node.set_node_name_if_not_final(local_name_dict.get("y", None))

    if x_node.references is None or len(x_node.references) < 2:
        return
    y_true_node = x_node.references[0]
    y_pred_node = x_node.references[1]
    model_node = y_pred_node.find_nearest_node_of_type(node_type=BaseTrackingNode.Type.MODEL)
    if model_node is None:
        return None
    return get_test_or_train_metric_node_with_seq_num(model_node, y_true_node, y_pred_node, ret_val, metric_names)


def add_custom_model_evaluation_metric(model, x_test, y_test, param_name: str, param_value):
    if not TrackingGraph.has_tracked_obj(obj=model) and not isinstance(model, (int, str)):
        raise ValueError("Scrybe is unable to track this model")
    if TrackingGraph.has_tracked_obj(obj=model):
        model_node = TrackingGraph.get_node_for_tracked_object(obj=model)
        if model_node.node_type != BaseTrackingNode.Type.MODEL:
            raise ValueError("%s is not a model" % type(model))

    # CAUTION: Currently it assumes that the user call is two frames down the stack
    local_names = inspect.currentframe().f_back.f_back.f_locals
    local_name_dict = {"model": None, "y_true": None, "x_test": None}
    for local_name, local_obj in local_names.items():
        if local_obj is model:
            local_name_dict["model"] = local_name
        if local_obj is y_test:
            local_name_dict["y_true"] = local_name
        if local_obj is x_test:
            local_name_dict["x_test"] = local_name

    metric_dict = {param_name: param_value}
    if isinstance(model, (int, str)):
        eval_metric_tuple = get_ghost_metric_node(y_true=y_test, x_test=x_test, ret_val=metric_dict,
                                                  server_model_id=model, metric_names=list(metric_dict.keys()),
                                                  local_name_dict=local_name_dict)
    else:
        eval_metric_tuple = get_eval_metric_node(y_true=y_test, x_test=x_test, ret_val=metric_dict, model=model,
                                                 metric_names=list(metric_dict.keys()), local_name_dict=local_name_dict)
    if eval_metric_tuple is None:
        return
    eval_metric_node, metric_seq_dict = eval_metric_tuple
    metric_dict.update(metric_seq_dict)
    eval_metric_node.add_metric(metric_dict)
    DataReceiver.receive_batch(data_dict_list=eval_metric_node.prepare_for_upload())


def add_custom_data_stats(data, stats_name: str, stats_value):
    if not TrackingGraph.has_tracked_obj(obj=data):
        raise ValueError("Scrybe is unable to track this dataset")
    else:
        dataset_node = TrackingGraph.get_node_for_tracked_object(obj=data)
        if dataset_node.node_type != BaseTrackingNode.Type.DATA:
            raise ValueError("%s is not a dataset" % type(data))

    # CAUTION: Currently it assumes that the user call is two frames down the stack
    local_names = sys._getframe().f_back.f_back.f_locals
    local_name_dict = {"dataset_1": None}
    for local_name, local_obj in local_names.items():
        if local_obj is data:
            local_name_dict["dataset_1"] = local_name

    artifact_type = ArtifactType.STATS_NUMBER
    artifact_identifier = get_artifact_identifier(artifact_type=artifact_type, stats_type='stats')
    stats_dict = {artifact_identifier: {stats_name: stats_value}}
    data_stats_node = get_data_artifact_node(dataset_1=data, dataset_2=None, ret_val=stats_dict,
                                             object_type=artifact_type, artifact_identifier=artifact_identifier,
                                             local_name_dict=local_name_dict)
    if data_stats_node is None:
        return
    data_stats_node.add_metric(stats_dict)
    set_dataset_info_and_maybe_upload(dataset_obj=data)
    DataReceiver.receive_batch(data_dict_list=data_stats_node.prepare_for_upload())
