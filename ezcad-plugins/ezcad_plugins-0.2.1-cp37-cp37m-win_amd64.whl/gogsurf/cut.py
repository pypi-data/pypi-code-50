# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""
This module cuts grid surface by cube section.
"""

import numpy as np
from ezcad.utils.convert_grid import ln2xy
from goline.line import Line


def update_gsurf_cut(gsurf, cube, section_type, line):
    """
    -i- gsurf : Gsurface
    -i- cube : Cube
    -i- section_type : string, 'iline' or 'xline'
    -i- line : Line
    Result is the input line item moved to the current section.
    """
    vertexes = calc_gsurf_cut_vertexes(gsurf, cube, section_type)
    line.set_pg3d_lines(pos=vertexes)


def make_gsurf_cut(gsurf, cube, section_type, line_name):
    """
    -i- gsurf : Gsurface
    -i- cube : Cube
    -i- section_type : string, 'iline' or 'xline'
    -i- line_name : string, name of the line dob to be created.
    -o- dob : Line
    """
    vertexes = calc_gsurf_cut_vertexes(gsurf, cube, section_type)
    dob = make_line_from_vertexes(line_name, vertexes)
    return dob


def make_line_from_vertexes(line_name, vertexes):
    """
    -i- line_name : string, name of the line dob to be created.
    -i- vertexes : array, n-by-3, [x,y,z] of cutting points.
    -o- dob : Line
    Make one line from all input vertexes.
    """
    dob = Line(line_name)
    dob.set_atom_style()
    dob.set_line_style()
    dob.set_vertexes(vertexes)
    dob.set_xyz_range()
    return dob


def calc_gsurf_cut_vertexes(gsurf, cube, section_type):
    """
    -i- gsurf : Gsurface
    -i- cube : Cube
    -i- section_type : string, 'iline' or 'xline'
    -o- vertexes : array, n-by-3, [x,y,z] of cutting points.
    Assume the surface is dense enough, preferably gridded on every IL/XL.
    For each trace in section, this function searches the nearest points
    in the grid surface. No interpolation is used.
    """
    # restrict by cube section, limit by gsurf extent.
    # The host is section. Surface cut traces in sections.
    if section_type == 'iline':
        # Get section [xl1, xl2] within gsurf [XL_FRST, XL_LAST]
        XL_FRST = cube.dict_vidx['XL_FRST']
        XL_LAST = cube.dict_vidx['XL_LAST']
        XL_AMNT = cube.dict_vidx['XL_AMNT']
        xlnos_cube = np.linspace(XL_FRST, XL_LAST, XL_AMNT)
        xl1_gsurf = gsurf.dict_sidx_ln['XL_FRST']
        xl2_gsurf = gsurf.dict_sidx_ln['XL_LAST']
        index = np.where(np.logical_and(xlnos_cube >= xl1_gsurf,
                                        xlnos_cube <= xl2_gsurf))
        xlnos_cut = xlnos_cube[index]

        ilno = cube.section_number[section_type]
        ilnos_cut = np.zeros(xlnos_cut.shape)
        ilnos_cut[:] = ilno

    elif section_type == 'xline':
        # Get section [il1, il2] within gsurf [IL_FRST, IL_LAST]
        IL_FRST = cube.dict_vidx['IL_FRST']
        IL_LAST = cube.dict_vidx['IL_LAST']
        IL_AMNT = cube.dict_vidx['IL_AMNT']
        ilnos_cube = np.linspace(IL_FRST, IL_LAST, IL_AMNT)
        il1_gsurf = gsurf.dict_sidx_ln['IL_FRST']
        il2_gsurf = gsurf.dict_sidx_ln['IL_LAST']
        index = np.where(np.logical_and(ilnos_cube >= il1_gsurf,
                                        ilnos_cube <= il2_gsurf))
        ilnos_cut = ilnos_cube[index]

        xlno = cube.section_number[section_type]
        xlnos_cut = np.zeros(ilnos_cut.shape)
        xlnos_cut[:] = xlno
    else:
        raise ValueError("Unknown value")

    # For section xlnos_cut, find the nearest xl in gsurf
    XL_FRST = gsurf.dict_sidx_ln['XL_FRST']
    XL_NCRT = gsurf.dict_sidx_ln['XL_NCRT']
    index_xls = (xlnos_cut - XL_FRST) / XL_NCRT
    index_xls = index_xls.astype(int)

    # For section ilnos_cut, find the nearest il in gsurf
    IL_FRST = gsurf.dict_sidx_ln['IL_FRST']
    IL_NCRT = gsurf.dict_sidx_ln['IL_NCRT']
    index_ils = (ilnos_cut - IL_FRST) / IL_NCRT
    index_ils = index_ils.astype(int)

    # For every trace being cut.
    pz = np.zeros(ilnos_cut.shape)
    for i in range(ilnos_cut.shape[0]):
        index_il = index_ils[i]
        index_xl = index_xls[i]
        pz[i] = gsurf.gridz['array'][index_il, index_xl]

    # get XY from LN for plot GLLinePlotItem
    traces_ln = np.stack((ilnos_cut, xlnos_cut), axis=-1)
    dict_sgmt = cube.survey.geometry
    dict_step = cube.survey.step
    traces_xy = ln2xy(traces_ln, dict_sgmt, dict_step)
    px, py = traces_xy[:,0], traces_xy[:,1]

    vertexes = np.stack((px, py, pz), axis=-1)
    return vertexes
