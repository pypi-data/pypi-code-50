from numbers import Real
from typing import Tuple

import jax.numpy as np

from timecast.learners.core import BaseLearner
from timecast.learners.core import TimeSeries
from timecast.learners.core import TimeSeriesMixin


class PredictLast(TimeSeriesMixin, BaseLearner):
    """
    Description: Predicts the value n steps ago in the time series, i.e.,
    x(t + 1) = x(t - n)
    """

    def __init__(self, shape: Tuple[int, int] = (1, 1), offset: int = 1, pad_value: Real = 0):
        """
        Description: Initializes LastMethod
        Args:
            offset (int): number of steps to look back in the time series
                TODO: how to size the buffer?
            pad_value (Real): value used to pad missing predictions.
                TODO: what if each value is vector?
        Returns:
            method (LastMethod):
        """
        super().__init__()
        self._shape = shape
        self._offset = offset
        self._pad_value = np.ones(shape) * pad_value

        # TODO: we don't know how to size buffer yet
        self._buffer = []
        self._index = -1
        self._prev_value = self._pad_value

    def predict(self, X: TimeSeries) -> TimeSeries:
        """
        TODO: Ignores the offset parameter
        Questions:
            - Does it make sense to take data in batch here except perhaps to
              advance the timeline by len number of steps?
        Args:
            data (TimeSeries):

        Returns:
            ts (TimeSeries):
        """
        if X.shape != self._shape:
            raise ValueError(
                "Predict received inconsistent shape {}. Should be {}.".format(X.shape, self._shape)
            )
        return self._prev_value

    def update(self, X: TimeSeries, y) -> "PredictLast":
        if X.shape != self._shape:
            raise ValueError(
                "Predict received inconsistent shape {}. Should be {}.".format(X.shape, self._shape)
            )
        if y.shape != self._shape:
            raise ValueError(
                "Predict received inconsistent shape {}. Should be {}.".format(y.shape, self._shape)
            )
        self._prev_value = X
        return self

    def reset(self, params: bool = False, state: bool = False) -> "PredictLast":
        self._prev_value = self._pad_value
        self._buffer = []
        self._index = -1
        return self
