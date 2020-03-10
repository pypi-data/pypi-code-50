import numpy as np
import pytest

from timecast.learners._predict_last import PredictLast


@pytest.mark.parametrize("n", [1, 10, 100])
@pytest.mark.parametrize("r", [1, 10, 100])
@pytest.mark.parametrize("c", [1, 10, 100])
def test_predict_last(n, r, c):
    X = np.random.rand(n, r, c)

    pl = PredictLast(shape=(r, c))
    prev = pl._pad_value
    for x in X[:-1, :, :]:
        assert np.array_equal(prev, pl.predict(x))
        pl.update(x, x)
        prev = x


@pytest.mark.parametrize("x_dim", [1, 10])
@pytest.mark.parametrize("y_dim", [10])
def test_predict_last_update_exception(x_dim, y_dim):
    pl = PredictLast()
    X = np.random.rand(1, x_dim)
    y = np.random.rand(1, y_dim)
    with pytest.raises(ValueError):
        pl.update(X, y)


def test_predict_last_predict_exception():
    pl = PredictLast()
    with pytest.raises(ValueError):
        pl.predict(np.random.rand(1, 2))


@pytest.mark.parametrize("params", [True, False])
@pytest.mark.parametrize("state", [True, False])
@pytest.mark.parametrize("func", ["reset", "freeze", "unfreeze"])
def test_predict_last_funcs(params, state, func):
    pl = PredictLast()

    if func == "reset":
        getattr(pl, func)(params=params, state=state)
        assert pl._buffer == [] and pl._index == -1 and pl._prev_value == pl._pad_value
    else:
        assert pl == getattr(pl, func)(params=params, state=state)
