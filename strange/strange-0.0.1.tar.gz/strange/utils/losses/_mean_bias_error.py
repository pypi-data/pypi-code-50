import jax.numpy as np

from strange.utils.losses.core import Loss


class MeanBiasError(Loss):
    def __init__(self):
        pass

    def compute(self, y_pred: np.ndarray, y_true: np.ndarray):
        """
        Description: mean bias error (L1)
        Args:
            y_pred (np.ndarray): value predicted by method
            y_true (np.ndarray): ground truth value
        Returns:
            error (Real):
        """
        return np.sum(y_pred - y_true) / y_pred.shape[0]
