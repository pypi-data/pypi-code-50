'''
Algorithm based on mean decrease in accuracy
'''
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from numpy import float64
from sklearn.externals.joblib.parallel import Parallel, delayed
from sklearn.utils.fixes import _joblib_parallel_args
from numpy.random import permutation
from numpy import vstack,mean,square,array,zeros
class lovim(RandomForestRegressor):
    '''
        This class completely inherit scikit-learn's RandomForestRegressor.
        I provide two additional function to compute local variable importance
         importance. One is compute_feature_importance and another is traverse
         which helps compute_feature_importance to traverse every tree in the forest.
    '''

    def __init__(self,
                 n_estimators='warn',
                 criterion="mse",
                 max_depth=None,
                 min_samples_split=2,
                 min_samples_leaf=1,
                 min_weight_fraction_leaf=0.,
                 max_features="auto",
                 max_leaf_nodes=None,
                 min_impurity_decrease=0.,
                 min_impurity_split=None,
                 bootstrap=True,
                 oob_score=False,
                 n_jobs=None,
                 random_state=None,
                 verbose=0,
                 warm_start=False):
        '''
            These parameters are completely same with the class 'RandomForestRegressor', you can
            refer to the help document of sklearn for more detailed information.
        '''
        super(lovim, self).__init__(
            n_estimators=n_estimators,
            criterion=criterion,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf,
            min_weight_fraction_leaf=min_weight_fraction_leaf,
            max_features=max_features,
            max_leaf_nodes=max_leaf_nodes,
            min_impurity_decrease=min_impurity_decrease,
            min_impurity_split=min_impurity_split,
            bootstrap=bootstrap,
            oob_score=oob_score,
            n_jobs=n_jobs,
            random_state=random_state,
            verbose=verbose,
            warm_start=warm_start)
        self.verbose = verbose
        self.n_estimators = n_estimators # trees
    def compute_feature_importance(self, x, y, group_by = None, std = 'Y', n_jobs = None):
        '''
        :param x: input X of data and must be Pandas.DataFrame or Pandas.series
        :param y: input Y of data and do not need specify the type, but must be supported in numpy
        :param group_by: used for separating the data into local groups and a column of data that
        can be hashed, but is not necessary. You can group the data in advance instead and input
        groups one by one.
        For example, if you want to compute local variable importance for each
        day, you only need to let group_by = day of year (1-365).
        :param std: Yes or No normalise the output resulting add up to up for each row.
        :param n_jobs: The number of jobs paralleling at the time. Please refer to class Parallel
        in package sklearn for more detailed information.
        :return:
        '''
        # to obtain the names of variables
        columns = x.columns
        # convert input X into np.array
        x = array(x, dtype=float64)
        # convert input Y to 1-D array
        y = array(y).ravel()
        # to obtain the number of variables
        self.FN = x.shape[1]
        # Produce data_choose array.This array contains bool values to choose rows for training or predictive data
        group_by = group_by
        if type(group_by) != type(None):
            group_by_factor = list(group_by)
            # use set structure to extract factors
            group_by_factor_set = set(group_by_factor)
            group_by_factor_list = list(group_by_factor_set)
            # to obtain the number of group attribute
            self.FL = len(group_by_factor_list)
            group_by_factor_arr = np.array(group_by_factor_list).reshape(self.FL, 1)
            # for each factor find out the rows of input group_by which is equal to it
            data_choose_bool = group_by_factor_arr == group_by_factor
        else:
            # if there is no group_by inputted, using all input rows
            self.FL = 1
            group_by_factor_list = None
            data_choose_bool = np.ones((1, x.shape[0])) == 1
        # Parallel each tree. It is inherited from sklearn, you can refer to sklearn more detailed description.
        indicators = Parallel(n_jobs=n_jobs, verbose=self.verbose, max_nbytes='1M',
                              **_joblib_parallel_args(prefer='threads'))(
            delayed(self.traverse)(tree,x,y,data_choose_bool)
            for tree in self.estimators_) # traverse each tree in a forest
        feature_importances = vstack(indicators) # Vertically stack the arrays returned by traverse forming a
        feature_importances_re = np.average(feature_importances, axis=0)  # To compute weighted feature importance
        if std == 'Y':# whether standardise the output
            # sum up each row
            sum_of_importance_re = feature_importances_re.sum(axis=1).reshape(feature_importances_re.shape[0], 1)
            # each one is divided by the sum of this row
            feature_importances_re = feature_importances_re / (sum_of_importance_re+(sum_of_importance_re == 0))
        else:
            pass
        # return the result with the form of DataFrame
        return pd.DataFrame(feature_importances_re, columns=columns, index=group_by_factor_list )
    def traverse(self,tree,x,y,data_choose_bool):
        '''
        This function is to compute local variable importance for each local group in one tree.
        It returns a 1*n_group*n_feature 3-d array containing the variable importance
        of all variables for each local group.
        :param tree: tree in random forests
        :param x: X of input data
        :param y: Y of input data
        :param data_choose_bool: a array contains bool value used for selecting records if group_by
        is not None.
        :return:a 1*n_group*n_feature 3-d array containing the variable importance
        of all variables for each group
        '''
        # one-time getting the index for selecting records
        data_choose_rows = [np.where(data_choose_bool_s)[0] for data_choose_bool_s in data_choose_bool]
        # permutating the index for selecting records
        per_choose_rows = [permutation(data_choose_rows_s) for data_choose_rows_s in data_choose_rows]
        # compute squared error before permutation for each record so-called original error
        error = square(y-tree.predict(x))
        # generate a array to contain the results
        imp_arr = zeros((1, self.FL, self.FN))
        for index1 in range(self.FL):
            # select records without permutation
            no_per_x = x[data_choose_rows[index1]]
            # select and permutate the records
            ye_per_copy_x = x[per_choose_rows[index1]].copy()
            # select original error
            base_error = error[data_choose_rows[index1]]
            # select input Y
            choose_y = y[data_choose_rows[index1]]
            for index2 in range(self.FN):
                no_per_copy_x = no_per_x.copy()
                # get X whose variable at index "index2" is permutated
                no_per_copy_x[:, index2] = ye_per_copy_x[:, index2]
                # get mean of squared error after permutation
                per_error = square(choose_y-tree.predict(no_per_copy_x))
                imp = mean(per_error - base_error)
                imp_arr[0, index1, index2] = imp
        return imp_arr
'''
Here we provide an example, you can use this class referring these steps below.
gvi = lovim(500,max_features=5,n_jobs=-30)# Generate random forests model
gvi.fit(X,Y) # training 
lvi = gvi.compute_feature_importance(X,Y,group_by=group_by,n_jobs=-30)# compute local variable importance
lvi.to_csv('/home/jjame.csv')# Save the output
'''