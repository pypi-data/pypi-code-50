import os
import sys
sys.path.append(os.pardir)
from math import sqrt

import numpy as np

import augpy


N, C, H, W = (16, 3, 128, 128)
I_TYPES = [
    (augpy.uint8, np.uint8),
    (augpy.int8, np.int8),
    (augpy.int16, np.int16),
    (augpy.uint16, np.uint16),
    (augpy.int32, np.int32),
    (augpy.uint32, np.uint32),
    (augpy.int64, np.int64),
    (augpy.uint64, np.uint64),
]
F_TYPES = [
    (augpy.float32, np.float32),
    (augpy.float64, np.float64),
]
TYPES = I_TYPES + F_TYPES
gen = augpy.RandomNumberGenerator(seed=1337)


def test_uniform():
    for ctype, ntype in TYPES:
        noise = augpy.CudaTensor((1000000,), dtype=ctype)
        minv = 5
        maxv = 123
        gen.uniform(noise, minv, maxv)
        array = noise.numpy()
        augpy.default_stream.synchronize()
        true_mean = (maxv+minv)/2
        # TODO check why high error tolerance is necessary
        assert abs(array.mean() - true_mean) < 0.3, (ctype, 'incorrect mean')
        assert array.min() >= minv, (ctype, 'incorrect min value')
        assert array.max() <= maxv, (ctype, 'incorrect max value')


def test_gaussian():
    for ctype, ntype in TYPES:
        noise = augpy.CudaTensor((10000000,), dtype=ctype)
        gen.gaussian(noise, 64, 7)
        array = noise.numpy()
        augpy.default_stream.synchronize()
        # TODO check why high error tolerance is necessary
        assert abs(array.mean() - 64) < 0.05, (ctype, 'incorrect mean')
        assert abs(array.std() - 7) < 0.05, (ctype, 'incorrect standard deviation')
