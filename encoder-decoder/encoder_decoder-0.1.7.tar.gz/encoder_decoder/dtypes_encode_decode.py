import numpy as np

def float_ndarray_to_dict(arr):
    return np_arr_to_dict(arr)

def dict_to_float_ndarray(string):
    return dict_to_np_arr(string)

def identity(e):
    return e

def float_to_string(num):
    return str(num)

def string_to_float(string):
    return float(string)

def np_arr_to_dict(arr):
    return {'arr': arr.tolist(),
        'shape':list(arr.shape),
        'dtype':str(arr.dtype)
    }

def dict_to_np_arr(data):
    arr, shape, dtype = data['arr'], data['shape'], data['dtype']
    return np.array(arr, dtype=dtype).reshape(tuple(shape))