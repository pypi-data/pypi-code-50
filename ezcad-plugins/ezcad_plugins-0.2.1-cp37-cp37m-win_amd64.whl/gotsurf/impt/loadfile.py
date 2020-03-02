# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import os
import numpy as np
from ..surface import Tsurface


# def surf_demo():
#     verts = np.array([
#         [0.0, 450000.0, -20000.0],
#         [400000.0, 450000.0, -20000.0],
#         [400000.0, 800000.0, -20000.0],
#         [0.0, 800000.0, -20000.0]
#     ])
#     faces = np.array([
#         [0, 1, 2],
#         [0, 2, 3]
#     ])
#     object_name = 'test_surf'
#     dob = Tsurface(object_name, verts, faces)
#     dob.set_xyz_range()
#     return dob


def load_gocad_tsurf(fufn, object_name=None, columns=None):
    """Load Gocad tsurf.

    :param fufn: full-path filename
    :type fufn: str
    :param object_name: name of the new object
    :type object_name: str
    :param columns: column number and name, e.g. 1,step;2,loss
    :type columns: str
    :return: a tsurface object
    :rtype: :class:`~ezcad.gotsurf.surface.Tsurface`
    """
    # read file
    prop_names, vertexes, arrayTriangles = \
        read_gocad_tsurf(fufn, columns=columns)
    # vertexes = arrayVertexes[:, 0:3]
    if object_name is None:
        path, fn = os.path.split(fufn)
        object_name = os.path.splitext(fn)[0]

    dob = Tsurface(object_name)
    # dob.set_atom_style()
    # dob.set_line_style()
    dob.set_vertexes(vertexes)
    dob.set_triangles(triangles=arrayTriangles)  # Delaunay
    dob.init_property(prop_names, vertexes)
    dob.set_xyz_range()
    return dob


def read_gocad_tsurf(fufn, columns=None):
    """Read Gocad tsurface file.

    :param fufn: full-path filename
    :type fufn: str
    :param columns: column number and name, e.g. 1,step;2,loss
    :type columns: str
    :return: prop_names, vertexes, triangles.
      prop_names: list, property names.
      vertexes: array, shape n by m where n is the number of vertexes
      and m is the number of properties.
      triangles: array, shape t by 3 where t is the number of triangles
      and 3 is the vertex index of the triangle.
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
    listTriangles = []
    f = open(fufn, 'r')
    for line in f:
        line = line.strip()
        lineColumns = line.split()
        if line[:4] == 'VRTX':
            take = [lineColumns[i-1] for i in propertyColumns]
            listVertexes.append(take)
        elif line[:5] == 'PVRTX':  # Gocad version 2009.4
            take = [lineColumns[i-1] for i in propertyColumns]
            listVertexes.append(take)
        elif line[:4] == 'TRGL':
            listTriangles.append(lineColumns[1:4])
        else:
            pass

    vertexes = np.array(listVertexes, dtype='float32')
    triangles = np.array(listTriangles, dtype='int32')

    # Gocad Tsurf VRTX index starts from 1, while Python list/array index
    # starts from 0, so here every element minus one.
    triangles -= 1

    return prop_names, vertexes, triangles


# def read_gocad_tsurf_auto(fufn):
#     prop_names = []
#     listVertexes = []
#     listTriangles = []
#     f = open(fufn, 'r')
#     for line in f:
#         line = line.strip()
#         columns = line.split()
#         if line[:21] == 'PROPERTY_CLASS_HEADER':
#             prop_names.append(columns[1])
#         elif line[:4] == 'VRTX':
#             # list has order, so no need to read the vertex sequence number.
#             # TODO read properties and save by name from metadata headers
#             # Use the first vertex to define number of columns, which
#             # is to handle some vertexes sometimes have "CNXYZ" at end.
#             if len(listVertexes) == 0:
#                 n = len(columns)
#             listVertexes.append(columns[2:n])
#         elif line[:5] == 'PVRTX':  # Gocad version 2009.4
#             if len(listVertexes) == 0:
#                 n = len(columns)
#             listVertexes.append(columns[2:n])
#         elif line[:4] == 'TRGL':
#             listTriangles.append(columns[1:4])
#         else:
#             pass
#
#     vertexes = np.array(listVertexes, dtype='float32')
#     triangles = np.array(listTriangles, dtype='int32')
#
#     nprop = len(prop_names)
#     ncolm = vertexes.shape[1]
#     print('Number of property names were read:', nprop)
#     print('Number of property columns were read:', ncolm)
#     if nprop < ncolm:
#         logger.warning("The number of properties is less than the number of "
#         "columns in data array. Default property names are used.")
#         prop_names = DEFAULT_PROPERTY_NAMES[:ncolm]
#     print('Property names to be used:', prop_names)
#
#     # Gocad Tsurf VRTX index starts from 1, while Python list/array index
#     # starts from 0, so here every element minus one.
#     triangles -= 1
#
#     return prop_names, vertexes, triangles
