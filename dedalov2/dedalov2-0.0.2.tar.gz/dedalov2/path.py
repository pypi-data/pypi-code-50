
from typing import Dict, Optional, Set

from .example import Example, Examples
from .knowledge_graph import Predicate, Vertex
from .linked_list import LinkedNode


class Path:

    @staticmethod
    def from_examples(starting_examples: Examples):
        path = Path()
        for example in starting_examples:
            path.start_to_ends.setdefault(example, set()).add(example.vertex)
            path.end_to_starts.setdefault(example.vertex, set()).add(example)
        return path

    def __init__(self):
        self.edges: Optional[LinkedNode] = None
        # TODO figure out what to do with this field.
        self.max_score_found_on_path: float = 0
        self.start_to_ends: Dict[Example, Set[Vertex]] = {}
        self.end_to_starts: Dict[Vertex, Set[Example]] = {}

    def extend(self, paths: Dict['Path', 'Path'], s: Vertex, p: Predicate, o: Vertex) -> 'Path':
        edges = LinkedNode(p, self.edges)
        path = Path()
        path.edges = edges
        if path in paths:
            path = paths[path]
        else:
            paths[path] = path
        starting_points: Set[Example] = self.get_starting_points_connected_to_endpoint(s)
        path.end_to_starts.setdefault(o, set()).update(starting_points)
        for e in starting_points:
            path.start_to_ends.setdefault(e, set()).add(o)
        return path

    def get_starting_points(self) -> Set[Example]:
        return set(self.start_to_ends.keys())

    def get_starting_points_connected_to_endpoint(self, o: Vertex) -> Set[Example]:
        return self.end_to_starts.get(o, set())

    def get_end_points(self) -> Set[Vertex]:
        return set(self.end_to_starts.keys())

    def get_end_points_connected_to_example(self, e: Example) -> Set[Vertex]:
        return self.start_to_ends.get(e, set())

    def __len__(self):
        if self.edges is None:
            return 0
        return len(self.edges)

    def __hash__(self):
        return hash(self.edges)

    def __eq__(self, other):
        return self.edges == other.edges

    def __str__(self):
        if self.edges is None:
            return ""
        return " -> ".join(map(lambda e: str(e), self.edges))
