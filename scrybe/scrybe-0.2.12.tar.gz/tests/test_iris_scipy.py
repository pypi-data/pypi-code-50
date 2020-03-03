import scrybe

import time

from scrybe.internal.depgraph import TrackingGraph

t = time.time()
from sklearn.base import BaseEstimator, ClassifierMixin, TransformerMixin
from sklearn.pipeline import Pipeline

import pandas
from sklearn import model_selection
from sklearn.metrics import classification_report, precision_recall_fscore_support, multilabel_confusion_matrix, \
    jaccard_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, auc, roc_curve, precision_recall_curve
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, \
    BaggingClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.preprocessing import LabelBinarizer
import xgboost as xgb

scrybe.init("scrybe e2e client testing")



# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

# shape
# two_class_data = dataset['class'] != 'Iris-setosa'
# dataset = dataset[two_class_data]
# dataset['class'] = [int(item == 'Iris-versicolor') for item in dataset['class']]
print(dataset.shape)


# head
print(dataset.head(20))

# descriptions
print(dataset.describe())

# class distribution
print(dataset.groupby('class').size())

# box and whisker plots
# dataset.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)
# plt.show()

# histograms
# dataset.hist()
# plt.show()

# scatter plot matrix
# scatter_matrix(dataset)
# plt.show()

# Split-out validation dataset
array = dataset.values
X = array[:, 0:4]
Y = array[:, 4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size,
                                                                                random_state=seed)


knn = KNeighborsClassifier()
scrybe.log_custom_hyperparameter(model=knn, param_name="custom_param", param_value=10)
knn.fit(X_train, Y_train)
TrackingGraph.get_node_for_tracked_object(obj=knn)
# print(json.dumps(knn_lineage.to_json(), indent=2))

pred_proba = knn.predict_proba(X_validation)
# print(json.dumps(TG.get_lineage_of_tracked_object(tracked_obj=pred_proba).to_json(), indent=2))
test = dataset[120:]
test['predictions'] = knn.predict(test[test.columns[: 4]])
# print(json.dumps(TG.get_lineage_of_tracked_object(tracked_obj=predictions).to_json(), indent=2))

print('Accuracy Score')
print(accuracy_score(y_true=test['class'], y_pred=test.predictions))
print('Confusion matrix')
print(confusion_matrix(test['class'], test.predictions))
predictions = knn.predict(X_validation)
print('Multilabel Confusion matrix')
print(multilabel_confusion_matrix(Y_validation, predictions))
#
result = classification_report(Y_validation, predictions)
scrybe.log_custom_model_evaluation_metric(model=knn, x_test=X_validation, y_test=Y_validation,
                                          param_name="custom_metric", param_value=2.0)
print("classification_report", result)
result = precision_recall_fscore_support(Y_validation, predictions)
print("precision_recall_fscore_support", result)
result = jaccard_score(Y_validation, predictions, average=None)
print("jaccard_score", result)
probabilities = knn.predict_proba(X_validation)

encoder = LabelBinarizer()
y_true_one_hot = encoder.fit_transform(Y_validation)
for i in range(y_true_one_hot.shape[1]):
    precisions, recalls, _ = precision_recall_curve(y_true_one_hot[:, i], probabilities[:, i])
    fpr, tpr, thresholds = roc_curve(y_true_one_hot[:, i], probabilities[:, i])
    print("auc", auc(fpr, tpr))
print(Y_validation.shape, predictions.shape)

# Test options and evaluation metric
seed = 7
scoring = 'accuracy'

# Spot Check Algorithms
models = [
    ('LR', LogisticRegression(solver='liblinear', multi_class='ovr')),
    ('LDA', LinearDiscriminantAnalysis()),
    ('KNN', KNeighborsClassifier()),
    ('CART', DecisionTreeClassifier()),
    ('NB', GaussianNB()),
    ('SVM', SVC(gamma='auto'))
]
# evaluate each model in turn
results = []
names = []


class Transformer(BaseEstimator, TransformerMixin):
    def __init__(self, model):
        self.model = model

    def fit(self, X, y=None):
        print("Transformer.fit: ", X.shape)
        return self

    def transform(self, X, copy=None):
        print("Transformer.transform: ", X.shape)
        return self.model.predict(X)


class Classifier(BaseEstimator, ClassifierMixin):
    def __init__(self, threshold):
        self.threshold = threshold

    def fit(self, X, y=None):
        print("Classifier.fit: ", X.shape)
        assert (type(self.threshold) == float), "threshold parameter must be float"
        self._threshold = self.threshold
        return self

    def predict(self, X, y=None):
        print("Classifier.predict: ", X.shape)
        try:
            getattr(self, "_threshold")
        except AttributeError:
            raise RuntimeError("You must train classifer before predicting data!")
        # X[X < self._threshold] = 0
        return X

    def score(self, X, y=None, sample_weight=None):
        # counts number of values bigger than mean
        return self.predict(X)


# def get_conditional_prob(model, threshold):
def fit_pipeline():
    steps = [('transformer', Transformer(model=knn)),
             ('classifier', Classifier(threshold=0.8))]
    pipeline = Pipeline(steps)
    pipeline.fit(X_train, Y_train)
    TrackingGraph.get_node_for_tracked_object(obj=pipeline)
    accuracy_score(Y_validation, pipeline.predict(X_validation))


fit_pipeline()


for name, model in models:
    kfold = model_selection.KFold(n_splits=5, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    # print(cv_results)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)


# Compare Algorithms
# fig = plt.figure()
# fig.suptitle('Algorithm Comparison')
# ax = fig.add_subplot(111)
# plt.boxplot(results)
# ax.set_xticklabels(names)
# plt.show()


# Make predictions on validation dataset
# print('Result of classification report:\n', result)

# import joblib
# import pickle
#
# print('Saving to file1')
# file1 = open('LibLinear Iris Model.pickle', 'wb')
# pickle.dump(models[0][1], file1)
# file1.close()
# print('Saving to file2')
# file2 = open('LDA Model.pickle', 'wb')
# joblib.dump(models[1][1], file2)
# file2.close()
#
# file3 = open('pipeline.pickle', 'wb')
# pickle.dump(pipeline, file3)
# file3.close()
#
# fp = open('LibLinear Iris Model.pickle', 'rb')
# lr = pickle.load(fp)
# fp.close()
# lda = joblib.load('LDA Model.pickle')
# fp = open('pipeline.pickle', 'rb')
# pipeline2 = pickle.load(fp)
# fp.close()
# pipeline2.fit(X_train, Y_train)

# n_clusters = (4, 3)
# data, rows, columns = make_checkerboard(
#     shape=(300, 300), n_clusters=n_clusters, noise=10,
#     shuffle=False, random_state=0)
#
#
# data, row_idx, col_idx = sg._shuffle(data, random_state=0)
# model = SpectralBiclustering(n_clusters=n_clusters, method='log',
#                              random_state=0)
# model.fit(data)
# score = consensus_score(model.biclusters_,
#                         (rows[:, row_idx], columns[:, col_idx]))
#
# print(score)
# print("consensus score: {:.1f}".format(score))
#
# fit_data = data[np.argsort(model.row_labels_)]
# fit_data = fit_data[:, np.argsort(model.column_labels_)]
#
# from sklearn.metrics import r2_score
# y_true = [3, 0.5, 2, 7]
# y_pred = [2.5, 0.0, 2, 8]
# print(r2_score(y_true, y_pred))  # doctest: +ELLIPSIS
# y_true = [[0.5, 1], [1, 1], [7, 6]]
# y_pred = [[0, 2], [1, 2], [8, 5]]
# print(r2_score(y_true, y_pred, multioutput='uniform_average'))
# y_true = [[0.5, 1, 2], [1, 1, 3], [7, 6, 5]]
# y_pred = [[0, 2, 1], [1, 2, 2], [8, 5, 1]]
# print(r2_score(y_true, y_pred, multioutput='raw_values'))
# y_true = [[0.5, 1], [-1, 1], [7, -6]]
# y_pred = [[0, 2], [-1, 2], [8, -5]]
# print(r2_score(y_true, y_pred, multioutput='variance_weighted'))
# y_true = [[0.5, 1, 2], [1, 1, 3], [7, 6, 5]]
# y_pred = [[0, 2, 1], [1, 2, 2], [8, 5, 1]]
# print(r2_score(y_true, y_pred, multioutput=[0.1, 0.7, 0.2]))

random_forest = RandomForestClassifier(n_jobs=10)
random_forest.fit(X_train, Y_train)
TrackingGraph.get_node_for_tracked_object(obj=random_forest)
predictions = random_forest.predict(X_validation)
accuracy_score(Y_validation, predictions)
adaboost = AdaBoostClassifier()
adaboost.fit(X_train, Y_train)
TrackingGraph.get_node_for_tracked_object(obj=adaboost)
predictions = adaboost.predict(X_validation)
accuracy_score(Y_validation, predictions)
extra_trees = ExtraTreesClassifier()
extra_trees.fit(X_train, Y_train)
TrackingGraph.get_node_for_tracked_object(obj=extra_trees)
predictions = extra_trees.predict(X_validation)
accuracy_score(Y_validation, predictions)
bagging_classifier = BaggingClassifier()
bagging_classifier.fit(X_train, Y_train)
TrackingGraph.get_node_for_tracked_object(obj=bagging_classifier)
predictions = bagging_classifier.predict(X_validation)
accuracy_score(Y_validation, predictions)
# model = IsolationForest()
# model.fit(X_train, Y_train)
model = GradientBoostingClassifier()
model.fit(X_train, Y_train)
TrackingGraph.get_node_for_tracked_object(obj=model)

# t_end = time.time()
# print(t_end - t)

# model = VotingClassifier()
# model.fit(X_train, Y_train)



# from sklearn.metrics import *
#
# func_list = [
#     max_error,
#     median_absolute_error,
#     explained_variance_score,
#     mean_absolute_error,
#     mean_squared_error,
#     mean_squared_log_error,
#     r2_score,
#     precision_recall_curve,
#     roc_curve,
#     classification_report,
#     fbeta_score,
#     f1_score,
#     jaccard_score,
#     precision_score,
#     recall_score,
#     precision_recall_fscore_support,
#     confusion_matrix,
#     multilabel_confusion_matrix,
#     auc,
#     average_precision_score,
#     coverage_error,
#     label_ranking_average_precision_score,
#     label_ranking_loss,
#     roc_auc_score,
#     accuracy_score,
#     balanced_accuracy_score,
#     cohen_kappa_score,
#     hamming_loss,
#     hinge_loss,
#     jaccard_similarity_score,
#     log_loss,
#     matthews_corrcoef,
#     zero_one_loss,
#     brier_score_loss,
#     homogeneity_completeness_v_measure,
#     adjusted_mutual_info_score,
#     adjusted_rand_score,
#     completeness_score,
#     homogeneity_score,
#     mutual_info_score,
#     normalized_mutual_info_score,
#     fowlkes_mallows_score,
#     v_measure_score,
#     silhouette_score,
#     calinski_harabasz_score,
#     calinski_harabaz_score,
#     davies_bouldin_score,
#     consensus_score,
# ]
#
# import inspect
# for func_name in func_list:
#     args = inspect.signature(func_name)
#     print(str(args), func_name.__name__, )


xgb_classifier = xgb.XGBClassifier()
xgb_classifier.fit(X_train, Y_train)
TrackingGraph.get_node_for_tracked_object(obj=xgb_classifier)
# eval_results = xgb_classifier.evals_result()
predictions = xgb_classifier.predict(X_validation)
print(classification_report(Y_validation, predictions))
t_end = time.time()
print(t_end - t)
