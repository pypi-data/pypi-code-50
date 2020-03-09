import jax.numpy as np
import pytest

from strange.learners._predict_last import PredictLast


@pytest.mark.parametrize(
    "x,y",
    [
        (0, 0),
        (4.3, 4.3),
        (np.array([0]), np.zeros(1)),
        (np.array([0, 1, 2, 3, 4]), np.asarray([0, 1, 2, 3, 4])),
    ],
)
def test_predict_last(x, y):
    predict_last = PredictLast()

    assert np.array_equal(predict_last.predict(x), y)
