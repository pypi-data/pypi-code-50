# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""
Make Cube from Velocity Toolbox Seis file.
"""

import os
import struct
from math import sqrt
import numpy as np
from ezcad.utils.convert_parms import get_vidx_from_parm, get_vxyz_from_parm


def load_cube(fufn, survey, object_name=None):
    """
    -i- fufn : string, full-path filename
    -i- survey : Survey, class object of survey parameters and plots.
        It is used to get the IL/XL for the parms file.
    """
    if object_name is None:
        path, fn = os.path.split(fufn)
        object_name = os.path.splitext(fn)[0]
    from ezcad.gocube.cube import Cube
    cube = Cube(object_name)
    read_parms(cube, fufn, survey)
    cube.calc_prop_percentile()
    cube.init_xyz_range()
    cube.set_section_number()
    cube.init_colormap()
    cube.set_current_property()
    return cube


def read_parms(cube, parmfn, survey=None):
    """
    -i- parmfn : string, parms filename
    -i- survey : Survey
    Make Cube from parm file. It is designed for VTB binary cube
    seis/parm format, which means a seis file always comes with a
    parm file (on grids, coordinates, units). The survey is
    essential to convert XY to get LN thus the physical indexing.
    If None, the Vidx/LN would be set from 1 to NIL/NXL.
    """
    # read parm file to dictionary
    dict_parm = read_parm(parmfn)
    # print_parm(dict_parm)

    # read cube file to array
    NIL = dict_parm['NPANEL']
    NXL = dict_parm['NTRACE']
    NDP = dict_parm['NSAMPLE']
    fpre = os.path.splitext(parmfn)[0]
    cubefn = fpre + ".seis"
    array3d = read_seis(cubefn, NIL, NXL, NDP)

    # get the dict_vxyz
    dict_vxyz = get_vxyz_from_parm(dict_parm)
    # print_vxyz(dict_vxyz)

    if survey is not None:
        dict_sgmt = survey.geometry
    else:
        dict_sgmt = {
            'P1_ILNO': 1,
            'P1_XLNO': 1,
            'P1_CRSX': dict_vxyz['AXIS_ORX'],
            'P1_CRSY': dict_vxyz['AXIS_ORY'],
            'P2_ILNO': 1,
            'P2_XLNO': NXL,
            'P2_CRSX': dict_vxyz['AXIS_XLX'],
            'P2_CRSY': dict_vxyz['AXIS_XLY'],
            'P3_ILNO': NIL,
            'P3_XLNO': 1,
            'P3_CRSX': dict_vxyz['AXIS_ILX'],
            'P3_CRSY': dict_vxyz['AXIS_ILY']
        }
    # print_sgmt(dict_sgmt)

    # get the dict_vidx
    dict_vidx = get_vidx_from_parm(dict_parm, dict_sgmt)

    prop_name = dict_parm['DATA_VEL_TYPE']
    cube.add_property(prop_name, array=array3d)

    # prop_name = 'test'
    # array3d = np.random.randn(NIL, NXL, NDP)
    # cube.add_property(prop_name, array=array3d)

    cube.dict_parm = dict_parm
    cube.dict_vidx = dict_vidx
    cube.dict_vxyz = dict_vxyz
    # cube.dict_sgmt = dict_sgmt  # TODO deprecate by survey
    cube.survey = survey


def write_parm(parmfn, dict_parm):
    print("Writing", parmfn)
    with open(parmfn, 'w') as f:
        f.write("NTRACE %i\n" % dict_parm['NTRACE'])
        f.write("NPANEL %i\n" % dict_parm['NPANEL'])
        f.write("NSAMPLE %i\n" % dict_parm['NSAMPLE'])
        f.write("TRACE_START %.3f\n" % dict_parm['TRACE_START'])
        f.write("PANEL_START %.3f\n" % dict_parm['PANEL_START'])
        f.write("SAMPLE_START %.3f\n" % dict_parm['SAMPLE_START'])
        f.write("TRACE_INC %.3f\n" % dict_parm['TRACE_INC'])
        f.write("PANEL_INC %.3f\n" % dict_parm['PANEL_INC'])
        f.write("SAMPLE_INC %.3f\n" % dict_parm['SAMPLE_INC'])
        f.write("DATA_PRECISION %i\n" % dict_parm['DATA_PRECISION'])
        f.write("DATA_VEL_TYPE %s\n" % dict_parm['DATA_VEL_TYPE'])
        f.write("DEPTH_OUTPUT %s\n" % dict_parm['DEPTH_OUTPUT'])
        f.write("TRACE_UNIT %s\n" % dict_parm['TRACE_UNIT'])
        f.write("PANEL_UNIT %s\n" % dict_parm['PANEL_UNIT'])
        f.write("SAMPLE_UNIT %s\n" % dict_parm['SAMPLE_UNIT'])
        f.write("DATA_UNIT %s\n" % dict_parm['DATA_UNIT'])
        f.write("DX %.3f %.3f\n" % (dict_parm['TRDX'], dict_parm['TRDY']))
        f.write("DY %.3f %.3f\n" % (dict_parm['PNDX'], dict_parm['PNDY']))


def read_seis(seisfn, npanel, ntrace, nsample):
    """
    Read .seis file of binary cube
    Return one 3D array
    """
    print("Reading", seisfn)
    f = open(seisfn, 'rb')
    # dtype = np.dtype('f4') # 32-bit float
    array1d = np.fromfile(f, dtype='float32')
    ngrid = len(array1d)
    # print(ngrid)
    # create array
    # array1d_unpack = np.zeros(ngrid)
    # unpack then convert tuple to array
    fmt = '>' + str(ngrid) + 'f'
    array1d_unpack = np.array(struct.unpack(fmt, array1d), 'float32')
    # unpack one-by-one, much slower than together
    # for i in range(len(array1d)):
    #   array1d_unpack[i] = struct.unpack('>f', array1d[i])[0]
    # shape 1D to 3D array
    array3d = array1d_unpack.reshape((npanel, ntrace, nsample))
    # print(array3d[npanel/2,ntrace/2,nsample/2])
    # print(array1d.shape)
    # print(array3d.shape)
    print("Return array3d data type:", array3d.dtype)
    return array3d


def write_seis(seisfn, array3d):
    print("Writing", seisfn)
    fh = open(seisfn, 'wb')
    if array3d.dtype != 'float32':
        array3d = array3d.astype('float32', copy=False)
    print("Write data type:", array3d.dtype)
    array1d = array3d.flatten()
    npts = len(array1d)
    print("Write number of points:", npts)
    # Cap to prevent memory fail and computer crash
    nptsCap = 100000000  # 100 million points ~ 400MB
    if npts < nptsCap:
        fmt = '>' + str(npts) + 'f'
        array1dPack = struct.pack(fmt, *array1d)
        fh.write(array1dPack)
    else:
        # split to smaller arrays
        nsplit = int(npts / nptsCap) + 1
        print("So many points - Split to %i parts" % nsplit)
        array1dSplit = np.array_split(array1d, nsplit)
        for i in range(nsplit):
            print("Writing part %i of %i" % (i, nsplit))
            array1dPart = array1dSplit[i]
            nptsPart = len(array1dPart)
            fmt = '>' + str(nptsPart) + 'f'
            array1dPartPack = struct.pack(fmt, *array1dPart)
            fh.write(array1dPartPack)
            # These two may not be necessary
            # With it, memory use is at low level.
            # Run is a tiny slower (1/50 minutes for 38GB file).
            fh.flush()  # flush internal buffer to OS buffer
            os.fsync(fh.fileno())  # push OS buffer to disk
    # array3d.tofile(fh) # not work for VTB loader
    fh.close()
    print("Write seis is completed.")


def read_parm(parmfn):
    """
    Read .parm which comes along with .seis file
    - parmfn : string, parm filename
    Return a dictionary defining the grid mesh
    """
    # set dictionary default key and value
    dict_parm = {'DATA_PRECISION': 4, 'DATA_VEL_TYPE': 'AVGVEL',
        'DEPTH_OUTPUT': 'POSITIVE', 'TRACE_UNIT': 'METERS',
        'PANEL_UNIT': 'METERS', 'SAMPLE_UNIT': 'MSECS',
        'DATA_UNIT': 'METERSPERSEC'}
    print("Reading", parmfn)
    f = open(parmfn, 'r')
    for line in f:
        line = line.strip()
        columns = line.split()
        key = columns[0]
        keys_with_value_int = ['NTRACE', 'NPANEL', 'NSAMPLE', 'DATA_PRECISION']
        keys_with_value_float = ['TRACE_START', 'PANEL_START', 'SAMPLE_START',
            'TRACE_INC', 'PANEL_INC', 'SAMPLE_INC', 'DATA_MIN', 'DATA_MAX']
        keys_with_value_string = ['DATA_VEL_TYPE', 'DEPTH_OUTPUT',
            'TRACE_UNIT', 'PANEL_UNIT', 'SAMPLE_UNIT', 'DATA_UNIT']
        if key in keys_with_value_int:
            value = int(columns[1])
            dict_parm[key] = value
        if key in keys_with_value_float:
            value = float(columns[1])
            dict_parm[key] = value
        if key in keys_with_value_string:
            value = columns[1]  # a string
            dict_parm[key] = value
        if key == 'DX':
            # Vector of Trace I to I+1: TRDX, TRDY
            key1 = 'TRDX'
            value1 = float(columns[1])
            dict_parm[key1] = value1
            key2 = 'TRDY'
            value2 = float(columns[2])
            dict_parm[key2] = value2
        if key == 'DY':
            # Vector of Panel I to I+1: PNDX, PNDY
            key1 = 'PNDX'
            value1 = float(columns[1])
            dict_parm[key1] = value1
            key2 = 'PNDY'
            value2 = float(columns[2])
            dict_parm[key2] = value2
    f.close()
    # for key, value in dict_parm.items():
    #   print(key, value)

    # Correct the parm file exported by Gocad VTB plugin
    stepTrace = sqrt(dict_parm['TRDX']**2 + dict_parm['TRDY']**2)
    stepPanel = sqrt(dict_parm['PNDX']**2 + dict_parm['PNDY']**2)
    if dict_parm['TRACE_INC'] != stepTrace:
        dict_parm['TRACE_INC'] = stepTrace
    if dict_parm['PANEL_INC'] != stepPanel:
        dict_parm['PANEL_INC'] = stepPanel
    print("WARNING: fixed increment when read file.")

    return dict_parm


def read_parm_old(parmfn):
    """
    Read .parm which comes along with .seis file
    Return parm defining the grid mesh
    """
    # An example parm file
    # ---------------------- #
    # NTRACE  225
    # NPANEL  282
    # NSAMPLE 500
    # TRACE_START  144884
    # PANEL_START  378608
    # SAMPLE_START 10
    # TRACE_INC  80.557
    # PANEL_INC  -80.557
    # SAMPLE_INC 10
    # DATA_PRECISION 4
    # DATA_VEL_TYPE AVGVEL
    # TRACE_UNIT  METERS
    # PANEL_UNIT  METERS
    # SAMPLE_UNIT MSECS
    # DATA_UNIT METERSPERSEC
    # DX 80.557 59.2501
    # DY 59.2501 -80.557
    # DATA_MIN 1418.21118164
    # DATA_MAX 4437.23632812
    # ---------------------- #
    print("Reading", parmfn)
    f = open(parmfn, 'r')
    for line in f:
        line = line.strip()
        columns = line.split()
        if columns[0] == 'NTRACE':
            ntrace = int(columns[1])
        if columns[0] == 'NPANEL':
            npanel = int(columns[1])
        if columns[0] == 'NSAMPLE':
            nsample = int(columns[1])
        if columns[0] == 'TRACE_START':
            ox = float(columns[1])
        if columns[0] == 'PANEL_START':
            oy = float(columns[1])
        if columns[0] == 'SAMPLE_START':
            oz = float(columns[1])
        if columns[0] == 'SAMPLE_INC':
            dz = float(columns[1])
        if columns[0] == 'DX':
            TRDX = float(columns[1])
            TRDY = float(columns[2])
        if columns[0] == 'DY':
            PNDX = float(columns[1])
            PNDY = float(columns[2])
    f.close()
    return ntrace,npanel,nsample,ox,oy,oz,dz,TRDX,TRDY,PNDX,PNDY


# def read_bin(binfn, NIL, NXL, NDP, dtype='float32'):
#     """
#     Read .bin file in binary format
#     Return one 3D array
#     """
#     print("Reading", binfn)
#     f = open(binfn, 'rb')
#     array1d = np.fromfile(f, dtype=dtype)
#     array3d = array1d.reshape(NIL, NXL, NDP)
#     print("Return array3d data type:", array3d.dtype)
#     return array3d
#
#
# def write_bin(binfn, array3d, dtype='float32'):
#     print("Writing", binfn)
#     fh = open(binfn, 'wb')
#     if array3d.dtype != dtype:
#         array3d = array3d.astype(dtype, copy=False)
#     print("Write data type:", array3d.dtype)
#     array3d.tofile(fh)
#     fh.close()
#
#
# def write_zhu(outfn, zhu, fmt='seis', dtype='float32'):
#     """
#     Deprecate write_zhu. Moved to class.method Cube.write
#     Write Cube to files
#     - outfn : string, output filename
#     - zhu : Cube, input custom data object
#     - fmt : string, 'seis' or 'bin'
#     - dtype : string, data type for bin format
#     """
#     # get parm filename
#     fpre = os.path.splitext(outfn)[0]
#     parmfn = fpre + ".parm"
#     # write parm file
#     dict_parm = zhu.dict_parm
#     write_parm(parmfn, dict_parm)
#     # write vidx file
#     vidxfn = fpre + ".vidx"
#     dict_vidx = zhu.dict_vidx
#     write_vidx(vidxfn, dict_vidx)
#     # write vxyz file
#     vxyzfn = fpre + ".vxyz"
#     dict_vxyz = zhu.dict_vxyz
#     write_vxyz(vxyzfn, dict_vxyz)
#     # write cube file
#     array3d = zhu.array3d
#     if fmt == 'seis':
#         write_seis(outfn, array3d)
#     elif fmt == 'bin':
#         write_bin(outfn, array3d, dtype)
#     else:
#         raise ValueError("Unknown file format.")


# From .parm File
# DX 80.557 59.2501
# DY 59.2501 -80.557
# Vector of Trace I to I+1: TRDX, TRDY
# Vector of Panel I to I+1: PNDX, PNDY
# Index variable for Panel-Trace is m-n or i-j
# Xmn = Xij + (m-i)*PNDX + (n-j)*TRDX
# Ymn = Yij + (m-i)*PNDY + (n-j)*TRDY
#    TRDX = 80.557
#    TRDY = 59.2501
#    PNDX = 59.2501
#    PNDY = -80.557

# Origin coordinate and index
#    ox = 144884
#    oy = 378608
#    oi = 0
#    oj = 0

# Input: TRDX, TRDY, PNDX, PNDY, i, j, Xij, Yij, m, n
# Output: Xmn, Ymn
# Xmn = Xij + (m-i)*PNDX + (n-j)*TRDX
# Ymn = Yij + (m-i)*PNDY + (n-j)*TRDY
#    m = 100
#    n = 100
#    xmn = ox + (m-oi)*PNDX + (n-oj)*TRDX
#    ymn = oy + (m-oi)*PNDY + (n-oj)*TRDY
#    print(xmn, ymn)

# Input: TRDX, TRDY, PNDX, PNDY, i, j, Xij, Yij, Xmn, Ymn
# Assume i=0 j=0
# Output: m, n
#    x = 152277
#    y = 368310
#    u = PNDY*(x-ox) - PNDX*(y-oy)
#    d = PNDY*TRDX    - PNDX*TRDY
#    n = int(round( u / d ))
#    m = int(round( (y-oy - n*TRDY) / PNDY ))
#    print(m, n)
