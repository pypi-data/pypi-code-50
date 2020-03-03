import numpy as  np
from math import gcd
import bisect
import copy

def get_obj_no_from_index(idx, object_example_lut):
    obj_idx = bisect.bisect(object_example_lut, idx) - 1
    offset = idx - object_example_lut[obj_idx]
    return obj_idx, offset

class prsample:

    def __init__(self, object_list, examples_per_batch, examples_per_obj, get_example_from_obj, shuffle = True, seed = 69):
        """
            Creates a prsample object.

            Args:
                object_list: A nested structure of datasets.
                examples_per_batch: A nested structure of datasets.
                examples_per_obj: A nested structure of datasets.
                get_example_from_obj: A nested structure of datasets.
                debug: A nested structure of datasets.
                shuffle: A nested structure of datasets.
                seed: A nested structure of datasets.

            Returns:
                None
        """
        
        self._object_list = []
        for class_no, data in enumerate(object_list):
            data['class_no'] = class_no
            self._object_list.append(data)

        assert isinstance(examples_per_batch, int) , 'examples_per_batch must be an int type.'
        assert examples_per_batch > 0, 'examples_per_batch must be positive.'
        self.examples_per_batch = examples_per_batch

        assert callable(examples_per_obj), "examples_per_obj must be a function."
        assert callable(get_example_from_obj), "get_example_from_obj must be a function."
        self.examples_per_object = examples_per_obj
        self.get_example_from_object = get_example_from_obj

        assert isinstance(shuffle, bool) , 'shuffle must be an bool type.'
        self.shuffle = shuffle
        self.unshuffled_object_list = object_list
        
        assert isinstance(seed, int) , 'seed must be an int type.'
        self.seed = seed
        
        self.init_prsample()

        return

    def __len__(self):
        return self.examples_per_batch_index

    def get_example(self, index, batch_index):

        idx = self._batch_to_idx(index, batch_index, self.examples_per_batch, self.batch_strides, \
            self.examples_per_batch_index, self.total_example_count)
        return self.get_example_from_object(idx, self.example_lut, self._object_list, self.cumulative_example_lut)

    def _batch_to_idx(self, index, batch_index, examples_per_batch, batch_strides, examples_per_batch_index, total_example_count):
        idx = (batch_index + examples_per_batch*(((index+batch_index) * batch_strides[batch_index])%examples_per_batch_index) )%total_example_count
        return idx

    # object_list - a list of objects from which examples will be extracted
    # examples_per_object -  function that takes a index into the object list and the object list and returns the count of examples this object can produce
    def _build_example_lut(self, object_list, examples_per_object):
        example_counter = 0
        object_example_lut = np.empty(len(object_list), dtype = int)
        for object_no in range(len(object_list)):
            object_example_lut[object_no] = example_counter
            example_counter += examples_per_object(object_no, object_list)
        return example_counter, object_example_lut

    def _is_coprime(self, a, b):
        return gcd(a, b) == 1

    def _find_batch_strides(self, examples_per_batch, total_example_count, examples_per_batch_index):
        if examples_per_batch_index == 1:
            batch_strides = np.empty(examples_per_batch, dtype = int)
        else:
            return np.ones(examples_per_batch, dtype = int)

        for batch_index in range(examples_per_batch):
            stride = np.random.randint(2, examples_per_batch_index)
            while not self._is_coprime(stride, examples_per_batch_index):
                stride = (stride + 1)%examples_per_batch_index
                if stride == 0:
                    stride = 2
            batch_strides[batch_index] = stride
        return batch_strides

    def init_prsample(self):
        
        self.seed += 1
        np.random.seed(self.seed)

        if self.shuffle:
            np.random.shuffle(self._object_list)

        class_count = len(self._object_list)
        self.cumulative_example_lut = np.zeros(class_count+1, dtype = int)
        for class_id in range(class_count):
            object_example_count = self._object_list[class_id]['class_example_count']
            self.cumulative_example_lut[class_id+1] =+ self.cumulative_example_lut[class_id] + object_example_count

        self.total_example_count, self.example_lut = self._build_example_lut(self._object_list, self.examples_per_object)

        self.number_of_batches = int(np.ceil(self.total_example_count / self.examples_per_batch))

        self.examples_per_batch_index = int(np.ceil(self.total_example_count/self.examples_per_batch))

        # Find the strides for the 
        self.batch_strides = self._find_batch_strides(self.examples_per_batch, self.total_example_count, self.examples_per_batch_index)

        return

    def run_self_checks(self):
        self._test_example_mapping(self.total_example_count, self.example_lut, self._object_list, self.unshuffled_object_list, self.get_example_from_object, self.cumulative_example_lut)
        self._test_batch_to_index_mapping(self.examples_per_batch, self.examples_per_batch_index, self.batch_strides, self.total_example_count)
        return

    # This test that given all expected indicies all outputs are unique
    def _test_example_mapping(self, total_example_count, object_example_lut, object_list, unshuffled_object_list,
            get_example_from_object, cumulative_example_lut):
        seen_examples = set()
        for idx in range(total_example_count):
            ex = get_example_from_object(idx, object_example_lut, object_list, cumulative_example_lut)
            
            assert(ex not in seen_examples)
            seen_examples.add(ex)

            if ex.is_valid != None:
                assert(ex.is_valid(unshuffled_object_list))

    def _test_batch_to_index_mapping(self, examples_per_batch, examples_per_batch_index, batch_strides, total_example_count):
        seen_indicies = set()
        for index in range(examples_per_batch_index):
            for batch_index in range(examples_per_batch):
                idx = self._batch_to_idx(index, batch_index, examples_per_batch, batch_strides, examples_per_batch_index, total_example_count)
                seen_indicies.add(idx)

        assert(len(seen_indicies) == total_example_count)
