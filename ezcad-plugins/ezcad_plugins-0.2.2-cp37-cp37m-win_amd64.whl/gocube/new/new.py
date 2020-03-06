# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""Create a new cube."""

import numpy as np
from ..cube import Cube
from gosurvey.new.new import new_survey_from_vidx


def new_cube_from_vidx(dict_vidx=None, survey=None, cube_name='cube',
    prop_name='amp', prop_method='zeros'):
    """Create cube from vidx.

    :param dict_vidx: volume indexes
    :type dict_vidx: dict
    :param survey: survey, used to convert LN to XY
    :type survey: :class:`~ezcad.gosurvey.survey.Survey`
    :param cube_name: name of the cube
    :type cube_name: str
    :param prop_name: name of the property
    :type prop_name: str
    :param prop_method: property generating method, e.g. zeros, random, isum
    :type prop_method: str
    :return: a cube object
    :rtype: :class:`~ezcad.gocube.cube.Cube`
    """
    if dict_vidx is None:
        dict_vidx = default_vidx()
    if survey is None:
        survey = new_survey_from_vidx(dict_vidx)
    
    # prepare data for 3D array
    IL_AMNT = dict_vidx['IL_AMNT']
    XL_AMNT = dict_vidx['XL_AMNT']
    DP_AMNT = dict_vidx['DP_AMNT']
    if prop_method == 'zeros':
        array3d = np.zeros((IL_AMNT, XL_AMNT, DP_AMNT))
    elif prop_method == 'random':
        array3d = np.random.randn(IL_AMNT, XL_AMNT, DP_AMNT)  # slow
    elif prop_method == 'isum':
        array3d = np.zeros((IL_AMNT, XL_AMNT, DP_AMNT))
        for i in range(IL_AMNT):
            for j in range(XL_AMNT):
                for k in range(DP_AMNT):
                    array3d[i, j, k] = i + j + k
    else:
        raise ValueError("Unknown value {}".format(prop_method))

    cube = Cube(cube_name)
    cube.make_from_vidx(dict_vidx, survey, array3d, dataVelType=prop_name)
    cube.calc_prop_percentile()
    cube.init_xyz_range()
    cube.set_section_number()
    cube.init_colormap()
    cube.set_current_property()
    return cube


def default_vidx():
    dict_vidx = {'IL_FRST': 1, 'IL_LAST': 11, 'IL_NCRT': 1, 'IL_AMNT': 11,
                'XL_FRST': 1, 'XL_LAST': 11, 'XL_NCRT': 1, 'XL_AMNT': 11,
                'DP_FRST': 0, 'DP_LAST': 100, 'DP_NCRT': 10, 'DP_AMNT': 11}
    return dict_vidx
