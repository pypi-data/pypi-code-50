import jax.numpy as np

from strange.utils.optimizers.core import Optimizer


class OGD(Optimizer):
    def __init__(self, learning_rate=1.0, max_norm=True):
        # Create dictionary of named arguments
        super().__init__()

        self.T = 0
        self.max_norm = max_norm
        self.original_max_norm = self.max_norm
        self.learning_rate = learning_rate

    def update(self, params, grad):
        self.T += 1

        # TODO: Don't overload `learning_rate`
        # TODO: OGD / SGD grand unification theory
        # TODO: Root T
        learning_rate = self.learning_rate / np.sqrt(self.T)

        if self.max_norm:
            self.max_norm = np.maximum(
                self.max_norm, np.linalg.norm([np.linalg.norm(dw) for dw in grad.values()]),
            )
            learning_rate = self.learning_rate / self.max_norm

        new_params = {key: params[key] - learning_rate * grad[key] for key in params}

        return new_params
