import scrybe
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import pandas
import time
import xgboost as xgb
import numpy as np
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
scrybe.log_feature_importances(model=knn, feature_importances={'sepal-length': 0.9, 'sepal-width': 0.6,
                                                               'petal-length': 0.4, 'petal-width': 0.1})


def train_xgb_model():
    training_start = time.time()
    params = {'learning_rate': [0.01],
              'min_child_weight': [10],
              'max_depth': [4],
              'subsample': [1.0],
              'colsample_bytree': [0.8, 1.0]
              }
    scale_pos_weight = 1
    xgb_classif = xgb.XGBClassifier(verbosity=0, n_estimators=10,
                                    objective='binary:logistic',
                                    scale_pos_weight=scale_pos_weight, reg_alpha=1,
                                    reg_lambda=0, random_state=101)
    grid_search = GridSearchCV(xgb_classif, param_grid=params, cv=5, scoring='accuracy')

    x_train = np.random.rand(100, 10)
    y_train = np.random.randint(2, size=100)
    x_train_np = x_train.view(np.ndarray)
    y_train_np = y_train.view(np.ndarray)
    grid_search.fit(x_train_np, y=y_train_np)
    print("XGB Training time: ", time.time() - training_start)


train_xgb_model()
random_forest = RandomForestClassifier(n_jobs=10)
random_forest.fit(X_train.to_numpy(), Y_train.to_numpy())

from scrybe.internal.depgraph import TrackingGraph
rf_node = TrackingGraph.get_node_for_tracked_object(obj=random_forest)
assert isinstance(rf_node._last_uploaded_feature_importance, np.ndarray)
scrybe.log_features(model=random_forest, feature_names=['sepal-length', 'sepal-width', 'petal-length', 'petal-width'])
