
from typing import Optional, Set

from .example import Example, Examples
from .knowledge_graph import Vertex
from .path import Path


class Explanation:
    def __init__(self, p: Path, value: Vertex):
        self.path: Path = p
        self.value: Vertex = value
        self.record: Optional[Record] = None

    def explains(self, examples: Examples) -> Set[Example]:
        return self.path.get_starting_points_connected_to_endpoint(self.value)

    def __lt__(self, other):
        return self.path < other.path

    def __eq__(self, other):
        return type(other) == Explanation and self.path == other.path and self.value == other.value

    def __hash__(self):
        return hash(self.path)*31+hash(self.value)

    def __str__(self):
        return "{} -| {}".format(self.path, self.value)


class Record:
    def __init__(self, explanation: Explanation, score: float, num_examples: int = None, num_positives: int = None,
                 num_connected_positives: int = None, num_connected_negatives: int = None):
        self.explanation: Explanation = explanation
        self.score: float = score
        self.num_examples: Optional[int] = num_examples
        self.num_positives: Optional[int] = num_positives
        self.num_connected_positives: Optional[int] = num_connected_positives
        self.num_connected_negatives: Optional[int] = num_connected_negatives

    def __str__(self):
        if self.num_examples is None or self.num_positives is None or self.num_connected_positives is None or self.num_connected_negatives is None:
            return "SCORE: {} EXPL: {}".format(self.score, self.explanation)
        else:
            return "SCORE: {} P:{}:{} N:{}:{} EXPL: {}".format(self.score,
                                                               self.num_connected_positives,
                                                               self.num_positives,
                                                               self.num_connected_negatives,
                                                               self.num_examples-self.num_positives,
                                                               self.explanation)

    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        same_exp = self.explanation == other.explanation
        if same_exp:
            assert self.score == other.score
        return same_exp
