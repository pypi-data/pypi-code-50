from numbers import Real

import jax.numpy as np

from strange.utils.losses.core import Loss


class Huber(Loss):
    def __init__(self, delta: Real = 2):
        self._delta = delta

    def compute(self, y_pred: np.ndarray, y_true: np.ndarray):
        """
        Description: Huber loss; square error when error is small, absolute
        error when large
        Args:
            y_pred (np.ndarray): value predicted by method
            y_true (np.ndarray): ground truth value
        Returns:
            error (Real):
        """
        diff = np.abs(y_pred - y_true)
        delta2 = self._delta * self._delta / 2

        return (
            np.sum(np.where(diff <= self._delta, diff * diff / 2, self._delta * diff - delta2,))
            / y_pred.shape[0]
        )
