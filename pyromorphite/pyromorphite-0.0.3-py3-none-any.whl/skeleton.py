from collections import defaultdict, namedtuple
from itertools import combinations, permutations

from .bag import Bag
from .utils import _powerset, _freqs, _pred, _succ, _freq2activity

_PairRelationship = namedtuple('PairRelationship', ['direction', 'pairs'])


def _equivalence(log: Bag, labels: list) -> _PairRelationship:
    """Pairs of activities, appearing in each trace an equal number of times.

    Returns
    -------
    set of pairs
    """

    if not isinstance(log, Bag):
        raise ValueError("Invalid Bag object.")

    r = {k: True for k in combinations(sorted(labels), r=2)}

    for trace in log:
        # Extract pairs in current trace
        w = dict()
        # labels appearing equal number of times in trace
        f2a = _freq2activity(trace)

        for s in f2a.values():
            for pair in combinations(sorted(s) + ["END"], r=2):
                if pair[0] not in w:
                    w[pair[0]] = []
                w[pair[0]].append(pair[1])

        # Check if the relationships found till now still hold
        for k, v in r.items():
            if v:
                if k[0] not in w and k[1] not in w:
                    continue

                if k[0] in w and k[1] not in w[k[0]]:
                    r[k] = False

    return _PairRelationship('lr', set([k for k, v in r.items() if v]))


def _never_together(log: Bag, labels: list) -> _PairRelationship:
    """Pairs of activities, never appearing together in any trace.

    Returns
    -------
    set of pairs
    """

    if not isinstance(log, Bag):
        raise ValueError("Invalid Bag object.")

    r = {k: True for k in combinations(sorted(labels), r=2)}
    for trace in log:
        for pair in combinations(sorted(trace), r=2):
            if pair in r and r[pair]:
                r[pair] = False
    return _PairRelationship('lr', set([k for k, v in r.items() if v]))


def _always_after(log: Bag, labels: list, start: str = "[>", end: str = "[]") -> _PairRelationship:
    """Pairs of activities, where if the former appears, the latter will appear
    surely afterwards.

    Returns
    -------
    set of pairs
    """

    if not isinstance(log, Bag):
        raise ValueError("Invalid Bag object.")

    r = {k: True for k in permutations(
        labels, r=2) if k[1] != start and k[0] != end}

    for trace in log:
        cur_succ = _succ(trace)
        for pair, value in r.items():
            if not value:
                continue
            if pair[0] in cur_succ and pair[1] not in cur_succ[pair[0]]:
                r[pair] = False

    r = set([k for k, v in r.items() if v])

    return _PairRelationship('lr', r)


def _always_before(log: Bag, labels: list, start: str = "[>", end: str = "[]") -> _PairRelationship:
    """Pairs of activities, where if the latter appears, the former has
    appeared already.

    Returns
    -------
    set of pairs
    """

    if not isinstance(log, Bag):
        raise ValueError("Invalid Bag object.")

    r = {k: True for k in permutations(
        labels, r=2) if k[0] != start and k[1] != end}

    for trace in log:
        cur_succ = _pred(trace)
        for pair, value in r.items():
            if not value:
                continue
            if pair[0] in cur_succ and pair[1] not in cur_succ[pair[0]]:
                r[pair] = False

    r = set([k for k, v in r.items() if v])

    return _PairRelationship('lr', r)


class Skeleton:

    def __init__(self, rels=None, stats=None):
        self.rels_ = rels
        self.stats_ = stats


def mine(log: Bag, labels: list = None, start="[>", end="[]") -> Skeleton:
    """Mine a log skeleton model from a log.

    Parameters
    ----------
    log: Bag
        Multi-set of traces.

    Examples
    --------
    >>> bag = pm.Bag({('a', 'b'): 4, ('c', 'd'): 2})
    >>> model = pm.skeleton.mine(bag)

    References
    ----------
    Verbeek, H., & de Carvalho, R. (2018). Log Skeletons: A Classification 
        Approach to Process Discovery. arXiv.org. Retrieved 14 February 2020,
        from https://arxiv.org/abs/1806.08247
    """

    if not isinstance(log, Bag):
        raise ValueError("Invalid Bag object.")

    log = log.augment(start, end)

    if labels is None:
        labels = log.labels()

    df_rel = log.to_dfg().edge_freq()

    # counters
    cs = {
        "depend": df_rel
    }
    cs["min"], cs["max"], cs["total"] = log.freqs()

    # relationships
    rels = {
        "depend": _PairRelationship('rl', set(cs["depend"].keys())),
        "equivalence": _equivalence(log, labels),
        "neverTogether": _never_together(log, labels),
        "alwaysAfter": _always_after(log, labels, start, end),
        "alwaysBefore": _always_before(log, labels, start, end)
    }

    return Skeleton(rels, cs)


def _subsume(skeleton: Skeleton, sigma: Skeleton) -> bool:
    keep = True
    for k, v in skeleton.rels_.items():
        if v.direction == "lr":
            for pair in v.pairs:
                if pair not in sigma.rels_[k].pairs:
                    keep = False
                    break

        if v.direction == "rl":
            for pair in sigma.rels_[k].pairs:
                if pair not in v.pairs:
                    keep = False
                    break

    return keep


def classify(log: Bag, traces: list, max_depth: int = 3) -> list:
    """Classify whether trace conforms to the event log.

    Parameters
    ----------
    log: Bag
        Base event log to compare against.

    traces: list-like
        List of traces (i.e. tuples of labels) to be classified.

    max-depth: int, default 3
        Max size of the filter sets (i.e. req. and fbd) to be used, to generate
        different versions of the log for classification. 

    Returns
    -------
    list of bool
        Truth values whether a trace was classified as belonging to the log or
        not.

    Examples
    --------
    >>> bag = pm.as_bag(pm.read_xes(os.path.join("B1.xes")))
    >>> traces = [("a1", "a4", "a5", "a7")]
    >>> pred = pm.skeleton.classify(bag, traces)
    >>> [False]


    References
    ----------
    Verbeek, H., & de Carvalho, R. (2018). Log Skeletons: A Classification 
        Approach to Process Discovery. arXiv.org. Retrieved 14 February 2020,
        from https://arxiv.org/abs/1806.08247
    """
    y = [True for _ in range(len(traces))]

    labels = log.labels()

    for req in _powerset(labels, max_depth):
        for fbd in _powerset(labels - set(req), max_depth):

            filtered_log = log.filter_traces(req, fbd)
            if len(filtered_log):
                skeleton = mine(filtered_log)

            for i, trace in enumerate(traces):
                if y[i]:
                    sigma = Bag({trace: 1}).filter_traces(req, fbd)
                    if not len(filtered_log) and not len(sigma):
                        continue
                    sigma_skeleton = mine(
                        sigma, filtered_log.augment().labels())
                    y[i] = _subsume(skeleton, sigma_skeleton)

    return y
