from abc import ABC
from abc import abstractmethod
from numbers import Real
from typing import Generator
from typing import TypeVar

import jax.numpy as np

# TODO: How to distinguish between a 1D time series value and a 1D time series?
# TODO: Enforce time series inputs
TimeSeries = TypeVar("TimeSeries", Real, np.ndarray)


class TimeSeriesMixin:
    def __init__(self, *args, **kwargs):
        super().__init__()
        self._timeseries = True


class RegressorMixin:
    def __init__(self, *args, **kwargs):
        super().__init__()
        self._regressor = True


class DifferentiableMixin:
    def __init__(self, *args, **kwargs):
        super().__init__()
        self._differentiable = True


class OfflineMixin(ABC):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self._offline = True

    @abstractmethod
    # TODO: Update documentation
    def fit(self, generator: Generator) -> "OfflineMixin":
        """
        Description: catch-all for training step (e.g., offline, pre-train,
            incremental).
        Args:
            data (TimeSeries):
        Returns:
            method (BaseMethod):
        """
        raise NotImplementedError()


class BaseLearner(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        """
        Description: Initialize BaseMethod
        Returns:
            method (BaseMethod):
        """
        super().__init__()

        # TODO: May want to check that certain keyword args are supplied
        for key in kwargs:
            if not hasattr(self, key):
                setattr(self, key, kwargs[key])

    @abstractmethod
    def predict(self, data: TimeSeries) -> TimeSeries:
        """
        Description: make a prediction about the next value based on current
            data.
        Args:
            data (TimeSeries):
        Returns:
            ts (TimeSeriesValue):
        """
        raise NotImplementedError()

    @abstractmethod
    # TODO: type hint y
    def update(self, data: TimeSeries, y) -> "BaseLearner":
        """
        Description: updates a model? What should this do?
        Args:
            data (TimeSeries):
        Returns:
            method (BaseMethod):
        """
        raise NotImplementedError()
