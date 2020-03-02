# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
# """To be integrated"""
#
# from ezcad.gocube.resample import rspCube_Map
# from ezcad.utils.convert_grid import getLNfromXY, get_step
#
#
# class Cube:
#
#     def map2pts_intp(self, prop_name, listPts):
#         """
#         Paint cube value onto target points, by tri-linear interpolation.
#         - self : Cube, custom data class
#         --- array3d : float array 3D, data cube
#         --- dict_vidx : dictionary, volume indices
#         - listPts : list 2D, [m,n,x,y,z,g,..], use 1,2,5 columns
#         """
#         IL_FRST = self.dict_vidx['IL_FRST']
#         IL_LAST = self.dict_vidx['IL_LAST']
#         IL_AMNT = self.dict_vidx['IL_AMNT']
#         XL_FRST = self.dict_vidx['XL_FRST']
#         XL_LAST = self.dict_vidx['XL_LAST']
#         XL_AMNT = self.dict_vidx['XL_AMNT']
#         DP_FRST = self.dict_vidx['DP_FRST']
#         DP_LAST = self.dict_vidx['DP_LAST']
#         DP_AMNT = self.dict_vidx['DP_AMNT']
#         x = np.linspace(IL_FRST, IL_LAST, IL_AMNT)
#         y = np.linspace(XL_FRST, XL_LAST, XL_AMNT)
#         z = np.linspace(DP_FRST, DP_LAST, DP_AMNT)
#         from scipy.interpolate import RegularGridInterpolator
#         array3d = self.prop[prop_name]['array3d']
#         f = RegularGridInterpolator((x,y,z), array3d)
#         npts = len(listPts)
#         myprint("Number of points to map =", npts)
#         pts = np.zeros((npts, 3))
#         for i in range(npts):
#             ILNO = listPts[i][0]
#             XLNO = listPts[i][1]
#             DPNO = listPts[i][4]
#             if ILNO < IL_FRST:
#                 ILNO = IL_FRST
#             if ILNO > IL_LAST:
#                 ILNO = IL_LAST
#             if XLNO < XL_FRST:
#                 XLNO = XL_FRST
#             if XLNO > XL_LAST:
#                 XLNO = XL_LAST
#             if DPNO < DP_FRST:
#                 DPNO = DP_FRST
#             if DPNO > DP_LAST:
#                 DPNO = DP_LAST
#             pts[i, 0] = ILNO
#             pts[i, 1] = XLNO
#             pts[i, 2] = DPNO
#         p = f(pts)
#         for i in range(npts):
#             listPts[i].append(p[i])
#         return listPts
#
#     def map2pts_near(self, prop_name, listPts, mapType=1, z1=0, nz=10, netAmp=0):
#         """
#         Paint cube value onto target geobody. It is from nearest
#         grid or cell. No trilinear interpolation.
#         The host is a 3D cube/volume loaded in as a 3D array.
#         The target where to focus eyes and to be displayed is
#         (1) 1D, at well-path, vertical or deviated wells.
#         (2) 2D, on horizon, at where the horizon cuts the cube.
#         (3) 2.5D, in slab, in an interval between two horizons.
#         (4) 3D, re-sample to sparser 3D grid (no interpolation).
#         In any case, the target file format is txt with minimum
#         five columes: m,n,x,y,z. It can have more columns,
#         such as well or horizon name (geologic bodies).
#         The extracted value is appended as the last column.
#         What used in locating are mnz (xy unused), so if you
#         have xyz, run a convert_grid code to generate the mn first.
#         If you have the well-head location of a vertical well,
#         run a separate code to generate the mnxyz of the full
#         well path before using this code, which is modulized
#         to do the mapping/painting only.
#         - self : Cube, custom data class
#         --- array3d : float array 3D, data cube
#         --- dict_vidx : dictionary, volume indices
#         - listPts : list 2D, [m,n,x,y,z,g,..], use list not array to
#           include strings of geo-body names like well/horizon.
#         - mapType : integer, 1 as is, 2 RMS on slab, 3 Net-To-Gross on slab
#         - z1 : integer, slab start sample referenced to horizon. -20 means
#           start from 20 samples above the horizon. 0 means start from at
#           horizon. 20 means below.
#         - nz : integer, number of samples in the slab
#         - netAmp : float, the amplitude of the net
#         Return a list of the input listPts appended by the mapped value.
#         """
#         array3d = self.prop[prop_name]['array3d']
#         myprint("Painting cube value onto geobody...")
#         # assign dictionary to "key" variables
#         IL_FRST = self.dict_vidx['IL_FRST']
#         IL_LAST = self.dict_vidx['IL_LAST']
#         IL_NCRT = self.dict_vidx['IL_NCRT']
#         XL_FRST = self.dict_vidx['XL_FRST']
#         XL_LAST = self.dict_vidx['XL_LAST']
#         XL_NCRT = self.dict_vidx['XL_NCRT']
#         DP_FRST = self.dict_vidx['DP_FRST']
#         DP_LAST = self.dict_vidx['DP_LAST']
#         DP_NCRT = self.dict_vidx['DP_NCRT']
#         npts = len(listPts)
#         myprint("Number of points to map =", npts)
#         p = np.zeros(npts)
#         for i in range(npts):
#             # get array index
#             ILNO = listPts[i][0]
#             XLNO = listPts[i][1]
#             DPNO = listPts[i][4]
#             if ILNO < IL_FRST:
#                 ILNO = IL_FRST
#             if ILNO > IL_LAST:
#                 ILNO = IL_LAST
#             if XLNO < XL_FRST:
#                 XLNO = XL_FRST
#             if XLNO > XL_LAST:
#                 XLNO = XL_LAST
#             if DPNO < DP_FRST:
#                 DPNO = DP_FRST
#             if DPNO > DP_LAST:
#                 DPNO = DP_LAST
#             ILNOIndex = int(round((ILNO - IL_FRST) / IL_NCRT))
#             XLNOIndex = int(round((XLNO - XL_FRST) / XL_NCRT))
#             DPNOIndex = int(round((DPNO - DP_FRST) / DP_NCRT))
#             # get attribute p[i]
#             if mapType == 1:
#                 # attribute as is on the horizon
#                 p[i] = array3d[ILNOIndex, XLNOIndex, DPNOIndex]
#             elif mapType == 2:
#                 # attribute RMS on a slab
#                 d1 = DPNOIndex + z1
#                 ampSquareSum = 0.0
#                 for j in range(nz):
#                     di = d1 + j
#                     amp = array3d[ILNOIndex, XLNOIndex, di]
#                     ampSquareSum = ampSquareSum + amp * amp
#                 ampMean = ampSquareSum / nz
#                 ampRMS = sqrt(ampMean)
#                 p[i] = ampRMS
#             elif mapType == 3:
#                 # facies net to gross
#                 net = 0.0
#                 gross = nz
#                 d1 = DPNOIndex + z1
#                 for j in range(gross):
#                     di = d1 + j
#                     amp = array3d[ILNOIndex, XLNOIndex, di]
#                     # gas sand 3, oil sand 2, wet sand 1
#                     if amp == netAmp:
#                         net = net + 1.0
#                     ntg = net / gross
#                 p[i] = ntg
#             else:
#                 raise ValueError("Invalid map type")
#         # p = np.round(p, 7) # round may cause Vint spikes
#         for i in range(npts):
#             listPts[i].append(p[i])
#         return listPts
#
#     def cvtVelType(self, prop_name, outVelType):
#         """
#         Auto detect input domain and velocity type from self.parm
#         Convert to another velocity type in the same domain
#         Return a new Cube
#         - outVelType : string, 'Vavg', 'Vint', 'Vrms', 'Dpth' or 'Time'
#         """
#         DP_FRST = self.dict_vidx['DP_FRST']
#         DP_LAST = self.dict_vidx['DP_LAST']
#         array3dIn = self.prop[prop_name]['array3d']
#
#         sampleUnit = self.dict_parm['SAMPLE_UNIT']
#         if sampleUnit == 'MSECS' or sampleUnit == 'SECS':
#             domain = 'Time'
#         elif sampleUnit == 'METERS' or sampleUnit == 'FEET':
#             domain = 'Dpth'
#         else:
#             raise ValueError("Unknown SAMPLE_UNIT in Parm.")
#
#         dataVelType = self.dict_parm['DATA_VEL_TYPE']
#         if dataVelType == 'INTVEL':
#             velType = 'Vint'
#         elif dataVelType == 'AVGVEL':
#             velType = 'Vavg'
#         elif dataVelType == 'RMSVEL':
#             velType = 'Vrms'
#         else:
#             raise ValueError("Unknown DATA_VEL_TYPE in Parm.")
#
#         if outVelType == 'Vavg':
#             dataVelTypeOut = 'AVGVEL'
#         elif outVelType == 'Vint':
#             dataVelTypeOut = 'INTVEL'
#         elif outVelType == 'Vrms':
#             dataVelTypeOut = 'RMSVEL'
#         elif outVelType == 'Dpth':
#             dataVelTypeOut = 'DEPTH'
#         elif outVelType == 'Time':
#             dataVelTypeOut = 'TIME'
#         else:
#             raise ValueError("Unknown output velocity type.")
#
#         typeIn = domain + '-' + velType
#         typeOut = domain + '-' + outVelType
#         myprint("Input velocity type is ", typeIn)
#         myprint("Output velocity type is", typeOut)
#         from cvtVelType import cvtVelTypeCube
#         # Replace zero velocity values with 1.0
#         # Otherwise, divide by zero warning, velocity nan, d2t seismic nan,
#         # which cannot be loaded Petrel. It can be loaded to Gocad, but not
#         # know how to replace the nan value yet.
#         array3dIn[array3dIn==0] = 1.0
#         array3d = cvtVelTypeCube(array3dIn, DP_FRST, DP_LAST, typeIn, typeOut)
#
#         # Update dict_parm and array3d
#         # TODO instead of replace, create new property
#         self.dict_parm['DATA_VEL_TYPE'] = dataVelTypeOut
#         self.prop[prop_name]['array3d'] = array3d
#
#     def resample(self, prop_name, dict_vidx_new, dict_sgmt=None):
#         """
#         - dict_vidx_new : dictionary, new vidx for re-sampling
#         - dict_sgmt : dictionary, Sgmt needed to calculate dict_parm
#         Use tri-linear interpolation
#         """
#         # Update array3d
#         array3d = self.prop[prop_name]['array3d']
#         dict_vidx = self.dict_vidx
#         # Use Map on 11 billion points, memory 258GB, 98%... MemoryError.
#         array3dNew = rspCube_Map(array3d, dict_vidx, dict_vidx_new)
#         # array3dNew = rspCube_RGI(array3d, dict_vidx, dict_vidx_new)
#         # Update dict_parm
#         # These parm do not change after re-sampling, so
#         # pass them to the new Cube
#         dict_parm = self.dict_parm
#         dataPrecision = dict_parm['DATA_PRECISION']
#         dataVelType = dict_parm['DATA_VEL_TYPE']
#         depthOutput = dict_parm['DEPTH_OUTPUT']
#         traceUnit = dict_parm['TRACE_UNIT']
#         panelUnit = dict_parm['PANEL_UNIT']
#         sampleUnit = dict_parm['SAMPLE_UNIT']
#         dataUnit = dict_parm['DATA_UNIT']
#         if dict_sgmt is None :
#             dict_sgmt = self.dict_sgmt
#         dict_parm = get_parm_from_vidx(dict_vidx_new, dict_sgmt,
#             dataPrecision=dataPrecision, dataVelType=dataVelType,
#             depthOutput=depthOutput, traceUnit=traceUnit,
#             panelUnit=panelUnit, sampleUnit=sampleUnit,
#             dataUnit=dataUnit)
#         # Update dict_vxyz
#         dict_vxyz = get_vxyz_from_parm(dict_parm)
#         # Assign to self
#         self.prop[prop_name]['array3d'] = array3dNew
#         self.dict_vidx = dict_vidx_new
#         self.dict_parm = dict_parm
#         self.dict_vxyz = dict_vxyz
#
#     def t2dVcube(self, prop_name, dmin=0, dmax=10000, dstp=10, switch='t2d'):
#         """
#         Class self is a Vavg cube. Convert cube T2D or D2T.
#         - dmin : float, minimum value in domain-to-be
#         - dmax : float, maximum value in domain-to-be
#         - dstp : float, sampling step in domain-to-be
#         - switch : string, 't2d' or 'd2t', conversion direction
#         """
#         # Update array3d and dict_vidx
#         array3d = self.prop[prop_name]['array3d']
#         dict_vidx = self.dict_vidx
#         from t2dCube import t2d
#         T2D = t2d() # instantiate Class even without data (only methods)
#         array3dNew, dict_vidx_new = \
#             T2D.VCube(array3d, dict_vidx, dmin, dmax, dstp, switch)
#         # Update dict_parm
#         dict_parm = self.dict_parm
#         dict_parm['NSAMPLE'] = dict_vidx_new['DP_AMNT']
#         dict_parm['SAMPLE_START'] = dict_vidx_new['DP_FRST']
#         dict_parm['SAMPLE_INC'] = dict_vidx_new['DP_NCRT']
#         if switch == 't2d':  # time to depth
#             dict_parm['SAMPLE_UNIT'] = 'METERS'  # or 'FEET'?
#         else:  # depth to time
#             dict_parm['SAMPLE_UNIT'] = 'MSECS'
#         # Update dict_vxyz
#         dict_vxyz = self.dict_vxyz
#         dict_vxyz['AXIS_DPZ'] = dict_vidx_new['DP_LAST']
#         # Assign to self
#         self.prop[prop_name]['array3d'] = array3dNew
#         self.dict_vidx = dict_vidx_new
#         self.dict_parm = dict_parm
#         self.dict_vxyz = dict_vxyz
#
#     def t2dAcube(self, prop_name, array3dVm, dict_vidxVm, dmin=0, dmax=10000, dstp=10,
#             switch='t2d'):
#         """
#         Class self is a Amplitude cube.
#         Case study. D2T seismic volume (44GB, 2400x2400x2001 grids, 18x18x6m
#         grid interval), using VM (7GB, 1200x1200x1201 grids, 36x36x10m) takes
#         7 hours; using VM (100MB, 300x300x301 grids, 144x144x40m) takes 10 minuts.
#         T2D/D2T do NOT need VM sampling too fine, take advantage of it.
#         """
#         # Update array3d and dict_vidx
#         array3dAm = self.prop[prop_name]['array3d']
#         dict_vidxAm = self.dict_vidx
#         # myprint("array3dVm data type is", array3dVm.dtype)
#         from t2dCube import t2d
#         T2D = t2d() # instantiate Class even without data (only methods)
#         array3dNew, dict_vidx_new = T2D.ACube_RGI_mt(array3dAm, dict_vidxAm,
#             array3dVm, dict_vidxVm, dmin, dmax, dstp, switch)
#         # Update dict_parm
#         dict_parm = self.dict_parm
#         dict_parm['NSAMPLE'] = dict_vidx_new['DP_AMNT']
#         dict_parm['SAMPLE_START'] = dict_vidx_new['DP_FRST']
#         dict_parm['SAMPLE_INC'] = dict_vidx_new['DP_NCRT']
#         if switch == 't2d':  # time to depth
#             dict_parm['SAMPLE_UNIT'] = 'METERS'  # or 'FEET'?
#         else :  # depth to time
#             dict_parm['SAMPLE_UNIT'] = 'MSECS'
#         # Update dict_vxyz
#         dict_vxyz = self.dict_vxyz
#         dict_vxyz['AXIS_DPZ'] = dict_vidx_new['DP_LAST']
#         # Assign to self
#         self.prop[prop_name]['array3d'] = array3dNew
#         self.dict_vidx = dict_vidx_new
#         self.dict_parm = dict_parm
#         self.dict_vxyz = dict_vxyz
#
#     def wellTieTaper(self, prop_name, listWellNames, listWellPaths,
#         wellInfRadius, wellBoreTie, lenVtaper):
#         """
#         Apply the uncertainty welltie tapering in depth domain.
#         i listWellNames : string list, of well names.
#         i listWellPaths : 2D list, X-Y-TVDSS-Wellname. Had been anchored
#             to Z=0 and interpolated DZ the same as the depth volume.
#         i wellInfRadius : float, well influence radius.
#         i wellBoreTie : float, the tie at wellbore. Can be 1/4 or 1/8
#             of the dominant wavelength.
#         i lenVtaper : float, length of vertical taper below well total depth.
#         i useVertApprox : bool. If wells are near vertical (deviation
#             smaller than volume grid), can set this to true, which speeds
#             up the process a lot. If on, no vertical taper?
#         o zhuWtie : Cube, the well-tied attribute volume.
#         o zhuWtaper : Cube, the tapering volume applied.
#         The 1st version was volume oriented (Loop IL-XL-DP-WN) and takes 11
#         days to run an average-size job. Upgrade to well oriented, the job
#         takes 4 minutes. New loop WN-DP-XL-IL.
#         """
#         IL_AMNT = self.dict_vidx['IL_AMNT']
#         IL_FRST = self.dict_vidx['IL_FRST']
#         IL_NCRT = self.dict_vidx['IL_NCRT']
#         XL_AMNT = self.dict_vidx['XL_AMNT']
#         XL_FRST = self.dict_vidx['XL_FRST']
#         XL_NCRT = self.dict_vidx['XL_NCRT']
#         DP_AMNT = self.dict_vidx['DP_AMNT']
#         # DP_FRST = self.dict_vidx['DP_FRST']
#         DP_NCRT = self.dict_vidx['DP_NCRT']
#         dict_sgmt = self.dict_sgmt
#
#         # well path XYD had been sampled the sampe as cube
#         ngridVtaper = int(lenVtaper / DP_NCRT)
#         arrayTaper = np.zeros((IL_AMNT, XL_AMNT, DP_AMNT))
#         wellInfRadSqr = wellInfRadius**2
#         arrayTaper[:] = wellInfRadSqr
#
#         # Work in LN domain, so get vector once for all
#         ILDX, ILDY, XLDX, XLDY = get_step(dict_sgmt)
#         ILStep = sqrt(ILDX**2 + ILDY**2)
#         XLStep = sqrt(XLDX**2 + XLDY**2)
#         wellInfRadiusNil = wellInfRadius / ILStep
#         wellInfRadiusNxl = wellInfRadius / XLStep
#
#         # Wells oriented and filter in LN domain
#         for wn in listWellNames:
#             myprint('Processing well:', wn)
#             wpath = [x for x in listWellPaths if x[3] == wn]
#             wlen = len(wpath)
#             wlenUse = wlen + ngridVtaper
#             if wlenUse > DP_AMNT:  # if well length longer than volume
#               wlenUse = DP_AMNT  # cut it
#             for k in range(wlenUse):
#               if k < wlen:  # befor hit well total depth
#                 kthis = k
#               else:
#                 kthis = wlen-1
#               wsample = wpath[kthis]
#               wx, wy = wsample[0:2]
#               wilno, wxlno = getLNfromXY(wx, wy, dict_sgmt)
#               ILNO1 = wilno - wellInfRadiusNil
#               ILNO2 = wilno + wellInfRadiusNil
#               XLNO1 = wxlno - wellInfRadiusNxl
#               XLNO2 = wxlno + wellInfRadiusNxl
#
#               for XLNO in np.arange(XLNO1, XLNO2, XL_NCRT):
#                 distXL = abs(XLNO - wxlno) * XLStep
#                 j = int(round((XLNO - XL_FRST) / XL_NCRT))
#                 if j < 0:
#                   j = 0
#                 if j >= XL_AMNT:
#                   j = XL_AMNT - 1
#
#                 for ILNO in np.arange(ILNO1, ILNO2, IL_NCRT):
#                   distIL = abs(ILNO - wilno) * ILStep
#                   dist = distIL**2 + distXL**2
#                   i = int(round((ILNO - IL_FRST) / IL_NCRT))
#                   if i < 0:
#                     i = 0
#                   if i >= IL_AMNT:
#                     i = IL_AMNT - 1
#
#                   if k < wlen:
#                     if dist < wellInfRadSqr and dist < arrayTaper[i, j, k]:
#                       arrayTaper[i, j, k] = dist
#                   else:
#                     if dist < wellInfRadSqr:
#                       scoef = (k - kthis) / ngridVtaper
#                       scomp = arrayTaper[i, j, k]  # from previous well
#                       wcoef = 1 - scoef
#                       wcomp = arrayTaper[i, j, kthis]
#                       arrayTaper[i, j, k] = wcomp * wcoef + scomp * scoef
#
#         # ZCI80 = (ZP90 - ZP10) / 2
#         arrayZci80 = self.prop[prop_name]['array3d']
#         # Taper by distance to wells
#         arrayZci80 = arrayZci80 * np.sqrt(arrayTaper) / wellInfRadius
#         # Replace values smaller than threshold
#         arrayZci80[arrayZci80 < wellBoreTie] = wellBoreTie
#
# #        zhuWtie = copy.deepcopy(self)
# #        zhuWtie.array3d = arrayZci80
# #        zhuWtaper = copy.deepcopy(self)
# #        zhuWtaper.array3d = arrayTaper
#         self.prop['taper']['array3d'] = arrayTaper
#         return zhuWtie, zhuWtaper
