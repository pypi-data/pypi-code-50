from . import _augpy
from ._augpy import *
import numpy as __np


__version__ = '1.0.0a1'


__all__ = [f for f in dir(_augpy) if not f.startswith('__')]


SCALE_MODE = {
    WARP_SCALE_LONGEST: WARP_SCALE_LONGEST,
    WARP_SCALE_SHORTEST: WARP_SCALE_SHORTEST,
    'shortest': WARP_SCALE_SHORTEST,
    'longest': WARP_SCALE_LONGEST,
}


AUGPY_TO_NUMPY_DTYPES = {
    uint8: __np.uint8,
    uint16: __np.uint16,
    uint32: __np.uint32,
    uint64: __np.uint64,
    int8: __np.int8,
    int16: __np.int16,
    int32: __np.int32,
    int64: __np.int64,
    float32: __np.float32,
    float64: __np.float64,
}


def to_numpy_dtype(augpy_dtype):
    return AUGPY_TO_NUMPY_DTYPES[augpy_dtype]


NUMPY_TO_AUGPY_DTYPES = {
    __np.uint8: uint8,
    __np.uint16: uint16,
    __np.uint32: uint32,
    __np.uint64: uint64,
    __np.int8: int8,
    __np.int16: int16,
    __np.int32: int32,
    __np.int64: int64,
    __np.float32: float32,
    __np.float64: float64,
}


def to_augpy_dtype(numpy_dtype):
    if isinstance(numpy_dtype, __np.dtype):
        numpy_dtype = numpy_dtype.type
    return NUMPY_TO_AUGPY_DTYPES[numpy_dtype]


DTYPE_MAP = {}
DTYPE_MAP.update(AUGPY_TO_NUMPY_DTYPES)
DTYPE_MAP.update(NUMPY_TO_AUGPY_DTYPES)


def swap_dtype(dtype):
    if isinstance(dtype, __np.dtype):
        dtype = dtype.type
    return DTYPE_MAP[dtype]


TEMP_DTYPES = {
    # augpy types
    uint8: float32,
    uint16: float32,
    uint32: float64,
    uint64: float64,
    int8: float32,
    int16: float32,
    int32: float64,
    int64: float64,
    float32: float32,
    float64: float64,
    # numpy types
    __np.uint8: __np.float32,
    __np.uint16: __np.float32,
    __np.uint32: __np.float64,
    __np.uint64: __np.float64,
    __np.int8: __np.float32,
    __np.int16: __np.float32,
    __np.int32: __np.float64,
    __np.int64: __np.float64,
    __np.float32: __np.float32,
    __np.float64: __np.float64,
}


def to_temp_dtype(dtype):
    if isinstance(dtype, __np.dtype):
        dtype = dtype.type
    return TEMP_DTYPES[dtype]


def make_transform(
        source_size,
        target_size,
        angle=0,
        scale=1,
        aspect=1,
        shift=None,
        shear=None,
        hmirror=False,
        vmirror=False,
        scale_mode=WARP_SCALE_SHORTEST,
        max_supersampling=3,
        out=None,
        __template__=__np.empty((2, 3), dtype=__np.float32),
        **__
):
    out = out if out is not None else __template__.copy()
    shift = shift or (0, 0)
    shear = shear or (0, 0)
    supersampling = make_affine_matrix(
        out,
        source_size[0], source_size[1],
        target_size[0], target_size[1],
        angle,
        scale,
        aspect,
        shift[0], shift[1],
        shear[0], shear[1],
        hmirror,
        vmirror,
        SCALE_MODE[scale_mode],
        max_supersampling
    )
    return out, supersampling
