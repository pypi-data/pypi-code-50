import inspect
import pickle
from abc import ABC
from abc import abstractmethod
from numbers import Real
from typing import Generator
from typing import Tuple
from typing import TypeVar

import numpy as np

# TODO: How to distinguish between a 1D time series value and a 1D time series?
# TODO: Enforce time series inputs
TimeSeries = TypeVar("TimeSeries", Real, np.ndarray)


class TimeSeriesMixin:
    pass


class RegressorMixin:
    pass


class DifferentiableMixin:
    pass


class OfflineMixin(ABC):
    @abstractmethod
    # TODO: Update documentation
    def fit(
        self, generator: Generator[Tuple[np.ndarray, np.ndarray], None, None]
    ) -> "OfflineMixin":
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
        self._freeze_params = False
        self._freeze_state = False

    @abstractmethod
    def predict(self, X: TimeSeries) -> TimeSeries:
        """
        Description: make a prediction about the next value based on current
            data.
        Args:
            X (TimeSeries):
        Returns:
            ts (TimeSeriesValue):
        """
        raise NotImplementedError()

    @abstractmethod
    # TODO: type hint y
    def update(self, X: TimeSeries, y) -> "BaseLearner":
        """
        Description: updates a model? What should this do?
        Args:
            X (TimeSeries):
        Returns:
            method (BaseMethod):
        """
        raise NotImplementedError()

    @abstractmethod
    def reset(self, params: bool = False, state: bool = False) -> "BaseLearner":
        raise NotImplementedError()

    def freeze(self, params: bool = False, state: bool = False) -> "BaseLearner":
        if params:
            self._freeze_params = True
        if state:
            self._freeze_state = True
        return self

    def unfreeze(self, params: bool = False, state: bool = False) -> "BaseLearner":
        if params:
            self._freeze_params = False
        if state:
            self._freeze_state = False
        return self

    def save(self, path: str) -> "BaseLearner":
        # Grab all items that aren't routines or Python
        with open(path, "wb") as f:
            pickle.dump(
                {
                    attr: getattr(self, attr)
                    for attr in dir(self)
                    if (
                        "abc" not in attr
                        and attr[:2] != "__"
                        and not inspect.isroutine(getattr(self, attr))
                    )
                },
                f,
            )

        return self

    @classmethod
    def load(cls, path: str) -> "BaseLearner":
        with open(path, "rb") as f:
            attrs = pickle.load(f)
        result = cls()

        for key, val in attrs.items():
            print(key, val)
            setattr(result, key, val)

        return result
