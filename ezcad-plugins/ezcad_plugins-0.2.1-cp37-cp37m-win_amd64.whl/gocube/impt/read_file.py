# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

# Author: Joseph Zhu
# Date: 07/21/2016


def read_vxyz(fn):
    """Read vxyz file.

    :param fn: filename
    :type fn: str
    :return: volume corners XYZ
    :rtype: dict
    """
    dict_vxyz = {}
    print("--Reading--", fn)
    f = open(fn, 'r')
    for line in f:
        line = line.strip()
        columns = line.split()
        axis = columns[0]
        if axis == "AXIS_OR":
            dict_vxyz['AXIS_ORX'] = float(columns[1])
            dict_vxyz['AXIS_ORY'] = float(columns[2])
            dict_vxyz['AXIS_ORZ'] = float(columns[3])
        if axis == "AXIS_DP":
            dict_vxyz['AXIS_DPX'] = float(columns[1])
            dict_vxyz['AXIS_DPY'] = float(columns[2])
            dict_vxyz['AXIS_DPZ'] = float(columns[3])
        if axis == "AXIS_XL":
            dict_vxyz['AXIS_XLX'] = float(columns[1])
            dict_vxyz['AXIS_XLY'] = float(columns[2])
            dict_vxyz['AXIS_XLZ'] = float(columns[3])
        if axis == "AXIS_IL":
            dict_vxyz['AXIS_ILX'] = float(columns[1])
            dict_vxyz['AXIS_ILY'] = float(columns[2])
            dict_vxyz['AXIS_ILZ'] = float(columns[3])
    f.close()
    return dict_vxyz


def read_vidx(fn):
    """Read vidx file.

    :param fn: filename
    :type fn: str
    :return: volume indexes
    :rtype: dict
    """
    dict_vidx = {}
    if fn == "init":
        # initialize without file, for Class init method
        dict_vidx['IL_FRST'] = -100
        dict_vidx['IL_LAST'] = 100
        dict_vidx['IL_NCRT'] = 1
        dict_vidx['IL_AMNT'] = 201
        dict_vidx['XL_FRST'] = -100
        dict_vidx['XL_LAST'] = 100
        dict_vidx['XL_NCRT'] = 1
        dict_vidx['XL_AMNT'] = 201
        dict_vidx['DP_FRST'] = -100
        dict_vidx['DP_LAST'] = 100
        dict_vidx['DP_NCRT'] = 1
        dict_vidx['DP_AMNT'] = 201
    else:
        print("--Reading--", fn)
        f = open(fn, 'r')
        for line in f:
            line = line.strip()
            columns = line.split()
            key = columns[0]
            value = int(columns[1])
            dict_vidx[key] = value
        f.close()
    return dict_vidx


# def read_vidx_old(fn):
#     """
#     Read .vidx which contains the index for 3D volume.
#     It is specific for each 3D volume or Segy file, like
#     the parm file is specific for each seis file.
#     Return an array defining and indexing the grid mesh.
#     """
#     # An example vidx file
#     # ---------------------- #
#     # IL_FRST 2100
#     # IL_LAST 2600
#     # IL_NCRT 1
#     # IL_AMNT 501
#     # XL_FRST 2500
#     # XL_LAST 3000
#     # XL_NCRT 1
#     # XL_AMNT 501
#     # DP_FRST 4500
#     # DP_LAST 6000
#     # DP_NCRT 4
#     # DP_AMNT 376
#     # ---------------------- #
#     if fn == "init":
#         # initialize without file, for Class init method
#         IL_FRST = 0
#         IL_LAST = 100
#         IL_NCRT = 1
#         IL_AMNT = 101
#         XL_FRST = 0
#         XL_LAST = 100
#         XL_NCRT = 1
#         XL_AMNT = 101
#         DP_FRST = 0
#         DP_LAST = 100
#         DP_NCRT = 1
#         DP_AMNT = 101
#     else:
#         print("--Reading--", fn)
#         f = open(fn, 'r')
#         for line in f:
#             line = line.strip()
#             columns = line.split()
#             if columns[0] == 'IL_FRST':
#                 IL_FRST = int(columns[1])
#             if columns[0] == 'IL_LAST':
#                 IL_LAST = int(columns[1])
#             if columns[0] == 'IL_NCRT':
#                 IL_NCRT = int(columns[1])
#             if columns[0] == 'IL_AMNT':
#                 IL_AMNT = int(columns[1])
#             if columns[0] == 'XL_FRST':
#                 XL_FRST = int(columns[1])
#             if columns[0] == 'XL_LAST':
#                 XL_LAST = int(columns[1])
#             if columns[0] == 'XL_NCRT':
#                 XL_NCRT = int(columns[1])
#             if columns[0] == 'XL_AMNT':
#                 XL_AMNT = int(columns[1])
#             if columns[0] == 'DP_FRST':
#                 DP_FRST = int(columns[1])
#             if columns[0] == 'DP_LAST':
#                 DP_LAST = int(columns[1])
#             if columns[0] == 'DP_NCRT':
#                 DP_NCRT = int(columns[1])
#             if columns[0] == 'DP_AMNT':
#                 DP_AMNT = int(columns[1])
#         f.close()
#
#     # print to screen for QC
#     print("IL_FRST, IL_LAST, IL_NCRT, IL_AMNT =",
#             IL_FRST, IL_LAST, IL_NCRT, IL_AMNT)
#     print("XL_FRST, XL_LAST, XL_NCRT, XL_AMNT =",
#             XL_FRST, XL_LAST, XL_NCRT, XL_AMNT)
#     print("DP_FRST, DP_LAST, DP_NCRT, DP_AMNT =",
#             DP_FRST, DP_LAST, DP_NCRT, DP_AMNT)
#
#     # make an array for compact pass in/out functions
#     cubeIndex = np.zeros(13, dtype=int)
#     cubeIndex[1] = IL_FRST
#     cubeIndex[2] = IL_LAST
#     cubeIndex[3] = IL_NCRT
#     cubeIndex[4] = IL_AMNT
#     cubeIndex[5] = XL_FRST
#     cubeIndex[6] = XL_LAST
#     cubeIndex[7] = XL_NCRT
#     cubeIndex[8] = XL_AMNT
#     cubeIndex[9] = DP_FRST
#     cubeIndex[10] = DP_LAST
#     cubeIndex[11] = DP_NCRT
#     cubeIndex[12] = DP_AMNT
#
#     return cubeIndex
