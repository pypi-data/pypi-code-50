# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""
Read Gocad PLine file.
"""

import numpy as np
from ezcad.utils.envars import DEFAULT_PROPERTY_NAMES


def read_gocad_pline(fufn):
    prop_names = []
    listVertexes = []
    # This listConnect is used for line plot by pyqtgraph.PlotDataItem
    # It assumes one vertex connects to the next and only breaks at 'ILINE'.
    # It ignores the file lines starting with 'SEG'.
    listConnect = []
    # This listSegment is used for line plot by vispy.LinePlotVisual
    listSegment = []
    f = open(fufn, 'r')
    count = 0
    for line in f:
        if line[:21] == 'PROPERTY_CLASS_HEADER':
            line = line.strip()
            columns = line.split()
            prop_names.append(columns[1])
            # TODO need test, what if name is "new prop"?

        if line[:4] == 'VRTX':
            count += 1
            line = line.strip()
            columns = line.split()
            # VRTX 1 159701.1 581228.6 -33982.3 0.21 1500.0
            # listVertexes.append(columns[2:5]) # XYZ
            listVertexes.append(columns[2:])
            connect = 1
            listConnect.append(connect)
        if line[:5] == 'ILINE':
            if count == 0:
                pass
            else:
                listConnect[count-1] = 0

        if line[:3] == 'SEG':
            line = line.strip()
            columns = line.split()
            listSegment.append(columns[1:3])

    connect = np.array(listConnect)
    segment = np.array(listSegment, dtype='int32')
    arrayVertexes = np.array(listVertexes, dtype='float32')

    segment -= 1  # python index starts 0 not 1

    nprop = len(prop_names)
    ncolm = arrayVertexes.shape[1]
    if nprop < ncolm:
        # file from older version, without this header.
        prop_names = DEFAULT_PROPERTY_NAMES[:ncolm]

    return prop_names, arrayVertexes, connect, segment
