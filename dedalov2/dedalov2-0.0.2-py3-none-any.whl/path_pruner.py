
import logging
from typing import Callable, Dict

from .example import Examples
from .path import Path

PathPruner = Callable[[Path], bool]

LOG = logging.getLogger('dedalov2.path_pruner')


def ple(explanation_evaluation_func: Callable[[Path, Examples], float], examples: Examples) -> PathPruner:
    def p(p: Path) -> bool:
        new_max = explanation_evaluation_func(p, examples)
        best_found = p.max_score_found_on_path
        should_prune = best_found >= new_max
        if should_prune:
            return True
        return False
    return p


def pl(explanation_evaluation_func: Callable[[Path, Examples], float], examples: Examples) -> PathPruner:
    def p(p: Path) -> bool:
        new_max = explanation_evaluation_func(p, examples)
        best_found = p.max_score_found_on_path
        should_prune = best_found > new_max
        if should_prune:
            return True
        return False
    return p


def gle(explanation_evaluation_func: Callable[[Path, Examples], float], examples: Examples) -> PathPruner:
    max_score: float = 0.0

    def p(p: Path) -> bool:
        nonlocal max_score
        new_max = explanation_evaluation_func(p, examples)
        should_prune = max_score >= new_max
        if should_prune:
            return True
        else:
            max_score = new_max
            return False
    return p


def gl(explanation_evaluation_func: Callable[[Path, Examples], float], examples: Examples) -> PathPruner:
    max_score: float = 0.0

    def p(p: Path) -> bool:
        nonlocal max_score
        new_max = explanation_evaluation_func(p, examples)
        should_prune = max_score > new_max
        if should_prune:
            return True
        else:
            max_score = new_max
            return False
    return p


def off(explanation_evaluation_func: Callable[[Path, Examples], float], examples: Examples) -> PathPruner:
    def p(p: Path) -> bool:
        return False
    return p


PathPrunerFactory = Callable[[Callable[[Path, Examples], float], Examples], PathPruner]


PATH_PRUNER_NAMES: Dict[str, PathPrunerFactory] = {
    "gle": gle,
    "gl": gl,
    "ple": ple,
    "pl": pl,
    "off": off,
}
