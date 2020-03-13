#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains implementation for Artella Manager plugin
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"


import logging

from Qt.QtCore import *
from Qt.QtWidgets import *

from artellapipe.launcher.core import plugin
from artellapipe.tools.artellamanager.widgets import artellamanagerwidget

LOGGER = logging.getLogger()


class ArtellaManager(plugin.ArtellaLauncherPlugin, object):

    LABEL = 'Artella Manager'
    ICON = 'artellamanager_plugin'

    def __init__(self, project, launcher, parent=None):
        super(ArtellaManager, self).__init__(project=project, launcher=launcher, parent=parent)

    def get_main_layout(self):
        """
        Overrides base get_main_layout function
        :return: QLayout
        """

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignTop)
        return main_layout

    def ui(self):
        super(ArtellaManager, self).ui()

        artella_manager_tool = artellamanagerwidget.ArtellaManagerWidget(project=self._project)

        self.main_layout.addWidget(artella_manager_tool)
