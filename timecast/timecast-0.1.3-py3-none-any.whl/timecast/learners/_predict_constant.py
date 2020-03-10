from numbers import Real
from typing import Tuple

import jax.numpy as np

from timecast.learners.core import BaseLearner
from timecast.learners.core import TimeSeries
from timecast.learners.core import TimeSeriesMixin


class PredictConstant(TimeSeriesMixin, BaseLearner):
    """
    Description: Predicts a constant value at each step, i.e., x(t + 1) = c
    """

    def __init__(self, shape: Tuple[int, int] = (1, 1), constant: Real = 0):
        """
        Description: Initialize ConstantMethod
        Args:
            constant (Real): value to predict at each time step
        Returns:
            method (ConstantMethod):
        """
        super().__init__()
        self._shape = shape
        self._constant = constant
        self._value = np.ones(shape) * self._constant

    def predict(self, X: TimeSeries) -> TimeSeries:
        if X.shape != self._shape:
            raise ValueError(
                "Predict received inconsistent shape {}. Should be {}.".format(X.shape, self._shape)
            )
        return self._value

    def update(self, X: TimeSeries, y) -> "PredictConstant":
        if X.shape != self._shape:
            raise ValueError(
                "Predict received inconsistent shape {}. Should be {}.".format(X.shape, self._shape)
            )
        if y.shape != self._shape:
            raise ValueError(
                "Predict received inconsistent shape {}. Should be {}.".format(y.shape, self._shape)
            )
        return self

    def reset(self, params: bool = False, state: bool = False) -> "PredictConstant":
        return self
