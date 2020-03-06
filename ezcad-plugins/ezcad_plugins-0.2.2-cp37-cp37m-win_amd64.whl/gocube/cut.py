# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""
  Replace array cubeIndex with dictionary dict_vidx
  Change section_type from integers to intuitive strings
  Replace arguments that may or may not be specified, with kwargs.
  @author Joseph Zhu
  @version 0.1
  @date 2016/12/19
 
  Cut a 3D cube to 2D section
  Input a 3D array and output a 2D array
  @author Joseph Zhu
  @version 0.0
  @date 2016/11/4
"""

import numpy as np


def cut_cube(array3d, dict_vidx, section_type, section_number, **kwargs):
    """Cut 3D cube to 2D section.
    If the section_type is aline, section_number is an integer array,
    n-by-2, [ILNO,XLNO] of the line.

    :param array3d: the 3D data array, [NIL,NXL,NDP]
    :type array3d: array
    :param dict_vidx: volume index
    :type dict_vidx: dict
    :param section_type: section type, e.g. iline, xline, depth, aline
    :type section_type: str
    :param section_number: section number
    :type section_number: int
    :param kwargs: key-word arguments
        xmin: integer, section minimum x to crop
        xmax: integer, section maximum x to crop
        ymin: integer, section minimum y to crop
        ymax: integer, section maximum y to crop
    :return: section 2D data array
    :rtype: array
    """
    IL_FRST = dict_vidx['IL_FRST']
    IL_LAST = dict_vidx['IL_LAST']
    IL_NCRT = dict_vidx['IL_NCRT']
    XL_FRST = dict_vidx['XL_FRST']
    XL_LAST = dict_vidx['XL_LAST']
    XL_NCRT = dict_vidx['XL_NCRT']
    DP_FRST = dict_vidx['DP_FRST']
    DP_LAST = dict_vidx['DP_LAST']
    DP_NCRT = dict_vidx['DP_NCRT']

    if section_number is None:
        # If not given, plot the first section.
        if section_type == 'iline':
            section_number = IL_FRST
        if section_type == 'xline':
            section_number = XL_FRST
        if section_type == 'depth':
            section_number = DP_FRST

    if section_type == 'iline':
        # plot is crossline (x) and depth (y)
        ilno = section_number
        ilno = IL_FRST if ilno < IL_FRST else ilno
        ilno = IL_LAST if ilno > IL_LAST else ilno
        xmin = kwargs.get('xmin', XL_FRST)
        xmin = XL_FRST if xmin < XL_FRST else xmin
        xmax = kwargs.get('xmax', XL_LAST)
        xmax = XL_LAST if xmax > XL_LAST else xmax
        ymin = kwargs.get('ymin', DP_FRST)
        ymin = DP_FRST if ymin < DP_FRST else ymin
        ymax = kwargs.get('ymax', DP_LAST)
        ymax = DP_LAST if ymax > DP_LAST else ymax
        ia = int(round((ilno - IL_FRST) / IL_NCRT))
        ja = int(round((xmin - XL_FRST) / XL_NCRT))
        jb = int(round((xmax - XL_FRST) / XL_NCRT))
        ka = int(round((ymin - DP_FRST) / DP_NCRT))
        kb = int(round((ymax - DP_FRST) / DP_NCRT))
        array2d = array3d[ia, ja:jb+1, ka:kb+1]

    elif section_type == 'xline':
        # plot is inline (x) and depth (y)
        xlno = section_number
        xlno = XL_FRST if xlno < XL_FRST else xlno
        xlno = XL_LAST if xlno > XL_LAST else xlno
        xmin = kwargs.get('xmin', IL_FRST)
        xmin = IL_FRST if xmin < IL_FRST else xmin
        xmax = kwargs.get('xmax', IL_LAST)
        xmax = IL_LAST if xmax > IL_LAST else xmax
        ymin = kwargs.get('ymin', DP_FRST)
        ymin = DP_FRST if ymin < DP_FRST else ymin
        ymax = kwargs.get('ymax', DP_LAST)
        ymax = DP_LAST if ymax > DP_LAST else ymax
        ia = int(round((xmin - IL_FRST) / IL_NCRT))
        ib = int(round((xmax - IL_FRST) / IL_NCRT))
        ja = int(round((xlno - XL_FRST) / XL_NCRT))
        ka = int(round((ymin - DP_FRST) / DP_NCRT))
        kb = int(round((ymax - DP_FRST) / DP_NCRT))
        array2d = array3d[ia:ib+1, ja, ka:kb+1]

    elif section_type == 'depth':
        # plot is inline (x) and crossline (y)
        dpno = section_number
        dpno = DP_FRST if dpno < DP_FRST else dpno
        dpno = DP_LAST if dpno > DP_LAST else dpno
        xmin = kwargs.get('xmin', IL_FRST)
        xmin = IL_FRST if xmin < IL_FRST else xmin
        xmax = kwargs.get('xmax', IL_LAST)
        xmax = IL_LAST if xmax > IL_LAST else xmax
        ymin = kwargs.get('ymin', XL_FRST)
        ymin = XL_FRST if ymin < XL_FRST else ymin
        ymax = kwargs.get('ymax', XL_LAST)
        ymax = XL_LAST if ymax > XL_LAST else ymax
        ia = int(round((xmin - IL_FRST) / IL_NCRT))
        ib = int(round((xmax - IL_FRST) / IL_NCRT))
        ja = int(round((ymin - XL_FRST) / XL_NCRT))
        jb = int(round((ymax - XL_FRST) / XL_NCRT))
        ka = int(round((dpno - DP_FRST) / DP_NCRT))
        array2d = array3d[ia:ib+1, ja:jb+1, ka]

    elif section_type == 'aline':
        # plot is arbitrary line (x) and depth (y)
        ymin = kwargs.get('ymin', DP_FRST)
        ymin = DP_FRST if ymin < DP_FRST else ymin
        ymax = kwargs.get('ymax', DP_LAST)
        ymax = DP_LAST if ymax > DP_LAST else ymax
        ka = int(round((ymin - DP_FRST) / DP_NCRT))
        kb = int(round((ymax - DP_FRST) / DP_NCRT))
        # get the section 2D list
        array2d = []
        line = section_number
        i_array = (line[:, 0] - IL_FRST) / IL_NCRT
        j_array = (line[:, 1] - XL_FRST) / XL_NCRT
        i_array = i_array.astype(int)
        j_array = j_array.astype(int)
        n_trace = line.shape[0]
        for i in range(n_trace):
            ia, ja = i_array[i], j_array[i]
            trace = array3d[ia, ja, ka:kb+1]
            array2d.append(trace)
        # convert list to array
        array2d = np.array(array2d)

    else:
        raise ValueError("Unknown section type")

    # For example, 2D array of shape [m, n], feed to vispy visual Image,
    # it renders an image of m rows and n columns.
    # The starter 3D array is of shape [NIL, NXL, NDP], and the cutting
    # preserves this order, i.e. at this step,
    # the iline section 2D array is [NXL, NDP],
    # the xline section 2D array is [NIL, NDP],
    # the depth section 2D array is [NIL, NXL],
    # the aline section 2D array is [NTR, NDP],
    # Geophysics convention is having depth in the vertical direction,
    # it is the Y axis in 2D XY coordinate system,
    # it is the m rows in the image example above.
    # This is why we do the transpose here.
    array2d = np.transpose(array2d, (1, 0))
    return array2d
