# -*- coding: utf-8 -*-

"""
Module that contains different utils functions related with Plot Twist project
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import tpDcc as tp


def clean_scene():
    """
    Clean current scene
    """

    if not tp.is_maya():
        return

    from tpDcc.dccs.maya.core import scene
    scene.clean_scene()

    extra_node_types_to_delete = []
