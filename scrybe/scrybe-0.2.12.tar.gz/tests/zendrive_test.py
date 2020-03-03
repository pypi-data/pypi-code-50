import scrybe
import xgboost as xgb
import joblib
from sklearn.model_selection import GridSearchCV


scrybe.init("scrybe e2e client testing")

train_test_df = joblib.load('tests/data/gb_5.csv')
train_df = train_test_df[train_test_df.train_test_tag == 'train']
train_label = train_df['trip_label']
test_df = train_test_df[train_test_df.train_test_tag == 'test']
test_label = test_df['trip_label']

dvp_features = ['Column 0', 'Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5', 'Column 6', 'Column 7',
                'Column 8', 'Column 9', 'Column 10', 'Column 11']

train_df = train_df[dvp_features].copy()

params = {'learning_rate': [0.01, 0.1, 0.5, 1.0],
          'min_child_weight': [10],
          'max_depth': [1, 2, 3, 4],
          'subsample': [0.5, 0.6, 0.8, 1.0],
          'colsample_bytree': [0.5, 0.6, 0.8, 1.0]
          }
scale_pos_weight = 1
xgb_classif = xgb.XGBClassifier(verbosity=2, n_estimators=n_estim,
                                objective='binary:logistic',
                                scale_pos_weight=scale_pos_weight, reg_alpha=1,
                                reg_lambda=0, random_state=101)
grid_search = GridSearchCV(xgb_classif, param_grid=params, cv=5, scoring='accuracy')
grid_search.fit(train_df, train_label)
best_estim = grid_search.best_estimator_


model_prob = best_estim.predict_proba(train_df)[:, 0]

# sk_mbl.plot_roc_curve(actual_label=train_label, model_prob=model_prob, positive_class='driver')
