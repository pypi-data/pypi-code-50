import copy
import json

from scrybe.internal.config import Config
from scrybe.internal.const import TRAIN_METRICS_PREFIX, SCRYBE_GRID_ID_KEY_KEYID, SCRYBE_GRID_ID_KEY
from scrybe.internal.depgraph import TrackingGraph
from scrybe.internal.depgraph.nodes import BaseTrackingNode
from scrybe.internal.depgraph.ops import Operations
from scrybe.internal.tracker.data.utils import maybe_track_dataset_and_upload_info
from scrybe.internal.tracker.metrics import get_test_or_train_metric_node, get_eval_metric_node
from scrybe.internal.tracker.model import get_or_create_model_node, is_model_obj, set_custom_hyperparam, \
    get_or_create_pipeline_node
from scrybe.internal.uploader import DataReceiver
from scrybe.internal.util import get_parameter_vals

CLASSIFICATION_FUNCS = [
    ('pyspark.ml.base', 'Estimator.fit'),
]

PIPELINE_FUNCS = [
    ('pyspark.ml.pipeline', 'Pipeline.fit'),
]

METRIC_FUNCS = [
    ('pyspark.ml.evaluation', 'Evaluator.evaluate'),
]

WRITER_LINEAGE_FUNCS = [
    ('pyspark.ml.util', 'JavaMLWriter.__init__'),
    ('pyspark.ml.pipeline', 'PipelineModelWriter.__init__'),
    ('pyspark.ml.pipeline', 'PipelineWriter.__init__'),
]

WRITER_FUNCS = [
    ('pyspark.ml.util', 'JavaMLWriter.save'),
    ('pyspark.ml.pipeline', 'PipelineModelWriter.save'),
    ('pyspark.ml.pipeline', 'PipelineWriter.save'),
]

LOADER_FUNC = [
    ('pyspark.ml.util', 'JavaMLReader.load'),
    ('pyspark.ml.pipeline', 'PipelineModelReader.load')
]


def get_hyperparams(model_obj, trim=False):
    hyperparams = dict()
    try:
        param_map = model_obj.extractParamMap()
        for param in param_map.keys():
            if trim:
                hyperparams[param.name] = get_parameter_vals(param_map[param])
            else:
                hyperparams[param.name] = param_map[param]
    except Exception as e:
        pass
    return hyperparams


def get_features_from_lineage(dataframe, feature_col):
    """
    Sample
    [
      {
        "class": "org.apache.spark.sql.execution.WholeStageCodegenExec",
        "num-children": 1,
        "child": 0,
        "codegenStageId": 5
      },
      {
        "class": "org.apache.spark.sql.execution.ProjectExec",
        "num-children": 1,
        "projectList": [
          [
            {
              "class": "org.apache.spark.sql.catalyst.expressions.Alias",
              "num-children": 1,
              "child": 0,
              "name": "features",
              "exprId": {
                "product-class": "org.apache.spark.sql.catalyst.expressions.ExprId",
                "id": 446,
                "jvmId": "c6c3fdf5-f8f2-4f92-9a81-c62f011a13ec"
              },
              "qualifier": [],
              "explicitMetadata": {}
            },
            {
              "class": "org.apache.spark.sql.catalyst.expressions.ScalaUDF",
              "num-children": 1,
              "function": null,
              "dataType": {
                "type": "udt",
                "class": "org.apache.spark.ml.linalg.VectorUDT",
                "pyClass": "pyspark.ml.linalg.VectorUDT",
                "sqlType": {
                  "type": "struct",
                  "fields": [
                    {
                      "name": "type",
                      "type": "byte",
                      "nullable": false,
                      "metadata": {}
                    },
                    {
                      "name": "size",
                      "type": "integer",
                      "nullable": true,
                      "metadata": {}
                    },
                    {
                      "name": "indices",
                      "type": {
                        "type": "array",
                        "elementType": "integer",
                        "containsNull": false
                      },
                      "nullable": true,
                      "metadata": {}
                    },
                    {
                      "name": "values",
                      "type": {
                        "type": "array",
                        "elementType": "double",
                        "containsNull": false
                      },
                      "nullable": true,
                      "metadata": {}
                    }
                  ]
                }
              },
              "children": [
                0
              ],
              "inputsNullSafe": null,
              "inputTypes": [],
              "nullable": true,
              "udfDeterministic": false
            },
            {
              "class": "org.apache.spark.sql.catalyst.expressions.CreateNamedStruct",
              "num-children": 8,
              "children": [
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7
              ]
            },
            {
              "class": "org.apache.spark.sql.catalyst.expressions.Literal",
              "num-children": 0,
              "value": "shop_id_double_VectorAssembler_be514c21f38c",
              "dataType": "string"
            },
            {
              "class": "org.apache.spark.sql.catalyst.expressions.Cast",
              "num-children": 1,
              "child": 0,
              "dataType": "double",
              "timeZoneId": "Asia/Kolkata"
            },
            {
              "class": "org.apache.spark.sql.catalyst.expressions.AttributeReference",
              "num-children": 0,
              "name": "shop_id",
              "dataType": "byte",
              "nullable": true,
              "metadata": {},
              "exprId": {
                "product-class": "org.apache.spark.sql.catalyst.expressions.ExprId",
                "id": 113,
                "jvmId": "c6c3fdf5-f8f2-4f92-9a81-c62f011a13ec"
              },
              "qualifier": []
            },
            {
              "class": "org.apache.spark.sql.catalyst.expressions.Literal",
              "num-children": 0,
              "value": "item_id_double_VectorAssembler_be514c21f38c",
              "dataType": "string"
            },
            {
              "class": "org.apache.spark.sql.catalyst.expressions.Cast",
              "num-children": 1,
              "child": 0,
              "dataType": "double",
              "timeZoneId": "Asia/Kolkata"
            },
            {
              "class": "org.apache.spark.sql.catalyst.expressions.AttributeReference",
              "num-children": 0,
              "name": "item_id",
              "dataType": "short",
              "nullable": true,
              "metadata": {},
              "exprId": {
                "product-class": "org.apache.spark.sql.catalyst.expressions.ExprId",
                "id": 120,
                "jvmId": "c6c3fdf5-f8f2-4f92-9a81-c62f011a13ec"
              },
              "qualifier": []
            },
            {
              "class": "org.apache.spark.sql.catalyst.expressions.Literal",
              "num-children": 0,
              "value": "item_price_double_VectorAssembler_be514c21f38c",
              "dataType": "string"
            },
            {
              "class": "org.apache.spark.sql.catalyst.expressions.Cast",
              "num-children": 1,
              "child": 0,
              "dataType": "double",
              "timeZoneId": "Asia/Kolkata"
            },
            {
              "class": "org.apache.spark.sql.catalyst.expressions.AttributeReference",
              "num-children": 0,
              "name": "item_price",
              "dataType": "float",
              "nullable": true,
              "metadata": {},
              "exprId": {
                "product-class": "org.apache.spark.sql.catalyst.expressions.ExprId",
                "id": 127,
                "jvmId": "c6c3fdf5-f8f2-4f92-9a81-c62f011a13ec"
              },
              "qualifier": []
            },
            {
              "class": "org.apache.spark.sql.catalyst.expressions.Literal",
              "num-children": 0,
              "value": "item_cnt_day_double_VectorAssembler_be514c21f38c",
              "dataType": "string"
            },
            {
              "class": "org.apache.spark.sql.catalyst.expressions.Cast",
              "num-children": 1,
              "child": 0,
              "dataType": "double",
              "timeZoneId": "Asia/Kolkata"
            },
            {
              "class": "org.apache.spark.sql.catalyst.expressions.AttributeReference",
              "num-children": 0,
              "name": "item_cnt_day",
              "dataType": "float",
              "nullable": true,
              "metadata": {},
              "exprId": {
                "product-class": "org.apache.spark.sql.catalyst.expressions.ExprId",
                "id": 134,
                "jvmId": "c6c3fdf5-f8f2-4f92-9a81-c62f011a13ec"
              },
              "qualifier": []
            }
          ]
        ],
        "child": 0
      },
    ]
    """
    try:
        from pyspark.sql import DataFrame
        if not isinstance(dataframe, DataFrame):
            return None
    except Exception as e:
        return None
    lineage = dataframe._jdf.queryExecution().executedPlan().toJSON()
    if not lineage:
        return None
    lineage = json.loads(lineage)
    for node in lineage:
        if not isinstance(node, dict):
            continue
        cls = node.get("class", None)
        if cls != "org.apache.spark.sql.execution.ProjectExec":
            continue
        outputs = node.get("projectList", None)
        if outputs is None or not isinstance(outputs, list) or len(outputs) == 0:
            continue
        for output in outputs:
            if not isinstance(output, list):
                continue
            attr_names = []
            feature_found = False
            for refs in output:
                if not isinstance(refs, dict):
                    continue
                ref_cls = refs.get("class", None)
                if ref_cls == "org.apache.spark.sql.catalyst.expressions.Alias" and refs["name"] != feature_col:
                    break
                elif ref_cls == "org.apache.spark.sql.catalyst.expressions.Alias" and refs["name"] == feature_col:
                    feature_found = True
                elif ref_cls == "org.apache.spark.sql.catalyst.expressions.AttributeReference":
                    attr_names.append(refs["name"])
            if feature_found:
                return attr_names
    return None


def get_features_from_metadata(metadata_dict):
    if 'num_attrs' in metadata_dict:
        attrs = metadata_dict.get('attrs', None)
        if attrs and isinstance(attrs, dict):
            feature_tuples = []
            num_features = 0
            for key, val in attrs.items():
                if isinstance(val, list):
                    for item in val:
                        name = item.get('name', None)
                        if name:
                            idx = item.get('idx')
                            feature_tuples.append((idx, name))
                            num_features += 1
                elif isinstance(val, dict):
                    name = val.get('name', None)
                    if name:
                        idx = val.get('idx')
                        feature_tuples.append((idx, name))
                        num_features += 1
            if num_features > 0:
                features = [""] * num_features
                for idx, name in feature_tuples:
                    features[idx] = name
                return features
            return None
    else:
        for key, val in metadata_dict.items():
            if isinstance(val, dict):
                features = get_features_from_metadata(metadata_dict=val)
                if features is not None and len(features) > 0:
                    return features
    return None


def set_features_and_importances(model_obj, training_data, model_node, hyperparams):
    features_col = hyperparams.get("featuresCol", None)
    if training_data is not None:
        if features_col is None:
            model_node.set_features(features=training_data.columns)
        else:
            features = None
            try:
                training_fields = training_data.schema.fields
                for field in training_fields:
                    if field.name != features_col:
                        continue
                    metadata = field.metadata
                    features = get_features_from_metadata(metadata_dict=metadata)
            except:
                pass
            try:
                if features is None or len(features) == 0:
                    features = get_features_from_lineage(training_data, features_col)
            except:
                pass
            if features is not None and len(features) > 0:
                model_node.set_features(features=features)
            else:
                model_node.set_features(features=[features_col])
    if hasattr(model_obj, 'featureImportances') and model_obj.featureImportances is not None:
        feature_importances = list(model_obj.featureImportances)
        model_node.set_feature_importance(feature_importance=feature_importances)
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


def get_pipeline_parameters(pipeline_obj, stages, deserialization=False, file_path=None, filename=None):
    parent_models = []
    hyperparameters = dict()
    approach = pipeline_obj.__class__.__name__
    step_count = 0
    if stages is None:
        return
    for stage in stages:
        step_count += 1
        stage_approach = stage.__class__.__name__
        step_name = 'step_' + str(step_count) + ":" + stage_approach
        try:
            from pyspark.ml import Pipeline, PipelineModel
            from pyspark.ml.base import Model
            if isinstance(stage, Pipeline):
                # This will be added as parent when fit is called on this stage
                step_stages = stage.getStages()
                stage_approach, stage_parent_models, stage_params = get_pipeline_parameters(pipeline_obj=stage,
                                                                                            stages=step_stages)
            elif isinstance(stage, Model):
                # Create a node for the underlying model object then only this can be added as a parent to pipeline
                is_model = True
                if deserialization:
                    is_model = maybe_create_model_node_after_deserialization(orig_object=stage,
                                                                             file_path=file_path,
                                                                             filename=step_name + ":" + filename,
                                                                             is_path_copied=True)
                # Fit will not be called for these models. Only transform will get called
                if is_model and TrackingGraph.has_tracked_obj(stage):
                    parent_models.append(stage)
                if isinstance(stage, PipelineModel):
                    step_stages = stage.stages
                    stage_approach, stage_parent_models, stage_params = get_pipeline_parameters(pipeline_obj=stage,
                                                                                                stages=step_stages)
                else:
                    stage_params = get_hyperparams(stage, trim=True)
            else:
                stage_params = get_hyperparams(stage, trim=True)
        except ImportError:
            stage_params = dict()
            pass
        # attr_model_keys = []
        # try:
        #     step_attr = step_object.__dict__.items()
        #     for attr_key, value in step_attr:
        #         if deserialization:
        #             is_value_a_model = maybe_create_model_node_after_deserialization(value)
        #         else:
        #             is_value_a_model = is_model_obj(value)
        #         if is_value_a_model:
        #             parent_models.append(value)
        #             attr_model_keys.append(attr_key)
        #             step_param_keys_to_remove = []
        #             for step_param_key in stage_params.keys():
        #                 if step_param_key == attr_key or step_param_key.startswith(attr_key + '__'):
        #                     step_param_keys_to_remove.append(step_param_key)
        #             for step_param_key in step_param_keys_to_remove:
        #                 stage_params.pop(step_param_key)
        # except Exception as e:
        #     pass
        hyperparameters[step_name] = stage_params
        approach += '_' + stage_approach
    return approach, parent_models, hyperparameters


def get_pipeline_model_parameters(pipeline_model_obj):
    stages = pipeline_model_obj.stages
    return get_pipeline_parameters(pipeline_obj=pipeline_model_obj, stages=stages)


def get_pipeline_estimator_parameters(pipeline_obj):
    stages = pipeline_obj.getStages()
    return get_pipeline_parameters(pipeline_obj=pipeline_obj, stages=stages)


def get_grid_metadata(grid_id):
    metadata_dict = {
        SCRYBE_GRID_ID_KEY: {SCRYBE_GRID_ID_KEY_KEYID: grid_id + '.' + Config.get_run_id()},
    }
    return metadata_dict


def set_grid_search_id(model_node, dataset):
    if dataset is None:
        return
    columns = dataset.columns
    grid_id = None
    for column in columns:
        if column.startswith('CrossValidator_') or column.startswith('TrainValidationSplit_'):
            grid_strs = column.split("_")
            if len(grid_strs) >= 2:
                grid_id = grid_strs[1]
    if grid_id is None:
        return
    metadata_dict = get_grid_metadata(grid_id=grid_id)
    model_node.set_cv_and_grid_id_if_possible(metadata_dict=metadata_dict)
    return metadata_dict


def create_model_payload(model_obj, training_data, estimator_obj, local_name_dict):
    # TODO(chandra): Handle custom hyperparameters
    model_node = get_or_create_model_node(model=model_obj, x_sample=training_data, y_sample=training_data,
                                          approach=model_obj.__class__.__name__, create_new=True,
                                          local_name_dict=local_name_dict)
    hyperparams = get_hyperparams(model_obj=model_obj)
    set_custom_hyperparam(model_node=model_node, estimator_obj=estimator_obj, hyperparams=hyperparams)
    set_features_and_importances(model_obj=model_obj, training_data=training_data, model_node=model_node,
                                 hyperparams=hyperparams)
    set_grid_search_id(model_node=model_node, dataset=training_data)
    maybe_track_dataset_and_upload_info(dataset=training_data, operation=Operations.TRAINING_DATA,
                                        model_node=model_node)
    if not model_node.is_created_in_pipeline:
        DataReceiver.receive_batch(data_dict_list=model_node.prepare_for_upload())


def set_grid_metadata_for_predecessor(metadata_dict, model_node):
    predecessor_model_nodes = []
    if metadata_dict is not None:
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
                predecessor_model_nodes.append(predecessor_node)
    return predecessor_model_nodes


def create_pipeline_model_payload(estimator_obj, training_data, pipeline_model_obj):
    # TODO(chandra): Handle custom hyperparameters
    TrackingGraph.replace_node_reference(orig_obj=estimator_obj, new_obj=pipeline_model_obj)
    model_node = TrackingGraph.get_node_for_tracked_object(obj=pipeline_model_obj)
    set_custom_hyperparam(model_node=model_node, estimator_obj=estimator_obj, hyperparams=model_node.get_hyperparams())
    metadata_dict = set_grid_search_id(model_node=model_node, dataset=training_data)
    set_grid_metadata_for_predecessor(metadata_dict=metadata_dict, model_node=model_node)
    set_features_and_importances(model_obj=pipeline_model_obj, training_data=training_data, model_node=model_node,
                                 hyperparams=model_node.get_hyperparams())
    maybe_track_dataset_and_upload_info(dataset=training_data, operation=Operations.TRAINING_DATA,
                                        model_node=model_node)
    if not model_node.is_created_in_pipeline:
        DataReceiver.receive_batch(data_dict_list=model_node.prepare_for_upload())


def create_metric_payload(evaluator, metric_val, predictions, local_name_dict):
    if not hasattr(evaluator, "getMetricName"):
        return
    metric_name = evaluator.getMetricName()
    metrics = {metric_name: metric_val}
    metric_tuple = get_test_or_train_metric_node(y_true=predictions, y_pred=predictions, ret_val=metric_val,
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


def get_model_node_params(model_obj, file_path, filename):
    architecture = dict()
    parent_models = []
    try:
        from pyspark.ml.base import Model
        from pyspark.ml import PipelineModel
        if not isinstance(model_obj, Model) or (
                hasattr(model_obj, '__module__') and model_obj.__module__ == "pyspark.ml.feature"):
            return
        if isinstance(model_obj, PipelineModel):
            approach, parent_models, hyperparameters = get_pipeline_parameters(pipeline_obj=model_obj,
                                                                               stages=model_obj.stages,
                                                                               deserialization=True,
                                                                               file_path=file_path,
                                                                               filename=filename)
            return approach, parent_models, hyperparameters, architecture
        else:
            approach = model_obj.__class__.__name__
            hyperparameters = get_hyperparams(model_obj=model_obj, trim=True)
            return approach, parent_models, hyperparameters, architecture
    except ImportError:
        pass
    return


def maybe_create_model_node_after_deserialization(orig_object, file_path, filename, is_path_copied=False):
    if is_model_obj(orig_model=orig_object):
        return True
    model_node_params = get_model_node_params(model_obj=orig_object, file_path=file_path, filename=filename)
    if model_node_params is None:
        return False
    approach, parent_models, hyperparameters, architecture = model_node_params
    if is_path_copied:
        file_path += ":" + approach
    try:
        from pyspark.ml import Pipeline, PipelineModel
        if isinstance(orig_object, Pipeline) and (parent_models is None or len(parent_models) == 0):
            get_or_create_pipeline_node(pipeline_obj=orig_object, hyperparameters=hyperparameters,
                                        architecture=architecture, approach=approach, name=filename, path=file_path,
                                        create_new=True, parent_models=None, created_in_run=False)
            return False
        elif isinstance(orig_object, PipelineModel) and (parent_models is None or len(parent_models) == 0):
            return False
    except Exception as e:
        return False
    # Deliberately not setting the is_pipeline_obj because if .fit is called then anyways a new
    # object pipeline object will be created. Without that is_pipeline_obj is not required
    model_node = get_or_create_model_node(orig_object, approach=approach, name=filename, path=file_path,
                                          create_new=True, parent_models=parent_models, created_in_run=False)
    model_node.set_architecture(architecture)
    model_node.set_hyperparams(hyperparameters)
    return True


def handle_grid_search_best_estimator(grid_search_model_obj, grid_search_obj, training_data):
    model_obj = grid_search_model_obj.bestModel
    if not TrackingGraph.has_tracked_obj(obj=model_obj):
        return
    grid_id = grid_search_obj.uid
    grid_id = grid_id.split("_")[1]
    model_node = TrackingGraph.get_node_for_tracked_object(obj=model_obj)
    metadata_dict = get_grid_metadata(grid_id=grid_id)
    model_node.set_cv_and_grid_id_if_possible(metadata_dict=metadata_dict)
    model_node.set_as_grid_search_best_estimator()
    predecessor_model_nodes = set_grid_metadata_for_predecessor(metadata_dict, model_node)
    for predecessor_model_node in predecessor_model_nodes:
        predecessor_model_node.set_as_grid_search_best_estimator()
        DataReceiver.receive_batch(data_dict_list=predecessor_model_node.prepare_for_upload())
    DataReceiver.receive_batch(data_dict_list=model_node.prepare_for_upload())
    try:
        evaluator = grid_search_obj.getOrDefault(grid_search_obj.evaluator)
        if hasattr(grid_search_model_obj, 'avgMetrics'):
            metrics = grid_search_model_obj.avgMetrics
        elif hasattr(grid_search_model_obj, 'validationMetrics'):
            metrics = grid_search_model_obj.validationMetrics
        else:
            return
        if evaluator.isLargerBetter():
            metric_val = max(metrics)
        else:
            metric_val = min(metrics)
        if not hasattr(evaluator, "getMetricName"):
            return
        metric_name = evaluator.getMetricName()
        metrics = {metric_name: metric_val}
        local_name_dict = {"model": None, "x_sample": None, "y_sample": None}
        eval_metric_tuple = get_eval_metric_node(y_true=training_data, x_test=training_data, ret_val=metrics,
                                                 model=model_obj, metric_names=list(metrics.keys()),
                                                 local_name_dict=local_name_dict)
        if eval_metric_tuple is None:
            return
        eval_metric_node, metric_seq_dict = eval_metric_tuple
        metrics.update(metric_seq_dict)
        eval_metric_node.add_metric(metrics)
        DataReceiver.receive_batch(data_dict_list=eval_metric_node.prepare_for_upload())
    except Exception as e:
        return
