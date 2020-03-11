"""
This module provides various utility functions  which do not implement business logic.
"""

####################################################################################################
# global imports
####################################################################################################
import argparse
import inspect
from logging import Logger, getLogger
from sys import exit as ext


####################################################################################################
# util functions
####################################################################################################


####################################################################################################
# exit_with_error
# --------------------------------------------------------------------------------------------------


def exit_with_error(logger: Logger, message: str, return_code: int = 0):
    """
    Exit the application with an error message and error code.

    :param return_code: the code to return
    :param logger: the logger to log to
    :param message: the message to log
    :return: status code
    """
    logger.critical(message)
    ext(return_code)


####################################################################################################
# exit_with_error
# --------------------------------------------------------------------------------------------------
def exit_clean(logger: Logger, message: str = "Done.", return_code: int = 0):
    """
    Exit the application with an error message and error code.

    :param return_code: the code to return
    :param logger: the logger to log to
    :param message: the message to log
    :return: status code
    """
    logger.debug(message)
    ext(return_code)


####################################################################################################
# exit_with_error
# --------------------------------------------------------------------------------------------------
def get_logger(name: str = None):
    if name is None:
        stack = inspect.stack()
        fct_stack = [stack[x][3] for x in range(2, len(stack))]
        formatted_fct_stack = str("/".join(reversed(fct_stack)))
        logger = getLogger(formatted_fct_stack)
    else:
        logger = getLogger(name)
    return logger


####################################################################################################
# dict_compare
# --------------------------------------------------------------------------------------------------
def dict_compare(dict_1: dict, dict_2: dict):
    """
    Compare dictionaries.
    Source: https://stackoverflow.com/a/18860653/3433306

    Example: added, removed, modified, same = dict_compare(x, y)
    >>> a = {"a": "a"}
    >>> b = {"b": "b"}
    >>> dict_compare(a, b)
    ({'a'}, {'b'}, {}, set())

    :param dict_1: first dictionary
    :param dict_2: second dictionary
    :return: added (set), removed (set), modified (dict), same (dict)
    """
    d1_keys = set(dict_1.keys())
    d2_keys = set(dict_2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o: (dict_1[o], dict_2[o]) for o in intersect_keys if dict_1[o] != dict_2[o]}
    same = set(o for o in intersect_keys if dict_1[o] == dict_2[o])
    return added, removed, modified, same


####################################################################################################
# dict_identical
# --------------------------------------------------------------------------------------------------
def dict_identical(dict_1: dict, dict_2: dict):
    """
    Compare dictionaries and check if they are identical.

    :param dict_1: first dictionary
    :param dict_2: second dictionary
    :return: boolean
    """
    added, removed, modified, same = dict_compare(dict_1, dict_2)
    return len(added) == 0 and len(removed) == 0 and len(modified) == 0


####################################################################################################
# util classes
####################################################################################################


####################################################################################################
# AliasedSubParsersAction
# --------------------------------------------------------------------------------------------------
class AliasedSubParsersAction(argparse._SubParsersAction):
    """
    Source: https://gist.github.com/sampsyo/471779
    """

    class _AliasedPseudoAction(argparse.Action):
        def __init__(self, name, aliases, help):
            dest = name
            if aliases:
                dest += ' (%s)' % ','.join(aliases)
            sup = super(AliasedSubParsersAction._AliasedPseudoAction, self)
            sup.__init__(option_strings=[], dest=dest, help=help)

    def add_parser(self, name, **kwargs):
        if 'aliases' in kwargs:
            aliases = kwargs['aliases']
            del kwargs['aliases']
        else:
            aliases = []

        parser = super(AliasedSubParsersAction, self).add_parser(name, **kwargs)

        # Make the aliases work.
        for alias in aliases:
            self._name_parser_map[alias] = parser
        # Make the help text reflect them, first removing old help entry.
        if 'help' in kwargs:
            help = kwargs.pop('help')
            self._choices_actions.pop()
            pseudo_action = self._AliasedPseudoAction(name, aliases, help)
            self._choices_actions.append(pseudo_action)

        return parser
