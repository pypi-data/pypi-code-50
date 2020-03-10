from typing import Callable

import jax

from timecast.learners.core import BaseLearner
from timecast.learners.core import DifferentiableMixin
from timecast.learners.core import TimeSeries
from timecast.utils.losses import MeanSquareError
from timecast.utils.losses.core import Loss
from timecast.utils.optimizers import OGD
from timecast.utils.optimizers.core import Optimizer


class BlackBox(BaseLearner):
    def __init__(self, predict: Callable):
        super().__init__()

        self._predict = predict

    def predict(self, X: TimeSeries) -> TimeSeries:
        # TODO: Assumes any featurizing is handled in self._predict
        return self._predict(X)

    def update(self, X: TimeSeries, y) -> "BlackBox":
        return self


class DifferentiableBlackBox(DifferentiableMixin, BlackBox):
    def __init__(
        self, predict: Callable, params: dict = None, optimizer: Optimizer = OGD, loss: Loss = None,
    ):
        super().__init__()

        self._predict = predict
        self._params = params
        self._optimizer = optimizer
        self._loss = MeanSquareError() if loss is None else loss

        try:
            self._predict = jax.jit(self._predict)
            self._objective = jax.jit(
                lambda _params, x, y: self._loss.compute(self._predict(_params, x), y)
            )
            self._grad = jax.jit(jax.grad(self._objective))
        except Exception as e:
            # TODO: Figure out actual jax exception
            raise ValueError(
                "Prediction function is not jitable via jax. Try"
                "`BlackBoxLearner` instead of"
                "`DifferentiableBlackBoxLearner`. {}".format(e)
            )

    def predict(self, X: TimeSeries) -> TimeSeries:
        # TODO: Assumes any featurizing is handled in self._predict
        return self._predict(self._params, X)

    def update(self, X: TimeSeries, y) -> "DifferentiableBlackBox":
        self._params = self._optimizer.update(self._params, self._grad(self._params, X, y))
        return self


def blackbox(
    predict: Callable,
    params: dict = None,
    optimizer: Optimizer = OGD,
    loss: Loss = MeanSquareError,
) -> BlackBox:
    try:
        return DifferentiableBlackBox(predict, params, optimizer, loss)
    except Exception as e:
        e
        return BlackBox(predict)
