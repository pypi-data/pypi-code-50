from collections import defaultdict
from ..dataset import Dataset


class Tracker:

    def __init__(self):
        self.examples = []
        self.preds = {}
        self.metrics = defaultdict(list)

    def add(self, examples=None, preds=None, metrics=None):
        metrics = metrics or {}
        self.examples.extend(examples or [])
        self.preds = Dataset.accumulate_preds(self.preds, preds or {})
        for k, v in metrics.items():
            self.metrics[k].append(v)

    def average_metrics(self):
        return {k: sum(v) / len(v) for k, v in self.metrics.items()}

    def clear(self):
        self.examples.clear()
        self.preds.clear()
        self.metrics.clear()
