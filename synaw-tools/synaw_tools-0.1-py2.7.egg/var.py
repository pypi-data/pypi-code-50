"""
This module provides functions for manipulating configuration variables as dictionaries.
"""


def copy_item(item):
    """
    Copy the item using its copy() function.
    Return item if it does not have a copy function.

    :param item: the item to be copied
    :return: the copied item
    """

    copy_function = getattr(item, "copy", None)
    if callable(copy_function):
        return item.copy()
    else:
        return item


def merge_elements(_a, _b, merge_lists=False, merge_dicts=True, ignored_elements=[]):
    """
    Merge b into a.
    Values in b override values in a if they cannot be merged.

    :param _a: first dictionary
    :param _b: second dictionary
    :param merge_lists: merge arrays (True) or replace arrays (False) - default: False
    :param merge_dicts: merge dicts (True) or replace dicts (False) - default: True
    :param ignored_elements: the list of elements to ignore
    :return: merged dict
    """

    a = copy_item(_a)
    b = copy_item(_b)

    if isinstance(a, dict) and isinstance(b, dict) and merge_dicts:
        for key in b:
            if key in ignored_elements:
                continue

            if key in a:
                a[key] = merge_elements(a[key], b[key], merge_lists, merge_dicts, ignored_elements)
            else:
                a[key] = b[key]

    elif isinstance(a, list) and isinstance(b, list) and merge_lists:
        a = a + b

    else:
        a = b

    return a


def raise_elements(_a, elements, ignored_elements=[]):
    """
    Raise dictionary items up if in list of elements.
    Dictionaries in lists are raised as well.

    :param _a: the dictionary
    :param elements: the list of elements to raise
    :param ignored_elements: the lis tof elements to ignore
    :return: dictionary with raised elements
    """

    a = copy_item(_a)

    if isinstance(a, dict):
        keys = a.keys()

        for key in keys:
            if key not in a or key in ignored_elements:
                continue

            a[key] = raise_elements(a[key], elements)

            if key in elements:
                a = merge_elements(a, a[key])

    elif isinstance(a, list):
        new_a = []
        for item in a:
            new_a.append(raise_elements(item, elements))
        a = new_a

    return a
