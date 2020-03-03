import scrybe
from sklearn.model_selection import KFold

from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
from tests.titanic_utils import *
from sklearn.ensemble import RandomForestRegressor
from tests import data_pipeline as dfp


scrybe.init("scrybe e2e client testing")
pd.set_option('max_columns', 200)


class drop_columns(BaseEstimator, TransformerMixin):
    '''
    Drops columns that are not useful for the model
    The decisions come from several iterations
    '''

    def __init__(self, lasso=False, ridge=False, forest=False, xgb=False, lgb=False):
        self.columns = []
        self.lasso = lasso
        self.ridge = ridge
        self.forest = forest
        self.xgb = xgb
        self.lgb = lgb

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        to_drop = [col for col in X.columns if 'NoGrg' in col]  # dropping dummies that are redundant
        to_drop += [col for col in X.columns if 'NoBsmt' in col]

        if self.lasso:
            to_drop += [col for col in X.columns if 'BsmtExposure' in col]
            to_drop += [col for col in X.columns if 'BsmtCond' in col]
            to_drop += [col for col in X.columns if 'ExterCond' in col]
            to_drop += [col for col in X.columns if 'HouseStyle' in col]
            to_drop += [col for col in X.columns if 'LotShape' in col]
            to_drop += [col for col in X.columns if 'LotFrontage' in col]
            to_drop += [col for col in X.columns if 'GarageYrBlt' in col]
            to_drop += [col for col in X.columns if 'GarageType' in col]
            to_drop += ['OpenPorchSF', '3SsnPorch']
        if self.ridge:
            to_drop += [col for col in X.columns if 'BsmtExposure' in col]
            to_drop += [col for col in X.columns if 'BsmtCond' in col]
            to_drop += [col for col in X.columns if 'ExterCond' in col]
            to_drop += [col for col in X.columns if 'LotFrontage' in col]
            to_drop += [col for col in X.columns if 'LotShape' in col]
            to_drop += [col for col in X.columns if 'HouseStyle' in col]
            to_drop += [col for col in X.columns if 'GarageYrBlt' in col]
            to_drop += [col for col in X.columns if 'GarageCars' in col]
            to_drop += [col for col in X.columns if 'BldgType' in col]
            to_drop += ['OpenPorchSF', '3SsnPorch']
        if self.forest:
            to_drop += [col for col in X.columns if 'BsmtExposure' in col]
            to_drop += [col for col in X.columns if 'BsmtCond' in col]
            to_drop += [col for col in X.columns if 'ExterCond' in col]
            to_drop += ['OpenPorchSF', '3SsnPorch']
        if self.xgb:
            to_drop += [col for col in X.columns if 'BsmtExposure' in col]
            to_drop += [col for col in X.columns if 'BsmtCond' in col]
            to_drop += [col for col in X.columns if 'ExterCond' in col]
        if self.lgb:
            to_drop += [col for col in X.columns if 'LotFrontage' in col]
            to_drop += [col for col in X.columns if 'HouseStyle' in col]
            to_drop += ['MisBsm']

        for col in to_drop:
            try:
                del X[col]
            except KeyError:
                pass

        self.columns = X.columns
        return X

    def get_feature_names(self):
        return list(self.columns)



import os
df_train = pd.read_csv('data/train.csv')
df_train = df_train[df_train.GrLivArea < 4500].reset_index(drop=True)


df_train.Neighborhood.value_counts(normalize=True)
df_train['target'] = np.log1p(df_train.SalePrice)
del df_train['SalePrice']

train_set, test_set = make_test(df_train,
                                test_size=0.2, random_state=654,
                                strat_feat='Neighborhood')
y = train_set['target'].copy()
del train_set['target']
y_test = test_set['target']
del test_set['target']

folds = KFold(5, shuffle=True, random_state=541)

numeric_forest = Pipeline([('fs', dfp.feat_sel('numeric')),
                         ('imp', dfp.df_imputer(strategy='median')),
                         ('transf', tr_numeric(SF_room=False,
                                               bedroom=False,
                                               lot=False))])


cat_forest = Pipeline([('fs', dfp.feat_sel('category')),
                     ('imp', dfp.df_imputer(strategy='most_frequent')),
                     ('ord', make_ordinal(['BsmtQual', 'KitchenQual', 'ExterQual', 'HeatingQC'],
                                          extra_cols=['BsmtExposure', 'BsmtCond', 'ExterCond'],
                                          include_extra='include')),
                     ('recode', recode_cat()),
                     ('dummies', dfp.dummify(drop_first=True))])


processing_forest = dfp.FeatureUnion_df(transformer_list=[('cat', cat_forest),
                                                 ('num', numeric_forest)])

forest_pipe = Pipeline([('gen_cl', general_cleaner()),
                       ('proc', processing_forest),
                       ('scaler', dfp.df_scaler(method='robust')),
                       ('dropper', drop_columns(forest=True)),
                       ('forest', RandomForestRegressor(n_estimators=5, max_depth=30,
                                                        max_features='sqrt',
                                                        n_jobs=-1, random_state=32))])

forest_oof, coefs = cv_score(train_set, y, folds, forest_pipe, imp_coef=True)
tmp = train_set.copy()
forest_pipe.fit(tmp, y)
tmp = test_set.copy()
print("Training Done")
preds = forest_pipe.predict(tmp)
print(forest_pipe.score(tmp, preds))
print(mean_squared_error(y_test, preds))