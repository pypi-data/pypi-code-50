# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""
This module cuts grid surface by cube section.
"""

import numpy as np
from ezcad.utils.convert_grid import ln2xy
from gogsurf.cut import make_line_from_vertexes


def update_tsurf_cut(tsurf, cube, section_type, line):
    """
    -i- tsurf : Gsurface
    -i- cube : Cube
    -i- section_type : string, 'iline' or 'xline'
    -i- line : Line
    Result is the input line item moved to the current section.
    """
    vertexes = calc_tsurf_cut_vertexes(tsurf, cube, section_type)
    line.set_pg3d_lines(pos=vertexes)


def make_tsurf_cut(tsurf, cube, section_type, line_name):
    """
    -i- tsurf : Tsurface
    -i- cube : Cube
    -i- section_type : string, 'iline' or 'xline'
    -i- line_name : string, name of the line dob to be created.
    -o- dob : Line
    """
    vertexes = calc_tsurf_cut_vertexes(tsurf, cube, section_type)
    dob = make_line_from_vertexes(line_name, vertexes)
    return dob


def calc_tsurf_cut_vertexes(tsurf, cube, section_type):
    """
    -i- tsurf : Tsurface
    -i- cube : Cube
    -i- section_type : string, 'iline' or 'xline'
    -o- vertexes : array, n-by-3, [x,y,z] of cutting points.
    For each trace in section, this function interpolates Z by the three
    vertexes of the triangle that contains the trace.
    """
    if section_type == 'iline':
        XL_FRST = cube.dict_vidx['XL_FRST']
        XL_LAST = cube.dict_vidx['XL_LAST']
        XL_AMNT = cube.dict_vidx['XL_AMNT']
        xlnos_cube = np.linspace(XL_FRST, XL_LAST, XL_AMNT)
        ilnos_cube = np.zeros(xlnos_cube.shape)
        ilno = cube.section_number[section_type]
        ilnos_cube[:] = ilno

    elif section_type == 'xline':
        IL_FRST = cube.dict_vidx['IL_FRST']
        IL_LAST = cube.dict_vidx['IL_LAST']
        IL_AMNT = cube.dict_vidx['IL_AMNT']
        ilnos_cube = np.linspace(IL_FRST, IL_LAST, IL_AMNT)
        xlnos_cube = np.zeros(ilnos_cube.shape)
        xlno = cube.section_number[section_type]
        xlnos_cube[:] = xlno
    else:
        raise ValueError("Unknown value")

    # Get XY from LN for each trace in section
    traces_ln = np.stack((ilnos_cube, xlnos_cube), axis=-1)
    dict_sgmt = cube.survey.geometry
    dict_step = cube.survey.step
    traces_xy = ln2xy(traces_ln, dict_sgmt, dict_step)

    # Find in which triangle the traces are.
    itri = tsurf.delaunay.find_simplex(traces_xy)

    # Find indexes of the three vertexes of the target triangle
    pidx = tsurf.delaunay.simplices[itri,:]

    pzTsurf = tsurf.vertexes['xyz'][:,2]
    pz = np.sum(pzTsurf[pidx], axis=1) / 3.0
    px, py = traces_xy[:,0], traces_xy[:,1]
    vertexes = np.stack((px, py, pz), axis=-1)
    return vertexes
