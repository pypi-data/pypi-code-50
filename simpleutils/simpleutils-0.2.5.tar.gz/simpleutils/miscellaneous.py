# -*- coding: utf-8 -*-
"""
Created on 2017-5-7

@author: cheng.li
"""

import sys
import os
from simpleutils.time import (
    dt2unix,
    unix2dt,
    to_datetime
)


def add_parent_path(name: str, level: int):
    """
    Add the target folder to the python search path

    :param name: str, file name
    :param level: int, how many level of parents folder should go up
    :return:
    """
    current_path = os.path.abspath(name)
    sys.path.append(os.path.sep.join(current_path.split(os.path.sep)[:-level]))


def list_eq(lhs: list, rhs: list):
    """
    Check the equality of 2 lists

    :param lhs: list
    :param rhs: list
    :return: bool
    """

    if not lhs and not rhs:
        return True

    if len(lhs) != len(rhs):
        return False

    for i, v1 in enumerate(lhs):
        if v1 != rhs[i]:
            return False
    return True
