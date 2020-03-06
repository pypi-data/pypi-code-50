# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import os
import pandas as pd
from .read_gocad_pline import read_gocad_pline
from ..line import Line
from ..new.new import init_dob_from_dframe


def load_gocad_pline(fufn, object_name=None, columns=None):
    """Load Gocad pline.

    :param fufn: full-path filename
    :type fufn: str
    :param object_name: name of the new object
    :type object_name: str
    :param columns: column number and name, e.g. 1,step;2,loss.
      It is not used for now.
    :type columns: str
    :return: a line object
    :rtype: :class:`~ezcad.goline.line.Line`
    """
    # read file
    prop_names, arrayVertexes, connect, segment = \
        read_gocad_pline(fufn)
    vertexes = arrayVertexes[:, 0:3]  # the first 3 columns for XYZ
    if object_name is None:
        path, fn = os.path.split(fufn)
        object_name = os.path.splitext(fn)[0]
    dob = Line(object_name, connect)
    dob.set_atom_style()
    dob.set_line_style()
    dob.set_vertexes(vertexes)
    dob.set_segment(segment)
    dob.init_property(prop_names, arrayVertexes)
    dob.set_xyz_range()
    return dob


def load_line_csv(fufn, object_name=None):
    """Load CSV file (comma-separated values).
    Format definition.
    The CSV file must have a header row as the first line.
    It must have ('X', 'Y', 'Z') at minimum in the header line.
    If it has the column named "Connect", the column has values of 0
    and 1. The 0 means this point (at the same line/row) is break from
    the next point, and the 1 means it is connected.
    If it does not have the column named "Connect", it connects the first
    to the last point.

    :param fufn: full-path filename
    :type fufn: str
    :param object_name: name of the new object
    :type object_name: str
    :return: a line object
    :rtype: :class:`~ezcad.goline.line.Line`
    """
    # read file with pandas
    dataframe = pd.read_csv(fufn, skipinitialspace=True)
    path, fn = os.path.split(fufn)
    if object_name is None:
        object_name = os.path.splitext(fn)[0]
    dob = init_dob_from_dframe(object_name, dataframe)
    return dob
