# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""
Make Cube from Voxet file.
"""

try:
    from collections.abc import OrderedDict
except ImportError:
    from collections import OrderedDict
import os.path as osp
import numpy as np
from ezcad.utils.convert_parms import get_parm_from_vidx, get_vxyz_from_parm
from ezcad.utils.convert_grid import xy2ln
from ezcad.utils.logger import logger
from ezcad.utils.functions import is_orthogonal
from .vtb_seis import read_seis, write_seis


def load_cube(fufn, prop_names, survey, object_name=None, progress_bar=None):
    """
    -i- fufn : string, full-path filename
    -i- prop_names : string, read all if 'DEFAULT'
    -i- survey : Survey
    """
    if object_name is None:
        path, fn = osp.split(fufn)
        object_name = osp.splitext(fn)[0]
    from ezcad.gocube.cube import Cube
    cube = Cube(object_name)
    read_voxet_files(cube, fufn, prop_names, survey, progress_bar)
    cube.calc_prop_percentile()
    cube.init_xyz_range()
    cube.set_section_number()
    cube.init_colormap()
    cube.set_current_property()
    return cube


def read_voxet_files(cube, file_name, prop_names, survey, progress_bar=None):
    """Prepare cube geometry and properties from Gocad voxet file.
    It can handle multiple properties.

    :param cube: cube object
    :type cube: :class:`~ezcad.gocube.cube.Cube`
    :param file_name: the voxet .vo filename
    :type file_name: str
    :param prop_names: names of the properties to read, comma separated.
      Read all if it is "DEFAULT".
    :type prop_names: str
    :param survey: survey object
    :type survey: :class:`~ezcad.gosurvey.survey.Survey`
    :param progress_bar: progress bar widget
    :type progress_bar: object
    """
    vo_dict = read_voxet_ascii(file_name)
    cube.survey = survey
    cube.dict_parm, cube.dict_vidx, cube.dict_vxyz = \
        get_cube_from_voxet(vo_dict, survey)
    logger.info("Done parsing the .vo file")

    NU = vo_dict['AXIS_NU']
    NV = vo_dict['AXIS_NV']
    NW = vo_dict['AXIS_NW']
    path, fn = osp.split(file_name)

    iprop = 0
    nprop = len(vo_dict['props'])
    if progress_bar is not None:
        progress_bar.setRange(0, nprop + 1)
        progress_bar.setValue(iprop)

    for propid in vo_dict['props']:
        iprop += 1
        prop_name = vo_dict['props'][propid]['name']
        if prop_names == 'DEFAULT' or prop_name in prop_names:
            pass
        else:
            continue
        propfn = vo_dict['props'][propid]['file']
        logger.info("Loading {}/{} property: {}".format(
            iprop, nprop, prop_name))
        fufn = osp.join(path, propfn)
        array3d = read_seis(fufn, NW, NV, NU)
        if cube.dict_vidx['NEED_TRANSPOSE']:
            array3d = np.transpose(array3d, (1, 0, 2))
            cube.dict_vidx['NEED_TRANSPOSE'] = False
            # At the end, need shape (NIL, NXL, NDP)
        if cube.dict_vidx['NEED_FLIP_IL']:
            array3d = np.flip(array3d, 0)
            cube.dict_vidx['NEED_FLIP_IL'] = False
        if cube.dict_vidx['NEED_FLIP_XL']:
            array3d = np.flip(array3d, 1)
            cube.dict_vidx['NEED_FLIP_XL'] = False
        cube.add_property(prop_name, array=array3d)
        if progress_bar is not None:
            progress_bar.setValue(iprop)


def write_voxet_files(cube, file_name, prop_names=None):
    fpre = osp.splitext(file_name)[0]
    voxetfn = fpre + ".vo"
    dictVoxet = get_voxet_from_cube(cube.dict_vxyz, cube.dict_vidx)
    if prop_names is None:
        prop_names = list(cube.prop.keys())
    write_voxet_ascii(voxetfn, dictVoxet, prop_names)
    for prop_name in prop_names:
        array3d = cube.prop[prop_name]['array3d']
        propfn = fpre + "_" + prop_name
        write_seis(propfn, array3d)


def read_voxet_ascii(voxetfn):
    """
    -i- voxetfn : string, voxet filename.
    -o- dictVoxet : dictionary, voxet parameters.
    Read Gocad .vo file.

    Gocad voxet is not an industry standard format. I've spent or wasted
    lots of time handling different voxets, putting into to surveys, and
    reverse engineering the labels. I cannot accomodate all cases yet.
    Maybe it's better to call Gocad reader or Company reader.

    I made some choices and assumptions:
    1) Do not use AXIS_LABEL_MIN and AXIS_LABEL_MAX, instead let the user
       survey to calculation the label or line numbers.
    2) Must have a survey before load voxet cube.
       This is because my visualization of cube cage and sections involves
       rotation transformation that needs survey azimuth.
    3) Read minimal keys to decode the cube.
       Then use ezcad system to manipulate or customize as needed.
    4) Look at AXIS_NAME. It may tell you (depth, crossline, inline)
       or (depth, inline, crossline).

    """
    dictVoxet = {}
    dictVoxet['props'] = {}
    with open(voxetfn, 'r') as f:
        for line in f:
            line = line.strip()
            columns = line.split()
            if len(columns) == 0:  # blank line
                continue  # skip process blank line
            key = columns[0]

            # TODO consider use Point object P(x,y,z) and P.x P.y P.z
            if key == 'AXIS_N':
                dictVoxet['AXIS_NU'] = int(columns[1])
                dictVoxet['AXIS_NV'] = int(columns[2])
                dictVoxet['AXIS_NW'] = int(columns[3])
            if key == 'AXIS_O':
                dictVoxet['AXIS_OX'] = float(columns[1])
                dictVoxet['AXIS_OY'] = float(columns[2])
                dictVoxet['AXIS_OZ'] = float(columns[3])
            if key == 'AXIS_U':
                dictVoxet['AXIS_UX'] = float(columns[1])
                dictVoxet['AXIS_UY'] = float(columns[2])
                dictVoxet['AXIS_UZ'] = float(columns[3])
            if key == 'AXIS_V':
                dictVoxet['AXIS_VX'] = float(columns[1])
                dictVoxet['AXIS_VY'] = float(columns[2])
                dictVoxet['AXIS_VZ'] = float(columns[3])
            if key == 'AXIS_W':
                dictVoxet['AXIS_WX'] = float(columns[1])
                dictVoxet['AXIS_WY'] = float(columns[2])
                dictVoxet['AXIS_WZ'] = float(columns[3])

            if line[:9] == 'PROPERTY ':
                propid = columns[1]  # string of number
                dictVoxet['props'][propid] = OrderedDict()
                dictVoxet['props'][propid]['name'] = columns[2].strip('\"')
                # DUV example PROPERTY 1 "vavg", so strip off.
            if key == 'PROP_FILE':
                propid = columns[1]
                dictVoxet['props'][propid]['file'] = columns[2].strip('\"')

    return dictVoxet


def write_voxet_ascii(voxetfn, dictVoxet, prop_names):
    print("--Writing--", voxetfn)
    fn = osp.basename(voxetfn)
    fpre = osp.splitext(fn)[0]
    strHeader = "GOCAD Voext 1 \n" + \
        "HEADER {\n" + \
        "name:%s\n" % fpre + \
        "ascii:off}\n"
    strCoord = "GOCAD_ORIGINAL_COORDINATE_SYSTEM\n" + \
        "NAME Default\n" + \
        "AXIS_NAME \"X\" \"Y\" \"Z\"\n" + \
        "AXIS_UNIT \"ft\" \"ft\" \"ft\"\n" + \
        "ZPOSITIVE Elevation\n" + \
        "END_ORIGINAL_COORDINATE_SYSTEM\n"
    with open(voxetfn, 'w') as f:
        f.write(strHeader)
        f.write(strCoord)
        f.write("AXIS_O %f %f %f\n" % dictVoxet['AXIS_O'])
        f.write("AXIS_U %f %f %f\n" % dictVoxet['AXIS_U'])
        f.write("AXIS_V %f %f %f\n" % dictVoxet['AXIS_V'])
        f.write("AXIS_W %f %f %f\n" % dictVoxet['AXIS_W'])
        f.write("AXIS_MIN %i %i %i\n" % dictVoxet['AXIS_MIN'])
        f.write("AXIS_MAX %i %i %i\n" % dictVoxet['AXIS_MAX'])
        f.write("AXIS_N %i %i %i\n" % dictVoxet['AXIS_N'])
        f.write("AXIS_NAME \"%s\" \"%s\" \"%s\"\n" % dictVoxet['AXIS_NAME'])
        f.write("AXIS_LABEL_MIN %i %i %i\n" % dictVoxet['AXIS_LABEL_MIN'])
        f.write("AXIS_LABEL_MAX %i %i %i\n" % dictVoxet['AXIS_LABEL_MAX'])
        f.write("AXIS_UNIT \"%s\" \"%s\" \"%s\"\n" % dictVoxet['AXIS_UNIT'])
        f.write("AXIS_TYPE even even even\n\n")

        pid = 0
        for name in prop_names:
            pid += 1
            f.write("PROPERTY %i \"%s\"\n" % (pid, name))
            f.write("PROPERTY_CLASS %i \"%s\"\n" % (pid, name+"_class"))
            f.write("PROPERTY_CLASS_HEADER %i \"%s\" {}\n" % (pid, name+"_class"))
            f.write("PROPERTY_SUBCLASS %i QUANTITY Float\n" % pid)
            f.write("PROP_ORIGINAL_UNIT %i none\n" % pid)
            f.write("PROP_UNIT %i none\n" % pid)
            f.write("PROP_NO_DATA_VALUE %i -99999\n" % pid)
            f.write("PROP_ESIZE %i 4\n" % pid)
            f.write("PROP_ETYPE %i IEEE\n" % pid)
            f.write("PROP_FORMAT %i Raw\n" % pid)
            f.write("PROP_OFFSET %i 0\n" % pid)
            f.write("PROP_FILE %i %s\n" % (pid, fpre + "_" + name))


def get_cube_from_voxet(dictVoxet, survey):
    """
    -i- dictVoxet : dictionary, from read .vo file.
    -i- survey : Survey
    -o- dict_parm : dictionary
    -o- dict_vidx : dictionary
    -o- dict_vxyz : dictionary
    """

    # Need to match voxet axis to survey lines
    # Voxet UVW can be depth, crossline, inline
    # Voxet UVW can be depth, inline, crossline

    oz = dictVoxet['AXIS_OZ']
    ux = dictVoxet['AXIS_UX']
    uy = dictVoxet['AXIS_UY']
    vz = dictVoxet['AXIS_VZ']
    wz = dictVoxet['AXIS_WZ']
    if oz != 0:
        raise NotImplementedError("AXIS_O is not at datum zero")
    if not (ux == 0 and uy == 0):
        raise NotImplementedError("AXIS_U is not vertical")
    if not (vz == 0 and wz == 0):
        raise NotImplementedError("AXIS_V or AXIS_W is not horizontal")

    axisOV = (dictVoxet['AXIS_VX'], dictVoxet['AXIS_VX'])
    # axisOW = (dictVoxet['AXIS_WX'], dictVoxet['AXIS_WX'])
    axisIL = survey.step['iline']
    # axisXL = survey.step['xline']

    dict_vidx = {}

    # TODO check for negative depths, (oz, uz) = (0, -1000)
    dict_vidx['DP_FRST'] = dictVoxet['AXIS_OZ']
    dict_vidx['DP_LAST'] = dictVoxet['AXIS_OZ'] + dictVoxet['AXIS_UZ']
    dict_vidx['DP_AMNT'] = dictVoxet['AXIS_NU']

    orBegX, orBegY = dictVoxet['AXIS_OX'], dictVoxet['AXIS_OY']
    ovEndX = orBegX + dictVoxet['AXIS_VX']
    ovEndY = orBegY + dictVoxet['AXIS_VY']
    owEndX = orBegX + dictVoxet['AXIS_WX']
    owEndY = orBegY + dictVoxet['AXIS_WY']

    if is_orthogonal(axisOV, axisIL):
        # axis OV is parallel with axis XL, NV = NXL
        points_xy = np.array([[orBegX, orBegY],
                              [ovEndX, ovEndY],  # first IL far end
                              [owEndX, owEndY]])  # first XL far end
        points_ln = xy2ln(points_xy, survey=survey)
        dict_vidx['IL_FRST'], dict_vidx['XL_FRST'] = points_ln[0]
        dict_vidx['IL_FRST'], dict_vidx['XL_LAST'] = points_ln[1]
        dict_vidx['IL_LAST'], dict_vidx['XL_FRST'] = points_ln[2]

        # Voxet UVW correspond to NDP, NXL, NIL
        dict_vidx['XL_AMNT'] = dictVoxet['AXIS_NV']
        dict_vidx['IL_AMNT'] = dictVoxet['AXIS_NW']
        dict_vidx['NEED_TRANSPOSE'] = False

    else:
        # axis OV is parallel with axis IL, NV = NIL
        points_xy = np.array([[orBegX, orBegY],
                              [owEndX, owEndY],  # first IL far end
                              [ovEndX, ovEndY]])  # first XL far end
        points_ln = xy2ln(points_xy, survey=survey)
        dict_vidx['IL_FRST'], dict_vidx['XL_FRST'] = points_ln[0]
        dict_vidx['IL_FRST'], dict_vidx['XL_LAST'] = points_ln[1]
        dict_vidx['IL_LAST'], dict_vidx['XL_FRST'] = points_ln[2]

        # Voxet UVW correspond to NDP, NIL, NXL
        dict_vidx['XL_AMNT'] = dictVoxet['AXIS_NW']
        dict_vidx['IL_AMNT'] = dictVoxet['AXIS_NV']
        dict_vidx['NEED_TRANSPOSE'] = True

    dict_vidx['DP_NCRT'] = (dict_vidx['DP_LAST'] - dict_vidx['DP_FRST']) / (
                dict_vidx['DP_AMNT'] - 1)
    dict_vidx['XL_NCRT'] = (dict_vidx['XL_LAST'] - dict_vidx['XL_FRST']) / (
                dict_vidx['XL_AMNT'] - 1)
    dict_vidx['IL_NCRT'] = (dict_vidx['IL_LAST'] - dict_vidx['IL_FRST']) / (
                dict_vidx['IL_AMNT'] - 1)

    # flip axis to increase direction
    dict_vidx['NEED_FLIP_IL'] = False
    dict_vidx['NEED_FLIP_XL'] = False
    if dict_vidx['IL_NCRT'] < 0:
        dict_vidx['NEED_FLIP_IL'] = True
        dum = dict_vidx['IL_FRST']
        dict_vidx['IL_FRST'] = dict_vidx['IL_LAST']
        dict_vidx['IL_LAST'] = dum
        dict_vidx['IL_NCRT'] = - dict_vidx['IL_NCRT']
    if dict_vidx['XL_NCRT'] < 0:
        dict_vidx['NEED_FLIP_XL'] = True
        dum = dict_vidx['XL_FRST']
        dict_vidx['XL_FRST'] = dict_vidx['XL_LAST']
        dict_vidx['XL_LAST'] = dum
        dict_vidx['XL_NCRT'] = - dict_vidx['XL_NCRT']
    # (DP_FRST, DP_LAST, DP_NCRT)
    # (-10, 0, 1), (-10, -1, 1), (0, -10, -1), (-1, -10, -1)
    # Consider the complexity of depth axis and datum, leave the flip
    # to data manipulation after loaded.

    dict_parm = get_parm_from_vidx(dict_vidx, survey)
    dict_vxyz = get_vxyz_from_parm(dict_parm)  # in case flipped dict_vidx

    return dict_parm, dict_vidx, dict_vxyz


def get_voxet_from_cube(dict_vxyz, dict_vidx):
    """
    -i- dict_vxyz : dict, cube xyz
    -i- dict_vidx : dict, cube line numbers
    -o- dictVoxet : dict, ready for write to .vo file
    """
    dictVoxet = {
        # "AXIS_NAME": ("X", "Y", "Z"),
        "AXIS_UNIT": ("ft", "ft", "ft"),
        "AXIS_MIN": (0, 0, 0),
        "AXIS_MAX": (1, 1, 1),
        "AXIS_NAME": ("depth", "XLINE_NO", "ILINE_NO")}

    ox = dict_vxyz['AXIS_ORX']
    oy = dict_vxyz['AXIS_ORY']
    oz = dict_vidx['DP_FRST']
    dictVoxet["AXIS_O"] = (ox, oy, oz)

    ux = uy = 0
    uz = dict_vidx['DP_LAST']
    dictVoxet["AXIS_U"] = (ux, uy, uz)

    vx = dict_vxyz['AXIS_XLX'] - ox
    vy = dict_vxyz['AXIS_XLY'] - oy
    vz = 0
    dictVoxet["AXIS_V"] = (vx, vy, vz)

    wx = dict_vxyz['AXIS_ILX'] - ox
    wy = dict_vxyz['AXIS_ILY'] - oy
    wz = 0
    dictVoxet["AXIS_W"] = (wx, wy, wz)

    NDP = dict_vidx['DP_AMNT']
    NXL = dict_vidx['XL_AMNT']
    NIL = dict_vidx['IL_AMNT']
    dictVoxet["AXIS_N"] = (NDP, NXL, NIL)

    dpno1 = dict_vidx['DP_FRST']
    xlno1 = dict_vidx['XL_FRST']
    ilno1 = dict_vidx['IL_FRST']
    dictVoxet["AXIS_LABEL_MIN"] = (dpno1, xlno1, ilno1)

    dpno2 = dict_vidx['DP_LAST']
    xlno2 = dict_vidx['XL_LAST']
    ilno2 = dict_vidx['IL_LAST']
    dictVoxet["AXIS_LABEL_MAX"] = (dpno2, xlno2, ilno2)

    #    dictVoxet["props"] =  {}
    #    pid = 0
    #    for prop_name in prop_names:
    #        pid += 1
    #        dictVoxet["props"][pid] = {}
    #        dictVoxet["props"][pid]['name'] = prop_name
    #        dictVoxet["props"][pid]['file'] = prop_name

    return dictVoxet
