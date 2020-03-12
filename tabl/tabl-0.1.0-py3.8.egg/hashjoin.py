#!/usr/bin/env python
"""
.. module:: tabl.hashjoin
.. moduleauthor:: Bastiaan Bergman <Bastiaan.Bergman@gmail.com>

"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from collections import defaultdict
import numpy as np
from .numpy_types import *                          # pylint: disable=wildcard-import
from .util import isstring

def arg_hash(arlst):
    """Return defaultdict with list of rownumbers
    """
    keylist = defaultdict(list)
    for i, elem in enumerate(zip(*(arlst))):
        keylist[elem].append(i)
    return keylist

def arg_left_join(tabl_l, index1, tabl_r, index2):
    """Join and return _column_indices
    """
    hash_r = arg_hash(tabl_r[:, index2].data)
    idx = np.array([(s, i) for i, r in enumerate(zip(*tabl_l[:, index1].data))
                    for s in hash_r.get(r, [-1])])
    return idx

def add_empty_row(tabl):
    """Add an empty row using the fill values to the end of an Tbl
    """
    empty_row = []
    for c in tabl.dtype.names:
        if tabl.dtype[c] in NP_FLOAT_TYPES:
            empty_row.append(tabl.join_fill_value['float'])
        if tabl.dtype[c].kind in {'U', 'S'}:
            empty_row.append(tabl.join_fill_value['string'])
        if tabl.dtype[c] in NP_INT_TYPES:
            empty_row.append(tabl.join_fill_value['integer'])
    try:
        tabl.row_append(empty_row)
        return tabl
    except ValueError:
        raise ValueError("Outer join cannot be fullfilled when there are other ",
                         "columns than float, string or integer because Tbl ",
                         "doesn't know what to fill it up with.")

def remove_empty_row(tabl):
    """Remove the last (emtpy) row of a Tbl, used for outer joins
    """
    tabl.data = [dt[0:-1] for dt in tabl.data]


class HashJoinMixin(object):
    """Mixin to add to the Tbl class, providing join and group_by methods
    """

    def _union(self, idx, key, tabl_r, key_r, jointype="inner", suffixes=("_l", "_r")):
        """Put together the final output based on indices.
        """
        col_l = [c for c in self.columns if c not in key]
        col_r = [c for c in tabl_r.columns if c not in key_r]

        if jointype in ("inner", "left"):
            columns = (key + [c+suffixes[0] for c in col_l] +
                       [c+suffixes[1] for c in col_r])
            col_l = key + col_l
        elif jointype == "outer":
            col_l = key + col_l
            col_r = key_r + col_r
            columns = ([c+suffixes[0] for c in col_l] +
                       [c+suffixes[1] for c in col_r])
        elif jointype == "right":
            columns = ([c+suffixes[0] for c in col_l] +
                       key_r + [c+suffixes[1] for c in col_r])
            col_r = key_r + col_r

        data = self[idx[:, 1], col_l].data + tabl_r[idx[:, 0], col_r].data
        return self.__class__(data, columns=columns)

    def _arg_inner_join(self, index1, tabl_r, index2):
        """Perform inner join and return row indices
        """
        hash_r = arg_hash(tabl_r[:, index2].data)
        return np.array([(s, i) for i, r in enumerate(zip(*self[:, index1].data))
                         for s in hash_r[r]])

    def _arg_outer_join(self, index1, tabl_r, index2):
        """Perform outer join and return indices
        """
        hash_l = arg_hash(self[:, index1].data)
        hash_r = arg_hash(tabl_r[:, index2].data)

        keys = set(hash_l.keys()).union(set(hash_r.keys()))

        def iter_join(h_l, h_r, join_keys):
            for join_key in join_keys:
                for elem in h_l.get(join_key, [-1]):
                    for other in h_r.get(join_key, [-1]):
                        yield (elem, other)
        idx = np.array(list(iter_join(hash_l, hash_r, keys)))
        return idx[:, [1, 0]]

    def join(self, tabl_r, key, key_r=None, jointype="inner", suffixes=('_l', '_r')):
        """dbase join tables with ind column(s) as the keys.

        Performs a database style joins on the two tables, the current instance
        and the provided tabl 'tabl_r' on the columns listed in 'key'.

        arguments:
            tabl_r (Tbl) :
                The right tabl to be joined.
            key (string or list) :
                Name of the column(s) to be used as the key(s).
            key_r (list) :
                A list of columnnames of the right tabl matching the left
                tabl. Defaults to the list provided in `ind`.
            jointype (str) :
                One of: `inner`, `left`, `right`, `outer`. If `inner`, returns
                the elements common to both tabls. If `outer`, returns the
                common elements as well as the elements of the left tabl not in
                the right tabl and the elements of the right tabl not in the
                left tabl. If `left`, returns the common elements and the
                elements of the left tabl not in the right tabl. If `right`,
                returns the common elements and the elements of the right tabl
                not in the left tabl.
            suffixes (tuple) :
                Strings to be added to the left and right tabl column names.

        returns:
            The joined tabl

        notes:
            The order and suffixes of the returned Tbl depend on the jointype.
            For all types, all but the key columns are suffixed with the left
            and the right suffix respectively. The left Tbl columns come first
            followed by the right Tbl columns, with the key column placed
            first of its Tbl columns. For `inner` and `left` jointypes the
            right key column is left out. for `right` jointype the left key
            column is left out. For the `outer` jointype both keys are present
            and suffixed.

        Examples:
            Join a Tbl into the current Tbl matching on column 'a':

            >>> tabl = Tbl({"a":list(range(4)), "b": ['a', 'b'] *2})
            >>> tabl_b = Tbl({"a":list(range(4)), "c": ['d', 'e'] *2})
            >>> tabl.join(tabl_b, "a")
               a | b_l   | c_r
            -----+-------+-------
               0 | a     | d
               1 | b     | e
               2 | a     | d
               3 | b     | e
            4 rows ['<i8', '<U1', '<U1']
        """
        key = key if not isstring(key) else [key]
        key_r = key if key_r is None else key_r

        if jointype == "inner":
            idx = self._arg_inner_join(key, tabl_r, key_r)
            return self._union(idx, key, tabl_r, key_r, jointype, suffixes)

        if jointype == "outer":
            idx = self._arg_outer_join(key, tabl_r, key_r)
            add_empty_row(self)
            add_empty_row(tabl_r)
            outp = self._union(idx, key, tabl_r, key_r, jointype, suffixes)
            remove_empty_row(self)
            remove_empty_row(tabl_r)
            return outp

        if jointype == "left":
            idx = arg_left_join(self, key, tabl_r, key_r)
            add_empty_row(tabl_r)
            outp = self._union(idx, key, tabl_r, key_r, jointype, suffixes)
            remove_empty_row(tabl_r)
            return outp

        if jointype == "right":
            idx = arg_left_join(tabl_r, key_r, self, key)
            idx = idx[:, [1, 0]]
            add_empty_row(self)
            outp = self._union(idx, key, tabl_r, key_r, jointype, suffixes)
            remove_empty_row(self)
            return outp
        raise NotImplementedError("No such jointype: {}".format(jointype))

    def group_by(self, key, aggregate_fie_col=None):
        """Groups and aggregates Tbl.

        Arguments:
            key (str or list) :
                name or list of names of the columns to be grouped by.

            aggregate_fie_col (list)
                list of tuples (`function`, `column`) where `function` is the
                function to be applied to aggregate and `column` is the string name
                of the column. `function` should take an 1D array as an input and
                the returned value is treated as a single element. Only the grouped
                columns of `key` are returned if ommited.

        Returns:
            Tbl object with requested columns

        Examples:
            grouping by 'a' and then by 'b', agregating with taking the sum of
            'a' elements and taking the first 'c' element of each group:

            >>> tabl = Tbl({'a':[10, 20, 30, 40]*3, 'b':["100", "200"]*6, 'c':[100, 200]*6})
            >>> from tabl import first
            >>> tabl.group_by(['b', 'a'], [ (np.sum, 'a'), (first, 'c')])
               b |   a |   a_sum |   c_first
            -----+-----+---------+-----------
             100 |  10 |      30 |       100
             200 |  20 |      60 |       200
             100 |  30 |      90 |       100
             200 |  40 |     120 |       200
            4 rows ['<U3', '<i8', '<i8', '<i8']

        """
        if aggregate_fie_col is None:
            aggregate_fie_col = list()
        key = key if not isstring(key) else [key]
        hash_groups = arg_hash(self[:, key].data)
        result = self.__class__()
        for group in hash_groups.values():
            row = {}
            row.update({k:v for k, v in zip(key, self[group[0], key])})
            for fie, col in aggregate_fie_col:
                row.update({col+"_"+fie.__name__:fie(self[group, col])})
            result.row_append(row)
        return result

def first(array):
    """
    Get the first element when doing a :mod:`tabl.Tbl.group_by`.

    Arguments :
        array (numpy ndarray) :
            numpy 1D array containing the subset of elements

    Returns :
        The first element of ar

    Examples :
        See Tbl.group_by for examples

    """
    return array[0] if len(array) > 0 else None
