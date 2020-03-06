# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""
Make Cube from Segy file.
"""

import os
try:
    from collections.abc import OrderedDict
except ImportError:
    from collections import OrderedDict
from datetime import datetime
import numpy as np
from ezcad.utils.convert_parms import get_vxyz_from_vidx, get_parm_from_vidx

lib = 'data_io/segy'
if os.getenv(lib) == 'True':
    print("Loading ext:", lib)
    from segypy import segypy
else:
    print("WARNING: Segy module is not enabled")


def load_cube(fufn, survey, object_name=None):
    """Load Segy file and setup cube.

    :param fufn: full-path filename
    :type fufn: str
    :param survey: survey, used to convert LN to XY
    :type survey: :class:`~ezcad.gosurvey.survey.Survey`
    :param object_name: name of the new object
    :type object_name: str
    :return: a cube object
    :rtype: :class:`~ezcad.gocube.cube.Cube`
    """
    if object_name is None:
        path, fn = os.path.split(fufn)
        object_name = os.path.splitext(fn)[0]

    # user set headers to read and byte location
    hdr = {}
    # hdr["cdpX"] = {"pos": 188 , "type": "int32"}
    # hdr["cdpY"] = {"pos": 192 , "type": "int32"}
    # hdr["Inline3D"] = {"pos": 180 , "type": "int32"}
    # hdr["Crossline3D"] = {"pos": 184 , "type": "int32"}

    from ezcad.gocube.cube import Cube
    cube = Cube(object_name)
    read_segy(cube, fufn, survey=survey, hdr=hdr)
    cube.calc_prop_percentile()
    cube.init_xyz_range()
    cube.set_section_number()
    cube.init_colormap()
    cube.set_current_property()
    return cube


def read_segy(cube, segyfn, survey=None, hdr=None, **kwargs):
    """Read Segy file to cube.
    The Segy file is a 3D seismic stack volume.
    The Segy trace sample data are reshaped to array3d.

    :param cube: cube object
    :type cube: :class:`~ezcad.gocube.cube.Cube`
    :param segyfn: Segy filename
    :type segyfn: str
    :param survey: survey, used to convert LN to XY
    :type survey: :class:`~ezcad.gosurvey.survey.Survey`
    :param hdr: byte location and data type of trace headers.
    :type hdr: dict
    :param kwargs: keyword argument passed to get_cube_from_sth.
    """
    # print("$$Read" + " Start @", datetime.now())
    custom_hdr = {}  # use a subset and default
    custom_hdr["SourceGroupScalar"] = {"pos": 70, "type": "int16"}
    custom_hdr["ns"] = {"pos": 114, "type": "uint16"}
    custom_hdr["dt"] = {"pos": 116, "type": "uint16"}
    custom_hdr["cdpX"] = {"pos": 180, "type": "int32"}
    custom_hdr["cdpY"] = {"pos": 184, "type": "int32"}
    custom_hdr["Inline3D"] = {"pos": 188, "type": "int32"}
    custom_hdr["Crossline3D"] = {"pos": 192, "type": "int32"}
    if hdr is not None:  # add new or reset existing entries
        for key in hdr.keys():
            custom_hdr[key] = hdr[key]

    Data, SH, trace_headers = segypy.readSegy(segyfn, custom_hdr)
    # print("$$Read" + " Ended @", datetime.now())

    # Get cube dicts from Segy trace headers
    dict_vidx, survey, dict_vxyz, dict_parm = \
        get_cube_from_sth(trace_headers, survey=survey, **kwargs)

    # Get array3d
    # print(Data.shape)  # nSamplePerTrace by nTrace
    # Data = np.transpose(Data)  # nTrace by nSamplePerTrace
    NIL, NXL, NDP = dict_vidx['IL_AMNT'], dict_vidx['XL_AMNT'], \
                    dict_vidx['DP_AMNT']
    array3d = Data.reshape((NIL, NXL, NDP))

    prop_name = dict_parm['DATA_VEL_TYPE']
    cube.add_property(prop_name, array=array3d)
    cube.dict_parm = dict_parm
    cube.dict_vidx = dict_vidx
    cube.dict_vxyz = dict_vxyz
    cube.survey = survey

    print('Data min/max value =', cube.prop[prop_name]['colorClip'])
    print('Data array shape =', cube.prop[prop_name]['array3d'].shape)
    print('Array data type =', cube.prop[prop_name]['array3d'].dtype)


def write_segy(cube, outfn, prop_name=None, stfhfn=None):
    """Write cube to Segy file.

    :param cube: cube object
    :type cube: :class:`~ezcad.gocube.cube.Cube`
    :param outfn: output Segy filename
    :type outfn: str
    :param prop_name: the name of the property to write
    :type prop_name: str
    :param stfhfn: Segy textual file header filename
    :type stfhfn: str
    """
    print("Info of the Segy to be written:")
    # print_vidx(cube.dict_vidx)
    # print_parm(cube.dict_parm)
    if prop_name is None:
        if cube.current_property is None:
            cube.set_current_property()
        prop_name = cube.current_property
    array3d = cube.prop[prop_name]['array3d']  # shape (nil,nxl,ndp)
    print('Data min value =', np.amin(array3d))
    print('Data max value =', np.amax(array3d))
    print('Data array shape =', array3d.shape)
    print('Array data type =', array3d.dtype)
    startTime = datetime.now()
    print("$$Write Segy" + " Start @", startTime)

    NIL, NXL, NDP = array3d.shape
    ns = NDP
    ntraces = NXL * NIL
    array3d = np.transpose(array3d, (2, 0, 1))  # (ndp,nil,nxl)
    array2d = array3d.reshape(ns, ntraces)

    DP_NCRT = cube.dict_vidx['DP_NCRT']
    # in time, millisecond to microsecond
    # in depth, meter to millimeter
    dt = DP_NCRT * 1000

    # prepare the header for each trace
    traces_ln = cube.get_traces_ln()
    traces_xy = cube.get_traces_xy()

    # Custom Segy trace header
    STHin = OrderedDict()
    # STHin = {}
    STHin['cdpX'] = {}
    STHin['cdpY'] = {}
    STHin['Inline3D'] = {}
    STHin['Crossline3D'] = {}
    STHin['TraceSequenceLine'] = {}
    STHin['SourceGroupScalar'] = {}
    for i in range(ntraces):
        STHin['cdpX'][i] = traces_xy[i, 0]
        STHin['cdpY'][i] = traces_xy[i, 1]
        STHin['Inline3D'][i] = traces_ln[i, 0]
        STHin['Crossline3D'][i] = traces_ln[i, 1]
        STHin["TraceSequenceLine"][i] = i % NXL + 1
        # CVX CalibSeis require it nonzero
        STHin['SourceGroupScalar'][i] = 1
    # print(len(STHin), len(STHin['cdpX']))

    # Prepare the string for Segy textual file header
    if stfhfn is not None:
        f = open(stfhfn, 'r')
        stfhString = ''
        ncLine = 80
        ctLine = 0
        for line in f:
            ctLine += 1
            if ctLine == 41:
                print("Lines after 40th will be ignored.")
                break
            line = line.strip('\n')  # strip off new line char
            if len(line) > ncLine:
                print("Line longer than 80 will be cut.")
                lineFull = line[:ncLine]
            else:  # fill with space
                lineFull = line + ' ' * (ncLine - len(line))
            stfhString = stfhString + lineFull
        # print(len(stfhString))
    else:  # None given, use default
        stfhString = "Ezcad"
        stfhString += ' ' * (3200 - len(stfhString))

    # Write Segy file
    segypy.writeSegy(outfn, array2d, dt, stfhString, STHin)

    endTime = datetime.now()
    print("$$Write Segy" + " Ended @", endTime)
    print("Time Used is", endTime - startTime)


def get_cube_from_sth(headers, survey=None, **kwargs):
    """Get cube geometry from Segy Trace Headers.
    Get the corner points from Segy trace header:
    P1 = [IL_FRST, XL_FRST, X, Y],
    P2 = [IL_FRST, XL_LAST, X, Y],
    P3 = [IL_LAST, XL_FRST, X, Y],
    P4 = [IL_LAST, XL_LAST, X, Y].
    The (P1,P2,P3)(LN) and (ns,dt) forms the dict_vidx.
    The (P1,P2,P3)(LN,XY) forms the dict_sgmt.
    The (P1,P2,P3)(XY) forms the dict_vxyz.
    The dict_sgmt and dict_vidx derive the dict_parm.
    The idea is that since it is a regularly sampled 3D cube, we do not
    need to store the LN/XY for each trace, but can get them from the
    dict_vidx and dict_sgmt using simple geometry.

    :param headers: Segy Trace Headers
    :type headers: dict
    :param survey: survey, used to convert LN to XY
    :type survey: :class:`~ezcad.gosurvey.survey.Survey`
    :param kwargs: keyword argument passed to
      :func:`~ezcad.utils.convert_parms.get_parm_from_vidx`
    :return: dict_vidx, survey, dict_vxyz, dict_parm
    """
    # Get dict_vidx
    array1dIlno = headers['Inline3D']
    array1dXlno = headers['Crossline3D']
    array1dNspt = headers['ns']  # Nspt: Number of samples per trace

    # QC if all inlines have the same number of crosslines
    unique, counts = np.unique(array1dIlno, return_counts=True)
    unique, counts = np.unique(counts, return_counts=True)
    if len(unique) > 1:
        raise ValueError("Not all ILs are the same length.")
    # QC if all crosslines have the same number of inlines
    unique, counts = np.unique(array1dXlno, return_counts=True)
    unique, counts = np.unique(counts, return_counts=True)
    if len(unique) > 1:
        raise ValueError("Not all XLs are the same length.")
    # QC if all traces have the same number of samples
    unique, counts = np.unique(array1dNspt, return_counts=True)
    if len(unique) > 1:
        raise ValueError("Not all traces are the same length.")

    unique, counts = np.unique(array1dIlno, return_counts=True)
    # dictUniqCounts = dict(zip(unique, counts))
    IL_AMNT = int(unique.shape[0])
    IL_FRST = unique[0]
    IL_LAST = unique[-1]
    if IL_AMNT > 1:
        IL_NCRT = unique[1] - unique[0]
    else:
        IL_NCRT = 0
    unique, counts = np.unique(array1dXlno, return_counts=True)
    XL_AMNT = int(unique.shape[0])
    XL_FRST = unique[0]
    XL_LAST = unique[-1]
    if XL_AMNT > 1:
        XL_NCRT = unique[1] - unique[0]
    else:
        XL_NCRT = 0

    DP_AMNT = int(headers['ns'][0])
    DP_NCRT = headers['dt'][0] * 0.001
    if abs(int(round(DP_NCRT)) - DP_NCRT) < 0.1:
        DP_NCRT = int(round(DP_NCRT))
    DP_FRST = 0  # Assume datum at zero. Can vertical shift later.
    DP_LAST = DP_FRST + DP_NCRT * (DP_AMNT - 1)

    dict_vidx = {
        'IL_FRST': int(IL_FRST),
        'IL_LAST': int(IL_LAST),
        'IL_NCRT': int(IL_NCRT),
        'IL_AMNT': int(IL_AMNT),
        'XL_FRST': int(XL_FRST),
        'XL_LAST': int(XL_LAST),
        'XL_NCRT': int(XL_NCRT),
        'XL_AMNT': int(XL_AMNT),
        'DP_FRST': DP_FRST,
        'DP_LAST': DP_LAST,
        'DP_NCRT': DP_NCRT,
        'DP_AMNT': DP_AMNT
    }

    # Get dict_sgmt
    if survey is not None:
        dict_sgmt = survey.geometry
    else:
        # Assume the coordinate scalar of all traces are the same sign.
        scalco = headers['SourceGroupScalar'][0]
        if scalco > 0:
            array1dCdpx = headers['cdpX'] * headers['SourceGroupScalar']
            array1dCdpy = headers['cdpY'] * headers['SourceGroupScalar']
        elif scalco < 0:
            array1dCdpx = headers['cdpX'] / abs(headers['SourceGroupScalar'])
            array1dCdpy = headers['cdpY'] / abs(headers['SourceGroupScalar'])
        else:  # scalco is zero and considered no scaling
            array1dCdpx = headers['cdpX']
            array1dCdpy = headers['cdpY']
        # array1dIlno = headers['Inline3D']
        # array1dXlno = headers['Crossline3D']
        # unique, counts = np.unique(array1dIlno, return_counts=True)
        # nil, nxl = unique.shape[0], counts[0]
        nil, nxl = IL_AMNT, XL_AMNT
        array2dCdpx = array1dCdpx.reshape(nil, nxl)
        array2dCdpy = array1dCdpy.reshape(nil, nxl)
        array2dIlno = array1dIlno.reshape(nil, nxl)
        array2dXlno = array1dXlno.reshape(nil, nxl)
        dict_sgmt = {
            'P1_ILNO': array2dIlno[0, 0],
            'P1_XLNO': array2dXlno[0, 0],
            'P1_CRSX': array2dCdpx[0, 0],
            'P1_CRSY': array2dCdpy[0, 0],
            'P2_ILNO': array2dIlno[0, -1],
            'P2_XLNO': array2dXlno[0, -1],
            'P2_CRSX': array2dCdpx[0, -1],
            'P2_CRSY': array2dCdpy[0, -1],
            'P3_ILNO': array2dIlno[-1, 0],
            'P3_XLNO': array2dXlno[-1, 0],
            'P3_CRSX': array2dCdpx[-1, 0],
            'P3_CRSY': array2dCdpy[-1, 0]
        }

        # Create survey
        from ezcad.gosurvey.survey import Survey
        survey_name = 'survey_from_segy'
        survey = Survey(survey_name)
        survey.set_geometry(dict_sgmt)
        survey.initialize()

    dict_vxyz = get_vxyz_from_vidx(dict_vidx, survey)
    dict_parm = get_parm_from_vidx(dict_vidx, survey, **kwargs)

    # Print to screen for QC
    # print_vidx(dict_vidx)
    # print_sgmt(dict_sgmt)
    # print_vxyz(dict_vxyz)
    # print_parm(dict_parm)
    return dict_vidx, survey, dict_vxyz, dict_parm


# def get_cube_from_segy(segyfn):
#     # print("$$Read" + " Start @", datetime.now())
#     custom_hdr = {}  # use a subset and default
#     custom_hdr["SourceGroupScalar"] = {"pos": 70, "type": "int16"}
#     custom_hdr["ns"] = {"pos": 114, "type": "uint16"}
#     custom_hdr["dt"] = {"pos": 116, "type": "uint16"}
#     custom_hdr["cdpX"] = {"pos": 180, "type": "int32"}
#     custom_hdr["cdpY"] = {"pos": 184, "type": "int32"}
#     custom_hdr["Inline3D"] = {"pos": 188, "type": "int32"}
#     custom_hdr["Crossline3D"] = {"pos": 192, "type": "int32"}
#     SH, STH = segypy.readSegy(segyfn, TH_dict=custom_hdr, TH_only=True)
    # print("$$Read" + " Ended @", datetime.now())
    # dict_vidx, dict_sgmt, dict_vxyz, dict_parm = \
    #     get_cube_from_sth(STH)
    # print_vidx(dict_vidx)
    # print_sgmt(dict_sgmt)
    # print_vxyz(dict_vxyz)
    # print_parm(dict_parm)
    # vidxfn = segyfn + '.vidx'
    # sgmtfn = segyfn + '.sgmt'
    # vxyzfn = segyfn + '.vxyz'
    # parmfn = segyfn + '.parm'
    # write_vidx(vidxfn, dict_vidx)
    # write_sgmt(sgmtfn, dict_sgmt)
    # write_vxyz(vxyzfn, dict_vxyz)
    # write_parm(parmfn, dict_parm)
