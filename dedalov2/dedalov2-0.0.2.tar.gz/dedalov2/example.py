
import logging
import os
from typing import Iterator, List

from .knowledge_graph import Vertex

LOG = logging.getLogger('dedalov2.example')

class Example:

    @staticmethod
    def fromString(uri: str, positive: bool = True) -> 'Example':
        if uri[0] == "<":
            uri = uri[1:]
        if uri[-1] == ">":
            uri = uri[:-1]
        vertex = Vertex.fromString(uri)
        return Example(vertex, positive)

    def __init__(self, vertex: Vertex, positive: bool = True):
        self.vertex: Vertex = vertex
        self.positive: bool = positive

    def __hash__(self):
        return hash(self.vertex) << 1 + (1 if self.positive else 0)

    def __eq__(self, other):
        return isinstance(other, Example) \
            and self.vertex == other.vertex \
            and self.positive == other.positive

    def __str__(self):
        return "{}-{}".format("P" if self.positive else "N", self.vertex)


class Examples:

    @staticmethod
    def fromCSV(filename: str, groupid=None, split_char=",", truncate: int = 0, balance: bool = False) -> 'Examples':
        examples = Examples()
        if filename is not None:
            if not os.path.isfile(filename):
                raise ValueError("File {} does not exist.".format(filename))
            first_line = True
            with open(filename) as fin:
                for line in fin:
                    parts = line.strip().split(split_char)
                    group = parts[0]
                    if first_line:
                        if groupid is None:
                            groupid = int(group)
                            LOG.warning("Positive example group ID not set. Using '{}'.".format(groupid))
                        else:
                            LOG.debug("Positive example group ID set to '{}'.".format(groupid))
                        first_line = False
                    uri = parts[1]
                    try:
                        e = Example.fromString(uri, int(group) == int(groupid))
                        examples.add_example(e)
                    except ValueError as err:
                        LOG.warning(err)
        if truncate > 0:
            examples.truncate(truncate)
        if balance:
            examples.balance()
        if len(examples.positives) <= 0:
            raise ValueError("Cannot run program without positive examples.")
        return examples

    def __init__(self):
        self.positives: List[Example] = []
        self.negatives: List[Example] = []

    def add_example(self, example: Example) -> None:
        assert example is not None
        if example.positive and example not in self.positives:
            self.positives.append(example)
        elif example not in self.negatives:
            self.negatives.append(example)

    def truncate(self, number: int) -> None:
        assert number > 0
        self.positives = self.positives[:number]
        self.negatives = self.negatives[:number]

    def balance(self) -> None:
        m = min(len(self.positives), len(self.negatives))
        self.positives = self.positives[:m]
        self.negatives = self.negatives[:m]

    def __len__(self):
        return len(self.positives) + len(self.negatives)

    def __iter__(self) -> Iterator[Example]:
        for p in self.positives:
            yield p
        for n in self.negatives:
            yield n
