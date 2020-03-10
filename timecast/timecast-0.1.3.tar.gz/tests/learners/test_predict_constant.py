import numpy as np
import pytest

from timecast.learners._predict_constant import PredictConstant


@pytest.mark.parametrize(
    "c,x,y",
    [
        (0, np.array([0]), np.zeros(1)),
        (0, np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), np.zeros(10)),
        (0, np.random.rand(2, 2), np.zeros((2, 2))),
        (0, np.random.rand(2, 2), np.zeros((2, 2))),
        (1, np.array([0]), np.ones(1)),
        (1, np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), np.ones(10)),
        (1, np.random.rand(2, 2), np.ones((2, 2))),
        (1, np.random.rand(2, 2), np.ones((2, 2))),
    ],
)
def test_predict_constant(c, x, y):
    predict_zero = PredictConstant(constant=c, shape=x.shape)

    assert np.array_equal(predict_zero.predict(x), y)


def test_predict_constant_update():
    pc = PredictConstant()

    assert pc == pc.update(np.array([[1]]), np.array([[1]]))


@pytest.mark.parametrize("x_dim", [1, 10])
@pytest.mark.parametrize("y_dim", [10])
def test_predict_last_update_exception(x_dim, y_dim):
    pc = PredictConstant()
    X = np.random.rand(1, x_dim)
    y = np.random.rand(1, y_dim)
    with pytest.raises(ValueError):
        pc.update(X, y)


def test_predict_last_predict_exception():
    pc = PredictConstant()
    with pytest.raises(ValueError):
        pc.predict(np.random.rand(1, 2))


@pytest.mark.parametrize("params", [True, False])
@pytest.mark.parametrize("state", [True, False])
@pytest.mark.parametrize("func", ["reset", "freeze", "unfreeze"])
def test_predict_constant_funcs(params, state, func):
    pc = PredictConstant()

    assert pc == getattr(pc, func)(params=params, state=state)
