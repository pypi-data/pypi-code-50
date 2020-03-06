# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""
Make Cube from JavaSeis file.
"""

import os
try:
    from collections.abc import OrderedDict
except ImportError:
    from collections import OrderedDict
from datetime import datetime
import numpy as np
from joblib import Parallel, delayed
from ezcad.utils.convert_parms import get_vxyz_from_vidx, get_parm_from_vidx
from ezcad.utils.logger import logger
from ezcad.utils.envars import NCORE
from gosurvey.new.new import new_survey_from_vidx
from ..function import vidx_format_dtype

lib = 'data_io/javaseis'
if os.getenv(lib) == 'True':
    print("Loading ext:", lib)
    from ezcad.utils.envars import JAVASEIS_DATA_SECONDARIES
    import pieseis.io.jsfile as jsfile
    from pieseis.io.stock_props import stock_props
else:
    print("WARNING: JavaSeis module is not enabled")


def load_cube(fufn, survey=None, object_name=None):
    """Load JavaSeis dataset and setup cube.

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
    from ezcad.gocube.cube import Cube
    cube = Cube(object_name)
    read_javaseis(cube, fufn, survey)
    cube.calc_prop_percentile()
    cube.init_xyz_range()
    cube.set_section_number()
    cube.init_colormap()
    cube.set_current_property()
    return cube


def read_javaseis(cube, jsfn, survey=None):
    """Read JavaSeis dataset to cube.

    :param cube: cube object
    :type cube: :class:`~ezcad.gocube.cube.Cube`
    :param jsfn: JavaSeis folder name
    :type jsfn: str
    :param survey: survey, used to convert LN to XY
    :type survey: :class:`~ezcad.gosurvey.survey.Survey`
    """
    print('Read JavaSeis:', jsfn)
    jsd = jsfile.JavaSeisDataset.open(jsfn)
    fps = jsd.file_properties

    ndim = fps.nr_dimensions
    if ndim != 3:
        raise ValueError("Data dimension {} is not 3".format(ndim))

    axisTrace, axisFrame = fps.axis_labels[1:3]
    if axisTrace not in ['XLINE_NO', 'CROSSLINE']:
        print('Axis of trace:', axisTrace)
        raise ValueError('Cannot handle this data context.')
    if axisFrame not in ['ILINE_NO', 'INLINE']:
        print('Axis of frame:', axisFrame)
        raise ValueError('Cannot handle this data context.')

    dict_vidx = {
        'DP_AMNT': fps.axis_lengths[0],
        'XL_AMNT': fps.axis_lengths[1],
        'IL_AMNT': fps.axis_lengths[2],
        'DP_FRST': fps.physical_origins[0],
        'XL_FRST': fps.logical_origins[1],
        'IL_FRST': fps.logical_origins[2],
        'DP_NCRT': fps.physical_deltas[0],
        'XL_NCRT': fps.logical_deltas[1],
        'IL_NCRT': fps.logical_deltas[2]
    }
    dict_vidx['DP_LAST'] = dict_vidx['DP_FRST'] + \
                           dict_vidx['DP_NCRT'] * (dict_vidx['DP_AMNT'] - 1)
    dict_vidx['XL_LAST'] = dict_vidx['XL_FRST'] + \
                           dict_vidx['XL_NCRT'] * (dict_vidx['XL_AMNT'] - 1)
    dict_vidx['IL_LAST'] = dict_vidx['IL_FRST'] + \
                           dict_vidx['IL_NCRT'] * (dict_vidx['IL_AMNT'] - 1)

    if survey is None:
        survey = new_survey_from_vidx(dict_vidx)

    vidx_format_dtype(dict_vidx)  # in-place change
    cube.dict_vidx = dict_vidx
    cube.survey = survey
    cube.dict_vxyz = get_vxyz_from_vidx(dict_vidx, survey)
    cube.dict_parm = get_parm_from_vidx(dict_vidx, survey)

    begTime = datetime.now()
    frames = []
    nframe = fps.axis_lengths[2]
    # Read by a single thread
    # for i in range(nframe):
    #     iframe = i + 1
    #     if iframe % 100 == 0:
    #         logger.info("Reading frame {} of {}".format(iframe, nframe))
    #      frame = jsd.read_frame_trcs(iframe) # shape (nxl,ndp)
    #      frames.append(frame)

    # Read by multi threads
    """
    https://github.com/joblib/joblib/issues/180
    https://stackoverflow.com/questions/27646052/multiprocessing-backed-parallel-loops-cannot-be-nested-below-threads
    https://stackoverflow.com/questions/23206787/check-if-current-thread-is-main-thread-in-python
    import threading
    threading.current_thread().name= 'MainThread'
    tested on 2019/5/26 but not work yet
    """
    frames = Parallel(n_jobs=NCORE)(delayed(read1frame)(i + 1, nframe, jsd)
                                    for i in range(nframe))

    endTime = datetime.now()
    logger.info("Time used is {}".format(endTime - begTime))
    array3d = np.array(frames)
    prop_name = cube.dict_parm['DATA_VEL_TYPE']
    cube.add_property(prop_name, array=array3d)
    

def write_javaseis(cube, outfn, prop_name=None, secondaries=None):
    """Write cube to JavaSeis

    :param cube: cube object
    :type cube: :class:`~ezcad.gocube.cube.Cube`
    :param outfn: output Segy filename
    :type outfn: str
    :param prop_name: the name of the property to write
    :type prop_name: str
    :param secondaries: path to secondary disk/storage
    :type secondaries: list
    """
    print("Writing:", outfn)
    startTime = datetime.now()

    nsample = int(cube.dict_vidx['DP_AMNT'])
    ntrace = int(cube.dict_vidx['XL_AMNT'])
    nframe = int(cube.dict_vidx['IL_AMNT'])
    axis_lengths = [nsample, ntrace, nframe]
    axis_propdefs = OrderedDict()
    axis_propdefs['DEPTH'] = stock_props['SAMPLE']
    axis_propdefs['XLINE_NO'] = stock_props['XLINE_NO']
    axis_propdefs['ILINE_NO'] = stock_props['ILINE_NO']
    axis_units = ["feet", "feet", "feet"]
    axis_domains = ["depth", "space", "space"]
    dp1 = cube.dict_vidx['DP_FRST']
    xl1 = cube.dict_vidx['XL_FRST']
    il1 = cube.dict_vidx['IL_FRST']
    dps = cube.dict_vidx['DP_NCRT']
    xls = cube.dict_vidx['XL_NCRT']
    ils = cube.dict_vidx['IL_NCRT']
    axis_lstarts = [int(x) for x in [dp1, xl1, il1]]
    axis_lincs = [int(x) for x in [1, xls, ils]]
    axis_pstarts = [0.0, 0.0, 0.0]
    axis_pincs = [float(dps), 1.0, 1.0]
    if secondaries is None:
        secondaries = JAVASEIS_DATA_SECONDARIES
    elif secondaries[0] == ".":
        secondaries = None
    jsd = jsfile.JavaSeisDataset.open(outfn, 'w', data_type="STACK",
                                      axis_lengths=axis_lengths,
                                      axis_propdefs=axis_propdefs,
                                      axis_units=axis_units,
                                      axis_domains=axis_domains,
                                      axis_lstarts=axis_lstarts,
                                      axis_lincs=axis_lincs,
                                      axis_pstarts=axis_pstarts,
                                      axis_pincs=axis_pincs,
                                      secondaries=secondaries)

    if prop_name is None:
        if cube.current_property is None:
            cube.set_current_property()
        prop_name = cube.current_property
    array3d = cube.prop[prop_name]['array3d']

    # prepare header data
    headers = {}
    TRC_TYPE = np.ones(ntrace, dtype='int32')
    TFULL_S = cube.dict_vidx['DP_FRST']
    TFULL_E = cube.dict_vidx['DP_LAST']
    TLIVE_S = cube.dict_vidx['DP_FRST']
    TLIVE_E = cube.dict_vidx['DP_LAST']
    start = cube.dict_vidx['XL_FRST']
    stop = cube.dict_vidx['XL_LAST']
    SEQNO = np.linspace(1, ntrace, ntrace, dtype='int32')
    XLINE_NO = np.linspace(start, stop, ntrace, dtype='int32')
    headers["SEQNO"] = SEQNO
    headers["XLINE_NO"] = XLINE_NO
    headers["TRC_TYPE"] = TRC_TYPE
    headers["TFULL_S"] = TFULL_S
    headers["TFULL_E"] = TFULL_E
    headers["TLIVE_S"] = TLIVE_S
    headers["TLIVE_E"] = TLIVE_E

    Parallel(n_jobs=NCORE)(delayed(write1frame)(i + 1, nframe, jsd,
        cube.dict_vidx, headers, ntrace, array3d[i]) for i in range(nframe))

    endTime = datetime.now()
    logger.info("Time Used is {}".format(endTime - startTime))


"""
When this function is defined inside the class method, after compiled by Cython,
joblib raises this error
_pickle.PicklingError: Cannot pickle <cyfunction Cube.inst_from_js_file.<locals>.read1frame
at 0x2aaab2687778>: attribute lookup read1frame on ezcad.gocube.cube failed
https://stackoverflow.com/questions/8804830/python-multiprocessing-picklingerror-cant-pickle-type-function
https://docs.python.org/3/library/pickle.html#what-can-be-pickled-and-unpickled
In particular, functions are only picklable if they are defined at the top-level of a module.
"""


def read1frame(iframe, nframe, jsd):
    # print to terminal by each work thread
    if iframe % 20 == 0:
        print("reading frame {} of {}".format(iframe, nframe))
    return jsd.read_frame_trcs(iframe)


def write1frame(iframe, nframe, jsd, dict_vidx, headers, fold, array2d):
    # print to terminal by each work thread
    if iframe % 20 == 0:
        print("writing frame {} of {}".format(iframe, nframe))
    ilno = dict_vidx['IL_FRST'] + (iframe - 1) * dict_vidx['IL_NCRT']
    headers["ILINE_NO"] = ilno
    headers["FRAME"] = iframe
    jsd.write_frame(array2d, headers, fold, iframe)
