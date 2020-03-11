"""
This module provides functions for manipulating configuration variables as dictionaries.
"""
from .util import get_logger


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


def merge_elements(_item_a, _item_b, merge_lists=False, merge_dicts=True, ignored_elements=None):
    """
    Merge item_b into item_a.
    Values in item_b override values in item_a if they cannot be merged.

    :param _item_a: first dictionary
    :param _item_b: second dictionary
    :param merge_lists: merge arrays (True) or replace arrays (False) - default: False
    :param merge_dicts: merge dicts (True) or replace dicts (False) - default: True
    :param ignored_elements: the list of elements to ignore
    :return: merged dict
    """

    if ignored_elements is None:
        ignored_elements = []

    item_a = copy_item(_item_a)
    item_b = copy_item(_item_b)

    if isinstance(item_a, dict) and isinstance(item_b, dict) and merge_dicts:
        for key in item_b:
            if key in ignored_elements:
                continue

            if key in item_a:
                item_a[key] = merge_elements(item_a[key], item_b[key],
                                             merge_lists, merge_dicts, ignored_elements)
            else:
                item_a[key] = item_b[key]

    elif isinstance(item_a, list) and isinstance(item_b, list) and merge_lists:
        item_a = item_a + item_b

    else:
        item_a = item_b

    return item_a


def raise_elements(_item_a, elements, ignored_elements=None):
    """
    Raise dictionary items up if in list of elements.
    Dictionaries in lists are raised as well.

    :param _item_a: the dictionary
    :param elements: the list of elements to raise
    :param ignored_elements: the lis tof elements to ignore
    :return: dictionary with raised elements
    """

    logger = get_logger("var/raise_elements")

    if ignored_elements is None:
        ignored_elements = []

    logger.debug("Raising elements %s in %s (ignoring %s)...", elements, _item_a, ignored_elements)

    item_a = copy_item(_item_a)

    if isinstance(item_a, dict):
        logger.debug("Processing item %s as dict...", item_a)

        keys = item_a.keys()
        logger.debug("Found dict keys: %s", keys)

        for key in keys:
            if not isinstance(item_a, dict) or key not in item_a or key in ignored_elements:
                continue

            item_a[key] = raise_elements(item_a[key], elements)

            if key in elements:
                item_a = merge_elements(item_a, item_a[key])

    elif isinstance(item_a, list):
        logger.debug("Processing item %s as list...", item_a)
        new_a = []
        for item in item_a:
            new_a.append(raise_elements(item, elements))
        item_a = new_a

    logger.debug("Returning leaf value %s...", item_a)
    return item_a
