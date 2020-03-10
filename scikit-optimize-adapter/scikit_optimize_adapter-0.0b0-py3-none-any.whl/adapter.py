from .cross_validator import CrossValidator
from .estimator import XgboostClassification
from .estimator import XgboostRegression
from .optimizer import gp_computation_graph
from .utils import get_host_ip_address
from .utils import get_available_port
from .utils import create_result
from .utils import plot_convergence

from dask.distributed import Client, TimeoutError, LocalCluster

import pandas as pd
import sys
import platform
import shutil
import os
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def compute_computation_graph(delayed_computation_graph, **kwargs):
    return delayed_computation_graph(**kwargs).compute()

class Adapter(object):
    
    def __init__(self, df, features, target, K,
                 groupby=None, orderby=None, num_partition=None, window_size=None,
                 cross_validation_scheme="random_shuffle", 
                 search_method="bayesian_optimization", 
                 estimator="xgboost_regression"):
        
        # check current OS:
        if sys.platform == "darwin":
            if platform.mac_ver()[0] > "10.13.4":  # macOS version for High Sierra
                os.environ["OBJC_DISABLE_INITIALIZE_FORK_SAFETY"] = "YES"
        
        # check dataframe input
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Expected training data input to be a Pandas "
                            "dataframe, but instead received: {}".format(type(df)))
            
        if not set(features) < set(df.columns):
            unrecognized_cols = set(features) - set(df.columns)
            raise ValueError("{} columns are missing from input "
                             "dataframe".format(unrecognized_cols))
            
        if not target in df.columns:
            raise ValueError("{} target column is missing from "
                             "input dataframe".format(target))
            
        if groupby:
            if not groupby in df.columns:
                raise ValueError("{} groupby column is missing from "
                                 "input dataframe".format(groupby))
            else:
                self.group_keys = df[groupby].unique()
            
        if orderby:
            if not orderby in df.columns:
                raise ValueError("{} orderby column is missing from "
                                 "input dataframe".format(orderby))
                
        self.groupby = groupby
        
        # reorder dataframe columns
        if not isinstance(features, list):
            features = list(features)
        column_order = features + [target]
        if groupby:
            column_order = [groupby] + column_order
        df = df[column_order]
        
        # check/set search_method
        allowed_search_methods = ["bayesian_optimization", "random_search"]
        if search_method not in allowed_search_methods:
            raise ValueError("Expected search_method to be in {allowed}, got "
                             "{chosen}".format(allowed=allowed_search_methods, 
                                               chosen=search_method))
        
        if search_method == "bayesian_optimization":
            self.build_computation_graph = gp_computation_graph
        else:
            self.build_computation_graph = None  # not implemented yet
            
        # check/set estimator
        if isinstance(estimator, str):
            implemented_estimators = ["xgboost_regression", "xgboost_classification"]
            if estimator not in implemented_estimators:
                raise ValueError("Expected estimator string input to be in {allowed}, "
                                 "got {chosen}".format(allowed=implemented_estimators, 
                                                       chosen=estimator))
            else:
                if estimator == "xgboost_regression":
                    self.estimator = XgboostRegression(n_jobs=1)  # dynamic thread computer needed
                else:
                    self.estimator = XgboostClassification(n_jobs=1)
        else:
            self.estimator = estimator
            # add checks to interface implementation
        
        # initialize dask distributed client
        host_ip = get_host_ip_address()
        dashboard_port = get_available_port(8787)
        scheduler_port = get_available_port(63482)
        
        logger.info(" http://{}:{}/status".format(host_ip, dashboard_port))
        
        cluster = LocalCluster(processes=True, 
                       host=host_ip, 
                       dashboard_address=':{}'.format(dashboard_port), 
                       scheduler_port=scheduler_port)
        self.client = Client(address=cluster, timeout='2s')
        
        # initialize CrossValidator 
        self.cross_validator = CrossValidator(df, features, target, K, groupby, 
                                              cross_validation_scheme, orderby, 
                                              num_partition, window_size)
        
        # consider moving these to run parameters
        # so you can use the same object and  test diff os  these
        # self.search_space = search_space
        # self.num_initial = num_initial
        # self.num_iter = num_iter
        
    def construct_delayed_graph(self, num_iter=5, num_initial=5, search_space=None, group_key=None):
        
        if self.groupby is not None and group_key is None:
            raise ValueError("group_key cannot be None if groupby is specified")

        if search_space is None:
            raise ValueError("You must specify the search_space")
            
        if num_iter is None:
            num_iter = self.num_iter
        if num_initial is None:
            num_initial = self.num_initial
        
        delayed_graph = self.build_computation_graph(estimator=self.estimator, 
                                                     cross_validator=self.cross_validator, 
                                                     group_key=None, dimensions=search_space, 
                                                     n_calls=num_iter, n_initial_points=num_initial)
        
        return delayed_graph
        
    def run_as_future(self, num_initial, num_iter, search_space):
        """consider more hard controlled submit process"""
        
        futures = dict()
        
        if self.groupby:

            for i, group_key in enumerate(self.group_keys):

                future = self.client.submit(compute_computation_graph, self.build_computation_graph, 
                                            estimator=self.estimator, cross_validator=self.cross_validator, 
                                            group_key=group_key, dimensions=search_space, 
                                            n_calls=num_iter, n_initial_points=num_initial,
                                            priority=-i) 
                futures[group_key] = future
        
            return futures
        
        else:
            
            future = self.client.submit(compute_computation_graph, self.build_computation_graph, 
                                        estimator=self.estimator, cross_validator=self.cross_validator, 
                                        n_calls=num_iter, n_initial_points=num_initial,
                                        group_key=None, dimensions=search_space) 
            
            return future

    def _create_result(self, optimizer_obj):

        return create_result(
            optimizer_obj.Xi, 
            optimizer_obj.yi, 
            optimizer_obj.space, 
            optimizer_obj.rng, 
            models=optimizer_obj.models
            )

    def run(self, num_initial, num_iter, search_space):

        if self.groupby:

            futures = self.run_as_future(num_initial, num_iter, search_space)
            self.results = {k: self._create_result(v.result()) for k, v in futures.items()}
            return self.results

        else:

            future = self.run_as_future(num_initial, num_iter, search_space)
            self.result = self._create_result(future.result())
            return self.result

    def plot_improvements(self, group_key=None):

        if self.groupby:

            if group_key is None:

                raise ValueError("You must specify group_key to produce the plot")

            else:

                plot_convergence(self.results[group_key])

        else:

            plot_convergence(self.result)


    def get_optimal_params(self):

        if self.groupby:

            return {k: v.x for k, v in self.results.items()}

        else:

            return self.result.x

    def cleanup(self):
        
        shutil.rmtree(self.cross_validator.temp_dir)

