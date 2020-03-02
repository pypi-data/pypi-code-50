# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import numpy as np
from ezcad.utils.functions import table2array
from ezcad.utils.convert_grid import ln2xy
from ..line import Line


def from_point(point, line_name, is_closed):
    """Create line from point.

    :param point: input point object
    :type point: :class:`~ezcad.gopoint.point.Point`
    :param line_name: name of the new line object
    :type line_name: str
    :param is_closed: is the line closed
    :type is_closed: bool
    :return: a line object
    :rtype: :class:`~ezcad.goline.line.Line`
    """
    dob = Line(line_name)
    dob.set_atom_style(point.atom_style)
    dob.set_line_style()
    if is_closed:
        dob.line_style['closed'] = True
    else:
        dob.line_style['closed'] = False

    for prop_name in point.prop:
        array = point.prop[prop_name][point.prop_array_key]
        newArray = np.copy(array)
        clip = point.prop[prop_name]['colorClip']
        gradient = point.prop[prop_name]['colorGradient']
        dob.add_property(prop_name, array=newArray, clip=clip,
                         gradient=gradient)
    dob.set_current_property(prop_name=point.current_property)
    dob.set_vertexes(np.copy(point.vertexes['xyz']))

    connect = dob.make_connect()
    dob.set_connect(connect)
    segment = dob.make_segment()
    dob.set_segment(segment)
    # dob.make_vs2d()
    # dob.make_vs3d()
    return dob


def from_coordinate(name, comment, delimiter, method, text, survey=None):
    """Create line from coordinate.

    :param name: name of the new object
    :type name: str
    :param comment: character denoting comment line
    :type comment: char
    :param delimiter: delimiter for columns
    :type delimiter: str
    :param method: coordinate method, xy or ln
    :type method: str
    :param text: text of the data table, usually from GUI text box
    :type text: str
    :param survey: survey, used to convert LN to XY
    :type survey: :class:`~ezcad.gosurvey.survey.Survey`
    :return: a line object
    :rtype: :class:`~ezcad.goline.line.Line`
    """
    dataArray = table2array(text, comment, delimiter)
    # TODO include properties
    if dataArray.shape[1] != 4:
        raise ValueError("Must have 4 columns")
    if method == 'ln':
        if survey is None:
            raise ValueError("Need survey to get line numbers to XYs")
        dataXy = ln2xy(dataArray, survey=survey)
        dataArray[:, 0] = dataXy[:, 0]
        dataArray[:, 1] = dataXy[:, 1]
    propList = ['X', 'Y', 'Z', 'Connect']
    dob = init_dob(name, propList, dataArray)
    return dob


def copy_object(line, name):
    """Copy a line object.

    :param line: input line object
    :type line: :class:`~ezcad.goline.line.Line`
    :param name: name of the new object
    :type name: str
    :return: a line object
    :rtype: :class:`~ezcad.goline.line.Line`
    """
    dob = Line(name)
    dob.set_atom_style(line.atom_style)
    dob.set_line_style(line.line_style)
    for prop_name in line.prop:
        array = line.prop[prop_name][line.prop_array_key]
        newArray = np.copy(array)
        clip = line.prop[prop_name]['colorClip']
        gradient = line.prop[prop_name]['colorGradient']
        dob.add_property(prop_name, array=newArray, clip=clip,
                         gradient=gradient)
    dob.set_current_property(prop_name=line.current_property)
    dob.set_vertexes(np.copy(line.vertexes['xyz']))
    dob.set_connect(np.copy(line.vertexes['connect']))
    dob.set_segment(np.copy(line.vertexes['segment']))
    dob.set_xyz_range()
    return dob


def init_dob_from_dframe(name, dataframe):
    """Create line from dataframe.
    It calls function :func:`~ezcad.goline.new.new.init_dob`.

    :param name: name of the new object
    :type name: str
    :param dataframe: a Pandas dataframe
    :type dataframe: dataframe
    :return: a line object
    :rtype: :class:`~ezcad.goline.line.Line`
    """
    props = dataframe.columns
    data_array = dataframe.values
    dob = init_dob(name, props, data_array)
    return dob


def init_dob(object_name, props, data_array):
    """Create line, base function.

    :param object_name: name of the new object
    :type object_name: str
    :param props: name of the properties
    :type props: list
    :param data_array: data array
    :type data_array: array
    :return: a line object
    :rtype: :class:`~ezcad.goline.line.Line`
    """
    dob = Line(object_name)
    dob.set_atom_style()
    dob.set_line_style()
    dob.init_property(props, data_array)
    dob.set_axes()
    dob.set_vertexes()

    conn = 'Connect'
    if conn in props:
        # More than 1 segments, defined by connection
        index = props.index(conn)
        connect = data_array[:, index]
    else:
        # Only 1 segment in the line
        connect = dob.make_connect()
    dob.set_connect(connect)
    segment = dob.make_segment()
    dob.set_segment(segment)
    # dob.make_pg2d()
    # dob.make_pg3d()
    # dob.make_vs2d()
    # dob.make_vs3d()
    dob.set_xyz_range()
    return dob
