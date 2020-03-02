# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

"""
Previous version only takes (ngil, ngxl, ngdp) and let the
IL_FRST and IL_LAST driven by the input cube. This is insufficient
for seismic stacks with different edges than the velocity model.
This version upgrades the re-sampling to a complete new dict_vidx.
@author Joseph Zhu
@version 0.1
@date 2016/12/22

Re-sample 3D cube to denser or sparser grid
@author Joseph Zhu
@version 0.0
@date 2016/12/15
"""

# Standard library imports
from datetime import datetime

# Third party imports
import numpy as np
from scipy.interpolate import RegularGridInterpolator
import scipy.ndimage as ndimage
# from joblib import Parallel, delayed

# Local imports
# from ezcad.gocube.expt.write_file import write_zhu
from ezcad.gosurvey.impt.read_file import read_sgmt
from ezcad.utils.print_overload import myprint


def main():
    sgmtfn = "/home/zhu/block0_survey_geometry.sgmt"
    dict_sgmt = read_sgmt(sgmtfn)

    parmfn = "volumes/hbbi_G3k_G16h_G8h_G4h_G2h_G1h_IDS6k.parm"
    from ezcad.gocube.cube import Cube
    zhuVm = Cube()
    zhuVm.instfromParmF(parmfn, sgmtfn)

    # Scipy.RGI requires output dict_vidx be within the bounds of
    # the input dict_vidx
    IL_FRST_NEW = 4100
    IL_LAST_NEW = 6300
    IL_NCRT_NEW = 1
    IL_AMNT_NEW = int((IL_LAST_NEW - IL_FRST_NEW) / IL_NCRT_NEW) + 1
    IL_LAST_NEW = IL_FRST_NEW + IL_NCRT_NEW * (IL_AMNT_NEW - 1)
    XL_FRST_NEW = 3800
    XL_LAST_NEW = 5550
    XL_NCRT_NEW = 1
    XL_AMNT_NEW = int((XL_LAST_NEW - XL_FRST_NEW) / XL_NCRT_NEW) + 1
    XL_LAST_NEW = XL_FRST_NEW + XL_NCRT_NEW * (XL_AMNT_NEW - 1)
    DP_FRST_NEW = 0
    DP_LAST_NEW = 5400
    DP_NCRT_NEW = 4
    DP_AMNT_NEW = int((DP_LAST_NEW - DP_FRST_NEW) / DP_NCRT_NEW) + 1
    DP_LAST_NEW = DP_FRST_NEW + DP_NCRT_NEW * (DP_AMNT_NEW - 1)
    dict_vidx_new = {
        'IL_FRST': IL_FRST_NEW,
        'IL_LAST': IL_LAST_NEW,
        'IL_NCRT': IL_NCRT_NEW,
        'IL_AMNT': IL_AMNT_NEW,
        'XL_FRST': XL_FRST_NEW,
        'XL_LAST': XL_LAST_NEW,
        'XL_NCRT': XL_NCRT_NEW,
        'XL_AMNT': XL_AMNT_NEW,
        'DP_FRST': DP_FRST_NEW,
        'DP_LAST': DP_LAST_NEW,
        'DP_NCRT': DP_NCRT_NEW,
        'DP_AMNT': DP_AMNT_NEW
    }
    zhuVmNew = rspCube_wrap(zhuVm, dict_vidx_new, dict_sgmt)
    myprint("stop here")
    exit()
    outseisfn = "/data/Dropbox/test/testnew.seis"
    # write_zhu(outseisfn, zhuVmNew)
    myprint("Done")


def rspCube_wrap(zhu, dict_vidx_new, dict_sgmt):
    """
    Deprecate rspCube_wrap. Moved to class.method Cube.resample
    Just a wrapper, for using custom data object Cube.
    - zhu : Cube, input custom data object
    - dict_vidx_new : dictionary, new vidx for re-sampling
    - dict_sgmt : dictionary, survey geometry. Needed to calculate
      XYs from MNs in the dict_vidx_new.
    Return a new Cube
    """
    array3d = zhu.array3d
    dict_vidx = zhu.dict_vidx
    array3dNew = rspCube_Map(array3d, dict_vidx, dict_vidx_new)
    # These parm do not change after re-sampling, so
    # pass them to the new Cube
    dict_parm = zhu.dict_parm
    dataPrecision = dict_parm['DATA_PRECISION']
    dataVelType = dict_parm['DATA_VEL_TYPE']
    depthOutput = dict_parm['DEPTH_OUTPUT']
    traceUnit = dict_parm['TRACE_UNIT']
    panelUnit = dict_parm['PANEL_UNIT']
    sampleUnit = dict_parm['SAMPLE_UNIT']
    dataUnit = dict_parm['DATA_UNIT']
    from ezcad.gocube.cube import Cube
    zhuNew = Cube()
    zhuNew.instfromVidxD(dict_vidx_new, dict_sgmt, array3dNew,
        dataPrecision=dataPrecision, dataVelType=dataVelType,
        depthOutput=depthOutput, traceUnit=traceUnit,
        panelUnit=panelUnit, sampleUnit=sampleUnit,
        dataUnit=dataUnit)
    return zhuNew


def rspCube_Map(array3d, dict_vidx, dict_vidx_new):
    """
    Re-sample 3D cube to a denser or sparser grid.
    - array3d : float array 3D, input cube
    - dict_vidx : dictionary, input cube physical indices
    - dict_vidx_new : dictionary, new vidx for re-sampling
    Return a new array3d on the dict_vidx_new
    """
    myprint("$$Interpolation" + " Start @", datetime.now())
    IL_FRST = dict_vidx['IL_FRST']
    IL_NCRT = dict_vidx['IL_NCRT']
    XL_FRST = dict_vidx['XL_FRST']
    XL_NCRT = dict_vidx['XL_NCRT']
    DP_FRST = dict_vidx['DP_FRST']
    DP_NCRT = dict_vidx['DP_NCRT']
    IL_FRST_NEW = dict_vidx_new['IL_FRST']
    IL_LAST_NEW = dict_vidx_new['IL_LAST']
    IL_AMNT_NEW = dict_vidx_new['IL_AMNT']
    XL_FRST_NEW = dict_vidx_new['XL_FRST']
    XL_LAST_NEW = dict_vidx_new['XL_LAST']
    XL_AMNT_NEW = dict_vidx_new['XL_AMNT']
    DP_FRST_NEW = dict_vidx_new['DP_FRST']
    DP_LAST_NEW = dict_vidx_new['DP_LAST']
    DP_AMNT_NEW = dict_vidx_new['DP_AMNT']
    # get pixel coordinate
    IL_PC1 = (IL_FRST_NEW - IL_FRST) / IL_NCRT
    IL_PC2 = (IL_LAST_NEW - IL_FRST) / IL_NCRT
    xnew = np.linspace(IL_PC1, IL_PC2, IL_AMNT_NEW)
    xnew = xnew.astype('float32', copy=False)
    XL_PC1 = (XL_FRST_NEW - XL_FRST) / XL_NCRT
    XL_PC2 = (XL_LAST_NEW - XL_FRST) / XL_NCRT
    ynew = np.linspace(XL_PC1, XL_PC2, XL_AMNT_NEW)
    ynew = ynew.astype('float32', copy=False)
    DP_PC1 = (DP_FRST_NEW - DP_FRST) / DP_NCRT
    DP_PC2 = (DP_LAST_NEW - DP_FRST) / DP_NCRT
    znew = np.linspace(DP_PC1, DP_PC2, DP_AMNT_NEW)
    znew = znew.astype('float32', copy=False)

    # Create coordinate matrix from coordinate vectors
    xv, yv, zv = np.meshgrid(xnew, ynew, znew)
    # myprint(xv.shape)   # xv.shape is (NXL, NIL, NDP)
    # myprint("xv", xv.dtype) # float64 direct from meshgrid
    xv = xv.astype('float32', copy=False)
    yv = yv.astype('float32', copy=False)
    zv = zv.astype('float32', copy=False)
    xv = np.transpose(xv, (1, 0, 2))
    yv = np.transpose(yv, (1, 0, 2))
    zv = np.transpose(zv, (1, 0, 2))
    # myprint(xv.shape)   # xv.shape is (NIL, NXL, NDP)
    xv = xv.flatten()   # flatten 3D array to 1D
    yv = yv.flatten()
    zv = zv.flatten()
    # myprint(xv.shape)     # xv.shape is (NIL*NXL*NDP,)

    # Map has extrapolation and RGI does not.
    # Map does not support 16 bit, and RGI does.
    # Speed on 215,755,995 points, RAM 258 GB, single thread
    # Map, memory 2%, time 35 seconds, used 32 bit
    # RGI, memory 8%, time 110 seconds, used 16 bit
    # Speed on 5,206,687,801 points, RAM 258 GB, single thread
    # Map, memory 50%, time 14 minutes, used 32 bit
    # RGI, memory 30-50-70-99%, time (failed), used 16 bit, MemoryError!
    # RGI, memory 44%, time 50 minutes, used 16 bit, split to 6 parts.

    # map's data and coordinate array data type not support float16
    array3d = array3d.astype('float32', copy=False)
    npts = IL_AMNT_NEW * XL_AMNT_NEW * DP_AMNT_NEW
    myprint("Number of points to interpolate =", npts)
    array1d = ndimage.map_coordinates(array3d, [xv, yv, zv], order=1,
                                      mode='nearest')
    array1d = array1d.astype('float32', copy=False)
    myprint("Number of points interpolated =", len(array1d))
    # Reshape 1D array to 3D
    array3dNew = array1d.reshape(IL_AMNT_NEW, XL_AMNT_NEW, DP_AMNT_NEW)
    myprint("$$Interpolation" + " Ended @", datetime.now())
    return array3dNew


def rspCube_RGI(array3d, dict_vidx, dict_vidx_new):
    """
    Re-sample 3D cube to a denser or sparser grid.
    - array3d : float array 3D, input cube
    - dict_vidx : dictionary, input cube physical indices
    - dict_vidx_new : dictionary, new vidx for re-sampling
    Return a new array3d on the dict_vidx_new
    """
    myprint("$$Interpolation" + " Start @", datetime.now())
    IL_FRST = dict_vidx['IL_FRST']
    IL_LAST = dict_vidx['IL_LAST']
    IL_AMNT = dict_vidx['IL_AMNT']
    XL_FRST = dict_vidx['XL_FRST']
    XL_LAST = dict_vidx['XL_LAST']
    XL_AMNT = dict_vidx['XL_AMNT']
    DP_FRST = dict_vidx['DP_FRST']
    DP_LAST = dict_vidx['DP_LAST']
    DP_AMNT = dict_vidx['DP_AMNT']
    int_dt = 'int32'
    x = np.linspace(IL_FRST, IL_LAST, IL_AMNT)
    x = x.astype(int_dt, copy=False)
    y = np.linspace(XL_FRST, XL_LAST, XL_AMNT)
    y = y.astype(int_dt, copy=False)
    z = np.linspace(DP_FRST, DP_LAST, DP_AMNT)
    y = y.astype(int_dt, copy=False)
    f = RegularGridInterpolator((x, y, z), array3d)

    IL_FRST_NEW = dict_vidx_new['IL_FRST']
    IL_LAST_NEW = dict_vidx_new['IL_LAST']
    IL_AMNT_NEW = dict_vidx_new['IL_AMNT']
    XL_FRST_NEW = dict_vidx_new['XL_FRST']
    XL_LAST_NEW = dict_vidx_new['XL_LAST']
    XL_AMNT_NEW = dict_vidx_new['XL_AMNT']
    DP_FRST_NEW = dict_vidx_new['DP_FRST']
    DP_LAST_NEW = dict_vidx_new['DP_LAST']
    DP_AMNT_NEW = dict_vidx_new['DP_AMNT']
    xnew = np.linspace(IL_FRST_NEW, IL_LAST_NEW, IL_AMNT_NEW)
    xnew = xnew.astype(int_dt, copy=False)
    ynew = np.linspace(XL_FRST_NEW, XL_LAST_NEW, XL_AMNT_NEW)
    ynew = ynew.astype(int_dt, copy=False)
    znew = np.linspace(DP_FRST_NEW, DP_LAST_NEW, DP_AMNT_NEW)
    znew = znew.astype(int_dt, copy=False)

    # Create coordinate matrix from coordinate vectors
    xv, yv, zv = np.meshgrid(xnew, ynew, znew)
    # myprint(xv.shape)   # xv.shape is (NXL, NIL, NDP)
    # myprint("xv", xv.dtype) # int64 direct from meshgrid
    xv = xv.astype(int_dt, copy=False)
    yv = yv.astype(int_dt, copy=False)
    zv = zv.astype(int_dt, copy=False)
    xv = np.transpose(xv, (1, 0, 2))
    yv = np.transpose(yv, (1, 0, 2))
    zv = np.transpose(zv, (1, 0, 2))
    # myprint(xv.shape)   # xv.shape is (NIL, NXL, NDP)
    xv = xv.flatten()   # flatten 3D array to 1D
    yv = yv.flatten()
    zv = zv.flatten()
    # myprint(xv.shape)     # xv.shape is (NIL*NXL*NDP,)

    # pts = [xv, yv, zv]  # pts is a list here
    # MemoryError for 5,206,687,801 points on 258GB memory blade.
    # pts = np.asarray(pts) # pts.shape is (3, NIL*NXL*NDP)
    # pts = pts.T
    # myprint(pts.shape)  # pts.shape is (NIL*NXL*NDP, 3)

    # Instead of through list and then convert list to array,
    # just assign...
    # MemoryError for 5,206,687,801 points on 258GB memory blade.

    npts = IL_AMNT_NEW * XL_AMNT_NEW * DP_AMNT_NEW
    myprint("Number of points to interpolate =", npts)
    # When memory usage approaches 90%, computer may crash/restart.
    nptsCap = 1000000000  # one billion cap to prevent memory fail
    if npts < nptsCap:
        pts = np.zeros((npts, 3), int_dt)
        pts[:, 0] = xv
        pts[:, 1] = yv
        pts[:, 2] = zv
        ptv = f(pts)
        array1d = ptv.astype('float32', copy=False)
    else:
        # split to smaller arrays
        nsplit = int(npts / nptsCap) + 1
        myprint("So many points - Split to %i parts" % nsplit)
        xvSplit = np.array_split(xv, nsplit)
        yvSplit = np.array_split(yv, nsplit)
        zvSplit = np.array_split(zv, nsplit)
        # split then run in sequential
        array1d = np.empty(shape=(0,), dtype='float32')
        for i in range(nsplit):
            myprint("Interpolating part %i of %i" % (i, nsplit))
            xva = xvSplit[i]
            yva = yvSplit[i]
            zva = zvSplit[i]
            pts = [xva, yva, zva]
            pts = np.asarray(pts)
            pts = pts.T
            ptv = f(pts)  # interpolate
            ptv = ptv.astype('float32', copy=False)
            array1d = np.concatenate((array1d, ptv))
        # split and run in parallel
        # OSError: [Errno 12] Cannot allocate memory
#       nproc = range(nsplit)
#       ncore = os.cpu_count()
#       myprint("Number of cores =", ncore)
#       lista = Parallel(n_jobs=ncore)(delayed(rspSlab)(i, xvSplit[i],
#           yvSplit[i], zvSplit[i], f) for i in nproc)
#       for i in range(len(lista)):
#           array1d = np.concatenate((array1d, lista[i]))

    myprint("Number of points interpolated =", len(array1d))
    # Reshape 1D array to 3D
    array3dNew = array1d.reshape(IL_AMNT_NEW, XL_AMNT_NEW, DP_AMNT_NEW)
    myprint("$$Interpolation" + " Ended @", datetime.now())
    return array3dNew


def rspSlab(i, xv, yv, zv, f):
    myprint("Interpolating", i)
    n = len(xv)
    pts = np.zeros((n, 3), 'int32')
    pts[:, 0] = xv
    pts[:, 1] = yv
    pts[:, 2] = zv
    v = f(pts)  # interpolate
    return v


if __name__ == '__main__':
    main()
