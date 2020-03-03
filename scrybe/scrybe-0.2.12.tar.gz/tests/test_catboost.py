import scrybe
from catboost import CatBoostClassifier, Pool, CatBoostRegressor, CatBoost
from catboost.utils import eval_metric, get_confusion_matrix, get_roc_curve, get_fpr_curve, get_fnr_curve
import numpy as np

from scrybe.internal.depgraph import TrackingGraph

scrybe.init("scrybe e2e client testing")

# initialize data
train_data = np.random.randint(0, 100, size=(100, 10))

train_label = np.random.randint(0, 2, size=100)

test_data = Pool(train_data, train_label)

model = CatBoostClassifier(iterations=2,
                           depth=2,
                           learning_rate=1,
                           loss_function='Logloss',
                           verbose=True)
# train the model
model.fit(train_data, train_label)
TrackingGraph.get_node_for_tracked_object(model)
# make the prediction using the resulting model
preds_class = model.predict(test_data)
preds_proba = model.predict_proba(test_data)
print(model.score(train_data, train_label))
print(model.eval_metrics(Pool(train_data, train_label), metrics=["Accuracy"]))
train_pool = Pool(train_data, train_label)
print(get_confusion_matrix(model, train_pool))
print(get_roc_curve(model, train_pool))
print(get_fpr_curve(model, train_pool))
print(get_fnr_curve(model, train_pool))


train_label = np.random.randint(0, 1000, size=100)
test_data = np.random.randint(0, 100, size=(50, 10))
test_label = np.random.randint(0, 100, size=50)
# initialize Pool
train_pool = Pool(train_data,
                  train_label,
                  cat_features=[0, 2, 5])
test_pool = Pool(test_data,
                 cat_features=[0, 2, 5])
# specify the training parameters
model = CatBoostRegressor(iterations=2,
                          depth=2,
                          learning_rate=1,
                          loss_function='RMSE')
# train the model
model.fit(train_pool, eval_set=[(train_data, train_label)])
TrackingGraph.get_node_for_tracked_object(model)
# make the prediction using the resulting model
preds = model.predict(test_pool)
print(model.score(test_data, test_label))
print(model.eval_metrics(Pool(test_data, test_label), metrics=["RMSE"]))


# print(preds, type(preds))

train_data = np.random.randint(0, 100, size=(100, 10))
train_label = np.random.randint(0, 2, size=100)
test_data = np.random.randint(0, 100, size=(50, 10))
test_label = np.random.randint(0, 2, size=50)
train_pool = Pool(train_data, train_label)

test_pool = Pool(test_data)
# specify training parameters via map

param = {'iterations': 5}
model = CatBoost(param)
# train the model
model.fit(train_pool, eval_set=[Pool(test_data, test_label)])
TrackingGraph.get_node_for_tracked_object(model)
print(model.evals_result_)
print(model.eval_metrics(data=Pool(test_data, test_label), metrics=["RMSE"]))
# make the prediction using the resulting model
preds_class = model.predict(test_pool, prediction_type='Class')
# print("Class", type(preds_class), preds_class)
preds_proba = model.predict(test_pool, prediction_type='Probability')
# print("Proba", type(preds_proba), preds_proba)
print(eval_metric(test_label, preds_proba[:, 0], metric="RMSE"))
preds_raw_vals = model.predict(test_pool, prediction_type='RawFormulaVal')
model.save_model("/tmp/catboost_model")
model = CatBoost()
model.load_model("/tmp/catboost_model")

