#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool that contains solstice outliner widget implementation
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from artellapipe.tools.outliner.widgets import outliner


class SolsticeOutlinerWidget(outliner.ArtellaOutlinerWidget, object):
    def __init__(self, project, config, settings, parent):
        super(SolsticeOutlinerWidget, self).__init__(project=project, config=config, settings=settings, parent=parent)
