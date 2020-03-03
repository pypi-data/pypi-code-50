import logging
from collections import Iterable

from scrybe.internal.const import KERAS_APPROACH, TRAIN_METRICS_PREFIX
from scrybe.internal.depgraph.nodes import BaseTrackingNode, ArtifactType
from scrybe.internal.depgraph.ops import Operations
from scrybe.internal.depgraph.tracking_graph import TrackingGraph
from scrybe.internal.tracker.data.utils import maybe_track_dataset_and_upload_info
from scrybe.internal.tracker.metrics import get_artifact_node, \
    get_auc_metric_node, get_eval_metric_node
from scrybe.internal.tracker.model import is_model_obj, get_or_create_model_node, get_or_create_pipeline_node, \
    set_custom_hyperparam
from scrybe.internal.tracker.nnet_decorator_func.nnet_util import get_architecture, \
    get_keras_hyperparameters, is_patched_keras_object
from scrybe.internal.tracker.tracker_util import warning_suppression_decorator, set_model_features_and_importance, \
    get_classification_model_node_parameters, pre_process_params, create_db_bulk_metric, get_arg_at_pos, get_labels, \
    handle_confusion_matrix, handle_curve
from scrybe.internal.tracker.xgb_decorator_func.xgb_util import XGB_MODULES
from scrybe.internal.uploader import DataReceiver
from scrybe.internal.util import is_patched_object, get_default_params, get_hyperparams, get_func_req_params, \
    get_func_arg_names

LOGGER = logging.getLogger(__name__)

# TODO(chandra): VotingClassifier, is not handled
CLASSIFICATION_FUNCTIONS = [
    ('sklearn.calibration', 'CalibratedClassifierCV'),
    ('sklearn.cross_decomposition.cca_', 'CCA'),
    ('sklearn.cross_decomposition._cca', 'CCA'),
    ('sklearn.cross_decomposition.pls_', 'PLSCanonical'),
    ('sklearn.cross_decomposition.pls_', 'PLSRegression'),
    ('sklearn.cross_decomposition._pls', 'PLSCanonical'),
    ('sklearn.cross_decomposition._pls', 'PLSRegression'),
    ('sklearn.discriminant_analysis', 'LinearDiscriminantAnalysis'),
    ('sklearn.discriminant_analysis', 'QuadraticDiscriminantAnalysis'),
    ('sklearn.ensemble.bagging', 'BaggingClassifier'),
    ('sklearn.ensemble.bagging', 'BaggingRegressor'),
    ('sklearn.ensemble._bagging', 'BaggingClassifier'),
    ('sklearn.ensemble._bagging', 'BaggingRegressor'),
    ('sklearn.ensemble.forest', 'ExtraTreesClassifier'),
    ('sklearn.ensemble.forest', 'ExtraTreesRegressor'),
    ('sklearn.ensemble.forest', 'RandomForestClassifier'),
    ('sklearn.ensemble.forest', 'RandomForestRegressor'),
    ('sklearn.ensemble._forest', 'ExtraTreesClassifier'),
    ('sklearn.ensemble._forest', 'ExtraTreesRegressor'),
    ('sklearn.ensemble._forest', 'RandomForestClassifier'),
    ('sklearn.ensemble._forest', 'RandomForestRegressor'),
    ('sklearn.ensemble.gradient_boosting', 'GradientBoostingClassifier'),
    ('sklearn.ensemble.gradient_boosting', 'GradientBoostingRegressor'),
    ('sklearn.ensemble._gb', 'GradientBoostingClassifier'),
    ('sklearn.ensemble._gb', 'GradientBoostingRegressor'),
    ('sklearn.ensemble.weight_boosting', 'AdaBoostClassifier'),
    ('sklearn.ensemble.weight_boosting', 'AdaBoostRegressor'),
    ('sklearn.ensemble._weight_boosting', 'AdaBoostClassifier'),
    ('sklearn.ensemble._weight_boosting', 'AdaBoostRegressor'),
    ('sklearn.gaussian_process.gaussian_process', 'GaussianProcess'),
    ('sklearn.gaussian_process.gpc', 'GaussianProcessClassifier'),
    ('sklearn.gaussian_process.gpr', 'GaussianProcessRegressor'),
    ('sklearn.gaussian_process._gpc', 'GaussianProcessClassifier'),
    ('sklearn.gaussian_process._gpr', 'GaussianProcessRegressor'),
    ('sklearn.kernel_ridge', 'KernelRidge'),
    ('sklearn.linear_model.base', 'LinearRegression'),
    ('sklearn.linear_model._base', 'LinearRegression'),
    ('sklearn.linear_model.bayes', 'ARDRegression'),
    ('sklearn.linear_model.bayes', 'BayesianRidge'),
    ('sklearn.linear_model._bayes', 'ARDRegression'),
    ('sklearn.linear_model._bayes', 'BayesianRidge'),
    ('sklearn.linear_model.coordinate_descent', 'ElasticNet'),
    ('sklearn.linear_model.coordinate_descent', 'ElasticNetCV'),
    ('sklearn.linear_model.coordinate_descent', 'Lasso'),
    ('sklearn.linear_model.coordinate_descent', 'LassoCV'),
    ('sklearn.linear_model.coordinate_descent', 'MultiTaskElasticNet'),
    ('sklearn.linear_model.coordinate_descent', 'MultiTaskElasticNetCV'),
    ('sklearn.linear_model.coordinate_descent', 'MultiTaskLasso'),
    ('sklearn.linear_model.coordinate_descent', 'MultiTaskLassoCV'),
    ('sklearn.linear_model._coordinate_descent', 'ElasticNet'),
    ('sklearn.linear_model._coordinate_descent', 'ElasticNetCV'),
    ('sklearn.linear_model._coordinate_descent', 'Lasso'),
    ('sklearn.linear_model._coordinate_descent', 'LassoCV'),
    ('sklearn.linear_model._coordinate_descent', 'MultiTaskElasticNet'),
    ('sklearn.linear_model._coordinate_descent', 'MultiTaskElasticNetCV'),
    ('sklearn.linear_model._coordinate_descent', 'MultiTaskLasso'),
    ('sklearn.linear_model._coordinate_descent', 'MultiTaskLassoCV'),
    ('sklearn.linear_model.huber', 'HuberRegressor'),
    ('sklearn.linear_model._huber', 'HuberRegressor'),
    ('sklearn.linear_model.least_angle', 'Lars'),
    ('sklearn.linear_model.least_angle', 'LarsCV'),
    ('sklearn.linear_model.least_angle', 'LassoLars'),
    ('sklearn.linear_model.least_angle', 'LassoLarsCV'),
    ('sklearn.linear_model.least_angle', 'LassoLarsIC'),
    ('sklearn.linear_model._least_angle', 'Lars'),
    ('sklearn.linear_model._least_angle', 'LarsCV'),
    ('sklearn.linear_model._least_angle', 'LassoLars'),
    ('sklearn.linear_model._least_angle', 'LassoLarsCV'),
    ('sklearn.linear_model._least_angle', 'LassoLarsIC'),
    ('sklearn.linear_model.logistic', 'LogisticRegression'),
    ('sklearn.linear_model.logistic', 'LogisticRegressionCV'),
    ('sklearn.linear_model._logistic', 'LogisticRegression'),
    ('sklearn.linear_model._logistic', 'LogisticRegressionCV'),
    ('sklearn.linear_model.omp', 'OrthogonalMatchingPursuit'),
    ('sklearn.linear_model.omp', 'OrthogonalMatchingPursuitCV'),
    ('sklearn.linear_model._omp', 'OrthogonalMatchingPursuit'),
    ('sklearn.linear_model._omp', 'OrthogonalMatchingPursuitCV'),
    ('sklearn.linear_model.passive_aggressive', 'PassiveAggressiveClassifier'),
    ('sklearn.linear_model.passive_aggressive', 'PassiveAggressiveRegressor'),
    ('sklearn.linear_model._passive_aggressive', 'PassiveAggressiveClassifier'),
    ('sklearn.linear_model._passive_aggressive', 'PassiveAggressiveRegressor'),
    ('sklearn.linear_model.perceptron', 'Perceptron'),
    ('sklearn.linear_model._perceptron', 'Perceptron'),
    ('sklearn.linear_model.ransac', 'RANSACRegressor'),
    ('sklearn.linear_model._ransac', 'RANSACRegressor'),
    ('sklearn.linear_model.ridge', 'Ridge'),
    ('sklearn.linear_model.ridge', 'RidgeCV'),
    ('sklearn.linear_model.ridge', 'RidgeClassifier'),
    ('sklearn.linear_model.ridge', 'RidgeClassifierCV'),
    ('sklearn.linear_model._ridge', 'Ridge'),
    ('sklearn.linear_model._ridge', 'RidgeCV'),
    ('sklearn.linear_model._ridge', 'RidgeClassifier'),
    ('sklearn.linear_model._ridge', 'RidgeClassifierCV'),
    ('sklearn.linear_model.stochastic_gradient', 'SGDClassifier'),
    ('sklearn.linear_model.stochastic_gradient', 'SGDRegressor'),
    ('sklearn.linear_model._stochastic_gradient', 'SGDClassifier'),
    ('sklearn.linear_model._stochastic_gradient', 'SGDRegressor'),
    ('sklearn.linear_model.theil_sen', 'TheilSenRegressor'),
    ('sklearn.linear_model._theil_sen', 'TheilSenRegressor'),
    ('sklearn.naive_bayes', 'BernoulliNB'),
    ('sklearn.naive_bayes', 'GaussianNB'),
    ('sklearn.naive_bayes', 'MultinomialNB'),
    ('sklearn.neighbors.classification', 'KNeighborsClassifier'),
    ('sklearn.neighbors.classification', 'RadiusNeighborsClassifier'),
    ('sklearn.neighbors._classification', 'KNeighborsClassifier'),
    ('sklearn.neighbors._classification', 'RadiusNeighborsClassifier'),
    ('sklearn.neighbors.nearest_centroid', 'NearestCentroid'),
    ('sklearn.neighbors._nearest_centroid', 'NearestCentroid'),
    ('sklearn.neighbors.regression', 'KNeighborsRegressor'),
    ('sklearn.neighbors.regression', 'RadiusNeighborsRegressor'),
    ('sklearn.neighbors._regression', 'KNeighborsRegressor'),
    ('sklearn.neighbors._regression', 'RadiusNeighborsRegressor'),
    ('sklearn.neural_network.multilayer_perceptron', 'MLPClassifier'),
    ('sklearn.neural_network.multilayer_perceptron', 'MLPRegressor'),
    ('sklearn.neural_network._multilayer_perceptron', 'MLPClassifier'),
    ('sklearn.neural_network._multilayer_perceptron', 'MLPRegressor'),
    ('sklearn.semi_supervised.label_propagation', 'LabelPropagation'),
    ('sklearn.semi_supervised.label_propagation', 'LabelSpreading'),
    ('sklearn.semi_supervised._label_propagation', 'LabelPropagation'),
    ('sklearn.semi_supervised._label_propagation', 'LabelSpreading'),
    ('sklearn.svm.classes', 'LinearSVC'),
    ('sklearn.svm.classes', 'LinearSVR'),
    ('sklearn.svm.classes', 'NuSVC'),
    ('sklearn.svm.classes', 'NuSVR'),
    ('sklearn.svm.classes', 'SVC'),
    ('sklearn.svm.classes', 'SVR'),
    ('sklearn.svm._classes', 'LinearSVC'),
    ('sklearn.svm._classes', 'LinearSVR'),
    ('sklearn.svm._classes', 'NuSVC'),
    ('sklearn.svm._classes', 'NuSVR'),
    ('sklearn.svm._classes', 'SVC'),
    ('sklearn.svm._classes', 'SVR'),
    ('sklearn.tree.tree', 'DecisionTreeClassifier'),
    ('sklearn.tree.tree', 'DecisionTreeRegressor'),
    ('sklearn.tree.tree', 'ExtraTreeClassifier'),
    ('sklearn.tree.tree', 'ExtraTreeRegressor'),
    ('sklearn.tree._classes', 'DecisionTreeClassifier'),
    ('sklearn.tree._classes', 'DecisionTreeRegressor'),
    ('sklearn.tree._classes', 'ExtraTreeClassifier'),
    ('sklearn.tree._classes', 'ExtraTreeRegressor'),
]

PIPELINE_FUNCTIONS = [("sklearn.pipeline", "Pipeline")]

FEATURE_UNION_FUNCTIONS = [
    ("sklearn.pipeline", "FeatureUnion.transform"),
    ("sklearn.pipeline", "FeatureUnion.fit_transform"),
]

PLOT_DATA = [
    ('sklearn.metrics.ranking', 'precision_recall_curve'),
    ('sklearn.metrics.ranking', 'roc_curve'),
    ('sklearn.metrics._ranking', 'precision_recall_curve'),
    ('sklearn.metrics._ranking', 'roc_curve'),
]

ARTIFACT_FUNCTIONS = [
    ('sklearn.metrics.classification', 'classification_report'),
    ('sklearn.metrics.classification', 'fbeta_score'),
    ('sklearn.metrics.classification', 'f1_score'),
    ('sklearn.metrics.classification', 'jaccard_score'),
    ('sklearn.metrics.classification', 'precision_score'),
    ('sklearn.metrics.classification', 'recall_score'),
    ('sklearn.metrics.classification', 'precision_recall_fscore_support'),
    ('sklearn.metrics.classification', 'confusion_matrix'),
    ('sklearn.metrics.classification', 'multilabel_confusion_matrix'),
    ('sklearn.metrics._classification', 'classification_report'),
    ('sklearn.metrics._classification', 'fbeta_score'),
    ('sklearn.metrics._classification', 'f1_score'),
    ('sklearn.metrics._classification', 'jaccard_score'),
    ('sklearn.metrics._classification', 'precision_score'),
    ('sklearn.metrics._classification', 'recall_score'),
    ('sklearn.metrics._classification', 'precision_recall_fscore_support'),
    ('sklearn.metrics._classification', 'confusion_matrix'),
    ('sklearn.metrics._classification', 'multilabel_confusion_matrix'),
]

METRICS_FUNCTIONS = [
    ('sklearn.metrics.ranking', 'auc'),
    ('sklearn.metrics.ranking', 'average_precision_score'),
    ('sklearn.metrics.ranking', 'coverage_error'),
    ('sklearn.metrics.ranking', 'label_ranking_average_precision_score'),
    ('sklearn.metrics.ranking', 'label_ranking_loss'),
    ('sklearn.metrics.ranking', 'roc_auc_score'),
    ('sklearn.metrics._ranking', 'auc'),
    ('sklearn.metrics._ranking', 'average_precision_score'),
    ('sklearn.metrics._ranking', 'coverage_error'),
    ('sklearn.metrics._ranking', 'label_ranking_average_precision_score'),
    ('sklearn.metrics._ranking', 'label_ranking_loss'),
    ('sklearn.metrics._ranking', 'roc_auc_score'),
    ('sklearn.metrics.classification', 'accuracy_score'),
    ('sklearn.metrics.classification', 'balanced_accuracy_score'),
    ('sklearn.metrics.classification', 'cohen_kappa_score'),
    ('sklearn.metrics.classification', 'hamming_loss'),
    ('sklearn.metrics.classification', 'hinge_loss'),
    ('sklearn.metrics.classification', 'jaccard_similarity_score'),
    ('sklearn.metrics.classification', 'log_loss'),
    ('sklearn.metrics.classification', 'matthews_corrcoef'),
    ('sklearn.metrics.classification', 'zero_one_loss'),
    ('sklearn.metrics.classification', 'brier_score_loss'),
    ('sklearn.metrics._classification', 'accuracy_score'),
    ('sklearn.metrics._classification', 'balanced_accuracy_score'),
    ('sklearn.metrics._classification', 'cohen_kappa_score'),
    ('sklearn.metrics._classification', 'hamming_loss'),
    ('sklearn.metrics._classification', 'hinge_loss'),
    ('sklearn.metrics._classification', 'jaccard_similarity_score'),
    ('sklearn.metrics._classification', 'log_loss'),
    ('sklearn.metrics._classification', 'matthews_corrcoef'),
    ('sklearn.metrics._classification', 'zero_one_loss'),
    ('sklearn.metrics._classification', 'brier_score_loss'),
    ('sklearn.metrics.cluster.supervised', 'homogeneity_completeness_v_measure'),
    ('sklearn.metrics.cluster.supervised', 'adjusted_mutual_info_score'),
    ('sklearn.metrics.cluster.supervised', 'adjusted_rand_score'),
    ('sklearn.metrics.cluster.supervised', 'completeness_score'),
    ('sklearn.metrics.cluster.supervised', 'homogeneity_score'),
    ('sklearn.metrics.cluster.supervised', 'mutual_info_score'),
    ('sklearn.metrics.cluster.supervised', 'normalized_mutual_info_score'),
    ('sklearn.metrics.cluster.supervised', 'fowlkes_mallows_score'),
    ('sklearn.metrics.cluster.supervised', 'v_measure_score'),
    ('sklearn.metrics.cluster._supervised', 'homogeneity_completeness_v_measure'),
    ('sklearn.metrics.cluster._supervised', 'adjusted_mutual_info_score'),
    ('sklearn.metrics.cluster._supervised', 'adjusted_rand_score'),
    ('sklearn.metrics.cluster._supervised', 'completeness_score'),
    ('sklearn.metrics.cluster._supervised', 'homogeneity_score'),
    ('sklearn.metrics.cluster._supervised', 'mutual_info_score'),
    ('sklearn.metrics.cluster._supervised', 'normalized_mutual_info_score'),
    ('sklearn.metrics.cluster._supervised', 'fowlkes_mallows_score'),
    ('sklearn.metrics.cluster._supervised', 'v_measure_score'),
    ('sklearn.metrics.cluster.unsupervised', 'silhouette_score'),
    ('sklearn.metrics.cluster.unsupervised', 'calinski_harabasz_score'),
    ('sklearn.metrics.cluster.unsupervised', 'calinski_harabaz_score'),
    ('sklearn.metrics.cluster.unsupervised', 'davies_bouldin_score'),
    ('sklearn.metrics.cluster._unsupervised', 'silhouette_score'),
    ('sklearn.metrics.cluster._unsupervised', 'calinski_harabasz_score'),
    ('sklearn.metrics.cluster._unsupervised', 'calinski_harabaz_score'),
    ('sklearn.metrics.cluster._unsupervised', 'davies_bouldin_score'),
    ('sklearn.metrics.cluster.bicluster', 'consensus_score'),
    ('sklearn.metrics.cluster._bicluster', 'consensus_score'),
    ('sklearn.metrics.regression', 'max_error'),
    ('sklearn.metrics.regression', 'median_absolute_error'),
    ('sklearn.metrics.regression', 'explained_variance_score'),
    ('sklearn.metrics.regression', 'mean_absolute_error'),
    ('sklearn.metrics.regression', 'mean_squared_error'),
    ('sklearn.metrics.regression', 'mean_squared_log_error'),
    ('sklearn.metrics.regression', 'r2_score'),
    ('sklearn.metrics._regression', 'max_error'),
    ('sklearn.metrics._regression', 'median_absolute_error'),
    ('sklearn.metrics._regression', 'explained_variance_score'),
    ('sklearn.metrics._regression', 'mean_absolute_error'),
    ('sklearn.metrics._regression', 'mean_squared_error'),
    ('sklearn.metrics._regression', 'mean_squared_log_error'),
    ('sklearn.metrics._regression', 'r2_score')
]


def get_patched_objects():
    return CLASSIFICATION_FUNCTIONS + PIPELINE_FUNCTIONS


def is_patched_pipeline_object(orig_object):
    return is_patched_object(orig_object, PIPELINE_FUNCTIONS)


def is_patched_sklearn_object(orig_object):
    return is_patched_object(orig_object, CLASSIFICATION_FUNCTIONS)


def is_patched_xgboost_object(orig_object):
    return is_patched_object(orig_object, XGB_MODULES)


def is_scrybe_patched_model(model_obj):
    if model_obj is None:
        return False
    return is_patched_sklearn_object(model_obj) or is_patched_xgboost_object(model_obj) or is_patched_pipeline_object(
        model_obj) or is_patched_keras_object(model_obj)


def get_model_node_params(model_obj, file_path=None, filename=None):
    if not is_scrybe_patched_model(model_obj=model_obj):
        return None
    architecture = dict()
    parent_models = []
    if is_patched_keras_object(model_obj):
        approach = KERAS_APPROACH
        architecture = get_architecture(model_obj)
        hyperparameters = get_keras_hyperparameters(params={}, model=model_obj)
    elif is_patched_pipeline_object(model_obj):
        approach, parent_models, hyperparameters = get_pipeline_db_parameters(model_obj, deserialization=True,
                                                                              file_path=file_path, filename=filename)
    else:
        # It must be sklearn object
        approach, hyperparameters = get_classification_model_node_parameters(model_obj)
    return approach, parent_models, hyperparameters, architecture


def maybe_create_model_node_after_deserialization(orig_object, file_path, filename, is_path_copied=False):
    if is_model_obj(orig_model=orig_object):
        return True
    model_node_params = get_model_node_params(model_obj=orig_object, file_path=file_path, filename=filename)
    if model_node_params is None:
        return False
    approach, parent_models, hyperparameters, architecture = model_node_params
    if is_path_copied:
        file_path += ":" + approach
    if is_patched_pipeline_object(orig_object=orig_object) and (parent_models is None or len(parent_models) == 0):
        get_or_create_pipeline_node(pipeline_obj=orig_object, hyperparameters=hyperparameters,
                                    architecture=architecture, approach=approach, name=filename, path=file_path,
                                    create_new=True, parent_models=None, created_in_run=False)
        return False
    # Deliberately not setting the is_pipeline_obj because if .fit is called then anyways a new
    # object pipeline object will be created. Without that is_pipeline_obj is not required
    model_node = get_or_create_model_node(orig_object, approach=approach, name=filename, path=file_path,
                                          create_new=True, parent_models=parent_models, created_in_run=False)
    model_node.set_architecture(architecture)
    model_node.set_hyperparams(hyperparameters)
    return True


@warning_suppression_decorator
def get_pipeline_db_parameters(orig_object, deserialization=False, file_path=None, filename=None):
    attributes = orig_object.get_params()
    parent_models = []
    hyperparameters = {}
    approach = orig_object.__class__.__name__
    step_count = 0
    if attributes is not None and "steps" in attributes:
        for step in attributes["steps"]:
            # FIXME(chandra): What if this step is itself a Pipeline?
            step_count += 1
            step_name, step_object = step
            approach += '_' + step_name
            if step_name is None:
                step_name = 'step_' + str(step_count)
            else:
                step_name = 'step_' + str(step_count) + ":" + step_name
            step_params = step_object.get_params()
            if deserialization:
                is_value_a_model = maybe_create_model_node_after_deserialization(step_object, file_path=file_path,
                                                                                 filename=step_name + ":" + filename,
                                                                                 is_path_copied=True)
            else:
                is_value_a_model = is_model_obj(step_object)
            if is_value_a_model:
                parent_models.append(step_object)
            attr_model_keys = []
            try:
                step_attr = step_object.__dict__.items()
                for attr_key, value in step_attr:
                    if deserialization:
                        is_value_a_model = maybe_create_model_node_after_deserialization(value, file_path=file_path,
                                                                                         filename=step_name + ":" + filename,
                                                                                         is_path_copied=True)
                    else:
                        is_value_a_model = is_model_obj(value)
                    if is_value_a_model:
                        parent_models.append(value)
                        attr_model_keys.append(attr_key)
                        step_param_keys_to_remove = []
                        for step_param_key in step_params.keys():
                            if step_param_key == attr_key or step_param_key.startswith(attr_key + '__'):
                                step_param_keys_to_remove.append(step_param_key)
                        for step_param_key in step_param_keys_to_remove:
                            step_params.pop(step_param_key)
            except Exception as e:
                pass
            processed_params = pre_process_params(step_params)
            req_args, default_dict = get_default_params(step_object)
            for attr_model_key in attr_model_keys:
                if attr_model_key in req_args:
                    req_args.remove(attr_model_key)
            step_hyperparam = get_hyperparams(processed_params, default_dict, req_args, trim=True)
            hyperparameters[str(step_name)] = step_hyperparam

    return approach, parent_models, hyperparameters


def handle_multilabel_confusion_matrix(arg_obj_names, kwargs_obj_names, ret_val, func_name, arg_names, *args, **kwargs):
    labels = get_labels(ret_val, 3, *args, **kwargs)
    result = dict()
    for i in range(len(labels)):
        result[labels[i]] = dict()
        for j in range(len(labels)):
            result[labels[i]]['TP'] = ret_val[i][1][1]
            result[labels[i]]['TN'] = ret_val[i][0][0]
            result[labels[i]]['FP'] = ret_val[i][0][1]
            result[labels[i]]['FN'] = ret_val[i][1][0]
    return {func_name: result}


def handle_classification_report(arg_obj_names, kwargs_obj_names, ret_val, func_name, arg_names, *args, **kwargs):
    agg_metric_names = ["accuracy", "micro avg", "macro avg", "weighted avg", "samples avg"]
    metrics = {}
    if isinstance(ret_val, dict):
        artifact = dict()
        for key in ret_val.keys():
            if key in agg_metric_names:
                if key == 'accuracy':
                    metrics['accuracy'] = ret_val['accuracy']
                    continue
                column_names = ret_val[key].keys()
                for column_name in column_names:
                    if column_name == 'support':
                        metrics['support'] = ret_val[key][column_name]
                    else:
                        metrics[column_name + '_' + key.replace(' ', '_')] = ret_val[key][column_name]
            else:
                artifact[key] = ret_val[key]
        create_db_bulk_metric(arg_obj_names, kwargs_obj_names, ret_val, metrics, arg_names, *args, **kwargs)
        return {func_name: artifact}
    elif isinstance(ret_val, str):
        artifact = dict()
        lines = ret_val.split('\n')
        column_names = []
        for i in range(len(lines)):
            line = lines[i]
            line = line.split()
            if len(line) == 0:
                continue
            if i == 0:
                column_names = line
                continue
            if line[0] == "accuracy":
                metrics['accuracy'] = eval(line[1])
            else:
                if len(line) > len(column_names) + 1:
                    merge_index = len(line) - len(column_names)
                    line[0: merge_index] = [' '.join(line[0: merge_index])]
                for value_index in range(1, len(line)):
                    value = eval(line[value_index])
                    if line[0] in agg_metric_names:
                        if column_names[value_index - 1] == 'support':
                            metrics['support'] = value
                        else:
                            metric_name = "%s_%s" % (column_names[value_index - 1], line[0].replace(' ', '_'))
                            metrics[metric_name] = value
                    else:
                        if line[0] not in artifact.keys():
                            artifact[line[0]] = dict()
                        artifact[line[0]][column_names[value_index - 1]] = value
        create_db_bulk_metric(arg_obj_names, kwargs_obj_names, ret_val, metrics, arg_names, *args, **kwargs)
        return {func_name: artifact}
    else:
        return dict()


def handle_prfs(arg_obj_names, kwargs_obj_names, ret_val, func_name, arg_names, *args, **kwargs):
    beta = get_arg_at_pos('beta', 2, *args, **kwargs)
    fbeta_score_metric_name = 'f1_score'
    if beta and beta != 1:
        fbeta_score_metric_name = 'fbeta=%s_score' % (str(round(beta, 2)))
    sample_weight = get_arg_at_pos('sample_weight', 7, *args, **kwargs)
    average_type = get_arg_at_pos('average', 5, *args, **kwargs)
    precision, recall, f_score, support = ret_val
    labels = get_labels(precision, 3, *args, **kwargs)
    if average_type is not None:
        precision_metric_name = "%s_%s_%s" % ('precision', average_type, 'avg')
        recall_metric_name = "%s_%s_%s" % ('recall', average_type, 'avg')
        fbeta_score_metric_name = "%s_%s_%s" % (fbeta_score_metric_name, average_type, 'avg')
        if labels is None:
            # TODO(chandra): Add sample weight metadata
            metrics = dict()
            if precision:
                metrics[precision_metric_name] = precision
            if recall:
                metrics[recall_metric_name] = recall
            if f_score:
                metrics[fbeta_score_metric_name] = f_score
            create_db_bulk_metric(arg_obj_names, kwargs_obj_names, ret_val, metrics, arg_names, *args, **kwargs)
            return
        else:
            # TODO(chandra): Add sample weight metadata
            # TODO(chandra): Add label names in metric keys
            result = dict()
            if precision:
                result[precision_metric_name] = precision
            if recall:
                result[recall_metric_name] = recall
            if f_score:
                result[fbeta_score_metric_name] = f_score
            return result
    else:
        result = dict()
        for i in range(len(precision)):
            result[labels[i]] = dict()
            if precision is not None:
                result[labels[i]]['precision'] = precision[i]
            if recall is not None:
                result[labels[i]]['recall'] = recall[i]
            if f_score is not None:
                result[labels[i]][fbeta_score_metric_name] = f_score[i]
            if support is not None:
                result[labels[i]]['support'] = support[i]
        return {func_name: result}


def handle_list_of_float_metric(arg_obj_names, kwargs_obj_names, ret_val, func_name, arg_names, *args, **kwargs):
    sample_weight = None
    average_type = None
    labels = None
    if func_name == 'fbeta_score':
        beta = args[2]
        if beta != 1:
            func_name = '%s_beta=%s' % (func_name, str(round(beta, 2)))
        labels = get_labels(ret_val, 3, *args, **kwargs)
        sample_weight = get_arg_at_pos('sample_weight', 6, *args, **kwargs)
        average_type = get_arg_at_pos('average', 5, *args, **kwargs)
    elif func_name in ['f1_score', 'jaccard_score', 'precision_score', 'recall_score']:
        labels = get_labels(ret_val, 2, *args, **kwargs)
        sample_weight = get_arg_at_pos('sample_weight', 5, *args, **kwargs)
        average_type = get_arg_at_pos('average', 4, *args, **kwargs)

    if average_type is not None:
        if labels is None:
            # TODO(chandra): Send sample weights as metadata
            create_db_metric(arg_obj_names, kwargs_obj_names, ret_val, "%s_%s_%s" % (func_name, average_type, 'avg'),
                             arg_names, *args, **kwargs)
            return
        else:
            # TODO(chandra): Send sample weights and labels as metadata
            result = {average_type + '_avg': ret_val}
    else:
        result = dict()
        if labels is None:
            create_db_metric(arg_obj_names, kwargs_obj_names, ret_val, func_name, arg_names, *args, **kwargs)
            return
        for i in range(len(ret_val)):
            result[labels[i]] = ret_val[i]
    return {func_name: result}


def handle_regression_score_raw_value(arg_obj_names, kwargs_obj_names, ret_val, func_name, arg_names, *args, **kwargs):
    labels = get_labels(ret_val, len(args), *args, **kwargs)
    result = dict()
    for i in range(len(ret_val)):
        result[labels[i]] = ret_val[i]
    return {func_name: result}


def handle_artifact(arg_obj_names, kwargs_obj_names, ret_val, func_name, arg_names, *args, **kwargs):
    func_artifact_map = {
        'classification_report': (handle_classification_report, ArtifactType.TABLE),
        'fbeta_score': (handle_list_of_float_metric, ArtifactType.PLOT_BAR),
        'f1_score': (handle_list_of_float_metric, ArtifactType.PLOT_BAR),
        'jaccard_score': (handle_list_of_float_metric, ArtifactType.PLOT_BAR),
        'precision_score': (handle_list_of_float_metric, ArtifactType.PLOT_BAR),
        'recall_score': (handle_list_of_float_metric, ArtifactType.PLOT_BAR),
        'precision_recall_fscore_support': (handle_prfs, ArtifactType.TABLE),
        'precision_recall_curve': (handle_curve, ArtifactType.PLOT_DATA),
        'roc_curve': (handle_curve, ArtifactType.PLOT_DATA),
        'confusion_matrix': (handle_confusion_matrix, ArtifactType.TABLE),
        'multilabel_confusion_matrix': (handle_multilabel_confusion_matrix, ArtifactType.TABLE),
        'explained_variance_score': (handle_regression_score_raw_value, ArtifactType.PLOT_BAR),
        'mean_absolute_error': (handle_regression_score_raw_value, ArtifactType.PLOT_BAR),
        'mean_squared_error': (handle_regression_score_raw_value, ArtifactType.PLOT_BAR),
        'mean_squared_log_error': (handle_regression_score_raw_value, ArtifactType.PLOT_BAR),
        'r2_score': (handle_regression_score_raw_value, ArtifactType.PLOT_BAR),
    }
    if func_name in func_artifact_map:
        func_callable, obj_type = func_artifact_map[func_name]
        artifact = func_callable(arg_obj_names, kwargs_obj_names, ret_val, func_name, arg_names, *args, **kwargs)
        return artifact, obj_type
    return None, None


def get_metric_dict(func_name, value):
    metrics_dict = dict()
    try:
        if not isinstance(value, str):
            float_value = float(value)
            int_value = int(value)
            if int_value == float_value:
                value = int_value
            else:
                value = float_value
    except Exception as e:
        LOGGER.warning("Cannot handle metrics which are not float, int or string")
        return dict()
    metrics_dict[func_name] = value
    return metrics_dict


def create_db_artifact(arg_obj_names, kwargs_obj_names, ret_val, func_name, arg_names, *args, **kwargs):
    metrics_dict, object_type = handle_artifact(arg_obj_names, kwargs_obj_names, ret_val, func_name, arg_names,
                                                *args, **kwargs)
    if metrics_dict is None:
        return
    y_true, y_pred = get_func_req_params(arg_names, [0, 1], *args, **kwargs)
    y_true_name, y_pred_name = get_func_req_params(arg_names, [0, 1], *arg_obj_names, **kwargs_obj_names)
    local_name_dict = {"y_true": y_true_name, "y_pred": y_pred_name}
    # support = len(y_pred)
    # metrics_dict[func_name + '_support'] = support
    # TODO(chandra): Handle different labels being passed to same func_name
    artifact_identifier = func_name
    artifact_node = get_artifact_node(y_true, y_pred, ret_val=ret_val, object_type=object_type,
                                      artifact_identifier=artifact_identifier, local_name_dict=local_name_dict)
    if artifact_node is None:
        return
    artifact_node.add_metric(metrics_dict)
    DataReceiver.receive_batch(data_dict_list=artifact_node.prepare_for_upload())
    # log_upload_data_to_file(upload_data=artifact_node.prepare_for_upload(), func_name=func_name)


def create_db_metric(arg_obj_names, kwargs_obj_names, ret_val, func_name, arg_names, *args, **kwargs):
    if func_name == 'homogeneity_completeness_v_measure':
        homogeneity_score, completeness_score, v_measure_score = ret_val
        metric_dict = get_metric_dict(homogeneity_score, 'homogeneity_score')
        metric_dict = metric_dict.update(get_metric_dict(completeness_score, 'completeness_score'))
        metric_dict = metric_dict.update(get_metric_dict(v_measure_score, 'v_measure_score'))
    elif func_name in ['explained_variance_score', 'mean_absolute_error', 'mean_squared_error',
                       'mean_squared_log_error', 'r2_score'] and not isinstance(ret_val, float):
        create_db_artifact(arg_obj_names, kwargs_obj_names, ret_val, func_name, arg_names, *args, **kwargs)
        return
    elif func_name == 'auc':
        x, y = get_func_req_params(arg_names, [0, 1], *args, **kwargs)
        x_name, y_name = get_func_req_params(arg_names, [0, 1], *arg_obj_names, **kwargs_obj_names)
        local_name_dict = {"x": x_name, "y": y_name}
        metrics = {func_name: ret_val}
        metric_tuple = get_auc_metric_node(ret_val=ret_val, x=x, y=y, metric_names=list(metrics.keys()),
                                           local_name_dict=local_name_dict)
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
        return
    else:
        metric_dict = get_metric_dict(func_name, ret_val)
    create_db_bulk_metric(arg_obj_names, kwargs_obj_names, ret_val, metric_dict, arg_names, *args, **kwargs)


def get_best_model_index_from_param(model_obj, grid_search_obj):
    if not hasattr(grid_search_obj, "cv_results_") or "mean_test_score" not in grid_search_obj.cv_results_ or \
            len(grid_search_obj.cv_results_["mean_test_score"]) == 0:
        return -1
    results = grid_search_obj.cv_results_
    model_config = model_obj.get_params()
    for i in range(len(results["params"])):
        param = results["params"][i]
        param_equals_config = True
        for key, value in param.items():
            param_equals_config = param_equals_config and model_config[key] == value
        if param_equals_config:
            return i
    return -1


def upload_best_estimator_and_metric(metadata_dict, grid_search_obj, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    x_train, y_train = get_func_req_params(get_func_arg_names(orig_func), [1, 2], *args, **kwargs)
    x_train_name, y_train_name = get_func_req_params(get_func_arg_names(orig_func), [1, 2], *arg_obj_names,
                                                     **kwargs_obj_names)
    local_name_dict = {"model": None, "x_sample": x_train_name, "y_sample": y_train_name}
    if (
            hasattr(grid_search_obj, "best_estimator_")
            and grid_search_obj.best_estimator_ is not None
            and TrackingGraph.has_tracked_obj(grid_search_obj.best_estimator_)
    ):
        model_obj = grid_search_obj.best_estimator_
        model_node = TrackingGraph.get_node_for_tracked_object(obj=model_obj)
        if model_node.node_type != BaseTrackingNode.Type.MODEL:
            return
        best_model_index = get_best_model_index_from_param(model_obj=model_obj, grid_search_obj=grid_search_obj)
    elif not hasattr(grid_search_obj, "estimator"):
        return
    elif (
            hasattr(grid_search_obj, "cv_results_") and
            (
                    (
                            "mean_test_score" in grid_search_obj.cv_results_ and
                            len(grid_search_obj.cv_results_["mean_test_score"]) > 0
                    )
                    or (
                            "rank_test_score" in grid_search_obj.cv_results_ and
                            len(grid_search_obj.cv_results_["rank_test_score"]) > 0
                    )
            )
    ):
        from sklearn.base import clone
        model_obj = clone(grid_search_obj.estimator)
        results = grid_search_obj.cv_results_
        if "rank_test_score" in results:
            optimal_param = results["params"][0]
            best_model_index = -1
            for i in range(len(results["rank_test_score"])):
                if results["rank_test_score"][i] == 1:
                    optimal_param = results["params"][i]
                    best_model_index = i
                    break
        else:
            max_score = max(results["mean_test_score"])
            optimal_param = results["params"][0]
            best_model_index = -1
            for i in range(len(results["mean_test_score"])):
                if results["mean_test_score"][i] == max_score:
                    optimal_param = results["params"][i]
                    best_model_index = i
                    break
        model_obj.set_params(**optimal_param)
        model_node_params = get_model_node_params(model_obj=model_obj)
        if model_node_params is None:
            return
        approach, parent_models, hyperparameters, architecture = model_node_params
        model_node = get_or_create_model_node(model=model_obj, x_sample=x_train, y_sample=y_train,
                                              approach=model_obj.__class__.__name__, parent_models=parent_models,
                                              create_new=True, created_in_run=True, local_name_dict=local_name_dict)
        set_custom_hyperparam(model_node=model_node, estimator_obj=grid_search_obj.estimator,
                              hyperparams=hyperparameters)
        model_node.set_architecture(architecture)
        model_node.set_cv_and_grid_id_if_possible(metadata_dict=metadata_dict)
    else:
        return
    if model_node.name is None:
        name = "best_estimator"
    else:
        name = model_node.name + ":best_estimator"
    model_node.set_node_name_if_not_final(name=name)
    model_node.set_as_grid_search_best_estimator()
    maybe_track_dataset_and_upload_info(dataset=x_train, operation=Operations.TRAINING_DATA, model_node=model_node)
    maybe_track_dataset_and_upload_info(dataset=y_train, operation=Operations.TRAINING_LABELS, model_node=model_node)
    set_model_features_and_importance(x_train=x_train, model_obj=model_obj, model_node=model_node,
                                      grid_best_estimator=True)
    DataReceiver.receive_batch(data_dict_list=model_node.prepare_for_upload())
    if not hasattr(grid_search_obj, "cv_results_") or best_model_index < 0:
        return
    metrics_dict = dict()
    for key in grid_search_obj.cv_results_:
        if key.startswith("param"):
            continue
        if isinstance(grid_search_obj.cv_results_[key], Iterable) and \
                len(grid_search_obj.cv_results_[key]) > best_model_index:
            metrics_dict[key] = grid_search_obj.cv_results_[key][best_model_index]
    if len(metrics_dict) == 0:
        return
    eval_metric_tuple = get_eval_metric_node(y_true=y_train, x_test=x_train, ret_val=metrics_dict, model=model_obj,
                                             metric_names=list(metrics_dict.keys()), local_name_dict=local_name_dict)
    if eval_metric_tuple is None:
        return
    eval_metric_node, metric_seq_dict = eval_metric_tuple
    metrics_dict.update(metric_seq_dict)
    eval_metric_node.add_metric(metrics_dict)
    DataReceiver.receive_batch(data_dict_list=eval_metric_node.prepare_for_upload())
