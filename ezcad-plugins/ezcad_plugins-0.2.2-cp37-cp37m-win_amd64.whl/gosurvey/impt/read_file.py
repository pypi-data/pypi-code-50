# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from ezcad.utils.functions import myprint


def read_vt3dc(fn):
    """
    -i- fn : string, full-path filename of the vt3dc file.
    -o- dict_sgmt : dictionary, survey geometry linking XY and LN.
    """
    dict_sgmt = {}
    myprint("--Reading--", fn)
    f = open(fn, 'r')
    for line in f:
        line = line.strip()
        columns = line.split()
        key = columns[0]

        if key == "X_ORIGIN":
            dict_sgmt["P1_CRSX"] = float(columns[1])
        if key == "Y_ORIGIN":
            dict_sgmt["P1_CRSY"] = float(columns[1])
        if key == "MINIMUM_INLINE_NUMBER":
            dict_sgmt["P1_ILNO"] = int(columns[1])
        if key == "MINIMUM_CROSSLINE_NUMBER":
            dict_sgmt["P1_XLNO"] = int(columns[1])

        if key == "X_FIRST_INLINE_END":
            dict_sgmt["P2_CRSX"] = float(columns[1])
        if key == "Y_FIRST_INLINE_END":
            dict_sgmt["P2_CRSY"] = float(columns[1])
        if key == "MINIMUM_INLINE_NUMBER":
            dict_sgmt["P2_ILNO"] = int(columns[1])
        if key == "MAXIMUM_CROSSLINE_NUMBER":
            dict_sgmt["P2_XLNO"] = int(columns[1])
        # dict_sgmt["P2_ILNO"] = dict_sgmt["P1_ILNO"]

        if key == "X_FIRST_CROSSLINE_END":
            dict_sgmt["P3_CRSX"] = float(columns[1])
        if key == "Y_FIRST_CROSSLINE_END":
            dict_sgmt["P3_CRSY"] = float(columns[1])
        if key == "MAXIMUM_INLINE_NUMBER":
            dict_sgmt["P3_ILNO"] = int(columns[1])
        if key == "MINIMUM_CROSSLINE_NUMBER":
            dict_sgmt["P3_XLNO"] = int(columns[1])
        # dict_sgmt["P3_XLNO"] = dict_sgmt["P1_XLNO"]
    f.close()
    return dict_sgmt


def read_sgmt(fn):
    """
    Read .sgmt file of survey corners: ILNO XLNO X Y.
    - fn : string, sgmt filename
    Return a dictionary linking LN and XY.
    """
    dict_sgmt = {}
    myprint("--Reading--", fn)
    f = open(fn, 'r')
    for line in f:
        line = line.strip()
        columns = line.split()
        key = columns[0]
        keys_with_value_int = ['P1_ILNO', 'P1_XLNO', 'P2_ILNO', 'P2_XLNO',
                               'P3_ILNO', 'P3_XLNO']
        keys_with_value_float = ['P1_CRSX', 'P1_CRSY', 'P2_CRSX', 'P2_CRSY',
                                 'P3_CRSX', 'P3_CRSY']
        if key in keys_with_value_int:
            value = int(columns[1])
            dict_sgmt[key] = value
        if key in keys_with_value_float:
            value = float(columns[1])
            dict_sgmt[key] = value
    f.close()
    return dict_sgmt


def read_sgmt_old(fn):
    """
    Read .sgmt which contains survey corners: ILNO XLNO X Y.
    It is also called the Survey Grid Mesh definition.
    It is also called the Survey GeoMeTry file.
    It is the same for the whole project or survey.
    Return parameters linking ILXL and XY.
    """
    # An example sgmt file
    # ---------------------- #
    # P1_ILNO 1257
    # P1_XLNO 161
    # P1_CRSX 186113.60
    # P1_CRSY 1781475.64
    # P2_ILNO 1257
    # P2_XLNO 10433
    # P2_CRSX 250966.38
    # P2_CRSY 2029948.88
    # P3_ILNO 3307
    # P3_XLNO 161
    # P3_CRSX 235702.41
    # P3_CRSY 1768532.79
    # ---------------------- #
    myprint("--Reading--", fn)
    f = open(fn, 'r')
    for line in f:
        line = line.strip()
        columns = line.split()
        if columns[0] == 'P1_ILNO':
            P1_ILNO = int(columns[1])
        if columns[0] == 'P1_XLNO':
            P1_XLNO = int(columns[1])
        if columns[0] == 'P1_CRSX':
            P1_CRSX = float(columns[1])
        if columns[0] == 'P1_CRSY':
            P1_CRSY = float(columns[1])
        if columns[0] == 'P2_ILNO':
            P2_ILNO = int(columns[1])
        if columns[0] == 'P2_XLNO':
            P2_XLNO = int(columns[1])
        if columns[0] == 'P2_CRSX':
            P2_CRSX = float(columns[1])
        if columns[0] == 'P2_CRSY':
            P2_CRSY = float(columns[1])
        if columns[0] == 'P3_ILNO':
            P3_ILNO = int(columns[1])
        if columns[0] == 'P3_XLNO':
            P3_XLNO = int(columns[1])
        if columns[0] == 'P3_CRSX':
            P3_CRSX = float(columns[1])
        if columns[0] == 'P3_CRSY':
            P3_CRSY = float(columns[1])
    f.close()

    # P1 is the survey origin, first inline/xline start.
    # P2 is the first crossline end, so P1_ILNO = P2_ILNO
    # P3 is the first inline end, so P1_XLNO = P3_XLNO
    # if P1_ILNO != P2_ILNO :
    #     raise ValueError("P1_ILNO must equal P2_ILNO.")
    # if P1_XLNO != P3_XLNO :
    #     raise ValueError("P1_XLNO must equal P3_XLNO.")
    # The three points are used to calculate IL/XL unit vector.
    # The getVector function in grid3D.py can handle any three
    # points, which do not have to be the line ends or corners.
    # However, the farther the three points are, the calculated
    # unit vectors are more accurate and strict orthogonal, so
    # the more precise converting line numbers from/to XYs.

    # print to screen for QC
    myprint("P1_ILNO, P1_XLNO, P1_CRSX, P1_CRSY =",
            P1_ILNO, P1_XLNO, P1_CRSX, P1_CRSY)
    myprint("P2_ILNO, P2_XLNO, P2_CRSX, P2_CRSY =",
            P2_ILNO, P2_XLNO, P2_CRSX, P2_CRSY)
    myprint("P3_ILNO, P3_XLNO, P3_CRSX, P3_CRSY =",
            P3_ILNO, P3_XLNO, P3_CRSX, P3_CRSY)

    return P1_ILNO, P1_XLNO, P1_CRSX, P1_CRSY, \
           P2_ILNO, P2_XLNO, P2_CRSX, P2_CRSY, \
           P3_ILNO, P3_XLNO, P3_CRSX, P3_CRSY
