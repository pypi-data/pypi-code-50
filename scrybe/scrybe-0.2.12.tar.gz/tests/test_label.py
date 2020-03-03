import scrybe
from sklearn.metrics import accuracy_score, confusion_matrix, multilabel_confusion_matrix, classification_report, \
    precision_recall_fscore_support, jaccard_score, precision_recall_curve, roc_curve, auc
from sklearn.preprocessing import LabelBinarizer

import pandas
from sklearn import model_selection
from sklearn.neighbors import KNeighborsClassifier


scrybe.init("scrybe e2e client testing")


# Load dataset
scrybe.set_label(label="iris_model_selection")
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)
array = dataset.values
X = dataset[dataset.columns[:4]]
Y = dataset[dataset.columns[4]]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size,
                                                                                random_state=seed)

scrybe.set_label(label=["iris_model_selection", "KNeighbour"])
knn = KNeighborsClassifier()
scrybe.log_custom_hyperparameter(model=knn, param_name="custom_param", param_value=10)
knn.fit(X_train, Y_train)
scrybe.set_label(label=None)

predictions = knn.predict(X_validation)
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
