from collections import defaultdict
from itertools import chain, combinations


def _base_dict(labels, value):
    return dict(zip(list(labels), [value for i in labels]))

def _freq2activity(trace: tuple) -> dict:
    a2f = _freqs(trace)
    f2a = defaultdict(list)
    for k, v in sorted(a2f.items()):
        f2a[v].append(k)
    return f2a

def _freqs(trace, freq=1):
    """Frequency of each label a trace.

    Parameters
    ----------
    trace: tuple of names

    freq: int
        Frequency of the given trace. A trace ("a", "b", "a", "c") w/ trace
        frequency of 3 would return the following frequency count:

        * a: 6
        * b: 3
        * c: 3

    Returns
    -------
    dict
        Frequency count of labels in trace.
    """
    freqs = {}
    for a in trace:
        if a not in freqs:
            freqs[a] = 0
        freqs[a] += 1 * freq
    return freqs


def _succ(trace):
    succ = defaultdict(set)
    for i, a in enumerate(trace):
        if i + 1 < len(trace):
            succ[a].update(x for x in set(trace[i+1:]) if a != x)
    return succ

def _pred(trace):
    pred = defaultdict(set)
    for i, a in enumerate(trace):
        if i > 0:
            pred[a].update(x for x in set(trace[:i]) if a != x)
    return pred

def _powerset(iterable, sz):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(sz + 1))