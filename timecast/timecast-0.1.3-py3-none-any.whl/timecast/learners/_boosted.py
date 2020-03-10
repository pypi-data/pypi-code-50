from typing import List

from timecast.learners.core import BaseLearner
from timecast.learners.core import TimeSeries


class Boosted(BaseLearner):
    def __init__(self, children: List[BaseLearner]):
        self._children = children

    def predict(self, X: TimeSeries) -> TimeSeries:
        pass

    def update(self, X: TimeSeries, y) -> "BaseLearner":
        pass


def boost(children: List[BaseLearner]) -> Boosted:
    return Boosted(children)
