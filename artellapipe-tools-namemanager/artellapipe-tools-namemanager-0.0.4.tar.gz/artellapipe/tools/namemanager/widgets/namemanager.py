#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool that allow to define the nomenclature of the pipeline files
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import logging

from tpDcc.tools.nameit.widgets import nameit

import artellapipe
from artellapipe.libs import naming
from artellapipe.libs.naming.core import naminglib

LOGGER = logging.getLogger()


class NameWidget(nameit.NameIt, object):

    NAMING_LIB = naminglib.ArtellaNameLib

    def __init__(self, project, parent=None):
        self._project = project
        super(NameWidget, self).__init__(data_file=naming.config.get_path(), parent=parent)


class NameManager(artellapipe.ToolWidget, object):
    def __init__(self, project, config, settings, parent):
        super(NameManager, self).__init__(project=project, config=config, settings=settings, parent=parent)

    def ui(self):
        super(NameManager, self).ui()

        self._name_widget = NameWidget(project=self._project)
        self.main_layout.addWidget(self._name_widget)

    # def close_tool_attacher(self):
    #     self._name_widget.NAMING_LIB().save_session()
    #     super(NameManager, self).close_tool_attacher()

    @property
    def nameit(self):
        return self._name_widget
