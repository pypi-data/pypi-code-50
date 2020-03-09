from numbers import Real

import jax.numpy as np

from strange.learners.core import BaseLearner
from strange.learners.core import TimeSeries
from strange.learners.core import TimeSeriesMixin


class PredictConstant(TimeSeriesMixin, BaseLearner):
    """
    Description: Predicts a constant value at each step, i.e., x(t + 1) = c
    """

    def __init__(self, constant: Real = 0):
        """
        Description: Initialize ConstantMethod
        Args:
            constant (Real): value to predict at each time step
        Returns:
            method (ConstantMethod):
        """
        super().__init__()
        self._constant = constant

    def predict(self, data: TimeSeries) -> TimeSeries:
        if np.isscalar(data):
            return self._constant
        else:
            return np.ones(np.asarray(data).shape) * self._constant

    def update(self, data: TimeSeries, y) -> "PredictConstant":
        return self
