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
    return {'str': np.ndarray.tostring(arr).decode('utf-8'),
        'shape':list(arr.shape),
        'dtype':str(arr.dtype)
    }

def dict_to_np_arr(data):
    arr, shape, dtype = data['str'].encode('utf-8'), data['shape'], data['dtype']
    return np.fromstring(arr, dtype=dtype).reshape(tuple(shape))