import scrybe
import time
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score, confusion_matrix, multilabel_confusion_matrix, classification_report, \
    precision_recall_fscore_support, jaccard_score, precision_recall_curve, roc_curve, auc
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import RandomizedSearchCV
from numpy import genfromtxt
from sklearn.neighbors import KNeighborsClassifier
import xgboost as xgb
import numpy as np
from scipy.stats import randint as sp_randint
from scipy.stats import uniform


scrybe.init("scrybe e2e client testing")
start_time = time.time()


def generate_test_data(x_file_path, y_file_path):
    dataset = np.random.rand(100, 10)
    np.savetxt(x_file_path, dataset, delimiter=",")

    y = np.random.randint(2, size=100)
    np.savetxt(y_file_path, y, delimiter=",")


def print_model_metrics(model):
    predictions = model.predict(x_val)
    print('Accuracy Score')
    print(accuracy_score(y_true=y_val, y_pred=predictions))
    print('Confusion matrix')
    print(confusion_matrix(y_val, predictions))
    print('Multilabel Confusion matrix')
    print(multilabel_confusion_matrix(y_val, predictions))
    #
    result = classification_report(y_val, predictions)
    scrybe.log_custom_model_evaluation_metric(model=model, x_test=x_val, y_test=y_val,
                                              param_name="custom_metric", param_value=float('nan'))
    print("classification_report", result)
    result = precision_recall_fscore_support(y_val, predictions)
    print("precision_recall_fscore_support", result)
    result = jaccard_score(y_val, predictions, average=None)
    print("jaccard_score", result)
    probabilities = model.predict_proba(x_val)

    encoder = LabelBinarizer()
    y_true_one_hot = encoder.fit_transform(y_val)
    plt.figure()
    for i in range(y_true_one_hot.shape[1]):
        precisions, recalls, _ = precision_recall_curve(y_true_one_hot[:, i], probabilities[:, i])
        fpr, tpr, thresholds = roc_curve(y_true_one_hot[:, i], probabilities[:, i])
        plt.plot(fpr, tpr, label='ROC curve %d (area = %0.2f)' % (i, auc(fpr, tpr)))
        plt.plot([0, 1], [0, 1], 'k--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        print("auc", auc(fpr, tpr))
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic MNIST')
    plt.legend(loc="lower right")
    print(x_val[:, 0].shape, y_val.shape)
    plt.scatter(x_val[:, 0], y_val)
    plt.show(block=False)


def train_xgb_model(verbose=True):
    training_start = time.time()
    params = {'learning_rate': [0.01, 0.1, 0.5, 1.0],
              'min_child_weight': [10],
              'max_depth': sp_randint(1, 4),
              'subsample': uniform(loc=0, scale=1),
              'colsample_bytree': [0.5]
              }
    scale_pos_weight = 1
    xgb_classif = xgb.XGBClassifier(verbosity=0, n_estimators=10,
                                    objective='binary:logistic',
                                    scale_pos_weight=scale_pos_weight, reg_alpha=1,
                                    reg_lambda=0, random_state=101)
    grid_search = RandomizedSearchCV(xgb_classif, param_distributions=params, cv=5, scoring='accuracy')

    x_train_np = x_train.view(np.ndarray)
    y_train_np = y_train.view(np.ndarray)
    grid_search.fit(x_train_np, y=y_train_np)
    # grid_search.fit(x_train, y_train)
    best_estim = grid_search.best_estimator_
    if verbose:
        print_model_metrics(best_estim)
    print("XGB Training time: ", time.time() - training_start)


def train_knn_model(verbose=True):
    training_start = time.time()
    knn_params = {'n_neighbors': [5],
                  'leaf_size': [30],
                  'p': sp_randint(1, 4),
                  }
    knn = KNeighborsClassifier()
    scrybe.log_custom_hyperparameter(knn, param_name='custom_param', param_value=float('nan'))
    grid_search = RandomizedSearchCV(knn, param_distributions=knn_params, cv=2, scoring='accuracy', n_jobs=2)
    grid_search.fit(x_train, y_train)
    best_estim = grid_search.best_estimator_
    if verbose:
        print_model_metrics(best_estim)
    print("KNN Training time: ", time.time() - training_start)


def main():
    train_knn_model()
    train_xgb_model()


x_file_path = '/tmp/hundred.csv'
y_file_path = '/tmp/y_hundred.csv'

generate_test_data(x_file_path=x_file_path, y_file_path=y_file_path)

x_train = genfromtxt(x_file_path, delimiter=',')
y_train = genfromtxt(y_file_path, delimiter=',')

x_val = genfromtxt(x_file_path, delimiter=',')[:40]
y_val = genfromtxt(y_file_path, delimiter=',')[:40]

main()

