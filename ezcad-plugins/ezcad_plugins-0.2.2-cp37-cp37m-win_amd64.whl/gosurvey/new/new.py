# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""Create a new survey"""

from ..survey import Survey


def from_coord(name, xOrigin, yOrigin, xInlineEnd, yInlineEnd,
    xCrosslineEnd, yCrosslineEnd, ilMin, ilMax, xlMin, xlMax):
    """Create survey from coordinate.
    Arguments follow convention in
    Landmark SeisSpace flow "3D Poststack Geometry" End Coordinates

    :return: a survey object
    :rtype: :class:`~ezcad.gosurvey.survey.Survey`
    """
    p1 = (ilMin, xlMin, xOrigin, yOrigin)    
    p2 = (ilMin, xlMax, xInlineEnd, yInlineEnd)
    p3 = (ilMax, xlMin, xCrosslineEnd, yCrosslineEnd)
    dict_sgmt = new_sgmt_from_points(p1, p2, p3)
    survey = new_survey_from_sgmt(dict_sgmt, name=name)
    return survey


def new_survey_from_vidx(dict_vidx, xys=None):
    """Create survey from vidx.

    :param dict_vidx: volume indexes
    :type dict_vidx: dict
    :param xys: (p1x, p1y, p2x, p2y, p3x, p3y)
    :type xys: tuple
    :return: a survey object
    :rtype: :class:`~ezcad.gosurvey.survey.Survey`
    """
    if xys is None:
        xys = (0.0, 0.0, 0.0, 10.0, 10.0, 0.0)
    dict_sgmt = {
        'P1_ILNO': dict_vidx['IL_FRST'],
        'P1_XLNO': dict_vidx['XL_FRST'],
        'P1_CRSX': xys[0],
        'P1_CRSY': xys[1],
        'P2_ILNO': dict_vidx['IL_FRST'],
        'P2_XLNO': dict_vidx['XL_LAST'],
        'P2_CRSX': xys[2],
        'P2_CRSY': xys[3],
        'P3_ILNO': dict_vidx['IL_LAST'],
        'P3_XLNO': dict_vidx['XL_FRST'],
        'P3_CRSX': xys[4],
        'P3_CRSY': xys[5]
    }
    survey = new_survey_from_sgmt(dict_sgmt)
    return survey


def new_survey_from_points(p1=None, p2=None, p3=None):
    """Create survey from points.

    :param p1: survey origin, (ilno, xlno, crsx, crsy)
    :type p1: tuple
    :param p2: survey corner, (ilno, xlno, crsx, crsy)
    :type p2: tuple
    :param p3: survey corner, (ilno, xlno, crsx, crsy)
    :type p3: tuple
    :return: a survey object
    :rtype: :class:`~ezcad.gosurvey.survey.Survey`
    """
    # y         p2         xlno2
    # |         |          |
    # |         |          |
    # o______x  p1_____p3  xlno1  ilno1_____ilno2
    dict_sgmt = new_sgmt_from_points(p1, p2, p3)
    survey = new_survey_from_sgmt(dict_sgmt)
    return survey


def new_survey_from_sgmt(dict_sgmt, name="DEFAULT"):
    """Create survey from sgmt.

    :param dict_sgmt: survey geometry
    :type dict_sgmt: dict
    :param name: name of the survey
    :type name: str
    :return: a survey object
    :rtype: :class:`~ezcad.gosurvey.survey.Survey`
    """
    survey = Survey(name)
    survey.set_geometry(dict_sgmt)
    survey.initialize()
    return survey


def new_sgmt_from_points(p1=None, p2=None, p3=None):
    """Create sgmt from points.

    :param p1: survey origin, (ilno, xlno, crsx, crsy)
    :type p1: tuple
    :param p2: survey corner, (ilno, xlno, crsx, crsy)
    :type p2: tuple
    :param p3: survey corner, (ilno, xlno, crsx, crsy)
    :type p3: tuple
    :return: a survey object
    :rtype: :class:`~ezcad.gosurvey.survey.Survey`
    """
    # y         p2         xlno2
    # |         |          |
    # |         |          |
    # o______x  p1_____p3  xlno1  ilno1_____ilno2
    if p1 is None:
        p1 = (1,  1,  0.0,  0.0)
    if p2 is None:
        p2 = (1, 11,  0.0, 10.0)
    if p3 is None:
        p3 = (11,  1, 10.0,  0.0)

    dict_sgmt = {
        'P1_ILNO': p1[0],
        'P1_XLNO': p1[1],
        'P1_CRSX': p1[2],
        'P1_CRSY': p1[3],
        'P2_ILNO': p2[0],
        'P2_XLNO': p2[1],
        'P2_CRSX': p2[2],
        'P2_CRSY': p2[3],
        'P3_ILNO': p3[0],
        'P3_XLNO': p3[1],
        'P3_CRSX': p3[2],
        'P3_CRSY': p3[3]
    }
    return dict_sgmt
