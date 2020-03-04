import scrybe
import lightgbm

import time
from numpy import genfromtxt
import numpy as np

from scrybe.internal.depgraph import TrackingGraph

scrybe.init("scrybe e2e client testing")


def generate_test_data(x_file_path, y_file_path):
    dataset = np.random.rand(100, 10)
    np.savetxt(x_file_path, dataset, delimiter=",")

    y = np.random.randint(2, size=100)
    np.savetxt(y_file_path, y, delimiter=",")


def train_model():
    training_start = time.time()
    scale_pos_weight = 1
    lgb_classif = lightgbm.LGBMClassifier(verbosity=0, n_estimators=5, scale_pos_weight=scale_pos_weight, reg_alpha=1,
                                          reg_lambda=0, random_state=101)
    eval_set = [(x_val, y_val), (x_train, y_train), (x_val, y_val), (x_train, y_train)]
    lgb_classif.fit(X=x_train, y=y_train, eval_metric=["error", 'auc'], eval_set=eval_set)
    # print(xgb_classif.best_iteration)
    print(lgb_classif.score(X=x_val, y=y_val))
    for key in lgb_classif.evals_result_:
        print(key, lgb_classif.evals_result_[key])
    print(lgb_classif.evals_result_.keys())
    print("Training time: ", time.time() - training_start)
    TrackingGraph.get_node_for_tracked_object(obj=lgb_classif)


def main():
    train_model()


x_file_path = '/tmp/hundred.csv'
y_file_path = '/tmp/y_hundred.csv'

generate_test_data(x_file_path=x_file_path, y_file_path=y_file_path)

x_train = genfromtxt(x_file_path, delimiter=',')
y_train = genfromtxt(y_file_path, delimiter=',')

x_val = genfromtxt(x_file_path, delimiter=',')[:40]
y_val = genfromtxt(y_file_path, delimiter=',')[:40]

main()




