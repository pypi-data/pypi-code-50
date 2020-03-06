# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""
Read Gocad VSet file.
"""

import numpy as np


def read_gocad_vset(fufn, columns=None):
    """Read Gocad vset file.

    :param fufn: full-path filename
    :type fufn: str
    :param columns: column number and name, e.g. 1,step;2,loss
    :type columns: str
    :returns: prop_names, list, property names, length m.
      vertexes, array, shape n by m where n is the number of vertexes
      and m is the number of properties.
    :rtype: tuple
    """
    prop_names = []
    propertyColumns = []
    if columns is None:
        columns = '3,X;4,Y;5,Z'
    columns = columns.split(';')
    columns = [x.strip() for x in columns]
    for column in columns:
        columnNumber = int(column.split(',')[0])
        columnName = column.split(',')[1].strip()
        prop_names.append(columnName)
        propertyColumns.append(columnNumber)

    listVertexes = []
    with open(fufn, 'r') as f:
        for line in f:
            line = line.strip()
            lineColumns = line.split()
            if line[:4] == 'VRTX' or line[:5] == 'PVRTX':
                take = [lineColumns[i-1] for i in propertyColumns]
                listVertexes.append(take)

    vertexes = np.array(listVertexes, dtype='float32')
    return prop_names, vertexes
