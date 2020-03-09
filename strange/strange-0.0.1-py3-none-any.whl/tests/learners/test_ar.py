# pylint: disable=unsubscriptable-object
import jax.numpy as np
import numpy as onp
import pytest

from strange.learners._ar import _ar_fit_constrained
from strange.learners._ar import _ar_fit_normalize_prod
from strange.learners._ar import _ar_fit_unconstrained
from strange.learners._ar import _ar_form_linear_constraints
from strange.learners._ar import _ar_predict
from strange.learners._ar import _ar_update_history
from strange.learners._ar import AR
from strange.utils.statistics import OnlineStatistics


def ols(X, y, input_dim, alpha=1, fit_intercept=True, normalize=False, constrain=False):
    if fit_intercept:
        X = onp.concatenate((np.ones((X.shape[0], input_dim if constrain else 1)), X), axis=1)

        if normalize:
            X = onp.nan_to_num((X - X.mean(axis=0)) / X.std(axis=0))
            y = (y - y.mean(axis=0)) / y.std(axis=0)
    return onp.linalg.inv(X.T @ X + alpha * np.eye(X.shape[1])) @ (X.T @ y)


@pytest.mark.parametrize(
    "history,data,expected",
    [
        (
            np.array([[1, 2, 3], [3, 2, 4], [3, 6, 2]]),
            [2, 4, 5],
            np.array([[2, 4, 5], [1, 2, 3], [3, 2, 4]]),
        ),
        (
            [
                [1, 2, 3, 4],
                [4, 2, 5, 2],
                [5, 3, 2, 1],
                [5, 2, 3, 1],
                [4, 2, 1, 2],
                [1, 2, 3, 4],
                [1, 2, 5, 4],
            ],
            [4, 5, 2, 1],
            [
                [4, 5, 2, 1],
                [1, 2, 3, 4],
                [4, 2, 5, 2],
                [5, 3, 2, 1],
                [5, 2, 3, 1],
                [4, 2, 1, 2],
                [1, 2, 3, 4],
            ],
        ),
    ],
)
def test_update_history(history, data, expected):
    updated = _ar_update_history(history, data)
    assert np.array_equal(expected, updated)


def test_update_history_exception():
    with pytest.raises(ValueError):
        _ar_update_history(onp.random.rand(10, 4), [1])


def generator(X, y, chunk_size=100):
    chunks = X.shape[0] // chunk_size
    next_index = 0
    for i in range(chunks):
        curr_index = i * chunk_size
        next_index = (i + 1) * chunk_size
        if len(y) == len(y.ravel()):
            yield X[curr_index:next_index, :], y[curr_index:next_index]
        else:
            yield X[curr_index:next_index, :], y[curr_index:next_index, :]
    if next_index < X.shape[0]:
        if len(y) == len(y.ravel()):
            yield X[next_index:, :], y[next_index:]
        else:
            yield X[next_index:, :], y[next_index:, :]


@pytest.mark.parametrize("n", [10, 1000])
@pytest.mark.parametrize("input_dim", [1, 10])
@pytest.mark.parametrize("output_dim", [1, 10])
@pytest.mark.parametrize("window_size", [1, 10])
@pytest.mark.parametrize("fit_intercept", [True, False])
@pytest.mark.parametrize("normalize", [True, False])
def test_fit_accumulate(n, input_dim, output_dim, window_size, fit_intercept, normalize):
    # NOTE: we use random data because we want to test dimensions and
    # correctness vs a second implementation
    X = onp.random.rand(n, input_dim * window_size)
    y = onp.random.rand(n, output_dim)

    ar = AR(input_dim, output_dim, window_size, fit_intercept=fit_intercept, normalize=normalize,)
    inv, Xy = ar._fit_accumulate(generator(X, y), alpha=1)

    if fit_intercept:
        X = onp.concatenate((onp.ones((X.shape[0], 1)), X), axis=1)

        if normalize:
            X = onp.nan_to_num((X - X.mean(axis=0)) / X.std(axis=0))
            y = (y - y.mean(axis=0)) / y.std(axis=0)

    result = onp.linalg.inv(X.T @ X + np.eye(inv.shape[1]))
    onp.testing.assert_array_almost_equal(result, inv, decimal=2)
    onp.testing.assert_array_almost_equal(X.T @ y, Xy, decimal=2)


@pytest.mark.parametrize("n", [10, 1000])
@pytest.mark.parametrize("input_dim", [1, 10])
@pytest.mark.parametrize("output_dim", [1, 10])
@pytest.mark.parametrize("window_size", [1, 10])
@pytest.mark.parametrize("fit_intercept", [True, False])
@pytest.mark.parametrize("normalize", [True, False])
def test_fit_unconstrained(n, input_dim, output_dim, window_size, fit_intercept, normalize):
    # NOTE: we use random data because we want to test dimensions and
    # correctness vs a second implementation
    X = onp.random.rand(n, input_dim * window_size)
    y = onp.random.rand(n, output_dim)

    ar = AR(input_dim, output_dim, window_size, fit_intercept=fit_intercept, normalize=normalize,)
    inv, Xy = ar._fit_accumulate(generator(X, y), alpha=1)
    beta = _ar_fit_unconstrained(inv, Xy)

    onp.testing.assert_array_almost_equal(
        beta,
        ols(X, y, input_dim, alpha=1, fit_intercept=fit_intercept, normalize=normalize,),
        decimal=3,
    )


@pytest.mark.parametrize("n", [10, 1000])
@pytest.mark.parametrize("input_dim", [1, 10])
@pytest.mark.parametrize("output_dim", [1, 10])
@pytest.mark.parametrize("window_size", [1, 10])
@pytest.mark.parametrize("fit_intercept", [True, False])
def test_fit_constrained(n, input_dim, output_dim, window_size, fit_intercept):
    # NOTE: we use random data because we want to test dimensions and
    # correctness vs a second implementation
    print(n, input_dim, output_dim, window_size, fit_intercept)
    X = onp.random.rand(n, input_dim * window_size)
    y = onp.random.rand(n, output_dim)

    ar = AR(input_dim, output_dim, window_size, fit_intercept=fit_intercept, constrain=True)
    inv, Xy = ar._fit_accumulate(generator(X, y), alpha=1)
    beta = _ar_fit_unconstrained(inv, Xy)

    # First double check that unconstrained also works
    onp.testing.assert_array_almost_equal(
        beta, ols(X, y, input_dim, alpha=1, fit_intercept=fit_intercept, constrain=True), decimal=3,
    )

    # Next, check that each chunk of input_dim features have the same coefficient
    R, r = _ar_form_linear_constraints(
        input_dim, output_dim, window_size, fit_intercept=fit_intercept
    )
    result = _ar_fit_constrained(beta, inv, R, r)

    num_params = window_size + (1 if fit_intercept else 0)
    assert np.sum([np.abs(x - x[0]) for x in result.reshape(num_params, input_dim, -1)]) < 1e-4

    # Finally, check that resulting vector is of the correct length and the
    # values are self-consistent
    ar = AR(input_dim, output_dim, window_size, fit_intercept=fit_intercept, constrain=True)
    ar.fit(generator(X, y))
    assert len(ar._params["phi"]) == num_params
    onp.testing.assert_array_almost_equal(
        ar._params["phi"], np.mean(result.reshape(num_params, input_dim, -1), axis=1), decimal=3,
    )


@pytest.mark.parametrize(
    "window_size,input_dim,output_dim,fit_intercept,expected_R,expected_r",
    [
        (
            3,
            2,
            1,
            False,
            np.array(
                [
                    [1.0, -1.0, 0.0, 0.0, 0.0, 0.0],
                    [0.0, 0.0, 1.0, -1.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0, 0.0, 1.0, -1.0],
                ]
            ),
            np.zeros(3),
        ),
        (
            3,
            2,
            1,
            True,
            np.array(
                [
                    [1.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                    [0.0, 0.0, 1.0, -1.0, 0.0, 0.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0, 0.0, 1.0, -1.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, -1.0],
                ]
            ),
            np.zeros(4),
        ),
        (4, 1, 1, True, np.zeros((0, 5)), np.zeros((0))),
        (
            3,
            2,
            2,
            True,
            np.array(
                [
                    [1.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                    [0.0, 0.0, 1.0, -1.0, 0.0, 0.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0, 0.0, 1.0, -1.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, -1.0],
                ]
            ),
            np.zeros((4, 2)),
        ),
    ],
)
def test_form_linear_constraints(
    window_size, input_dim, output_dim, fit_intercept, expected_R, expected_r
):
    R, r = _ar_form_linear_constraints(input_dim, output_dim, window_size, fit_intercept)

    r = r.squeeze()

    assert np.array_equal(expected_R, R)
    assert np.array_equal(expected_r, r)


@pytest.mark.parametrize("num_observations,num_features", [(2, 1), (2, 10), (10, 1), (10, 10)])
def test_fit_normalize_xtx(num_observations, num_features):
    # TODO: Investigate numerical stability
    # NOTE: Number of observations must be greater than 1
    M = onp.random.randint(0, 500, (num_observations, num_features))
    mu = M.mean(axis=0)
    sigma = M.std(axis=0)

    M_stats = OnlineStatistics(M.shape[1])
    for m in M:
        M_stats.update(m)

    A = (M - mu) / sigma
    onp.testing.assert_array_almost_equal(
        np.nan_to_num(A.T @ A), _ar_fit_normalize_prod(M.T @ M, M_stats, M_stats), decimal=2,
    )


@pytest.mark.parametrize(
    "n,A_features,B_features", [(2, 1, 10), (2, 10, 1), (10, 1, 10), (10, 10, 1), (10, 100, 100)],
)
def test_fit_normalize_ab(n, A_features, B_features):
    # TODO: Investigate numerical stability
    # NOTE: Number of observations must be greater than 1
    A = onp.random.randint(0, 500, (n, A_features))
    A_mu = A.mean(axis=0)
    A_sigma = A.std(axis=0)

    A_stats = OnlineStatistics(A.shape[1])
    for a in A:
        A_stats.update(a)

    A_norm = (A - A_mu) / A_sigma

    B = onp.random.rand(n, B_features)
    B_mu = B.mean(axis=0)
    B_sigma = B.std(axis=0)

    B_stats = OnlineStatistics(B.shape[1])
    for b in B:
        B_stats.update(b)

    B_norm = (B - B_mu) / B_sigma

    onp.testing.assert_array_almost_equal(
        np.nan_to_num(A_norm.T @ B_norm),
        _ar_fit_normalize_prod(A.T @ B, A_stats, B_stats),
        decimal=2,
    )


def test_fit_normalize_exception():
    A = OnlineStatistics(1)
    B = OnlineStatistics(1)

    X = onp.random.rand(4, 1)
    for x in X:
        B.update(x)

    with pytest.raises(ValueError):
        _ar_fit_normalize_prod(X.T @ X, A, B)


def test_fit_accumulate_incompatible_feature_num():
    def gen():
        yield onp.random.rand(10, 2), 4

    ar = AR()
    with pytest.raises(ValueError):
        ar._fit_accumulate(gen())


def test_fit_accumulate_bad_y_shape():
    def gen():
        yield onp.random.rand(10, 3), onp.random.rand(10, 2)

    ar = AR()
    with pytest.raises(ValueError):
        ar._fit_accumulate(gen())


def test_fit_accumulate_incompatible_n():
    def gen():
        yield onp.random.rand(10, 3), onp.random.rand(4, 1)

    ar = AR()
    with pytest.raises(ValueError):
        ar._fit_accumulate(gen())


def test_update_history_incompatible_dim():
    with pytest.raises(ValueError):
        _ar_update_history(onp.random.rand(10, 100), onp.random.rand(10))


@pytest.mark.parametrize("n", [10, 1000])
@pytest.mark.parametrize("input_dim", [1, 10])
@pytest.mark.parametrize("output_dim", [1, 10])
@pytest.mark.parametrize("window_size", [1, 10])
@pytest.mark.parametrize("fit_intercept", [True, False])
@pytest.mark.parametrize("constrain", [True, False])
def test_fit_accumulate_shape(n, input_dim, output_dim, window_size, fit_intercept, constrain):
    X = onp.random.rand(n, input_dim * window_size)
    y = onp.random.rand(n, output_dim)
    ar = AR(input_dim, output_dim, window_size, fit_intercept=fit_intercept, constrain=constrain,)
    ar.fit(generator(X, y), alpha=1)

    shape = ar._params["phi"].shape

    if fit_intercept and constrain:
        assert shape == (window_size + 1, output_dim)
    if fit_intercept and not constrain:
        assert shape == (window_size * input_dim + 1, output_dim)
    if not fit_intercept and constrain:
        assert shape == (window_size, output_dim)
    if not fit_intercept and not constrain:
        assert shape == (window_size * input_dim, output_dim)


@pytest.mark.parametrize("input_dim", [1, 10])
@pytest.mark.parametrize("output_dim", [1, 10])
@pytest.mark.parametrize("window_size", [1, 10])
@pytest.mark.parametrize("fit_intercept", [True, False])
@pytest.mark.parametrize("constrain", [True, False])
def test_predict_shape(input_dim, output_dim, window_size, fit_intercept, constrain):
    history = onp.random.rand(window_size, input_dim)
    params = {}

    if fit_intercept and constrain:
        shape = (window_size + 1, output_dim)
    if fit_intercept and not constrain:
        shape = (window_size * input_dim + 1, output_dim)
    if not fit_intercept and constrain:
        shape = (window_size, output_dim)
    if not fit_intercept and not constrain:
        shape = (window_size * input_dim, output_dim)

    params["phi"] = onp.random.rand(*shape)
    result = _ar_predict(params, history, fit_intercept=fit_intercept, constrain=constrain)

    if constrain:
        assert result.shape == (input_dim, output_dim)
    else:
        assert result.shape == (output_dim,)
