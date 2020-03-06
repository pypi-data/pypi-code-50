# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.


def vidx_dict2list(dict_vidx):
    il0 = dict_vidx['IL_FRST']
    il1 = dict_vidx['IL_LAST']
    ils = dict_vidx['IL_NCRT']
    iln = dict_vidx['IL_AMNT']
    xl0 = dict_vidx['XL_FRST']
    xl1 = dict_vidx['XL_LAST']
    xls = dict_vidx['XL_NCRT']
    xln = dict_vidx['XL_AMNT']
    dp0 = dict_vidx['DP_FRST']
    dp1 = dict_vidx['DP_LAST']
    dps = dict_vidx['DP_NCRT']
    dpn = dict_vidx['DP_AMNT']
    return [il0, il1, ils, iln,
            xl0, xl1, xls, xln,
            dp0, dp1, dps, dpn]


def vidx_format_dtype(dict_vidx):
    """
    Fix data type. It helps populate GUI with correct integer or float,
    and save you some ValueError later on.
    """
    dict_vidx['IL_FRST'] = int(dict_vidx['IL_FRST'])
    dict_vidx['IL_LAST'] = int(dict_vidx['IL_LAST'])
    dict_vidx['IL_NCRT'] = int(dict_vidx['IL_NCRT'])
    dict_vidx['IL_AMNT'] = int(dict_vidx['IL_AMNT'])
    dict_vidx['XL_FRST'] = int(dict_vidx['XL_FRST'])
    dict_vidx['XL_LAST'] = int(dict_vidx['XL_LAST'])
    dict_vidx['XL_NCRT'] = int(dict_vidx['XL_NCRT'])
    dict_vidx['XL_AMNT'] = int(dict_vidx['XL_AMNT'])
    dict_vidx['DP_FRST'] = float(dict_vidx['DP_FRST'])
    dict_vidx['DP_LAST'] = float(dict_vidx['DP_LAST'])
    dict_vidx['DP_NCRT'] = float(dict_vidx['DP_NCRT'])
    dict_vidx['DP_AMNT'] = int(dict_vidx['DP_AMNT'])
