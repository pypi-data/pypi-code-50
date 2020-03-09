from numbers import Real

import jax.numpy as np

from strange.learners.core import BaseLearner
from strange.learners.core import TimeSeries
from strange.learners.core import TimeSeriesMixin


class PredictLast(TimeSeriesMixin, BaseLearner):
    """
    Description: Predicts the value n steps ago in the time series, i.e.,
    x(t + 1) = x(t - n)
    """

    def __init__(self, offset: int = 1, pad_value: Real = 0):
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
        self._offset = offset
        self._pad_value = pad_value

        # TODO: we don't know how to size buffer yet
        self._buffer_ = []
        self._index = -1

    def predict(self, data: TimeSeries) -> TimeSeries:
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
        if np.isscalar(data) or isinstance(data, np.ndarray):
            return data
        else:
            return np.asarray(data)

    def update(self, data: TimeSeries, y) -> "PredictLast":
        return self
