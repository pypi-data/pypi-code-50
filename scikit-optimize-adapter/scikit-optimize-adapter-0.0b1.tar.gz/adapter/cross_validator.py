import numpy as np
import tempfile
import os
import logging
import shutil


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class CrossValidator(object):
    
    def __init__(self, df, features, target, K, groupby=None, 
                 cross_validation_scheme='random_shuffle', 
                 orderby=None, num_partition=None, window_size=None):
        
        self.groupby = groupby

        # not sure what the window specs should look like
                
        self.cross_validation_scheme = cross_validation_scheme
        
        allowed_cross_validation_schemes = ["random_shuffle", "ordered", "binary_classification", 
                                            "stratified_sampling", "expanding_window"]
        
        if self.cross_validation_scheme not in allowed_cross_validation_schemes:
            raise ValueError("Expected cross_validation_scheme to be in {allowed}, got {chosen}".format(
                allowed=allowed_cross_validation_schemes, chosen=self.cross_validation_scheme))
            
        if self.cross_validation_scheme == "random_shuffle":
            
            df = df.sample(frac=1).reset_index(drop=True)
            self._cross_validation_scheme = self._random_shuffle_scheme
            scheme_kwargs = {}
        
        elif self.cross_validation_scheme == "ordered":
            
            if orderby is None or not isinstance(orderby, str):
                raise ValueError("")
                
            self._cross_validation_scheme = self._ordered_scheme
            scheme_kwargs = {"orderby": orderby}
            
        elif self.cross_validation_scheme == "binary_classification":
            
            df = df.sample(frac=1).reset_index(drop=True)
            unique_values = df[target].unique()
            
            if len(unique_values) != 2:
                raise ValueError("Expected target values to be in [0.0, 1.0], instead "
                                 "found {}".format(unique_values))
            if not np.allclose(np.array([0.0, 1.0]), unique_values):
                raise ValueError("Expected target values to be in [0.0, 1.0], instead "
                                 "found {}".format(unique_values))
                
            self._cross_validation_scheme = self._binary_classification_scheme
            scheme_kwargs = {"target": target}
        
        elif self.cross_validation_scheme == "stratified_sampling":
            
            df = df.sample(frac=1).reset_index(drop=True)
            if num_partition is None or num_partition <= 0:
                raise ValueError("")
                
            self._cross_validation_scheme = self._stratified_sampling_scheme
            scheme_kwargs = {"num_partition": num_partition}
                
        self.K = K
        self.num_features = len(features)
        
        if self.K < 0:
            raise ValueError("")
            
        self.prepare_folds(df, **scheme_kwargs)
            
    def _random_shuffle_scheme(self, df, random_state=None, **kwargs):

        data = df.to_numpy()
        return data
    
    def _ordered_scheme(self, df, random_state=None, **kwargs):
        # if we sort before, groupby might preserve the order...
        
        orderby = kwargs["orderby"]
        df = df.sort_values(by=orderby).reset_index(drop=True, **kwargs)
        data = df.to_numpy()
        return data
        
    def _binary_classification_scheme(self, df, random_state=None, **kwargs):
        
        target = kwargs["target"]
        target_array = df[target].values

        target0_indices = np.where(np.isclose(target_array, 0.0))[0]
        target1_indices = np.where(np.isclose(target_array, 1.0))[0]

        target0_index_partitions = np.array_split(target0_indices, K)
        target1_index_partitions = np.array_split(target1_indices, K)

        index_partitions = []

        for i in range(K):

            indices = np.concatenate([target0_index_partitions[i], target1_index_partitions[i]])
            np.random.shuffle(indices)
            index_partitions.append(indices)
            
        data_arr_indices = np.concatenate(index_partitions)
        data = df.to_numpy()
        data = data[data_arr_indices]
        return data
        
    def _stratified_sampling_scheme(self, df, random_state=None, **kwargs):
        raise NotImplementedError
        
    def _expanding_window_scheme(self, df, random_state=None, **kwargs):
        raise NotImplementedError
        
    def prepare_folds(self, df, **kwargs):
        """

        We need to write memory map files for X and y separately in order to preserve c-contiguity. 
        Refer: https://github.com/dmlc/xgboost/pull/4165/files/0eb3dd332df1c319a72a82af76f14b13cdf74ae8:611
        """
        
        self.temp_dir = tempfile.mkdtemp()
        
        logger.info(" Created a temporary directory: {}".format(self.temp_dir))
        
        if self.groupby:
            
            self.group_key_filepath_dict = {}
            self.group_key_N_dict = {}
            
            for group_key, grouped_df in df.groupby(by=self.groupby):

                grouped_df = grouped_df.iloc[:, 1:]
                
                self.group_key_N_dict[group_key] = len(grouped_df)

                temp_X_filepath = os.path.join(
                    self.temp_dir, "{group_key}_X.dat".format(group_key=group_key)
                    )

                temp_y_filepath = os.path.join(
                    self.temp_dir, "{group_key}_y.dat".format(group_key=group_key)
                    )

                self.group_key_filepath_dict[group_key] = [temp_X_filepath, temp_y_filepath]
                
                data = self._cross_validation_scheme(grouped_df, **kwargs)
                self._write_memory_map(data[:, :-1], temp_X_filepath)
                self._write_memory_map(data[:, -1], temp_y_filepath)
             
        else:
            
            self.N = len(df)

            temp_X_filepath = os.path.join(self.temp_dir, "data_X.dat")
            temp_y_filepath = os.path.join(self.temp_dir, "data_y.dat")
            self.temp_filepaths = [temp_X_filepath, temp_y_filepath]
            
            data = self._cross_validation_scheme(df, **kwargs)
            self._write_memory_map(data[:, :-1], temp_X_filepath)
            self._write_memory_map(data[:, -1], temp_y_filepath)

    def _write_memory_map(self, data, temp_filepath):

        data = np.ascontiguousarray(data)
        writable_memmap = np.memmap(temp_filepath, dtype="float32", mode="w+", 
                                    shape=(data.shape))
        writable_memmap[:] = data[:]
        del writable_memmap

    def evaluate_fold(self, estimator, k, params, group_key=None):
        
        if group_key:
            N = self.group_key_N_dict[group_key]
            temp_X_filepath = self.group_key_filepath_dict[group_key][0]
            temp_y_filepath = self.group_key_filepath_dict[group_key][1]
        else:
            N = self.N
            temp_X_filepath = self.temp_filepaths[0]
            temp_y_filepath = self.temp_filepaths[1]
            
        readonly_memmap_X = np.memmap(
            temp_X_filepath, dtype="float32", mode="r", shape=(N, self.num_features)
            )
        
        readonly_memmap_y = np.memmap(
            temp_y_filepath, dtype="float32", mode="r", shape=(N, )
            )

        mult, rem = divmod(N, self.K)
        index_partitions = [(i * mult + min(rem, i), 
                             (i + 1) * mult + min(rem, i + 1)) 
                            for i in range(self.K)]

        train_index_partitions = [index_partition for (i, index_partition) in 
                                  enumerate(index_partitions) if i != k]
        train_index_slices = [slice(*index_tuple) for index_tuple in 
                              train_index_partitions]
        train_index = (lambda *args: np.r_[args])(*train_index_slices)

        train_X = readonly_memmap_X[train_index]
        train_y = readonly_memmap_y[train_index]

        validation_index_slice = slice(*index_partitions[k])
        validation_index = np.r_[validation_index_slice]

        validation_X = readonly_memmap_X[validation_index]
        validation_y = readonly_memmap_y[validation_index]

        assert train_X.flags.c_contiguous
        assert train_y.flags.c_contiguous
        assert validation_X.flags.c_contiguous
        assert validation_y.flags.c_contiguous
        
        if estimator:
            estimator.fit(train_X, train_y, params)
            error = estimator.score(validation_X, validation_y)
        else:
            error = None
        
        del readonly_memmap_X
        del train_X
        del validation_X
        del readonly_memmap_y
        del train_y
        del validation_y
        
        return error

    def remove_tempdir(self):

        shutil.rmtree(self.temp_dir)
