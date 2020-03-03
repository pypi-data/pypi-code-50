from __future__ import division

from sciencebeam_alignment.align import GlobalSequenceMatcher, SimpleScoring


LEVENSHTEIN_SCORING = SimpleScoring(match_score=1, mismatch_score=-1, gap_score=-1)


def _get_match_length(matching_blocks):
    return sum(size for _, _, size in matching_blocks)


def get_levenshtein_distance(a, b):
    return max(len(a), len(b)) - _get_match_length(
        GlobalSequenceMatcher(a=a, b=b, scoring=LEVENSHTEIN_SCORING)
        .get_matching_blocks()
    )


def get_levenshtein_ratio(a, b):
    max_length = max(len(a), len(b))
    if not max_length:
        return 0.0
    return 1.0 - get_levenshtein_distance(a, b) / max_length
