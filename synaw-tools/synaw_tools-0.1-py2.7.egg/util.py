"""
This module provides various utility functions  which do not implement business logic.
"""


def dict_compare(d1, d2):
    """
    Compare dictionaries.
    Source: https://stackoverflow.com/a/18860653/3433306

    Example: added, removed, modified, same = dict_compare(x, y)
    >>> a = {"a": "a"}
    >>> b = {"b": "b"}
    >>> dict_compare(a, b)
    ({'a'}, {'b'}, {}, set())

    :param d1: first dictionary
    :param d2: second dictionary
    :return: added (set), removed (set), modified (dict), same (dict)
    """
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o: (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
    same = set(o for o in intersect_keys if d1[o] == d2[o])
    return added, removed, modified, same


def dict_identical(d1, d2):
    """
    Compare dictionaries and check if they are identical.

    :param d1: first dictionary
    :param d2: second dictionary
    :return: boolean
    """
    added, removed, modified, same = dict_compare(d1, d2)
    return len(added) == 0 and len(removed) == 0 and len(modified) == 0
