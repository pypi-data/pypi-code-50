# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
#
# from datetime import datetime
# import os
# import pickle
# from pathlib import Path
#
#
# class Cube:
#     def instfromVidxF(self, vidxfn, sgmtfn, cubefn, **kwargs):
#         """
#         Make Cube from vidx file. It is designed for segy and voxet
#         files. Prepare a vidx file before run this function. The sgmt file
#         is essential to convert LN to get XY thus the parm.
#         - vidxfn : string, vidx filename
#         - sgmtfn : string, sgmt filename. Need it to calculate parm from vidx.
#         - cubefn : string, cube filename
#         - kwargs : keyword argument passed to get_parm_from_vidx
#         -- dataPrecision : integer, 4 for 32-bit float, 8 for 64-bit float.
#         -- dataVelType : string, 'AVGVEL', 'INTVEL', 'RMSVEL'
#         -- depthOutput : string, 'POSITIVE', 'NEGATIVE'
#         -- traceUnit : string, 'METERS', 'FEET'
#         -- panelUnit : string, 'METERS', 'FEET'
#         -- sampleUnit : string, 'MSECS', 'METERS', 'FEET'
#         -- dataUnit : string, 'METERSPERSEC', 'FEETPERSEC'
#         Return a new Cube
#         """
#         # read vidx file to dictionary
#         dict_vidx = read_vidx(vidxfn)
#         # print_vidx(dict_vidx)
#
#         # read sgmt file to dictionary
#         dict_sgmt = read_sgmt(sgmtfn)
#         # print_sgmt(dict_sgmt)
#
#         # read cube file to array
#         NIL = dict_vidx['IL_AMNT']
#         NXL = dict_vidx['XL_AMNT']
#         NDP = dict_vidx['DP_AMNT']
#         if cubefn is not None:
#             array3d = load_cube(cubefn, NIL, NXL, NDP)
#         else:
#             array3d = np.random.randn(NIL, NXL, NDP)
#
#         # get the dict_parm
#         dict_parm = get_parm_from_vidx(dict_vidx, dict_sgmt, **kwargs)
#         # print_parm(dict_parm)
#
#         # get the dict_vxyz
#         dict_vxyz = get_vxyz_from_parm(dict_parm)
#         # print_vxyz(dict_vxyz)
#
#         prop_name = dict_parm['DATA_VEL_TYPE']
#         self.add_property(prop_name, array=array3d)
#         self.dict_parm = dict_parm
#         self.dict_vidx = dict_vidx
#         self.dict_vxyz = dict_vxyz
#         self.dict_sgmt = dict_sgmt
#
#     def instfromParmD(self, dict_parm, dict_sgmt, array3d):
#         """
#         Make Cube from parm dictionary. Comparing to the instfrom*F
#         used at the beginning to read from files, it is used at the end,
#         to prepare a Cube for write to files. The sgmt is essential
#         to convert XY to LN for the vidx. The array3d is the data cube.
#         - dict_parm : dictionary, parameters parm
#         - dict_sgmt : dictionary, survey geometry
#         - array3d : float array 3D, the cube
#         Return a new Cube
#         """
#         # get the dict_vidx
#         dict_vidx = get_vidx_from_parm(dict_parm, dict_sgmt)
#         # print_parm(dict_vidx)
#         # get the dict_vxyz
#         dict_vxyz = get_vxyz_from_parm(dict_parm)
#         # print_vxyz(dict_vxyz)
#
#         prop_name = dict_parm['DATA_VEL_TYPE']
#         self.add_property(prop_name, array=array3d)
#         self.dict_parm = dict_parm
#         self.dict_vidx = dict_vidx
#         self.dict_vxyz = dict_vxyz
#         self.dict_sgmt = dict_sgmt
#
#     def inst_from_four_files(self, cubefn):
#         """
#         This method is used for cubes written to files by this class,
#         which means it has the four metadata files available.
#         """
#         # Prepare filenames
#         fpre = osp.splitext(cubefn)[0]
#         parmfn = fpre + ".parms"
#         vidxfn = fpre + ".vidx"
#         vxyzfn = fpre + ".vxyz"
#         # read parm file to dictionary
#         dict_parm = read_parm(parmfn)
#         # read vidx file to dictionary
#         dict_vidx = read_vidx(vidxfn)
#         # read vxyz file to dictionary
#         dict_vxyz = read_vxyz(vxyzfn)
#         # read cube file to array
#         NIL = dict_parm['NPANEL']
#         NXL = dict_parm['NTRACE']
#         NDP = dict_parm['NSAMPLE']
#         array3d = load_cube(cubefn, NIL, NXL, NDP)
#         prop_name = dict_parm['DATA_VEL_TYPE']
#
#         self.add_property(prop_name, array=array3d)
#         self.dict_parm = dict_parm
#         self.dict_vidx = dict_vidx
#         self.dict_vxyz = dict_vxyz
#
#     # def instfromFourObjects(self, array3d, dict_parm, dict_vidx, dict_vxyz):
#     def inst_from_objects(self, listFive):
#         """
#         i listFive : list, elements are in order
#           [array3d, dict_vidx, dict_sgmt, dict_vxyz, dict_parm]
#         Objects are Python's abstraction for data.
#         This method is used for cube generated from existing cubes which means
#         the four dictionary objects are already available. A good example is
#         convert Dpth-Vint cube to Dpth-Vavg cube, or T2D a Time-Vavg cube.
#         """
#         self.dict_vidx = listFive[1]
#         self.dict_sgmt = listFive[2]
#         self.dict_vxyz = listFive[3]
#         self.dict_parm = listFive[4]
#
#         prop_name = listFive[4]['DATA_VEL_TYPE']
#         self.add_property(prop_name, array=listFive[0])
#
#     def inst_from_dict_files(self, basefn):
#         vidxfn = basefn + ".vidx"
#         sgmtfn = basefn + ".sgmt"
#         vxyzfn = basefn + ".vxyz"
#         parmfn = basefn + ".parm"
#         dict_vidx = read_vidx(vidxfn)
#         dict_sgmt = read_sgmt(sgmtfn)
#         dict_vxyz = read_vxyz(vxyzfn)
#         dict_parm = read_parm(parmfn)
#         # initialize cube with zeros
#         NIL = dict_parm['NPANEL']
#         NXL = dict_parm['NTRACE']
#         NDP = dict_parm['NSAMPLE']
#         array3d = np.zeros((NIL, NXL, NDP))
# #        prop_name = 'prop_1'
#         prop_name = dict_parm['DATA_VEL_TYPE']
#
#         self.add_property(prop_name, array=array3d)
#         self.dict_vidx = dict_vidx
#         self.dict_sgmt = dict_sgmt
#         self.dict_vxyz = dict_vxyz
#         self.dict_parm = dict_parm
#
#     def create_jsdict(self, prop_name=None, axis_domains=None, axis_units=None):
#         """
#         Used by WRITE_JAVASEIS - a Julia function using TeaSeis.
#         """
#         if prop_name is None:
#             if self.current_property is None:
#                 self.set_current_property()
#             prop_name = self.current_property
#         if axis_domains is None:
#             axis_domains = ["depth", "space", "space"]
#         if axis_units is None:
#             axis_units = ["feet", "UNKNOWN", "UNKNOWN"]
#         jsdict = copy.deepcopy(self.dict_vidx)
#         jsdict["array3d"] = self.prop[prop_name]['array3d']
#         jsdict["axis_domains"] = axis_domains
#         jsdict["axis_units"] = axis_units
#         jsdict["traces_xy"] = self.get_traces_xy()
#         return jsdict
#
#     def write(self, prop_name, outfn, fmt='seis', dtype='float32'):
#         """
#         Write Cube to files
#         - outfn : string, output filename
#         - fmt : string, 'seis' or 'bin'
#         - dtype : string, data type for bin format
#         """
#         # get parm filename
#         fpre = osp.splitext(outfn)[0]
#         parmfn = fpre + ".parms"
#         # write parm file
#         dict_parm = self.dict_parm
#         write_parm(parmfn, dict_parm)
#         # write vidx file
#         vidxfn = fpre + ".vidx"
#         dict_vidx = self.dict_vidx
#         write_vidx(vidxfn, dict_vidx)
#         # write vxyz file
#         vxyzfn = fpre + ".vxyz"
#         dict_vxyz = self.dict_vxyz
#         write_vxyz(vxyzfn, dict_vxyz)
#         # write cube file
#         array3d = self.prop[prop_name]['array3d']
#         if fmt == 'seis':
#             write_seis(outfn, array3d)
#         elif fmt == 'bin':
#             write_bin(outfn, array3d, dtype)
#         else:
#             raise ValueError("Unknown file format.")
#
#
# def load_cube(cubefn, NIL, NXL, NDP):
#     """Deprecated
#     Read data or pickle file to a 3D array
#     """
#     # first check if pickle file exist
#     # pklpath = "/data/Dropbox/pickles/"
#     pklpath = os.environ['pklpath']
#     cfnopath = os.path.split(cubefn)[1]
#     pklfn = pklpath + cfnopath + ".pkl"
#     pklfile = Path(pklfn)
#     if pklfile.is_file():
#         # pickle file exist, get time stamp
#         mtimePklfn = os.path.getmtime(pklfn)
#         mtimeCubefn = os.path.getmtime(cubefn)
#     if pklfile.is_file() and mtimePklfn > mtimeCubefn :
#         # pickle file is newer than cube file
#         # To prevent the case of cube file is newly created, but still
#         # load the old pickle file, ends up array indexing error etc.
#         myprint("$$Load Pickle" + " Start @", datetime.now())
#         myprint("--Loading--", pklfn)
#         with open(pklfn, 'rb') as f:
#             array3d = pickle.load(f)
#         myprint("$$Load Pickle" + " Ended @", datetime.now())
#         # decimate for quick test
#         # temp = array3d[::4,::4,:]
#     else:
#         # pickle file not exist, read raw file and write pickle
#         myprint("--Reading--", cubefn)
#         myprint("$$Read" + " Start @", datetime.now())
#         listSegy = ['.sgy', '.segy', '.seg-y', '.SGY', '.SEGY',
#                     '.SEG-Y', '.Sgy', '.Segy', '.Seg-y']
#         listSeis = ['.seis', '.SEIS', '.Seis']
#         fext = os.path.splitext(cubefn)[1]
#         if fext in listSegy:
#             # read SEGY file
#             array3d = read_segy_ks(cubefn,NIL,NXL,NDP)
#         elif fext in listSeis:
#             # read VTB .seis file
#             array3d = read_seis(cubefn,NIL,NXL,NDP)
#         elif cubefn[-1] == '@':
#             # sometimes it is .data
#             # filename ends with the sign @
#             # read Gocad voxet property file
#             array3d = read_seis(cubefn,NIL,NXL,NDP)
#         else :
#             raise ValueError("Unknown cube file format.")
#         myprint("$$Read" + " Ended @", datetime.now())
#         # write pickle for fast read later
#         # myprint("Dumping pickle file:", pklfn)
#         # myprint("$$Dump" + " Start @", datetime.now())
#         # with open(pklfn, 'wb') as f :
#         #     # pickle.dump(array3d, f, pickle.HIGHEST_PROTOCOL)
#         #     # literal -1 is equivalent to highest protocol
#         #     pickle.dump(array3d, f, -1)
#         # myprint("$$Dump" + " Ended @", datetime.now())
#     return array3d
#
#
# def read_segy_ks(segyfn, NIL, NXL, NDP):
#     """
#     Read SEGY file
#     - segyfn : string, segy filename
#     - NIL : integer, number of inlines
#     - NXL : integer, number of crosslines
#     - NDP : integer, number of samples per trace
#     Return one 3D array with all headers stripped off
#     """
#     myprint("--Reading--", segyfn)
#     import ezcad.utils.segy as segy
#     fsegy = segy.Segy(segyfn)
#
#     ntrace = NIL * NXL
#     nsample = ntrace * NDP
#     # ntrace = int(fsegy.getNumberOfTraces())
#     myprint("Number of Traces =", ntrace)
#
#     # QC the first trace
#     itrace = 1
#     t = fsegy.getTraceHdr(itrace)
#     # This is the SEG SEGY regulation
#     cdpx = t.getHeader('Xensemble') # 181-184, CDP X
#     cdpy = t.getHeader('Yensemble') # 185-188, CDP Y
#     ilno = t.getHeader('PostInLineNo') # 189-192, ILNO
#     xlno = t.getHeader('PostCrossLineNo') # 193-196, XLNO
#     # This is the Company ETC convention
#     #ilno = t.getHeader('Xensemble') # 181-184, INLINE
#     #xlno = t.getHeader('Yensemble') # 185-188, CROSSLINE
#     #cdpx = t.getHeader('PostInLineNo') # 189-192, CDPX_COORD
#     #cdpy = t.getHeader('PostCrossLineNo') # 193-196, CDPY_COORD
#     scalco = t.getHeader('ScalerCoord') # 71-72, scalar
#     myprint('scalco =', scalco)
#     if scalco > 0 :
#       cdpx *= scalco
#       cdpy *= scalco
#     elif scalco < 0 :
#       cdpx /= abs(scalco)
#       cdpy /= abs(scalco)
#     else :
#       raise ValueError("Unknown value")
#     myprint("First Trace CDP XY =", cdpx, cdpy)
#     myprint("First Trace IL, XL =", ilno, xlno)
#
#     myprint("Reading Segy file...")
#     # dataList = []
#     # For known size, do not need use list and append, which takes
#     # time and memory for large arrays.
#     array1d = np.zeros(nsample, 'float32')
#     for i in range(ntrace) :
#       if (i % 100000) == 0 :
#         myprint("Reading trace =", i)
#       traceNumber = i + 1
#       traceData = fsegy.getTraceData(traceNumber)
#       i1 = NDP * i
#       i2 = NDP * (i+1)
#       array1d[i1:i2] = traceData
#       # dataList.append(traceData)
#       # select an inline or a trace to QC values
#       # t = fsegy.getTraceHdr(traceNumber)
#       # ilno = t.getHeader('PostInLineNo')
#       # xlno = t.getHeader('PostCrossLineNo')
#       # if ilno == 2100 and xlno == 2500:
#       #   traceQc = traceData
#       #   traceQcArray = np.array(traceQc)
#       #   for j in range(len(traceQc)) :
#       #     myprint(ibm2ieee(traceQcArray[j]))
#     # myprint("Converting list to array...")
#     # array1d = np.array(dataList) # convert list to array
#
#     fmt = fsegy.header.getBinEntry('SampleFormat')
#     if fmt == 1 :
#       myprint("Converting IBM Format...")
#       for i in range(nsample):
#         array1d[i] = ibm2ieee(array1d[i])
#     # myprint("First Trace Samples =\n", array1d[0])
#
#     # shape array from 1D to 3D
#     myprint("Reshape Array 1D to 3D...")
#     array3d = array1d.reshape(NIL, NXL, NDP)
#     myprint("Reshape Finished")
#     myprint("Return array3d data type:", array3d.dtype)
#     return array3d
#
#
# def ibm2ieee(ibm):
#     """
#     Converts an IBM floating point number into IEEE format.
#     - ibm : 32 bit unsigned integer: unpack('>L', f.read(4))
#     """
#     sign = ibm >> 31 & 0x01
#     exponent = ibm >> 24 & 0x7f
#     mantissa = ibm & 0x00ffffff
#     mantissa = (mantissa * 1.0) / pow(2, 24)
#     ieee = (1 - 2 * sign) * mantissa * pow(16, exponent - 64)
#     return ieee
