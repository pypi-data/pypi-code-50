import numpy as np


def rotate_indexes(array, axis, m):

    # This function rotates the indexes of "array" on the "axis" by "m" indexes.
    # It returns None.

    shape_array = np.asarray(array.shape, dtype=int)
    n_axes = shape_array.size
    n_indexes = shape_array[axis]

    m %= n_indexes

    index_in = np.empty(n_axes, dtype=object)
    index_in[:] = slice(None)
    index_out = np.copy(index_in)

    index_in[axis] = slice(n_indexes - m, n_indexes, 1)
    array_out_0_to_m = np.copy(array[tuple(index_in)])

    index_in[axis] = slice(0, n_indexes - m, 1)
    index_out[axis] = slice(m, n_indexes, 1)
    array[tuple(index_out)] = array[tuple(index_in)]

    index_out[axis] = slice(0, m, 1)
    array[tuple(index_out)] = array_out_0_to_m

    return None
