
from typing import Set, Tuple

from .example import Example, Examples
from .explanation import Explanation, Record
from .path import Path


def find_best_explanation(explanations: Set[Explanation], examples: Examples) -> None:
    for e in explanations:
        new_score = evaluate_explanation(e, examples)
        roots = e.explains(examples)
        positive_example_set = set(examples.positives)
        r = Record(e, new_score, num_examples=len(examples), num_positives=len(examples.positives), num_connected_positives=ftp(roots, positive_example_set),
                   num_connected_negatives=ffp(roots, positive_example_set))
        e.record = r
        e.path.max_score_found_on_path = max(e.path.max_score_found_on_path, new_score)


def evaluate_explanation(e: Explanation, examples: Examples) -> float:
    return fuzzy_f_measure(e, examples)


def fuzzy_f_measure(e: Explanation, examples: Examples) -> float:
    return _fuzzy_f_measure(e.explains(examples), examples)


def max_fuzzy_f_measure(p: Path, examples: Examples) -> float:
    return _fuzzy_f_measure(p.get_starting_points(), examples)


def _fuzzy_f_measure(roots: Set[Example], examples: Examples) -> float:
    ftp_value, ffp_value, ffn_value = _tfpn_roots_positives(roots, set(examples.positives))
    fp_value = fp(ftp_value, ffp_value)
    fr_value = fr(ftp_value, ffn_value)
    if fp_value + fr_value == 0:
        return 0.0
    res = 2 * (fp_value*fr_value)/(fp_value+fr_value)
    return res


def ffp(roots: Set[Example], positives: Set[Example]) -> int:
    return len(roots - positives)


def ffn(roots: Set[Example], positives: Set[Example]) -> int:
    return len(positives - roots)


def ftp(roots: Set[Example], positives: Set[Example]) -> int:
    return len(roots & positives)


def fr(ftp_value: float, ffn_value: float) -> float:
    if ftp_value == 0:
        return 0.0
    return ftp_value / (ftp_value + ffn_value)


def fp(ftp_value: float, ffp_value: float) -> float:
    if ftp_value == 0:
        return 0.0
    return ftp_value / (ftp_value + ffp_value)


def tfpn(e: Explanation, examples: Examples) -> Tuple[float, float, float]:
    roots = e.explains(examples)
    return _tfpn_roots_positives(roots, set(examples.positives))


def _tfpn_roots_positives(roots: Set[Example], positives: Set[Example]) -> Tuple[float, float, float]:
    tp = ftp(roots, positives)
    fp = ffp(roots, positives)
    fn = ffn(roots, positives)
    return (tp, fp, fn)
