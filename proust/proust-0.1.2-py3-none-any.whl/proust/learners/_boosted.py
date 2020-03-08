from typing import List

from proust.learners.core import BaseLearner, TimeSeries


class Boosted(BaseLearner):
    def __init__(self, children: List[BaseLearner]):
        self._children = children

    def predict(self, data: TimeSeries) -> TimeSeries:
        pass

    def update(self, data: TimeSeries, y) -> "BaseLearner":
        pass


def boost(children: List[BaseLearner]) -> Boosted:
    return Boosted(children)
