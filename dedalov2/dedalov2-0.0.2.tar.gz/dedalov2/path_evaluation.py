
import logging
import math
from typing import Callable, Dict, Optional, Set

from .example import Examples
from .path import Path
from .path_pruner import PathPruner

LOG = logging.getLogger('dedalov2.path_evaluation')
SearchHeuristic = Callable[[Path, Examples], float]


def find_best_path(heuristic: SearchHeuristic, paths: Dict[Path, Path], examples: Examples, pruner: PathPruner, max_length: float = float('inf')) -> Optional[Path]:
    LOG.debug("EVALUATING {} POSSIBLE PATHS".format(len(paths)))
    score = float('-inf')
    res: Optional[Path] = None
    paths_to_delete: Set[Path] = set()
    pruned: int = 0
    too_long: int = 0
    for path in paths:
        if len(path) > max_length:
            paths_to_delete.add(path)
            too_long += 1
            continue
        if pruner(path):
            paths_to_delete.add(path)
            pruned += 1
            continue

        new_score = heuristic(path, examples)
        if new_score > score:
            score = new_score
            res = path
    for path in paths_to_delete:
        paths.pop(path, None)
    LOG.debug("PRUNED {} PATHS".format(pruned))
    LOG.debug("REMOVED {} TOO LONG PATHS".format(too_long))
    LOG.debug("NEXT ROUND HAS {} REMAINING PATHS".format(len(paths)))
    return res


def entropy(p: Path, examples: Examples) -> float:
    res: float = 0
    for obj in p.get_end_points():
        num_roots = len(p.get_starting_points_connected_to_endpoint(obj))
        frac = num_roots/len(examples)
        assert frac >= 0
        assert frac <= 1
        res -= frac * math.log10(frac)
    return res

def entropy_corrected(p: Path, examples: Examples) -> float:
    res: float = 0
    for obj in p.get_end_points():
        frac: float = 0.0
        starting_points_to_obj = p.get_starting_points_connected_to_endpoint(obj)
        for starting_point in starting_points_to_obj:
            numexamples = p.get_end_points_connected_to_example(starting_point)
            frac += 1 / (len(numexamples) * len(starting_points_to_obj))
        assert frac >= 0
        assert frac <= 1
        res -= frac * math.log10(frac)
    return res


def shortest_path(p: Path, examples: Examples) -> float:
    return -float(len(p))


def longest_path(p: Path, examples: Examples) -> float:
    return float(len(p))


HEURISTIC_NAMES: Dict[str, Callable[[Path, Examples], float]] = {
    "spf": shortest_path,
    "entropy": entropy,
    "lpf": longest_path,
    "ec": entropy_corrected,
}
