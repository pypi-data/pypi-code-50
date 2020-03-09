from typing import List

from strange.learners.core import BaseLearner
from strange.learners.core import TimeSeries


class Boosted(BaseLearner):
    def __init__(self, children: List[BaseLearner]):
        self._children = children

    def predict(self, data: TimeSeries) -> TimeSeries:
        pass

    def update(self, data: TimeSeries, y) -> "BaseLearner":
        pass


def boost(children: List[BaseLearner]) -> Boosted:
    return Boosted(children)
