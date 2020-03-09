from numbers import Real

import jax.numpy as np

from strange.utils.losses.core import Loss


class CrossEntropy(Loss):
    def __init__(self, eps: Real = 1e-15):
        self._eps = eps

    def compute(self, y_pred: np.ndarray, y_true: np.ndarray):
        """
        Description: cross entropy loss, y_pred is equivalent to logits and
        y_true to labels
        Args:
            y_pred (np.ndarray): value predicted by method
            y_true (np.ndarray): ground truth value
        Returns:
            error (Real):
        """
        return -np.sum(y_true * np.log(y_pred + self._eps)) / y_pred.shape[0]
