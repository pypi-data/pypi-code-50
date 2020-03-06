# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""
This module loads points from file, by steps:
    1) read files of different formats,
    2) make and initialize Point data object,
    3) return the data object dob.
"""

import os
import numpy as np
import pandas as pd
from ezcad.utils.envars import DELIMITER2CHAR
from ..new.new import init_dob, init_dob_from_dframe
from .ss_header_dump import read_chd
from .space_delimited import read_sdt
from .read_gocad_vset import read_gocad_vset


def load_gocad_vset(fufn, object_name=None, columns=None):
    """Load Gocad vset.

    :param fufn: full-path filename
    :type fufn: str
    :param object_name: name of the new object
    :type object_name: str
    :param columns: column number and name, e.g. 1,step;2,loss
    :type columns: str
    :return: a point object
    :rtype: :class:`~ezcad.gopoint.point.Point`
    """
    prop_names, vertexes = read_gocad_vset(fufn, columns=columns)
    if object_name is None:
        path, fn = os.path.split(fufn)
        object_name = os.path.splitext(fn)[0]
    dob = init_dob(object_name, prop_names, vertexes)
    return dob


def load_point_csv(fufn, object_name=None):
    """Load CSV file (comma-separated values).

    :param fufn: full-path filename
    :type fufn: str
    :param object_name: name of the new object
    :type object_name: str
    :return: a point object
    :rtype: :class:`~ezcad.gopoint.point.Point`
    """
    # synthesize data
    # fufn = '/test/example.csv'
    # dataFrame = pd.DataFrame(np.random.randn(100,3), columns=['X','Y','Z'])

    # read data with pandas
    dataFrame = pd.read_csv(fufn, skipinitialspace=True, comment='#')
    if object_name is None:
        path, fn = os.path.split(fufn)
        object_name = os.path.splitext(fn)[0]
    dob = init_dob_from_dframe(object_name, dataFrame)
    return dob


def load_point_chd(fufn, object_name=None, skip_lines=-1):
    """Load SeisSpace custom header dump file.

    :param fufn: full-path filename
    :type fufn: str
    :param object_name: name of the new object
    :type object_name: str
    :param skip_lines: number of lines to skip
    :type skip_lines: int
    :return: a point object
    :rtype: :class:`~ezcad.gopoint.point.Point`
    """
    dataFrame = read_chd(fufn, skip_lines=skip_lines)
    if object_name is None:
        path, fn = os.path.split(fufn)
        object_name = os.path.splitext(fn)[0]
    dob = init_dob_from_dframe(object_name, dataFrame)
    return dob


def load_point_sdt(fufn):
    """Load space-delimited text file.
    The object name defaults to the file name.

    :param fufn: full-path filename
    :type fufn: str
    :return: a point object
    :rtype: :class:`~ezcad.gopoint.point.Point`
    """
    data_frame = read_sdt(fufn)
    path, fn = os.path.split(fufn)
    object_name = os.path.splitext(fn)[0]
    dob = init_dob_from_dframe(object_name, data_frame)
    return dob


def load_numpy(fn, comment, delim, props, object_name):
    delimiter = DELIMITER2CHAR[delim]
    dataArray = np.loadtxt(fn, comments=comment, delimiter=delimiter)
    propList = props.split(',')
    propList = [x.strip() for x in propList]
    dob = init_dob(object_name, propList, dataArray)
    return dob
