"""
Algorithm based on total decrease in node impurity
"""
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from numpy import vstack
from sklearn.externals.joblib.parallel import Parallel, delayed
from sklearn.ensemble import RandomForestRegressor
from sklearn.utils.fixes import _joblib_parallel_args
from numpy import float64
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
        These parameters are completely same with the class 'RandomForestRegressor' in scikit-learn,
         you can refer to the help document of scikit-learn for more detailed information.
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
        # convert input X into numpy.array
        x = np.array(x, dtype=float64)
        y = csr_matrix(np.array(y).reshape(1, x.shape[0]))
        # to obtain the number of variables
        self.FN = x.shape[1]
        # Produce data_choose array.This array contains bool values to select rows for input data.
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
        # to obtain squared y
        y_squared = y.multiply(y)
        # Parallel each tree. It is imported from sklearn, you can refer to sklearn more detailed description.
        indicators = Parallel(n_jobs=n_jobs, verbose=self.verbose, max_nbytes='1M',
                              **_joblib_parallel_args(prefer='threads'))(
            delayed(self.traverse)(tree,x,y,y_squared,
                                     data_choose_bool)
            for tree in self.estimators_) # traverse each tree in a forest
        feature_importances = vstack(indicators) # Vertically stack the arrays returned by traverse forming a
        feature_importances_re = np.average(feature_importances, axis=0)# To compute weighted feature importance
        if std == 'Y':# whether standardise the output
            # sum up each row
            sum_of_importance_re = feature_importances_re.sum(axis=1).reshape(feature_importances_re.shape[0], 1)
            # each one is divided by the sum of this row
            feature_importances_re = feature_importances_re / (sum_of_importance_re+(sum_of_importance_re == 0))
        else:
            pass
        # return the result with the form of DataFrame
        return pd.DataFrame(feature_importances_re, columns=columns, index=group_by_factor_list )
    def traverse(self,tree,x,y,y_squared,data_choose_bool):
        '''
        This function is to compute variable importance for each local group in one tree.
        It returns a 1*n_group*n_feature 3-d array containing the variable importance
        of all variables for each local group
        :param tree: a tree in random forests
        :param x: X of input data
        :param y: Y of input data
        :param y_squared: Squared y
        :param data_choose_bool: a array contains bool value used for selecting rows
        if group_by is not None.
        :return:a 1*n_group*n_feature 3-d array containing the variable importance
        of all variables for each group in this tree
        '''
        feature_index = np.arange(0, self.FN)
        # to obtain the split feature at each node in this tree
        node_fa_feature = tree.tree_.feature
        # reshape it
        node_fa_feature_co = node_fa_feature.reshape(node_fa_feature.shape[0], 1)
        # use sparse matrix to contain to feature array
        fa_feature = csr_matrix(node_fa_feature_co == feature_index)
        # to obtain the index of left child node for each split node
        children_left = tree.tree_.children_left
        # to obtain the index of right child node for each split node
        children_right = tree.tree_.children_right
        # generate a zero matrix to contain the results
        feature_importance = np.zeros((1,self.FL, self.FN))
        for inde in range(self.FL):
            # to obtain the index of row
            data_choose = np.where(data_choose_bool[inde])
            # via index of row to select rows of X
            choose_x = x[data_choose]
            # via index of row to select rows of Y
            choose_y = y[0, data_choose]
            # via index of row to select rows of squared Y
            choose_y_squared = y_squared[0, data_choose]
            # to obtain decision path for each row
            decision_path_v = tree.decision_path(choose_x)
            # to obtain the numbers of records at each node in this tree
            data_num = np.array(decision_path_v.sum(axis=0))[0]
            # to select node which containing more than one record. Because there is no squared error if the node has less than tow records.
            data_num_lar = (data_num > 1)
            # to obtain the index of node which containing more one record.
            col_choose = np.where(data_num_lar)[0]
            # select nodes
            decision_path_pre = decision_path_v[:, col_choose]
            # compute sum of y for each selected nodes
            node_y_sum = choose_y.dot(decision_path_pre)
            # to compute squared sum of y for each selected nodes
            node_y_sum_squared = node_y_sum.multiply(node_y_sum)
            # compute sum of squared y for every selected nodes
            node_y_squared_sum = choose_y_squared.dot(decision_path_pre)
            # get sum of squared error
            node_sse_v = node_y_squared_sum - node_y_sum_squared / data_num[col_choose]
            node_sse_v = np.array(node_sse_v)[0]
            # select nodes index of left child node for nodes which have more than one records
            choose_children_left = children_left[col_choose]
            # select nodes index of right child node for nodes which have more than one records
            choose_children_right = children_right[col_choose]
            left_inter_sse = np.intersect1d(col_choose, choose_children_left, return_indices=True)
            right_inter_sse = np.intersect1d(col_choose, choose_children_right, return_indices=True)
            # get the index of 'col_choose' which the  element is in 'choose_children_left'
            searchsort_sse_left = left_inter_sse[1]
            # get the index of 'col_choose' which the  element is in 'choose_children_right'
            searchsort_sse_right = right_inter_sse[1]
            # get the index of 'choose_children_left' which the  element is in 'col_choose'
            node_left_index = left_inter_sse[2]
            # get the index of 'choose_children_right' which the  element is in 'col_choose'
            node_right_index = right_inter_sse[2]
            left_sse = np.zeros(node_sse_v.shape)
            right_sse = left_sse.copy()
            # assign sum of squared error of left child node to index where the parent node at
            left_sse[node_left_index] = node_sse_v[searchsort_sse_left]
            # assign sum of squared error of right child node to index where the parent node at
            right_sse[node_right_index] = node_sse_v[searchsort_sse_right]
            #parent node sum of squared error minus the corresponding position left child node and right child node sum of squared error
            node_rsse = node_sse_v - left_sse - right_sse
            fa_feature_choose = fa_feature[col_choose]
            # assign all reduction of sum of squared error to the corresponding variable and sum them.
            feature_importance[0, inde] = csr_matrix(node_rsse).dot(fa_feature_choose).toarray()
        return feature_importance
'''
Here we provide an example, you can use this class referring these steps below.
gvi = lovim(500,max_features=5,n_jobs=-30)# Generate random forests model
gvi.fit(X,Y) # training 
lvi = gvi.compute_feature_importance(X,Y,group_by=group_by,n_jobs=-30)# compute local variable importance
lvi.to_csv('/home/jjame.csv')# Save the output
'''