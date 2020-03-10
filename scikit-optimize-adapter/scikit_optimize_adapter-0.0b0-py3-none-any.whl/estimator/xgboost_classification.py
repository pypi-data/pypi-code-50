from .base_estimator import BaseEstimator
import xgboost as xgb
from sklearn.metrics import mean_absolute_error as mae
# add more metrics

class XgboostClassification(BaseEstimator):
    
    def __init__(self, **kwargs):
        self.n_jobs = kwargs["n_jobs"]
    
    def fit(self, X, y, params):
        
        learning_rate = params[0]
        gamma = params[1]
        max_depth = int(params[2])
        n_estimators = int(params[3])
        learning_rate = learning_rate / float(n_estimators)
        min_child_weight = int(params[4])
        colsample_bytree = params[5]
        subsample = params[6]

        algo = xgb.XGBRegressor(objective ="binary:logistic", 
                                learning_rate=learning_rate,
                                gamma=gamma,
                                max_depth=max_depth,
                                n_estimators=n_estimators,
                                min_child_weight=min_child_weight,
                                colsample_bytree=colsample_bytree,
                                subsample=subsample,
                                n_jobs=self.n_jobs,
                                tree_method='hist')  # for fast hyperparameter tuning)

        self.model = algo.fit(X, y)
        
    def predict(self, X):
        
        return self.model.predict(X)
        
    def score(self, X, y, score_metric="mae"):
        
        pred = self.model.predict(X)
        return mae(pred, y)
    
    