from collections import Counter, namedtuple

import pandas as pd
import networkx as nx

from .utils import _base_dict, _freqs
from .dfgraph import DFGraph

_LabelFreqs = namedtuple('LabelFreqs', ['min', 'max', 'total'])


class Bag(Counter):

    def __init__(self, iterable=None, **kwds):
        """Create a new, empty Bag object.  And if given, count elements
        from an input iterable.  Or, initialize the count from another mapping
        of elements to their counts.

        Examples
        --------
        >>> b = pm.Bag()                               # a new, empty bag
        # a new bag from an iterable
        >>> b = pm.Bag([('a', 'b'), ('c', 'd')])
        # a new bag from a mapping
        >>> b = pm.Bag({('a', 'b'): 4, ('c', 'd'): 2})
        # a new bag from keyword args
        >>> b = pm.Bag(('a', 'b')=4, ('c', 'd')=2)
        """
        super(Counter, self).__init__()
        self.update(iterable, **kwds)

    def augment(self, start="[>", end="[]") -> "Bag":
        """Augment each trace in a bag with a start and end activity.

        Parameters
        ----------
        start: str, default '[>'
            Start activity label.

        end: str, default '[]'
            End activity label.

        Returns
        -------
        Bag
            Augmented multi-set of traces.

        Examples
        --------
        >>> bag = pm.Bag({('a', 'b'): 4, ('c', 'd'): 2})
        >>> bag.augment()
        Bag({('[>', 'a', 'b', '[]'): 4, ('[>', 'c', 'd', '[]'): 2})


        >>> bag = pm.Bag({('a', 'b'): 4, ('c', 'd'): 2})
        >>> bag.augment(start="<s>", end="</s>")
        Bag({('<s>', 'a', 'b', '</s>'): 4, ('<s>', 'c', 'd', '</s>'): 2})
        """
        a = {}
        for trace, freq in self.items():
            _trace = (start, ) + trace + (end, )
            a[_trace] = freq
        return Bag(a)

    def labels(self) -> set:
        """Label or activity names of the traces.

        Returns
        -------
        set of names

        Examples
        --------
        >>> bag = pm.Bag({('a', 'b'): 4, ('c', 'd'): 2})
        >>> bag.labels()
        {'a', 'b', 'c', 'd'}
        """
        l = set()
        for trace in self.keys():
            for a in trace:
                l.add(a)
        return l

    def freqs(self) -> _LabelFreqs:
        """Frequency statistics of labels in traces.

        Returns
        -------
        LabelFreqs
            Minima, maxima of label in a trace and total count of label in log.

        Examples
        --------
        >>> bag = pm.Bag({('a', 'b'): 4, ('c', 'd'): 2})
        >>> bag.freqs()
        LabelFreqs(
        ... min={'a': 0, 'd': 0, 'b': 0, 'c': 0},
        ... max={'a': 1, 'd': 1, 'b': 1, 'c': 1},
        ... total={'a': 4, 'd': 2, 'b': 4, 'c': 2}
        )
        """
        l = self.labels()
        _base = _base_dict(l, 0)
        c_min, c_max = _base_dict(l, float('inf')), _base_dict(l, 0),
        c_total = _base_dict(l, 0)

        for trace, freq in self.items():
            c = _base.copy()
            c.update(_freqs(trace))
            c_total = {k: c[k] * freq + c_total[k] for k in l}
            c_min = {k: min(c[k], c_min[k]) for k in l}
            c_max = {k: max(c[k], c_max[k]) for k in l}

        return _LabelFreqs(c_min, c_max, c_total)

    def to_dfg(self) -> dict:
        """Directly follows graph w/ arc frequency.

        Mine a directly follows (aka. dependency) graph as a dict, where the
        keys are pairs of arcs and the values their frequency.

        Returns
        -------
        dict
            Keys are pairs of arcs and the values their frequency in a directly
            follows graph.

        Examples
        --------
        >>> bag = pm.Bag({('a', 'b'): 4, ('c', 'd'): 2})
        >>> bag.to_dfg()
        DFGraph(nodes=['a', 'b', 'c', 'd'], arcs=[('a', 'b'): 4, ('c', 'd'): 2])
        

        References
        ----------
        Mining, A., Ferreira, D. and Publishing, S. Mining, A., Ferreira, D., &
            Publishing, S. (2020). A Primer on Process Mining - Practical 
            Skills with Python and Graphviz | Diogo R. Ferreira 
        """
        d = dict()
        s, e = set(), set()
        eps = 0

        for trace, freq in self.items():
            if len(trace) > 0:
                s.add(trace[0])
                e.add(trace[-1])

                for i in range(len(trace) - 1):
                    pair = trace[i], trace[i+1]
                    if pair not in d:
                        d[pair] = 0
                    d[pair] += 1 * freq
            else:
                eps += freq
                
        G = DFGraph(self.labels(), [[u, v, w] for (u, v), w in d.items()], s, e, eps)

        return G

    def filter_labels(self, labels: list = None) -> "Bag":
        """Filter the labels of every trace.

        Parameters
        ----------
        labels: list of names
            Labels keep in each trace.

        Returns
        -------
        Bag
            Multi-set of traces.
            
        Examples
        --------
        >>> bag = pm.Bag({('a', 'b'): 4, ('c', 'd'): 2})
        >>> pm.bag.filter_labels(['a']])
        pm.Bag({('a',): 4, (): 2})
        """
        if labels is None:
            return self.copy()
        
        # Single Item
        if isinstance(labels, str):
            labels = [labels]

        L = Bag()        
        for trace, freq in self.items():
            subtrace = tuple(a for a in trace if a in labels)
            if subtrace not in L:
                L[subtrace] = 0
            L[subtrace] += freq

        return L

    def filter_traces(self, req: list = None, fbd: list = None) -> "Bag":
        """Filter a bags traces based on required and forbidden labels.

        Parameters
        ----------
        req: list of names
            Labels required in a trace.

        fbd: list of names
            Labels forbidden in a trace.

        Returns
        -------
        Bag
            Multi-set of traces.

        Examples
        --------
        >>> bag = pm.Bag({('a', 'b'): 4, ('c', 'd'): 2})
        >>> pm.bag.filter_bag(bag, req=['a'])
        pm.Bag({('a', 'b'): 4})
        
        >>> bag = pm.Bag({('a', 'b'): 4, ('c', 'd'): 2})
        >>> pm.bag.filter_bag(bag, fbd=['a'])
        pm.Bag({('c', 'd'): 2})
        """
        if req is None:
            req = []

        if fbd is None:
            fbd = []

        filtered = self.copy()

        for a in req:
            for trace in self.keys():
                if a not in trace:
                    if trace in filtered:
                        del filtered[trace]
            
        for a in fbd:
            for trace in self.keys():
                if a in trace:
                    if trace in filtered:
                        del filtered[trace]
        
        return filtered

def as_bag(df: pd.DataFrame, case="T_concept:name", time=None, activity="E_concept:name") -> Bag:
    """Convert the input to a bag (multi-set of traces).

    Parameters
    ----------
    df: pandas DataFrame
        A valid log as a DataFrame object. Expected to have at least features 
        for:

        * cases ID: Feature to uniquly identify an event belonging to a trace.
        * timestamp: Timestamp to sort the events chronologically.
        * activity: The activity describing the event.

    case: name, default 'T_concept:name'
        Column name of the DataFrame to associate events to a trace and sort
        by.

    time: name, default `None`
        Column name of the DataFrame repesenting a timestamp to sort by. If
        None sorting is assumed.

    activity: name, default 'E_Activity'
        Column name of the DataFrame describing an event.

    Returns
    -------
    Bag
        Multi-set of traces.

    Examples
    --------
    >>> df = pm.read_xes('data.xes') # doctest: +SKIP
    ... log = pm.as_bag(df)
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input has to be a pandas DataFrame.")

    if time is not None:
        df = df.sort_values([case, time], kind="mergesort")
    else:
        df = df.sort_values([case], kind="mergesort")

    _groupby_df = df.groupby(case)[activity].agg(
        lambda x: tuple(x.tolist()))

    _traces = _groupby_df.values.tolist()

    return Bag(_traces)


