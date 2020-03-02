# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""
This module creates points.
"""

import numpy as np
from ezcad.utils.envars import COORDINATE_PROPERTY_NAMES
from ezcad.utils.functions import table2array
from ezcad.utils.convert_grid import ln2xy
from ..point import Point


def from_random_numbers(name='random', nvtx=1000, mean=0.0, std=1.0):
    """Create point from random numbers.

    :param name: name of the new object
    :type name: str
    :param nvtx: number of vertexes
    :type nvtx: int
    :param mean: mean of the random numbers
    :type mean: float
    :param std: standard deviation of the random numbers
    :type std: float
    :return: a point object
    :rtype: :class:`~ezcad.gopoint.point.Point`
    """
    props = COORDINATE_PROPERTY_NAMES
    data_array = np.random.normal(mean, std, (nvtx, 3))
    dob = from_data_array(data_array, props, name)
    return dob


def from_coordinate(name, comment, delimiter, method, text, survey=None):
    """Create point from coordinate.

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
    :return: a point object
    :rtype: :class:`~ezcad.gopoint.point.Point`
    """
    data_raw = table2array(text, comment, delimiter)
    nrow, ncol = data_raw.shape
    data_array = np.zeros((nrow, 3))
    # TODO include properties
    if ncol > 3:
        raise ValueError("Must have <= 3 columns")
    # maybe 3 columns XYZ, maybe 2 columns XY
    for j in range(ncol):
        data_array[:, j] = data_raw[:, j]
    if method == 'ln':
        if survey is None:
            raise ValueError("Need survey to get line numbers to XYs")
        data_xy = ln2xy(data_raw, survey=survey)
        data_array[:, 0] = data_xy[:, 0]
        data_array[:, 1] = data_xy[:, 1]
    props = COORDINATE_PROPERTY_NAMES
    dob = from_data_array(data_array, props, name)
    return dob


def from_data_array(data_array, props=None, object_name=None):
    """Create point from data array.
    It calls function :func:`~ezcad.gopoint.new.new.init_dob`.

    :param data_array: data array
    :type data_array: array
    :param props: name of the properties
    :type props: list
    :param object_name: name of the new object
    :type object_name: str
    :return: a point object
    :rtype: :class:`~ezcad.gopoint.point.Point`
    """
    if props is None:
        props = COORDINATE_PROPERTY_NAMES
    if object_name is None:
        object_name = "New_point"
    dob = init_dob(object_name, props, data_array)
    return dob


def subset_from_prop_range(point, prop_name, vmin=None, vmax=None):
    """Create point from an existing object by property range.

    :param point: input point object
    :type point: :class:`~ezcad.gopoint.point.Point`
    :param prop_name: name of the conditional property
    :type prop_name: str
    :param vmin: minimum value
    :type vmin: float
    :param vmax: maximum value
    :type vmax: float
    :return: a point object
    :rtype: :class:`~ezcad.gopoint.point.Point`
    """
    prop_array = point.prop[prop_name][point.prop_array_key]
    if vmin is None:
        vmin = np.amin(prop_array)
    if vmax is None:
        vmax = np.amax(prop_array)
    condition = np.where(np.logical_and(prop_array>=vmin, prop_array<=vmax))

    name = point.name + '_pt'
    dob = Point(name)
    dob.set_atom_style(point.atom_style)
    for prop_name in point.prop:
        array = point.prop[prop_name][point.prop_array_key]
        newArray = array[condition]
        gradient = point.prop[prop_name]['colorGradient']
        dob.add_property(prop_name, array=newArray, gradient=gradient)
    dob.set_current_property(prop_name=point.current_property)
    dob.set_vertexes(point.vertexes['xyz'][condition])
    dob.set_xyz_range()
    # dob.make_pg2d()
    # dob.make_pg3d()
    return dob


def copy_object(point, name):
    """Copy a point object.

    :param point: input point object
    :type point: :class:`~ezcad.gopoint.point.Point`
    :param name: name of the new object
    :type name: str
    :return: a point object
    :rtype: :class:`~ezcad.gopoint.point.Point`
    """
    dob = Point(name)
    dob.set_atom_style(point.atom_style)
    for prop_name in point.prop:
        array = point.prop[prop_name][point.prop_array_key]
        newArray = np.copy(array)
        clip = point.prop[prop_name]['colorClip']
        gradient = point.prop[prop_name]['colorGradient']
        dob.add_property(prop_name, array=newArray, clip=clip, gradient=gradient)
    dob.set_current_property(prop_name=point.current_property)
    dob.set_vertexes(np.copy(point.vertexes['xyz']))
    dob.set_xyz_range(np.copy(point.xyz_range))
    return dob


def init_dob_from_dframe(name, dataframe):
    """Create point from dataframe.
    It calls function :func:`~ezcad.gopoint.new.new.init_dob`.

    :param name: name of the new object
    :type name: str
    :param dataframe: a Pandas dataframe
    :type dataframe: dataframe
    :return: a point object
    :rtype: :class:`~ezcad.gopoint.point.Point`
    """
    props = dataframe.columns
    data_array = dataframe.values
    dob = init_dob(name, props, data_array)
    return dob


def init_dob(object_name, props, data_array):
    """Create point, base function.

    :param object_name: name of the new object
    :type object_name: str
    :param props: name of the properties
    :type props: list
    :param data_array: data array
    :type data_array: array
    :return: a point object
    :rtype: :class:`~ezcad.gopoint.point.Point`
    """
    dob = Point(object_name)
    dob.init_property(props, data_array)

    axes = find_xyz_in_list(props)
    dob.set_axes(axes)
    dob.set_vertexes()
    dob.set_current_property()
    dob.set_xyz_range()

    # NOT make plot here, instead when the first time add to viewer,
    # then make appropriate plot depending on the current viewer type.
    # dob.make_pg2d()
    # dob.make_pg3d()
    return dob


def find_xyz_in_list(props):
    """Find XYZ from a list of properties.
    Intelligently select possible XYZ columns.

    :param props: name of the properties
    :type props: list
    :returns: property names for XYZ
    :rtype: tuple
    """
    # default column number for XYZ
    if len(props) == 0:
        raise ValueError("List is empty.")
    elif len(props) == 1:
        colno_x, colno_y, colno_z = 0, 0, 0
    elif len(props) == 2:
        colno_x, colno_y, colno_z = 0, 1, 0
    elif len(props) >= 3:
        colno_x, colno_y, colno_z = 0, 1, 2
    else:
        raise ValueError("Unknown value")

    props_lc = [x.lower() for x in props]
    prefx = ['x', 'cdp_x', 'rec_x', 'sou_x', 's_id_sx']
    for x in prefx:
        if x in props_lc:
            colno_x = props_lc.index(x)
            break
    prefy = ['y', 'cdp_y', 'rec_y', 'sou_y', 's_id_sy']
    for y in prefy:
        if y in props_lc:
            colno_y = props_lc.index(y)
            break
    prefz = ['z', 't', 'depth', 'time', 'fold']
    for z in prefz:
        if z in props_lc:
            colno_z = props_lc.index(z)
            break

    xname = props[colno_x]  # string
    yname = props[colno_y]  # string
    zname = props[colno_z]  # string
    axes = (xname, yname, zname)
    return axes
