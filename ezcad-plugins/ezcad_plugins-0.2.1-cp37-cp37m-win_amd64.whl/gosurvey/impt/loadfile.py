# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import os.path as osp
from .read_file import read_sgmt, read_vt3dc
from ..survey import Survey


def load_survey_sgmt(fufn, object_name=None):
    """Load survey from sgmt file.

    :param fufn: full-path filename
    :type fufn: str
    :param object_name: name of the new object
    :type object_name: str
    :return: a survey object
    :rtype: :class:`~ezcad.gosurvey.survey.Survey`
    """
    if object_name is None:
        path, fn = osp.split(fufn)
        object_name = osp.splitext(fn)[0]
    dict_sgmt = read_sgmt(fufn)
    survey = Survey(object_name)
    survey.set_geometry(dict_sgmt)
    survey.initialize()
    return survey


def load_survey_vt3dc(fufn, object_name=None):
    """Load survey from vt3dc file.
    vt3dc stands for the Dual Coordinates of 3 vertices
    of the rectangle of the survey bounding box.

    :param fufn: full-path filename
    :type fufn: str
    :param object_name: name of the new object
    :type object_name: str
    :return: a survey object
    :rtype: :class:`~ezcad.gosurvey.survey.Survey`
    """
    if object_name is None:
        path, fn = osp.split(fufn)
        object_name = osp.splitext(fn)[0]
    dict_sgmt = read_vt3dc(fufn)
    survey = Survey(object_name)
    survey.set_geometry(dict_sgmt)
    survey.initialize()
    return survey
