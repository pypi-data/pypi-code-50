from abc import ABC
from abc import abstractmethod

import jax.numpy as np


class Loss(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError()

    @abstractmethod
    def compute(self, y_pred: np.ndarray, y_true: np.ndarray):
        raise NotImplementedError()
