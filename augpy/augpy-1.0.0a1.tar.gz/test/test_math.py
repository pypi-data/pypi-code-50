import random
from math import log

import numpy as np
import pytest

import augpy
from augpy.numeric_limits import CAST_LIMITS

from _common import I_TYPES
from _common import F_TYPES
from _common import TYPES
from _common import safe_cast
from _common import is_int
from _common import dtype_info


SIZE = (2, 178, 347)


def ind_rand_percentage(arr, pct):
    ind = np.linspace(0, 1, arr.size)
    np.random.shuffle(ind)
    return ind.reshape(arr.shape) <= pct


# noinspection PyUnresolvedReferences
def _random_tensor(dtype, size=SIZE, ttype=None, default_vmin=-128, default_vmax=127):
    if ttype is None:
        ttype = augpy.to_temp_dtype(dtype)
    info = dtype_info(dtype)
    mu = 0
    sigma = log(info.max - mu)
    # avoid majority of values == 0 for unsinged int case
    if info.min == 0:
        mu = 3
    # create a random scalar
    if size == ():
        rand = np.random.normal(mu, sigma, 1)[0]
    # create a random tensor
    else:
        rand = np.random.normal(mu, sigma, size)
        # for int types, set 1% of values to min/max
        if is_int(dtype):
            rand[ind_rand_percentage(rand, 0.01)] = info.min
            rand[ind_rand_percentage(rand, 0.01)] = info.max
        # ensure no overflow will occur when casting to dtype
        rand = rand.clip(info.min, info.max)
    rand = rand.astype(dtype)
    # ensure there are no zeros in tensor
    # zeroes are bad for testing:
    # - not distinguishable from uninitialized memory
    # - not effect for add/sub
    # - zero division
    if size is ():
        if rand == 0:
            rand = dtype(1)
    else:
        rand[rand == 0] = 1
    return augpy.array_to_tensor(rand), rand.astype(ttype)


def _random_scalar(dtype):
    ttype = augpy.to_temp_dtype(dtype)
    vmin, vmax = CAST_LIMITS[(ttype, dtype)]
    vmin = vmin or 0
    vmax = vmax or 255
    s = random.random() * (vmax-vmin) + vmin
    if s == 0:
        return 1
    return s


# noinspection PyUnresolvedReferences
def __random(fa, fn, close_allowed=False, rtol=1e-6, atol=1e-8,
             size1=SIZE, size2=None, size3=None):
    if size2 is None:
        size2 = size1
    for ctype, ntype in TYPES:
        c, a = _random_tensor(ntype, size1)
        d, b = _random_tensor(ntype, size2)
        if size3 is None:
            augpy_result = fa(c, d).numpy()
        else:
            result = augpy.CudaTensor(size3, dtype=ctype)
            fa(c, d, result)
            augpy_result = result.numpy()
        numpy_result = safe_cast(fn(a, b), ntype)
        augpy.default_stream.synchronize()
        if close_allowed:
            if is_int(ntype):
                atol = 1
            assert np.isclose(augpy_result, numpy_result, rtol=rtol, atol=atol).all(), ctype
        else:
            assert (augpy_result == numpy_result).all(), ctype


# noinspection PyUnresolvedReferences
def __random_scalar(fa, fn, close_allowed=False, rtol=1e-6, atol=1e-8, size=SIZE):
    for ctype, ntype in TYPES:
        a, n = _random_tensor(ntype, size)
        s = _random_scalar(ntype)
        augpy_result = fa(a, s).numpy()
        numpy_result = safe_cast(fn(n, s), ntype)
        augpy.default_stream.synchronize()
        if close_allowed:
            assert np.isclose(augpy_result, numpy_result, rtol=rtol, atol=atol).all(), ctype
        else:
            assert (augpy_result == numpy_result).all(), ctype


# noinspection PyUnresolvedReferences
def __random_unary(fa, fn, close_allowed=False, rtol=1e-6, atol=1e-8, size=SIZE, cast=True):
    for ctype, ntype in TYPES:
        a, n = _random_tensor(ntype, size)
        augpy_result = fa(a).numpy()
        numpy_result = fn(n)
        if cast:
            numpy_result = safe_cast(numpy_result, ntype)
        augpy.default_stream.synchronize()
        if close_allowed:
            assert np.isclose(augpy_result, numpy_result, rtol=rtol, atol=atol).all(), ctype
        else:
            assert (augpy_result == numpy_result).all(), ctype


# noinspection PyUnresolvedReferences
def __infix_random_scalar(fn, scalar, close_allowed=False):
    for ctype, ntype in TYPES:
        a, n = _random_tensor(ntype)
        a1 = fn(a, scalar).numpy()
        a2 = fn(scalar, a).numpy()
        n1 = safe_cast(fn(n, scalar), ntype)
        n2 = safe_cast(fn(scalar, n), ntype)
        augpy.default_stream.synchronize()
        if close_allowed:
            assert np.isclose(a1, n1, rtol=1e-6).all(), ctype
            assert np.isclose(a2, n2, rtol=1e-6).all(), ctype
        else:
            assert (a1 == n1).all(), ctype
            assert (a2 == n2).all(), ctype


# noinspection PyUnresolvedReferences
def __infix_random_tensor(fn, close_allowed=False, rtol=1e-6, atol=1e-8):
    for ctype, ntype in TYPES:
        a1, n1 = _random_tensor(ntype)
        a2, n2 = _random_tensor(ntype)
        ra1 = fn(a1, a2).numpy()
        ra2 = fn(a2, a1).numpy()
        rn1 = safe_cast(fn(n1, n2), ntype)
        rn2 = safe_cast(fn(n2, n1), ntype)
        augpy.default_stream.synchronize()
        if close_allowed:
            assert np.isclose(ra1, rn1, rtol=rtol, atol=atol).all(), ctype
            assert np.isclose(ra2, rn2, rtol=rtol, atol=atol).all(), ctype
        else:
            assert (ra1 == rn1).all(), ctype
            assert (ra2 == rn2).all(), ctype


# ---------------------------- INFIX TESTS ------------------------------------


def test_infix_add_scalar():
    __infix_random_scalar(lambda a, b: a + b, 10)


def test_infix_add_tensor():
    __infix_random_tensor(lambda a, b: a + b)


def test_infix_sub_scalar():
    __infix_random_scalar(lambda a, b: a - b, 10)


def test_infix_sub_tensor():
    __infix_random_tensor(lambda a, b: a - b)


def test_infix_mul_scalar():
    __infix_random_scalar(lambda a, b: a * b, 10)


def test_infix_mul_tensor():
    __infix_random_tensor(lambda a, b: a * b)


def test_infix_div_scalar():
    __infix_random_scalar(lambda a, b: a / b, 10, close_allowed=True)


def test_infix_div_tensor():
    __infix_random_tensor(lambda a, b: a / b, close_allowed=True, atol=1)


# -----------------------------------------------------------------------------


def test_fma():
    ctype = augpy.float32
    ntype = np.float32
    result = augpy.CudaTensor((10, 10), dtype=ctype)
    a = np.arange(100, dtype=ntype).reshape((10, 10)).astype(ntype)
    b = np.arange(100, dtype=ntype).reshape((10, 10)).astype(ntype)
    c = augpy.array_to_tensor(a)
    d = augpy.array_to_tensor(b)
    s = 2
    augpy.fma(s, c, d, result)
    result_array = augpy.tensor_to_array(result)
    augpy.default_stream.synchronize()
    assert ((s * a + b == result_array).all())


# -------------------- TEST GENERIC KERNEL IMPLEMENTATIONS --------------------


def test_add():
    __random(augpy.add, lambda a, b: a + b)


def test_sub():
    __random(augpy.sub, lambda a, b: a - b)


def test_mul():
    __random(augpy.mul, lambda a, b: a * b)


def test_div():
    __random(augpy.div, lambda a, b: a/b, close_allowed=True, atol=1)


def test_mul1d():
    for num in range(1, 100001, 3456):
        __random(augpy.mul, lambda a, b: a * b, size1=(num,))


# -----------------------------------------------------------------------------


def test_add_scalar():
    __random_scalar(augpy.add, lambda a, b: a + b)


def test_sub_scalar():
    __random_scalar(augpy.sub, lambda a, b: a - b)


def test_mul_scalar():
    __random_scalar(augpy.mul, lambda a, b: a * b)


def test_div_scalar():
    __random_scalar(augpy.div, lambda a, b: a / b, close_allowed=True)


# ----------------------------TEST-GEMM----------------------------------------


def test_mmul_float():
    a = augpy.array_to_tensor(np.asarray([[1, 2, 3], [4, 5, 6]], np.float32))
    b = augpy.array_to_tensor(np.asarray([[7, 8], [9, 10], [11, 12]], np.float32))
    c = augpy.array_to_tensor(np.zeros((2, 2), np.float32))
    augpy.gemm(a, b, c, 1.0, 0.0)
    augpy_result = c.numpy()
    augpy.default_stream.synchronize()
    assert (np.all(augpy_result == np.asarray([[58, 64], [139, 154]], np.float32)))


def test_mmul_float2():
    a = np.random.rand(100, 20).astype(np.float32)
    b = np.random.rand(20, 300).astype(np.float32)
    c = augpy.array_to_tensor(np.zeros((100, 300), np.float32))
    t_a = augpy.array_to_tensor(a)
    t_b = augpy.array_to_tensor(b)
    augpy.gemm(t_a, t_b, c, 1.0, 0.0)
    augpy_result = c.numpy()
    numpy_result = np.matmul(a, b)
    augpy.default_stream.synchronize()
    assert np.sum(np.absolute(augpy_result - numpy_result)) / (100 * 300) < 1e-6


# ----------------------------TEST-CAST----------------------------------------


def test_cast():
    for ctype, ntype in TYPES:
        for ctype_target, ntype_target in TYPES:
            a, n = _random_tensor(ntype, ttype=ntype)
            augpy_result = augpy.CudaTensor(SIZE, dtype=ctype_target)
            augpy.cast(a, augpy_result)
            augpy_result = augpy_result.numpy()
            numpy_result = safe_cast(n, ntype_target)
            augpy.default_stream.synchronize()
            assert (augpy_result == numpy_result).all(), (ctype, ctype_target)


# ----------------------------TEST-EXCEPTIONS----------------------------------


def test_mmul_wrong_shape1():
    a = augpy.array_to_tensor(np.random.rand(200, 20).astype(np.float32))
    b = augpy.array_to_tensor(np.random.rand(20, 300).astype(np.float32))
    c = augpy.array_to_tensor(np.zeros((100, 300), np.float32))
    with pytest.raises(ValueError) as excinfo:
        augpy.gemm(a, b, c, 1.0, 0.0)
    assert "shape of C must match A*C" in str(excinfo.value)


def test_mmul_wrong_shape2():
    a = augpy.array_to_tensor(np.random.rand(100, 21).astype(np.float32))
    b = augpy.array_to_tensor(np.random.rand(20, 300).astype(np.float32))
    c = augpy.array_to_tensor(np.zeros((100, 300), np.float32))
    with pytest.raises(ValueError) as excinfo:
        augpy.gemm(a, b, c, 1.0, 0.0)
    assert "A.shape[1] must match B.shape[0]" in str(excinfo.value)


def test_add_wrong_shape1():
    for ctype, ntype in TYPES:
        result = augpy.CudaTensor((10, 10), dtype=ctype)
        a = np.arange(90, dtype=ntype).reshape((9, 10)).astype(ntype)
        b = np.arange(100, dtype=ntype).reshape((10, 10)).astype(ntype)
        c = augpy.array_to_tensor(a)
        d = augpy.array_to_tensor(b)
        with pytest.raises(ValueError) as excinfo:
            augpy.add(c, d, result)
            augpy.tensor_to_array(result)
            augpy.default_stream.synchronize()
        assert "argument 1 (dim 0=9) must broadcastable to output (dim 0=10)" in str(excinfo.value)


def test_add_wrong_shape2():
    for ctype, ntype in TYPES:
        result = augpy.CudaTensor((10, 10), dtype=ctype)
        a = np.arange(100, dtype=ntype).reshape((10, 10)).astype(ntype)
        b = np.arange(90, dtype=ntype).reshape((9, 10)).astype(ntype)
        c = augpy.array_to_tensor(a)
        d = augpy.array_to_tensor(b)
        with pytest.raises(ValueError) as excinfo:
            augpy.add(c, d, result)
            augpy.tensor_to_array(result)
            augpy.default_stream.synchronize()
        assert "argument 2 (dim 0=9) must broadcastable to output (dim 0=10)" in str(excinfo.value)


def test_add_wrong_shape3():
    for ctype, ntype in TYPES:
        result = augpy.CudaTensor((9, 10), dtype=ctype)
        a = np.arange(100, dtype=ntype).reshape((10, 10)).astype(ntype)
        b = np.arange(100, dtype=ntype).reshape((10, 10)).astype(ntype)
        c = augpy.array_to_tensor(a)
        d = augpy.array_to_tensor(b)
        with pytest.raises(ValueError) as excinfo:
            augpy.add(c, d, result)
            augpy.tensor_to_array(result)
            augpy.default_stream.synchronize()
        assert "argument 1 (dim 0=10) must broadcastable to output (dim 0=9)" in str(excinfo.value)


def test_mul_wrong_shape1():
    for ctype, ntype in TYPES:
        result = augpy.CudaTensor((10, 10), dtype=ctype)
        a = np.arange(90, dtype=ntype).reshape((9, 10)).astype(ntype)
        b = np.arange(100, dtype=ntype).reshape((10, 10)).astype(ntype)
        c = augpy.array_to_tensor(a)
        d = augpy.array_to_tensor(b)
        with pytest.raises(ValueError) as excinfo:
            augpy.mul(c, d, result)
            augpy.tensor_to_array(result)
            augpy.default_stream.synchronize()
        assert "argument 1 (dim 0=9) must broadcastable to output (dim 0=10)" in str(excinfo.value)


def test_mul_wrong_shape2():
    for ctype, ntype in TYPES:
        result = augpy.CudaTensor((10, 10), dtype=ctype)
        a = np.arange(100, dtype=ntype).reshape((10, 10)).astype(ntype)
        b = np.arange(90, dtype=ntype).reshape((9, 10)).astype(ntype)
        c = augpy.array_to_tensor(a)
        d = augpy.array_to_tensor(b)
        with pytest.raises(ValueError) as excinfo:
            augpy.mul(c, d, result)
            augpy.tensor_to_array(result)
            augpy.default_stream.synchronize()
        assert "argument 2 (dim 0=9) must broadcastable to output (dim 0=10)" in str(excinfo.value)


def test_mul_wrong_shape3():
    for ctype, ntype in TYPES:
        result = augpy.CudaTensor((9, 10), dtype=ctype)
        a = np.arange(100, dtype=ntype).reshape((10, 10)).astype(ntype)
        b = np.arange(100, dtype=ntype).reshape((10, 10)).astype(ntype)
        c = augpy.array_to_tensor(a)
        d = augpy.array_to_tensor(b)
        with pytest.raises(ValueError) as excinfo:
            augpy.mul(c, d, result)
            augpy.tensor_to_array(result)
            augpy.default_stream.synchronize()
        assert "argument 1 (dim 0=10) must broadcastable to output (dim 0=9)" in str(excinfo.value)


def test_div_wrong_shape1():
    for ctype, ntype in TYPES:
        result = augpy.CudaTensor((10, 10), dtype=ctype)
        a = np.arange(90, dtype=ntype).reshape((9, 10)).astype(ntype)
        b = np.arange(100, dtype=ntype).reshape((10, 10)).astype(ntype)
        c = augpy.array_to_tensor(a)
        d = augpy.array_to_tensor(b)
        with pytest.raises(ValueError) as excinfo:
            augpy.div(c, d, result)
            augpy.tensor_to_array(result)
            augpy.default_stream.synchronize()
        assert "argument 1 (dim 0=9) must broadcastable to output (dim 0=10)" in str(excinfo.value)


def test_div_wrong_shape2():
    for ctype, ntype in TYPES:
        result = augpy.CudaTensor((10, 10), dtype=ctype)
        a = np.arange(100, dtype=ntype).reshape((10, 10)).astype(ntype)
        b = np.arange(90, dtype=ntype).reshape((9, 10)).astype(ntype)
        c = augpy.array_to_tensor(a)
        d = augpy.array_to_tensor(b)
        with pytest.raises(ValueError) as excinfo:
            augpy.div(c, d, result)
            augpy.tensor_to_array(result)
            augpy.default_stream.synchronize()
        assert "argument 2 (dim 0=9) must broadcastable to output (dim 0=10)" in str(excinfo.value)


def test_div_wrong_shape3():
    for ctype, ntype in TYPES:
        result = augpy.CudaTensor((9, 10), dtype=ctype)
        a = np.arange(100, dtype=ntype).reshape((10, 10)).astype(ntype)
        b = np.arange(100, dtype=ntype).reshape((10, 10)).astype(ntype)
        c = augpy.array_to_tensor(a)
        d = augpy.array_to_tensor(b)
        with pytest.raises(ValueError) as excinfo:
            augpy.div(c, d, result)
            augpy.tensor_to_array(result)
            augpy.default_stream.synchronize()
        assert "argument 1 (dim 0=10) must broadcastable to output (dim 0=9)" in str(excinfo.value)


def test_div_by_0_inf():
    for ctype, ntype in F_TYPES:
        result = augpy.CudaTensor((1000,), dtype=ctype)
        a = augpy.array_to_tensor(np.arange(1000, dtype=ntype) + 1)
        b = augpy.array_to_tensor(np.asarray([0], dtype=ntype))
        augpy.div(a, b, result)
        result_array = augpy.tensor_to_array(result)
        augpy.default_stream.synchronize()
        print(result_array)
        assert np.isinf(result_array).all()


def test_div_by_0_nan():
    for ctype, ntype in F_TYPES:
        result = augpy.CudaTensor((1000,), dtype=ctype)
        a = augpy.array_to_tensor(np.zeros(1000, dtype=ntype))
        b = augpy.array_to_tensor(np.asarray([0], dtype=ntype))
        augpy.div(a, b, result)
        result_array = augpy.tensor_to_array(result)
        augpy.default_stream.synchronize()
        print(result_array)
        assert np.isnan(result_array).all()


def test_sadd_wrong_shape1():
    for ctype, ntype in TYPES:
        a = np.arange(100, dtype=ntype).reshape((10, 10))
        d = augpy.CudaTensor((9, 10), dtype=ctype)
        c = augpy.array_to_tensor(a)
        rand = random.random() * 100
        with pytest.raises(ValueError) as excinfo:
            augpy.add(c, rand, d)
            augpy.tensor_to_array(d)
            augpy.default_stream.synchronize()
        assert "argument 1 (dim 0=10) must broadcastable to output (dim 0=9)" in str(excinfo.value)


def test_sadd_wrong_shape2():
    for ctype, ntype in F_TYPES:
        a = np.arange(90, dtype=ntype).reshape((9, 10))
        d = augpy.CudaTensor((10, 10), dtype=ctype)

        c = augpy.array_to_tensor(a)
        rand = random.random() * 100

        with pytest.raises(ValueError) as excinfo:
            augpy.add(c, rand, d)
            augpy.tensor_to_array(d)
            augpy.default_stream.synchronize()
        assert "argument 1 (dim 0=9) must broadcastable to output (dim 0=10)" in str(excinfo.value)


# --------------------------- TEST SCALAR ARRAYS ------------------------------


def test_add_scalar1():
    __random(augpy.add, lambda a, b: a + b, size1=SIZE, size2=(1,))


if __name__ == '__main__':
    test_add_scalar1()


def test_add_scalar2():
    __random(augpy.add, lambda a, b: a + b, size1=(1,), size2=SIZE)


def test_add_scalar_scalar():
    __random(augpy.add, lambda a, b: a + b, size1=(1,), size2=(1,))


def test_add_scalar_as_target():
    __random(augpy.add, lambda a, b: a + b, size1=(), size2=(), size3=())


def test_sub_scalar1():
    __random(augpy.sub, lambda a, b: a - b, size1=SIZE, size2=(1,))


def test_sub_scalar2():
    __random(augpy.sub, lambda a, b: a - b, size1=(1,), size2=SIZE)


def test_sub_scalar_scalar():
    __random(augpy.sub, lambda a, b: a - b, size1=(1,), size2=(1,))


def test_sub_scalar_as_target():
    __random(augpy.sub, lambda a, b: a - b, size1=(), size2=(), size3=())


def test_mul_scalar1():
    __random(augpy.mul, lambda a, b: a * b, size1=SIZE, size2=(1,))


def test_mul_scalar2():
    __random(augpy.mul, lambda a, b: a * b, size1=(1,), size2=SIZE)


def test_mul_scalar_scalar():
    __random(augpy.mul, lambda a, b: a * b, size1=(1,), size2=(1,))


def test_mul_scalar_as_target():
    __random(augpy.mul, lambda a, b: a * b, size1=(), size2=(), size3=())


def test_div_scalar1():
    __random(augpy.div, lambda a, b: a / b, size1=SIZE, size2=(1,), close_allowed=True)


def test_div_scalar2():
    __random(augpy.div, lambda a, b: a / b, size1=(1,), size2=SIZE, close_allowed=True)


def test_div_scalar_scalar():
    __random(augpy.div, lambda a, b: a / b, size1=(1,), size2=(1,), close_allowed=True)


def test_div_scalar_as_target():
    __random(augpy.div, lambda a, b: a / b, size1=(), size2=(), size3=(), close_allowed=True)


def test_sum():
    __random_unary(lambda a: a.sum(upcast=False), lambda a: a.sum(dtype=a.dtype),
                   size=SIZE, close_allowed=True, cast=True)


def test_sum_upcast():
    __random_unary(lambda a: a.sum(upcast=True), lambda a: a.sum(dtype=a.dtype),
                   size=SIZE, close_allowed=True, cast=False)


def test_sum_axis():
    __random_unary(lambda a: a.sum(1, upcast=False), lambda a: a.sum(axis=1, dtype=a.dtype),
                   size=SIZE, close_allowed=True, cast=True)


def test_sum_axis_upcast():
    __random_unary(lambda a: a.sum(1, upcast=True), lambda a: a.sum(axis=1, dtype=a.dtype),
                   size=SIZE, close_allowed=True, cast=False)
