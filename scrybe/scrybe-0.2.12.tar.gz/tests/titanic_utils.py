import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import StratifiedShuffleSplit, RandomizedSearchCV, GridSearchCV


class general_cleaner(BaseEstimator, TransformerMixin):
    '''
    This class applies what we know from the documetation.
    It cleans some known missing values
    If flags the missing values

    This process is supposed to happen as first step of any pipeline
    '''

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        # LotFrontage
        X.loc[X.LotFrontage.isnull(), 'LotFrontage'] = 0
        # Alley
        X.loc[X.Alley.isnull(), 'Alley'] = "NoAlley"
        # MSSubClass
        X['MSSubClass'] = X['MSSubClass'].astype(str)
        # MissingBasement
        fil = ((X.BsmtQual.isnull()) & (X.BsmtCond.isnull()) & (X.BsmtExposure.isnull()) &
               (X.BsmtFinType1.isnull()) & (X.BsmtFinType2.isnull()))
        fil1 = ((X.BsmtQual.notnull()) | (X.BsmtCond.notnull()) | (X.BsmtExposure.notnull()) |
                (X.BsmtFinType1.notnull()) | (X.BsmtFinType2.notnull()))
        X.loc[fil1, 'MisBsm'] = 0
        X.loc[fil, 'MisBsm'] = 1  # made explicit for safety
        # BsmtQual
        X.loc[fil, 'BsmtQual'] = "NoBsmt"  # missing basement
        # BsmtCond
        X.loc[fil, 'BsmtCond'] = "NoBsmt"  # missing basement
        # BsmtExposure
        X.loc[fil, 'BsmtExposure'] = "NoBsmt"  # missing basement
        # BsmtFinType1
        X.loc[fil, 'BsmtFinType1'] = "NoBsmt"  # missing basement
        # BsmtFinType2
        X.loc[fil, 'BsmtFinType2'] = "NoBsmt"  # missing basement
        # BsmtFinSF1
        X.loc[fil, 'BsmtFinSF1'] = 0  # No bsmt
        # BsmtFinSF2
        X.loc[fil, 'BsmtFinSF2'] = 0  # No bsmt
        # BsmtUnfSF
        X.loc[fil, 'BsmtUnfSF'] = 0  # No bsmt
        # TotalBsmtSF
        X.loc[fil, 'TotalBsmtSF'] = 0  # No bsmt
        # BsmtFullBath
        X.loc[fil, 'BsmtFullBath'] = 0  # No bsmt
        # BsmtHalfBath
        X.loc[fil, 'BsmtHalfBath'] = 0  # No bsmt
        # FireplaceQu
        X.loc[(X.Fireplaces == 0) & (X.FireplaceQu.isnull()), 'FireplaceQu'] = "NoFire"  # missing
        # MisGarage
        fil = ((X.GarageYrBlt.isnull()) & (X.GarageType.isnull()) & (X.GarageFinish.isnull()) &
               (X.GarageQual.isnull()) & (X.GarageCond.isnull()))
        fil1 = ((X.GarageYrBlt.notnull()) | (X.GarageType.notnull()) | (X.GarageFinish.notnull()) |
                (X.GarageQual.notnull()) | (X.GarageCond.notnull()))
        X.loc[fil1, 'MisGarage'] = 0
        X.loc[fil, 'MisGarage'] = 1
        # GarageYrBlt
        X.loc[X.GarageYrBlt > 2200, 'GarageYrBlt'] = 2007  # correct mistake
        X.loc[fil, 'GarageYrBlt'] = X['YearBuilt']  # if no garage, use the age of the building
        # GarageType
        X.loc[fil, 'GarageType'] = "NoGrg"  # missing garage
        # GarageFinish
        X.loc[fil, 'GarageFinish'] = "NoGrg"  # missing
        # GarageQual
        X.loc[fil, 'GarageQual'] = "NoGrg"  # missing
        # GarageCond
        X.loc[fil, 'GarageCond'] = "NoGrg"  # missing
        # Fence
        X.loc[X.Fence.isnull(), 'Fence'] = "NoFence"  # missing fence
        # Pool
        fil = ((X.PoolArea == 0) & (X.PoolQC.isnull()))
        X.loc[fil, 'PoolQC'] = 'NoPool'

        # del X['Id']
        # del X['MiscFeature']  # we already know it doesn't matter

        return X


class tr_numeric(BaseEstimator, TransformerMixin):
    def __init__(self, SF_room=True, bedroom=True, bath=True, lot=True, service=True):
        self.columns = []  # useful to well behave with FeatureUnion

    def fit(self, X, y=None):
        return self

    def remove_skew(self, X, column):
        X[column] = np.log1p(X[column])
        return X

    def transform(self, X, y=None):
        for col in ['GrLivArea', '1stFlrSF', 'LotArea']:
            X = self.remove_skew(X, col)

        self.columns = X.columns
        return X

    def get_features_name(self):
        return self.columns


class make_ordinal(BaseEstimator, TransformerMixin):
    '''
    Transforms ordinal features in order to have them as numeric (preserving the order)
    If unsure about converting or not a feature (maybe making dummies is better), make use of
    extra_cols and unsure_conversion
    '''

    def __init__(self, cols, extra_cols=None, include_extra=True):
        self.cols = cols
        self.extra_cols = extra_cols
        self.mapping = {'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5}
        self.include_extra = include_extra

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        if self.extra_cols:
            if self.include_extra:
                self.cols += self.extra_cols
            else:
                for col in self.extra_cols:
                    del X[col]

        for col in self.cols:
            X.loc[:, col] = X[col].map(self.mapping).fillna(0)
        return X


class recode_cat(BaseEstimator, TransformerMixin):
    '''
    Recodes some categorical variables according to the insights gained from the
    data exploration phase.
    '''

    def fit(self, X, y=None):
        return self

    def tr_GrgType(self, data):
        data['GarageType'] = data['GarageType'].map({'Basment': 'Attchd',
                                                     'CarPort': 'Detchd',
                                                     '2Types': 'Attchd'}).fillna(data['GarageType'])
        return data

    def tr_LotShape(self, data):
        fil = (data.LotShape != 'Reg')
        data['LotShape'] = 1
        data.loc[fil, 'LotShape'] = 0
        return data

    def tr_LandCont(self, data):
        fil = (data.LandContour == 'HLS') | (data.LandContour == 'Low')
        data['LandContour'] = 0
        data.loc[fil, 'LandContour'] = 1
        return data

    def tr_MSZoning(self, data):
        data['MSZoning'] = data['MSZoning'].map({'RH': 'RM',  # medium and high density
                                                 'C (all)': 'RM',  # commercial and medium density
                                                 'FV': 'RM'}).fillna(data['MSZoning'])
        return data

    def tr_Alley(self, data):
        fil = (data.Alley != 'NoAlley')
        data['Alley'] = 0
        data.loc[fil, 'Alley'] = 1
        return data

    def tr_LotConfig(self, data):
        data['LotConfig'] = data['LotConfig'].map({'FR3': 'Corner',  # corners have 2 or 3 free sides
                                                   'FR2': 'Corner'}).fillna(data['LotConfig'])
        return data

    def tr_BldgType(self, data):
        data['BldgType'] = data['BldgType'].map({'Twnhs': 'TwnhsE',
                                                 '2fmCon': 'Duplex'}).fillna(data['BldgType'])
        return data

    def tr_MasVnrType(self, data):
        data['MasVnrType'] = data['MasVnrType'].map({'BrkCmn': 'BrkFace'}).fillna(data['MasVnrType'])
        return data

    def tr_HouseStyle(self, data):
        data['HouseStyle'] = data['HouseStyle'].map({'1.5Fin': '1.5Unf',
                                                     '2.5Fin': '2Story',
                                                     '2.5Unf': '2Story',
                                                     'SLvl': 'SFoyer'}).fillna(data['HouseStyle'])
        return data

    def transform(self, X, y=None):
        X = self.tr_GrgType(X)
        X = self.tr_LotShape(X)
        X = self.tr_LotConfig(X)
        X = self.tr_MSZoning(X)
        X = self.tr_Alley(X)
        X = self.tr_LandCont(X)
        X = self.tr_BldgType(X)
        X = self.tr_MasVnrType(X)
        X = self.tr_HouseStyle(X)
        return X


class drop_columns(BaseEstimator, TransformerMixin):
    '''
    Drops columns that are not useful for the model
    '''

    def __init__(self):
        self.columns = []

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        to_drop = [col for col in X.columns if 'NoGrg' in col]  # dropping dummies that are redundant
        to_drop += [col for col in X.columns if 'NoBsmt' in col]
        # other not useful columns
        to_drop += [col for col in X.columns if 'MSSubClass' in col]
        to_drop += [col for col in X.columns if 'Neighborhood' in col]  # maybe useful in the future
        to_drop += [col for col in X.columns if 'Condition1' in col]
        to_drop += [col for col in X.columns if 'Condition2' in col]
        to_drop += [col for col in X.columns if 'ExterCond' in col]  # maybe make it ordinal
        to_drop += [col for col in X.columns if 'Exterior1st' in col]
        to_drop += [col for col in X.columns if 'Exterior2nd' in col]
        to_drop += [col for col in X.columns if 'Functional' in col]
        to_drop += [col for col in X.columns if 'Heating_' in col]  # we don't want to drop the dummies of HeatingQC too
        to_drop += [col for col in X.columns if 'PoolQC' in col]
        to_drop += [col for col in X.columns if 'RoofMatl' in col]
        to_drop += [col for col in X.columns if 'RoofStyle' in col]
        to_drop += [col for col in X.columns if 'SaleCondition' in col]
        to_drop += [col for col in X.columns if 'SaleType' in col]
        to_drop += [col for col in X.columns if 'Utilities' in col]
        to_drop += [col for col in X.columns if 'BsmtCond' in col]  # maybe ordinal
        to_drop += [col for col in X.columns if 'Electrical' in col]
        to_drop += [col for col in X.columns if 'Foundation' in col]
        to_drop += [col for col in X.columns if 'LandSlope' in col]
        to_drop += [col for col in X.columns if 'Street' in col]
        to_drop += [col for col in X.columns if 'Fence' in col]
        to_drop += [col for col in X.columns if 'PavedDrive' in col]

        for col in to_drop:
            try:
                del X[col]
            except KeyError:
                pass

        self.columns = X.columns
        return X

    def get_feature_names(self):
        return list(self.columns)


def make_test(train, test_size, random_state, strat_feat=None):
    if strat_feat:

        split = StratifiedShuffleSplit(n_splits=1, test_size=test_size, random_state=random_state)

        for train_index, test_index in split.split(train, train[strat_feat]):
            train_set = train.loc[train_index]
            test_set = train.loc[test_index]

    return train_set, test_set


def cv_score(df_train, y_train, kfolds, pipeline, imp_coef=False):
    oof = np.zeros(len(df_train))
    train = df_train.copy()

    feat_df = pd.DataFrame()

    for n_fold, (train_index, test_index) in enumerate(kfolds.split(train.values)):

        trn_data = train.iloc[train_index][:]
        val_data = train.iloc[test_index][:]

        trn_target = y_train.iloc[train_index].values.ravel()
        val_target = y_train.iloc[test_index].values.ravel()

        pipeline.fit(trn_data, trn_target)

        oof[test_index] = pipeline.predict(val_data).ravel()

        if imp_coef:
            try:
                fold_df = get_coef(pipeline)
            except AttributeError:
                fold_df = get_feature_importance(pipeline)

            fold_df['fold'] = n_fold + 1
            feat_df = pd.concat([feat_df, fold_df], axis=0)

    if imp_coef:
        feat_df = feat_df.groupby('feat')['score'].agg(['mean', 'std'])
        feat_df['abs_sco'] = (abs(feat_df['mean']))
        feat_df = feat_df.sort_values(by=['abs_sco'], ascending=False)
        del feat_df['abs_sco']
        return oof, feat_df
    else:
        return oof


def grid_search(data, target, estimator, param_grid, scoring, cv, random=False):
    if random:
        grid = RandomizedSearchCV(estimator=estimator, param_distributions=param_grid, cv=cv, scoring=scoring,
                                  n_iter=random, n_jobs=-1, random_state=434, iid=False)
    else:
        grid = GridSearchCV(estimator=estimator, param_grid=param_grid,
                            cv=cv, scoring=scoring, n_jobs=-1, return_train_score=False)

    pd.options.mode.chained_assignment = None  # turn on and off a warning of pandas
    tmp = data.copy()
    grid = grid.fit(tmp, target)
    pd.options.mode.chained_assignment = 'warn'

    result = pd.DataFrame(grid.cv_results_).sort_values(by='mean_test_score',
                                                        ascending=False).reset_index()

    del result['params']
    times = [col for col in result.columns if col.endswith('_time')]
    params = [col for col in result.columns if col.startswith('param_')]

    result = result[params + ['mean_test_score', 'std_test_score'] + times]

    return result, grid.best_params_, grid.best_estimator_


def get_coef(pipe):
    imp = pipe.steps[-1][1].coef_.tolist()
    feats = pipe.steps[-2][1].get_feature_names()
    result = pd.DataFrame({'feat': feats, 'score': imp})
    result['abs_res'] = abs(result['score'])
    result = result.sort_values(by=['abs_res'], ascending=False)
    del result['abs_res']
    return result


def get_feature_importance(pipe):
    imp = pipe.steps[-1][1].feature_importances_.tolist()  # it's a pipeline
    feats = pipe.steps[-2][1].get_feature_names()
    result = pd.DataFrame({'feat': feats, 'score': imp})
    result = result.sort_values(by=['score'], ascending=False)
    return result


def _plot_diagonal(ax):
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    low = min(xmin, xmax)
    high = max(xmin, xmax)
    scl = (high - low) / 100

    line = pd.DataFrame({'x': np.arange(low, high, scl),  # small hack for a diagonal line
                         'y': np.arange(low, high, scl)})
    ax.plot(line.x, line.y, color='black', linestyle='--')

    return ax


def plot_predictions(data, true_label, pred_label, feature=None, hue=None, legend=False):
    tmp = data.copy()
    tmp['Prediction'] = pred_label
    tmp['True Label'] = true_label
    tmp['Residual'] = tmp['True Label'] - tmp['Prediction']

    diag = False
    alpha = 0.7
    label = ''

    fig, ax = plt.subplots(1, 2, figsize=(15, 6))

    if feature is None:
        feature = 'True Label'
        diag = True
    else:
        legend = 'full'
        sns.scatterplot(x=feature, y='True Label', data=tmp, ax=ax[0], label='True',
                        hue=hue, legend=legend, alpha=alpha)
        label = 'Predicted'
        alpha = 0.4

    sns.scatterplot(x=feature, y='Prediction', data=tmp, ax=ax[0], label=label,
                    hue=hue, legend=legend, alpha=alpha)
    if diag:
        ax[0] = _plot_diagonal(ax[0])

    sns.scatterplot(x=feature, y='Residual', data=tmp, ax=ax[1],
                    hue=hue, legend=legend, alpha=0.7)
    ax[1].axhline(y=0, color='r', linestyle='--')

    ax[0].set_title('%s vs Predictions' % feature)
    ax[1].set_title('%s vs Residuals' % feature)


def SF_per_room(data):
    data['sf_per_room'] = data['GrLivArea'] / data['TotRmsAbvGrd']
    return data


def bedroom_prop(data):
    data['bedroom_prop'] = data['BedroomAbvGr'] / data['TotRmsAbvGrd']
    return data


def total_bath(data):
    data['total_bath'] = data[[col for col in data.columns if 'FullBath' in col]].sum(axis=1) + 0.5 * data[
        [col for col in data.columns if 'HalfBath' in col]].sum(axis=1)
    return data


def lot_prop(data):
    data['lot_prop'] = data['LotArea'] / data['GrLivArea']
    return data


def service_area(data):
    data['service_area'] = data['TotalBsmtSF'] + data['GarageArea']
    return data


def tr_neighborhood(data, y=None):
    # mean and standard deviation of the price per Neighborhood
    means = data.groupby('Neighborhood')['target'].mean()
    stds = data.groupby('Neighborhood')['target'].std()
    data['Neig_target_mean'] = data['Neighborhood'].map(means)
    data['Neig_target_std'] = data['Neighborhood'].map(stds)
    # mean and standard deviation of the house size per Neighborhood
    means = data.groupby('Neighborhood')['GrLivArea'].mean()
    stds = data.groupby('Neighborhood')['GrLivArea'].std()
    data['Neig_GrLivArea_mean'] = data['Neighborhood'].map(means)
    data['Neig_GrLivArea_std'] = data['Neighborhood'].map(stds)

    return data


def tr_mssubclass(data, y=None):
    # mean and standard deviation of the price per Neighborhood
    means = data.groupby('MSSubClass')['target'].mean()
    stds = data.groupby('MSSubClass')['target'].std()
    data['MSSC_target_mean'] = data['MSSubClass'].map(means)
    data['MSSC_target_std'] = data['MSSubClass'].map(stds)
    # mean and standard deviation of the house size per Neighborhood
    means = data.groupby('MSSubClass')['GrLivArea'].mean()
    stds = data.groupby('MSSubClass')['GrLivArea'].std()
    data['MSSC_GrLivArea_mean'] = data['MSSubClass'].map(means)
    data['MSSC_GrLivArea_std'] = data['MSSubClass'].map(stds)

    return data

