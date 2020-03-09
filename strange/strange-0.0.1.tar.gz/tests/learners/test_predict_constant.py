import numpy as np
import pytest

from strange.learners._predict_constant import PredictConstant


@pytest.mark.parametrize(
    "c,x,y",
    [
        (0, 0, 0),
        (0, np.array([0]), np.zeros(1)),
        (0, np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), np.zeros(10)),
        (0, np.random.rand(2, 2), np.zeros((2, 2))),
        (0, np.random.rand(2, 2), np.zeros((2, 2))),
        (1, 0, 1),
        (1, np.array([0]), np.ones(1)),
        (1, np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), np.ones(10)),
        (1, np.random.rand(2, 2), np.ones((2, 2))),
        (1, np.random.rand(2, 2), np.ones((2, 2))),
    ],
)
def test_predict_constant(c, x, y):
    predict_zero = PredictConstant(constant=c)

    assert np.array_equal(predict_zero.predict(x), y)
