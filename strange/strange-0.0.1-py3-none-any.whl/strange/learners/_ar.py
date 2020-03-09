"""
AR: a linear auto-regressive learner

Assumptions
- Time series values have the same dimension as the predicted value or is scalar
- In the scalar scenario, all features in the input_dim x window_size history
  are flattened to predict the single scalar value (input_dim x window_size features)
- In the vector scenario, each input_dim-sized vector in the window_size history
  is treated as its own regressor (window_size features)
"""
from numbers import Real
from typing import Generator
from typing import Tuple
from typing import Union

import jax.experimental.stax as stax
import jax.numpy as np
import jax.ops
import numpy as onp

from strange.learners.core import BaseLearner
from strange.learners.core import DifferentiableMixin
from strange.learners.core import OfflineMixin
from strange.learners.core import RegressorMixin
from strange.learners.core import TimeSeries
from strange.learners.core import TimeSeriesMixin
from strange.utils.losses import MeanSquareError
from strange.utils.losses.core import Loss
from strange.utils.optimizers import OGD
from strange.utils.optimizers.core import Optimizer
from strange.utils.random import generate_key
from strange.utils.statistics import OnlineStatistics

# TODO: should we normalize online data as it's coming in if we don't have any
# pre-training?


# TODO: Type hint data
# TODO: Test data input (R,1) vs (R,)
def _ar_update_history(history: np.ndarray, data) -> np.ndarray:
    history = np.asarray(history)
    if history.shape[1] != len(data):
        raise ValueError("Attempting to update history with time series value of differing shape.")
    _updated_history = np.roll(history, len(data))
    _updated_history = jax.ops.index_update(_updated_history, 0, data)
    return _updated_history


def _ar_predict(
    params: dict, history: np.ndarray, fit_intercept: bool = True, constrain: bool = False,
) -> np.ndarray:
    """
    Description: predicts based on params and history

    Args:

        params (dict): Currently implemented as a dictionary with key 'phi'
        that holds an (window_size + 1)-d vector of parameters for a history of
        window_size n-d vectors
        history (np.ndarray): A history of n-d vectors; two-dimensional array
        where the first dimension is time and the second dimension (if any) is
        the time series value, which may be multidimensional
        fit_intercept (bool): whether or not to fit an intercept
        constrain (bool): whether or not we constrain parameters (i.e., one
        for each vector in the window or one for each value in the window)

    Raises:
        ValueError: [description]
        ValueError: [description]

    Returns:
        np.ndarray: An n-d prediction
    """

    # (fit_intercept, constrain): params, history
    # w: window_size
    # i: input_dim
    # o: output_dim

    # (True, True): (w + 1, o), (w + 1, i)
    # (True, False): (w * i + 1, o), (w * i + 1, 1)
    # (False, True): (w, o), (w, i)
    # (False, False): (w * i, o), (w * i, 1)

    if fit_intercept and constrain:
        return np.dot(np.vstack((np.ones((1, history.shape[1])), history)).T, params["phi"])

    if fit_intercept and not constrain:
        return np.dot(np.concatenate((np.array([1]), history.ravel())), params["phi"])

    if not fit_intercept and constrain:
        return np.dot(history.T, params["phi"])

    if not fit_intercept and not constrain:
        return np.dot(history.ravel(), params["phi"])


def _ar_form_linear_constraints(
    input_dim: int, output_dim: int, window_size: int, fit_intercept: bool = True
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Description: Sets the linear constraint matrix and vector R and r,
    respectively for constraining the `_params` vector. Specifically, each row
    in R is a linearly independent constraint where we force each dimension in
    the time series value to share a coefficient across the window.

    References: https://www.le.ac.uk/users/dsgp1/COURSES/TOPICS/restrict.pdf

    Args:
        input_dim (int): number of dimensions in the time series value
        output_dim (int): number of dimensions in the output
        window_size (int): window size for the auto reggressor
        fit_intercept (bool, optional): whether or not to fit an intercept.
        Defaults to True.

    Returns:
        Tuple[np.ndarray, np.ndarray]: RB = r
    """
    if fit_intercept:
        window_size += 1

    num_constraints = window_size * (input_dim - 1)

    R = onp.zeros((num_constraints, input_dim * window_size))
    r = onp.zeros((num_constraints, output_dim))

    # To share a parameter p across features x1 and x2, create a new row in R
    # with index 1 set to 1, index 2 set to -1, the rest set to 0 and the
    # corresponding row in r set to 0 (i.e., x1 + x2 = 0)
    for i in range(window_size):
        for j in range(input_dim - 1):

            # Set the constraint row
            row = i * (input_dim - 1) + j

            # Column indices for the first and second feature to tie. Note that
            # within the inner for loop, we tie multiple features to the same
            # parameter
            col1 = i * input_dim + j
            col2 = i * input_dim + j + 1

            # Update R appropriately
            R[row, col1] = 1
            R[row, col2] = -1

    return R, r


def _ar_fit_normalize_prod(
    # inv: np.ndarray, mu: np.ndarray, sigma: np.ndarray, s: np.ndarray, n: int
    AB: np.ndarray,
    A_stats: OnlineStatistics,
    B_stats: OnlineStatistics,
) -> np.ndarray:
    """
    Normalize the product of matrices A and B if we only have running mean, std,
    sum

    Args:
        AB (np.ndarray): The product of matrix A and B
        A_stats (OnlineStatistics): running mean, std, sum for matrix A
        B_stats (OnlineStatistics): running mean, std, sum for matrix B

    Raises:
        ValueError: [description]

    Returns:
        np.ndarray: Normalized AB
    """

    if A_stats.observations() != B_stats.observations():
        raise ValueError(
            "A and B should have the same number of observations ({}, {})".format(
                A_stats.observations(), B_stats.observations()
            )
        )

    n = A_stats.observations()

    result = (
        AB
        + n * np.outer(A_stats.mean(), B_stats.mean())
        - np.outer(A_stats.mean(), B_stats.sum())
        - np.outer(A_stats.sum(), B_stats.mean())
    ) / np.outer(A_stats.std(), B_stats.std())

    # Replace nans with 0s because std of some column was 0
    return np.nan_to_num(result)


def _ar_fit_unconstrained(inv: np.ndarray, Xy: np.ndarray) -> np.ndarray:
    return inv @ Xy


def _ar_fit_constrained(beta, inv, R, r):
    return beta - inv @ (R.T @ onp.linalg.inv(R @ (inv @ R.T))) @ (R @ beta - r)


class AR(
    DifferentiableMixin, OfflineMixin, RegressorMixin, TimeSeriesMixin, BaseLearner,
):
    def __init__(
        self,
        input_dim: int = 1,
        output_dim: int = 1,
        window_size: int = 3,
        optimizer: Optimizer = OGD,
        loss: Loss = None,
        fit_intercept: bool = True,
        normalize: bool = False,
        constrain: bool = False,
    ):
        super().__init__()

        self._input_dim = input_dim
        self._output_dim = output_dim
        self._window_size = window_size
        self._optimizer = optimizer
        self._loss = MeanSquareError() if loss is None else loss
        self._fit_intercept = fit_intercept
        self._normalize = normalize
        self._constrain = constrain

        self._num_features = self._input_dim * self._window_size
        self._num_features_with_intercepts = self._num_features

        # If we want to fit an intercept, need to add features
        if self._fit_intercept:
            # If we're constraining so each input_dim vector in the window is
            # its own regressor, add input_dim intercepts
            if self._constrain:
                self._num_features_with_intercepts += self._input_dim

            # If unconstrained, add 1
            else:
                self._num_features_with_intercepts += 1

        self._param_dim = [self._window_size, 1]
        if self._fit_intercept:
            self._param_dim[0] += 1

        # TODO: The great (R,), (R,1) debate rages on! Here, we've chosen
        #  (R,) in the case of scalar time series values
        self._history_shape = (self._window_size, self._input_dim)
        self._history = np.zeros(self._history_shape)

        glorot_init = stax.glorot()
        self._params = {"phi": glorot_init(generate_key(), self._param_dim)}

        self._update_history = jax.jit(lambda history, data: _ar_update_history(history, data))

        self._predict = jax.jit(lambda params, data: _ar_predict(params, data, self._fit_intercept))

        self._objective = jax.jit(
            lambda params, x, y: self._loss.compute(self._predict(params, x), y)
        )

        self._grad = jax.jit(jax.grad(self._objective))

        self._X_stats = OnlineStatistics(self._window_size * self._input_dim)
        self._y_stats = OnlineStatistics(self._output_dim)

    def predict(self, data: TimeSeries) -> TimeSeries:
        if self._fit_intercept and self._normalize:
            data = self._X_stats.zscore(data)
        # NOTE: We call self._update_history twice each iteration; once in
        # predict, once in update
        return self._predict(self._params, self._update_history(self._history, data))

    def update(self, data: TimeSeries, y) -> "AR":
        new_data = data
        if self._fit_intercept and self._normalize:
            self._X_stats.update(data)
            new_data = self._X_stats.zscore(data)

        # NOTE: update both state and params here. Must be run using the same
        # data as in predict (preferably right after running predict)
        self._history = self._update_history(self._history, new_data)
        self._params = self._optimizer.update(self._params, self._grad(self._params, data, y))
        return self

    # `fit` helper function split out for testing
    def _fit_accumulate(
        self,
        generator: Generator[Tuple[np.ndarray, np.ndarray], None, None],
        alpha: Union[Real, np.ndarray] = 1,
    ) -> (np.ndarray, np.ndarray):

        XTX = onp.zeros((self._num_features, self._num_features))
        Xy = onp.zeros((self._num_features, self._output_dim))

        for X, y in generator:
            # We don't use num_features here because this is data unmodified by
            # intercepts
            if X.shape[1] != self._num_features:
                raise ValueError(
                    "Generator provided X {} that has shape inconsistent with"
                    "`input_dim` {} and `window_size` {}".format(
                        X.shape, self._input_dim, self._window_size
                    )
                )

            if len(y.shape) > 1 and y.shape[1] != self._output_dim:
                raise ValueError(
                    "Generator provided y {} inconsistent with `output_dim` {}".format(
                        y.shape, self._output_dim
                    )
                )

            if X.shape[0] != y.shape[0]:
                raise ValueError(
                    "X and y different observations: {}, {}".format(X.shape[0], y.shape[0]),
                )

            # Force vectors into matrices
            if len(X.shape) == 1:
                X = X[:, np.newaxis]
            if len(y.shape) == 1:
                y = y[:, np.newaxis]

            XTX += X.T @ X
            Xy += X.T @ y

            for (X_, y_) in zip(X, y):
                self._X_stats.update(X_)
                self._y_stats.update(y_)

        if self._fit_intercept:
            if self._normalize:

                XTX = _ar_fit_normalize_prod(XTX, self._X_stats, self._X_stats)
                Xy = _ar_fit_normalize_prod(Xy, self._X_stats, self._y_stats)

            num_rc = self._input_dim if self._constrain else 1

            # pylint: disable=unsubscriptable-object
            XTX = onp.concatenate((np.zeros((XTX.shape[0], num_rc)), XTX), axis=1)
            XTX = onp.concatenate((np.zeros((num_rc, XTX.shape[1])), XTX), axis=0)
            Xy = onp.concatenate((np.zeros((num_rc, Xy.shape[1])), Xy), axis=0)

            if not self._normalize:
                S = onp.tile(self._X_stats.sum(), (num_rc, 1))
                XTX[:num_rc, :num_rc] = self._X_stats.observations()
                XTX[:num_rc, num_rc:] = S
                XTX[num_rc:, :num_rc] = S.T

                S = onp.tile(self._y_stats.sum(), (num_rc, 1))
                Xy[:num_rc, :] = S

        inv = onp.linalg.inv(XTX + alpha * np.eye(XTX.shape[1]))

        return inv, Xy

    def fit(
        self, generator: Generator[Tuple[np.ndarray, np.ndarray], None, None], alpha: Real = 1,
    ) -> "AR":
        """
        Description: Incrementally computes a ridge regression given data yielded
        by `generator`. NOTE: this will retrain the underlying predictor from scratch.

        References: https://www.le.ac.uk/users/dsgp1/COURSES/TOPICS/restrict.pdf

        Args:
            generator (Generator[(np.ndarray, np.ndarray), None, None]): yields (X,
            y) tuples representing inputs and outputs, respectively. X is a
            two-dimensional array where the first dimension is number of
            observations and the second dimension is the flattened features
            alpha (Union[Real, np.ndarray], optional): [TODO]. Defaults to 1.

        Returns:
            self
        """

        # Sum up data incrementally
        inv, Xy = self._fit_accumulate(generator, alpha=alpha)
        self._params["phi"] = _ar_fit_unconstrained(inv, Xy)

        if self._constrain:
            R, r = _ar_form_linear_constraints(
                self._input_dim,
                self._output_dim,
                self._window_size,
                fit_intercept=self._fit_intercept,
            )
            self._params["phi"] = _ar_fit_constrained(self._params["phi"], inv, R, r)
            self._params["phi"] = self._params["phi"].take(
                np.arange(0, len(self._params["phi"]), self._input_dim), axis=0
            )

        return self
