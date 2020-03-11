import numpy as np
import pytest

import augpy


N, C, H, W = (16, 3, 56, 57)
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


# -----------------------------------------------------------------------------


def test_index_operator_slice():
    a = np.arange(100).reshape((10, 10))
    b = augpy.array_to_tensor(a)
    numpy_slice = a[0]
    result = b[0].numpy()
    augpy.default_stream.synchronize()
    print(result)
    assert (numpy_slice == result).all()


def test_index_operator_slice_middle():
    a = np.arange(100).reshape((10, 10))
    b = augpy.array_to_tensor(a)
    numpy_slice = a[4:6]
    result = b[4:6].numpy()
    augpy.default_stream.synchronize()
    print(result)
    print(numpy_slice)
    assert (numpy_slice == result).all()


def test_index_scalar_exception():
    scalar = 1337.0
    numpy_scalar = np.asarray(scalar)
    augpy_scalar = augpy.array_to_tensor(numpy_scalar)
    with pytest.raises(IndexError) as excinfo:
        augpy_scalar[0]
    # assert "ADFASDFASDF" in str(excinfo.value)


def test_types():
    assert augpy.float16.bits == 16
    assert augpy.float32.bits == 32
    assert augpy.float64.bits == 64
    assert augpy.int8.bits == 8
    assert augpy.uint8.bits == 8
    assert augpy.int16.bits == 16
    assert augpy.uint16.bits == 16
    assert augpy.int32.bits == 32
    assert augpy.uint32.bits == 32


def test_numpy_function_noncontiguous():
    a = np.arange(100).reshape((10, 10))
    b = augpy.array_to_tensor(a)
    numpy_result = a[::2]
    augpy_result = b[::2].numpy()
    augpy.default_stream.synchronize()
    assert (numpy_result == augpy_result).all()


# --------------- TEST FOR ABSENCE OF CRASHES OF AUGMENTATIONS ----------------


def test_gamma():
    a = np.random.rand(N, C, H, W)
    b = augpy.array_to_tensor(a)
    gamma_grays = augpy.array_to_tensor(np.random.rand(N)) + 0.25
    gamma_colors = augpy.array_to_tensor(np.random.rand(N, C)) + 0.25
    contrasts = augpy.array_to_tensor(np.random.rand(N, C)) + 0.2
    result = augpy.add_gamma(b, gamma_grays, gamma_colors, contrasts, float(1.0))
    result = result.numpy()
    augpy.default_stream.synchronize()
    assert not (a == result).all()
