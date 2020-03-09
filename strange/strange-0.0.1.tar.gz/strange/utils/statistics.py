from numbers import Real
from typing import Tuple
from typing import Union

import jax.numpy as np


class OnlineStatistics:
    def __init__(self, input_dim: Union[Tuple[int], int]):
        self._input_dim = input_dim
        self._is_scalar = input_dim == 1
        self._mean = 0 if self._is_scalar else np.zeros(self._input_dim)
        self._variance = 0 if self._is_scalar else np.zeros(self._input_dim)
        self._sum = 0 if self._is_scalar else np.zeros(self._input_dim)
        self._observations = 0

    # TODO: Do we want to support batching?
    def update(self, observation: Union[Real, np.ndarray]) -> None:
        if not self._is_scalar:
            observation = np.asarray(observation)

        self._observations += 1
        prev_mean = self._mean
        self._mean = self._mean + (observation - self._mean) / self._observations
        self._variance = self._variance + (observation - prev_mean) * (observation - self._mean)
        self._sum += observation

    def mean(self) -> Union[Real, np.ndarray]:
        return self._mean

    def var(self) -> Union[Real, np.ndarray]:
        return self._variance / self._observations

    def std(self) -> Union[Real, np.ndarray]:
        return np.sqrt(self._variance / self._observations)

    def sum(self) -> Union[Real, np.ndarray]:
        return self._sum

    def observations(self) -> int:
        return self._observations

    def zscore(self, data: np.ndarray) -> Real:
        return (data - self.mean()) / self.std()
