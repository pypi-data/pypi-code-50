import numpy as np

import augpy
from augpy.numeric_limits import CAST_LIMITS


# noinspection PyUnresolvedReferences
I_TYPES = [
    (augpy.uint8, np.uint8),
    (augpy.int8, np.int8),
    (augpy.uint16, np.uint16),
    (augpy.int16, np.int16),
    (augpy.uint32, np.uint32),
    (augpy.int32, np.int32),
    (augpy.uint64, np.uint64),
    (augpy.int64, np.int64),
]
# noinspection PyUnresolvedReferences
F_TYPES = [
    (augpy.float32, np.float32),
    (augpy.float64, np.float64),
]
TYPES = I_TYPES + F_TYPES


def dtype_info(dtype):
    try:
        return np.iinfo(dtype)
    except ValueError:
        try:
            return np.finfo(dtype)
        except ValueError:
            raise ValueError('%r is neither int nor float type' % dtype)


def is_int(dtype):
    try:
        np.iinfo(dtype)
        return True
    except ValueError:
        return False


def is_float(dtype):
    try:
        np.finfo(dtype)
        return True
    except ValueError:
        return False


def safe_cast(a, dtype):
    if isinstance(dtype, np.dtype):
        dtype = dtype.type
    vmin, vmax = CAST_LIMITS.get((a.dtype.type, dtype), (None, None))
    if is_float(a.dtype) and not is_float(dtype):
        a = np.round(a)
    a = a.astype(np.float128)
    vmin = None if vmin is None else np.float128(vmin)
    vmax = None if vmax is None else np.float128(vmax)
    if vmin is not None or vmax is not None:
        a = np.clip(a, vmin, vmax)
    return np.asanyarray(a).astype(dtype)
