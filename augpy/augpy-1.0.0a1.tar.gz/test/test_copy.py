import numpy as np

import augpy

from _common import TYPES
from _common import safe_cast


n, c, h, w = (69, 4, 186, 47)


# -----------------------------------------------------------------------------
# THE FOLLOWING 3 TESTS TEST ONLY FOR THE ABSENCE OF CRASHES


def test_1():
    for ctype, ntype in TYPES:
        b = augpy.CudaTensor((n, c, h, w), dtype=ctype)
        augpy.copy(b, b)
        augpy.copy(b[128:], b[128:])
        augpy.copy(b[::2], b[::2])


def test_contiguous():
    for ctype, ntype in TYPES:
        a = augpy.CudaTensor((2 * n, 2 * c, 2 * h, 2 * w), dtype=ctype)
        b = augpy.CudaTensor((n, c, h, w), dtype=ctype)
        number = 10
        for _ in range(number):
            augpy.copy(a[::2, ::2, ::2, ::2], b)


def test_broadcast():
    for ctype, ntype in TYPES:
        b = augpy.CudaTensor((n, c, h, w), dtype=ctype)
        scalar = b[0, 0, 0, 0]
        number = 10
        for _ in range(number):
            augpy.copy(scalar, b)


# -----------------------------------------------------------------------------


def test_2dim_strided_1st():
    for ctype, ntype in TYPES:
        c = np.arange(100, dtype=ntype).reshape((10, 10))
        d = augpy.CudaTensor((5, 10), dtype=ctype)
        c = augpy.array_to_tensor(c)
        c = c[::2]
        augpy.copy(c, d, 1, 128)
        for i in range(5):
            for j in range(10):
                assert augpy.tensor_to_array(d[i, j]) == 20 * i + j
