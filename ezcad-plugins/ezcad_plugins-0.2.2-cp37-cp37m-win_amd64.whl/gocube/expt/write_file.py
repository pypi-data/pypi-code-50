# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from ezcad.utils.functions import myprint


def write_vxyz(fn, dict_vxyz):
    myprint("--Writing--", fn)
    with open(fn, 'w') as f:
        f.write("AXIS_OR %.3f %.3f %.3f\n" % (dict_vxyz['AXIS_ORX'],
            dict_vxyz['AXIS_ORY'], dict_vxyz['AXIS_ORZ']))
        f.write("AXIS_DP %.3f %.3f %.3f\n" % (dict_vxyz['AXIS_DPX'],
            dict_vxyz['AXIS_DPY'], dict_vxyz['AXIS_DPZ']))
        f.write("AXIS_XL %.3f %.3f %.3f\n" % (dict_vxyz['AXIS_XLX'],
            dict_vxyz['AXIS_XLY'], dict_vxyz['AXIS_XLZ']))
        f.write("AXIS_IL %.3f %.3f %.3f\n" % (dict_vxyz['AXIS_ILX'],
            dict_vxyz['AXIS_ILY'], dict_vxyz['AXIS_ILZ']))


def write_sgmt(fn, dict_sgmt):
    myprint("--Writing--", fn)
    with open(fn, 'w') as f:
        f.write("P1_ILNO %i\n" % dict_sgmt['P1_ILNO'])
        f.write("P1_XLNO %i\n" % dict_sgmt['P1_XLNO'])
        f.write("P1_CRSX %.3f\n" % dict_sgmt['P1_CRSX'])
        f.write("P1_CRSY %.3f\n" % dict_sgmt['P1_CRSY'])
        f.write("P2_ILNO %i\n" % dict_sgmt['P2_ILNO'])
        f.write("P2_XLNO %i\n" % dict_sgmt['P2_XLNO'])
        f.write("P2_CRSX %.3f\n" % dict_sgmt['P2_CRSX'])
        f.write("P2_CRSY %.3f\n" % dict_sgmt['P2_CRSY'])
        f.write("P3_ILNO %i\n" % dict_sgmt['P3_ILNO'])
        f.write("P3_XLNO %i\n" % dict_sgmt['P3_XLNO'])
        f.write("P3_CRSX %.3f\n" % dict_sgmt['P3_CRSX'])
        f.write("P3_CRSY %.3f\n" % dict_sgmt['P3_CRSY'])


def write_vidx(fn, dict_vidx):
    myprint("--Writing--", fn)
    with open(fn, 'w') as f:
        f.write("IL_FRST %i\n" % dict_vidx['IL_FRST'])
        f.write("IL_LAST %i\n" % dict_vidx['IL_LAST'])
        f.write("IL_NCRT %i\n" % dict_vidx['IL_NCRT'])
        f.write("IL_AMNT %i\n" % dict_vidx['IL_AMNT'])
        f.write("XL_FRST %i\n" % dict_vidx['XL_FRST'])
        f.write("XL_LAST %i\n" % dict_vidx['XL_LAST'])
        f.write("XL_NCRT %i\n" % dict_vidx['XL_NCRT'])
        f.write("XL_AMNT %i\n" % dict_vidx['XL_AMNT'])
        f.write("DP_FRST %i\n" % dict_vidx['DP_FRST'])
        f.write("DP_LAST %i\n" % dict_vidx['DP_LAST'])
        f.write("DP_NCRT %i\n" % dict_vidx['DP_NCRT'])
        f.write("DP_AMNT %i\n" % dict_vidx['DP_AMNT'])


# def write5c(filename, m, n, x, y, z, xprecision=13, yprecision=13):
#   with open(filename,'w') as f:
#     for a, b, c, d, e in izip(m, n, x, y, z):
#       print >> f, "%i %i %f %f %f" % (a, b, c, d, e)
#   return
#
# # write XY numbers to ASCII file
# def writexy(filename, x, y, xprecision=13, yprecision=13):
#   with open(filename,'w') as f:
#     for a, b in itertools.izip(x, y):
#       print >> f, "%.*g %.*g" % (xprecision, a, yprecision, b)
#   return
#
#
# def write_list2d(fn, list2d, delim='space', header=None):
#     """
#     Write 2D list to file
#     - fn : string, filename
#     - list2d : 2D list, can also be 2D array
#       The 1st dimension is [number of points].
#       The 2nd dimension is [number of attributes in each point].
#     """
#     myprint("--Writing--", fn)
#     with open(fn, 'w') as f:
#         if header is not None:
#             f.writelines(header + '\n')
#         if delim == 'space' or delim == 'spaces' or delim == ' ':
#             f.writelines(' '.join(str(j) for j in i) + '\n' for i in list2d)
#         elif delim == 'comma' or delim == ',':
#             f.writelines(','.join(str(j) for j in i) + '\n' for i in list2d)
#         else:
#             raise ValueError('Unknown deliminator.')
#
#
# def write_list3d(fn, list3d):
#     """
#     Write 3D list to file
#     - fn : string, filename
#     - list3d : 3D list.
#       The 1st dimension is [number of wells].
#       The 2nd dimension is [number of points in each well].
#       The 3rd dimension is [number of attributes in each point].
#     """
#     myprint("--Writing--", fn)
#     with open(fn, 'w') as f:
#         for list2d in list3d:
#             f.writelines(' '.join(str(j) for j in i) + '\n' for i in list2d)
