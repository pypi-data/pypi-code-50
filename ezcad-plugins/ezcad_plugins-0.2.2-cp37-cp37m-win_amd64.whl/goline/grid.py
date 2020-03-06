# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""
Read ILNO,XLNO of points defining an arbitrary line.
Read the dict_vidx of cube.
Get the nearest cube voxel along the line.

Every thing in this module is done in (ILNO,XLNO) domain.
If provided XYs, run gridPoints.py first to get ILNO,XLNO.
"""

import numpy as np
from scipy import interpolate
from ezcad.utils.functions import myprint


def grid_line(line, dict_vidx):
    """
    -i- line : array, 2D, [ILNO, XLNO] of points define the line.
    -i- dict_vidx : dictionary, volume indexes.
    -o- grid : array, 2D, [ILNO, XLNO] of points in cube along the line.
    """

    IL_FRST = dict_vidx['IL_FRST']
    IL_LAST = dict_vidx['IL_LAST']
    IL_AMNT = dict_vidx['IL_AMNT']
    XL_FRST = dict_vidx['XL_FRST']
    XL_LAST = dict_vidx['XL_LAST']
    XL_AMNT = dict_vidx['XL_AMNT']

    ilnoInCube = np.linspace(IL_FRST, IL_LAST, IL_AMNT)
    xlnoInCube = np.linspace(XL_FRST, XL_LAST, XL_AMNT)

    myprint('Input line =', line)
    ilno = line[:, 0]
    xlno = line[:, 1]

    ilnoSgmts = []
    xlnoSgmts = []

    numSgmt = len(line) - 1
    for i in range(numSgmt):
        myprint("Gridding line segment", i+1)

        # prepare interpolation function
        sgmtStartX = ilno[i]
        sgmtStartY = xlno[i]
        sgmtEndX = ilno[i+1]
        sgmtEndY = xlno[i+1]
        x = np.zeros(2)
        y = np.zeros(2)
        x[0] = sgmtStartX
        y[0] = sgmtStartY
        x[1] = sgmtEndX
        y[1] = sgmtEndY
        fx2y = interpolate.interp1d(x, y, kind='linear')
        fy2x = interpolate.interp1d(y, x, kind='linear')

        # interpolate on very ILNO, select later
        if sgmtStartX < sgmtEndX:
            ilstep = 1
        else:
            ilstep = -1
        ilnoIntpI2X = np.arange(sgmtStartX, sgmtEndX, ilstep)
        xlnoIntpI2X = fx2y(ilnoIntpI2X)

        # interpolate on very XLNO, select later
        if sgmtStartY < sgmtEndY:
            xlstep = 1
        else:
            xlstep = -1
        xlnoIntpX2I = np.arange(sgmtStartY, sgmtEndY, xlstep)
        ilnoIntpX2I = fy2x(xlnoIntpX2I)

        # best practice to make a sub array
        # a = np.arange(2000, 2100, 4)
        # b = np.where(np.logical_and(a >= 2020, a <= 2050))
        # c = a[b]
        # myprint(a)
        # myprint(b)
        # myprint(c)

        # find ILNO that are in this segment and ilnoInCube
        a = ilnoInCube
        if sgmtStartX < sgmtEndX:
            left = sgmtStartX
            right = sgmtEndX
        else:
            left = sgmtEndX
            right = sgmtStartX
        # np.where get indices
        # np.logical_and set two conditions
        # assume ilnoInCube is always increasing
        b = np.where(np.logical_and(a >= left, a <= right))
        # b is array of indices whose elements satisfy the condition
        c = a[b]  # c.shape (n,)
        # make d in the order same as segment
        if sgmtStartX < sgmtEndX:
            d = c
        else:
            d = c[::-1]  # reverse
            # myprint(d.shape)
            # myprint(d)
        ilnoInCubeInSgmt = d

        # find XLNO that are in this segment and ilnoInCube
        a = xlnoInCube
        if sgmtStartY < sgmtEndY:
            left = sgmtStartY
            right = sgmtEndY
        else:
            left = sgmtEndY
            right = sgmtStartY
        # np.where get indices
        # np.logical_and set two conditions
        # assume ilnoInCube is always increasing
        b = np.where(np.logical_and(a >= left, a <= right))
        # b is array of indices whose elements satisfy the condition
        c = a[b] # c.shape (n,)
        # make d in the order same as segment
        if sgmtStartY < sgmtEndY:
            d = c
        else:
            d = c[::-1]  # reverse
            # myprint(d.shape)
            # myprint(d)
        xlnoInCubeInSgmt = d

        if len(ilnoInCubeInSgmt) >= len(xlnoInCubeInSgmt):
            # line angle to x-axis is less than 45 degrees
            # ilnoInCubeInSgmt is the base to loop through
            # xlnoInCubeInSgmt is the goal
            a = ilnoInCubeInSgmt
            b = np.zeros(len(a))
            for i in range(len(a)):
                # 1st search to find xGrid in interpolation xIntp
                # 2nd search to find yIntp corresponding to xGrid
                # 3rd search to find yGrid corresponding to yIntp
                # xControl -> xIntp -> xGrid -> yIntp -> yGrid
                # -- 1st search -- #
                u = a[i]
                # ilnoIntp is the segment interpolated at every inline
                array = ilnoIntpI2X
                # index in ilnoIntp whose element is ilnoInCubeInSgmt
                idx = (np.abs(array-u)).argmin()  # find nearest
                # -- 2nd search -- #
                # same index in xlnoIntp gives the XLNO interpolated
                v = xlnoIntpI2X[idx]
                # -- 3rd search -- #
                # assume xlnoInCube is always increasing
                if v < xlnoInCube[0] or v > xlnoInCube[-1]:
                  # for XLNO that are outside cube
                  w = -1
                else:
                  # for XLNO that are inside cube
                  # find the grid nearest to the XLNO
                  array = xlnoInCube
                  idx = (np.abs(array-v)).argmin()  # find nearest
                  w = array[idx]
                b[i] = w
                # xlnoInCubeInSgmt = b

        else:
            # line angle to x-axis is more than 45 degrees
            # xlnoInCubeInSgmt is the base to loop through
            # ilnoInCubeInSgmt is the goal
            a = xlnoInCubeInSgmt
            b = np.zeros(len(a))
            for i in range(len(a)):
                # yControl -> yIntp -> yGrid -> xIntp -> xGrid
                # -- 1st search -- #
                u = a[i]
                # xlnoIntp is the segment interpolated at every crossline
                array = xlnoIntpX2I
                # index in ilnoIntp whose element is ilnoInCubeInSgmt
                idx = (np.abs(array-u)).argmin()  # find nearest
                # -- 2nd search -- #
                # same index in ilnoIntp gives the ILNO interpolated
                v = ilnoIntpX2I[idx]
                # -- 3rd search -- #
                # assume ilnoInCube is always increasing
                if v < ilnoInCube[0] or v > ilnoInCube[-1]:
                    # for ILNO that are outside cube
                    w = -1
                else:
                    # for ILNO that are inside cube
                    # find the grid nearest to the ILNO
                    array = ilnoInCube
                    idx = (np.abs(array-v)).argmin()  # find nearest
                    w = array[idx]
                b[i] = w
                # ilnoInCubeInSgmt = b

        # remove points whose XLNO is marker -1
        # a = ilnoInCubeInSgmt
        # b = xlnoInCubeInSgmt
        c = []
        d = []
        for i in range(len(a)):
            if b[i] != -1:
                c.append(a[i])
                d.append(b[i])
        # convert list to array
        c = np.array(c)
        d = np.array(d)
        if len(c) > 0:
            myprint("This segment first point:", c[0], d[0])
            myprint("This segment last point:", c[-1], d[-1])

        # Now c is ilnoInCubeInSgmt with xlnoInCubeInSgmt
        # Now d is the c-corresponding xlno
        # append this segment
        # Segment last point is bad, so do not append.
        for i in range(len(c)-1):
            if len(ilnoInCubeInSgmt) >= len(xlnoInCubeInSgmt):
                ilnoSgmts.append(c[i])
                xlnoSgmts.append(d[i])
            else:
                ilnoSgmts.append(d[i])
                xlnoSgmts.append(c[i])

    # append the last control point
    # unsafe if line is longer than cube
    # ilnoSgmts.append(ilno[-1])
    # xlnoSgmts.append(xlno[-1])

    # convert list to array
    ilnoSgmts = np.array(ilnoSgmts)
    xlnoSgmts = np.array(xlnoSgmts)

    # print to screen for QC
    myprint("Arbitrary line has control points:", len(ilno))
    # for i in range(len(ilno)):
    #     myprint("--", ilno[i], xlno[i])
    myprint("Arbitrary line has gridded points:", len(ilnoSgmts))
    # for i in range(len(ilnoSgmts)):
    #     myprint("--", ilnoSgmts[i], xlnoSgmts[i])

    # myprint("Plotting...")
    # import matplotlib.pyplot as plt
    # # plt.plot(ilnoIntp, xlnoIntp, 'bo')
    # # plt.plot(ilnoInCubeInSgmt, xlnoInCubeInSgmt, 'g^')
    # plt.plot(ilno, xlno, 'r-', linewidth=0.5)
    # plt.plot(ilnoSgmts, xlnoSgmts, 'g^')
    # plt.axes().set_aspect('equal')
    # plt.tight_layout()
    # plt.show()

    grid = np.stack((ilnoSgmts, xlnoSgmts), axis=-1)
    return grid


def main():
    line = np.array([[100,100], [600, 200], [700,700], [900,900]])
    dict_vidx = {'IL_FRST': 0, 'IL_LAST': 1000, 'IL_NCRT': 10, 'IL_AMNT': 101,
                'XL_FRST': 0, 'XL_LAST': 1000, 'XL_NCRT': 10, 'XL_AMNT': 101}
    grid = grid_line(line, dict_vidx)
    myprint(grid.shape)


if __name__ == '__main__':
    main()
