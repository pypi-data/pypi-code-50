import scrybe
from scrybe.internal.depgraph import TrackingGraph
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline

from sklearn.metrics import accuracy_score, confusion_matrix, multilabel_confusion_matrix, classification_report, \
    precision_recall_fscore_support, jaccard_score, roc_curve, auc, precision_recall_curve
from sklearn.preprocessing import LabelBinarizer

import pandas
from sklearn import model_selection
from sklearn.neighbors import KNeighborsClassifier
import pickle
import joblib


scrybe.init("scrybe e2e client testing")
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

# Split-out validation dataset
array = dataset.values
X = array[:, 0:4]
Y = array[:, 4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size,
                                                                                random_state=seed)


knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
knn_file_name = '/tmp/KNN Iris Model.pickle'
file1 = open(knn_file_name, 'wb')
pickle.dump(knn, file1)
file1.close()
knn_node = TrackingGraph.get_node_for_tracked_object(obj=knn)
assert knn_node.is_name_final

file1 = open(knn_file_name, 'rb')
knn = pickle.load(file1)
knn_node = TrackingGraph.get_node_for_tracked_object(obj=knn)
assert knn_node.path
assert not knn_node.created_in_run
pred_proba = knn.predict_proba(X_validation)
# print(json.dumps(TG.get_lineage_of_tracked_object(tracked_obj=pred_proba).to_json(), indent=2))
predictions = knn.predict(X_validation)
# print(json.dumps(TG.get_lineage_of_tracked_object(tracked_obj=predictions).to_json(), indent=2))
print('Accuracy Score')
print(accuracy_score(y_true=Y_validation, y_pred=predictions))
print('Confusion matrix')
print(confusion_matrix(Y_validation, predictions))
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
assert not knn_node.path

knn = KNeighborsClassifier()


class Transformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        print("Transformer.fit: ", X.shape)
        return self

    def transform(self, X, copy=None):
        print("Transformer.transform: ", X.shape)
        return X


steps = [('transformer', Transformer()),
         ('classifier', knn)]
pipeline = Pipeline(steps)
pipeline.fit(X_train, Y_train)
pipeline_file_name = '/tmp/Pipeline Iris Model.pickle'
joblib.dump(pipeline, pipeline_file_name)
pipeline_node = TrackingGraph.get_node_for_tracked_object(obj=pipeline)
assert pipeline_node.is_name_final

loaded_pipe = joblib.load(pipeline_file_name)
pipeline_node = TrackingGraph.get_node_for_tracked_object(obj=loaded_pipe)
assert pipeline_node.path
assert not pipeline_node.created_in_run
print(accuracy_score(Y_validation, loaded_pipe.predict(X_validation)))
assert not pipeline_node.path

