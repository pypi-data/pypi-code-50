# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import numpy as np
from scipy.interpolate import griddata
from ..surface import Gsurface
from ezcad.utils.envars import COORDINATE_PROPERTY_NAMES


def from_tsurf(tsurf, survey, dict_sidx_ln, gsurf_name, method='linear'):
    """Create gsurface from tsurface.

    :param tsurf: input tsurface object
    :type tsurf: :class:`~ezcad.gotsurf.surface.Tsurface`
    :param survey: survey object
    :type survey: :class:`~ezcad.gosurvey.survey.Survey`
    :param dict_sidx_ln: surface index in LN.
      Defines gsurf spatial extent and density in line number domain.
    :type dict_sidx_ln: dict
    :param gsurf_name: name of the gsurface
    :type gsurf_name: str
    :param method: interpolation method
    :type method: str
    :return: a tsurface object
    :type: :class:`~ezcad.gogsurf.surface.Gsurface`
    """
    # Prepare tsurf XY in grid-line domain
    tsurf.set_survey(survey)
    linos = tsurf.calc_line_numbers()
    m, n = linos[:, 0], linos[:, 1]

    # Prepare gsurf XY in grid-line domain
    IL_FRST = dict_sidx_ln['IL_FRST']
    IL_LAST = dict_sidx_ln['IL_LAST']
    IL_AMNT = dict_sidx_ln['IL_AMNT']
    XL_FRST = dict_sidx_ln['XL_FRST']
    XL_LAST = dict_sidx_ln['XL_LAST']
    XL_AMNT = dict_sidx_ln['XL_AMNT']
    xi = np.linspace(IL_FRST, IL_LAST, IL_AMNT)
    yi = np.linspace(XL_FRST, XL_LAST, XL_AMNT)

    # z = tsurf.vertexes['xyz'][:,2]
    # zi = griddata((m, n), z, (xi[None,:], yi[:,None]), method='cubic')
    #    fill_value=100000)
    # zi is nan at grids outside of the convext hull of control points.
    # print(zi.shape)  # (len(yi),len(xi))
    # gridz = zi.T # transpose to (IL, XL)

    dob = Gsurface(gsurf_name)
    # Interpolate tsurf properties onto gsurf grid and add
    for prop_name in tsurf.prop:
        prop_array = tsurf.prop[prop_name][tsurf.prop_array_key]
        propGrid = griddata((m, n), prop_array, (xi[None, :], yi[:, None]),
                            method=method, fill_value=0)
        propGrid = propGrid.T
        dob.add_property(prop_name, array=propGrid)
        if prop_name == COORDINATE_PROPERTY_NAMES[2]:
            dob.set_gridz(propGrid)

    dob.set_current_property()
    dob.set_survey(survey)
    dob.set_dict_sidx(dict_sidx_ln)
    dob.init_corners()
    dob.set_xyz_range()
    return dob


def from_point(point, survey, dict_sidx_ln, gsurf_name):
    """Create gsurface from point object.
    It calls function :func:`~ezcad.gogsurface.new.new.from_tsurf`.

    :param point: input point object
    :type point: :class:`~ezcad.gopoint.point.Point`
    :param survey: survey object
    :type survey: :class:`~ezcad.gosurvey.survey.Survey`
    :param dict_sidx_ln: surface index in LN.
      Defines gsurf spatial extent and density in line number domain.
    :type dict_sidx_ln: dict
    :param gsurf_name: name of the gsurface
    :type gsurf_name: str
    :return: a tsurface object
    :type: :class:`~ezcad.gogsurf.surface.Gsurface`
    """
    dob = from_tsurf(point, survey, dict_sidx_ln, gsurf_name)
    return dob
