#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool to manage the nomenclature of the project
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import artellapipe

# Defines ID of the tool
TOOL_ID = 'artellapipe-tools-namemanager'

# We skip the reloading of this module when launching the tool
no_reload = True


class NameManagerTool(artellapipe.Tool, object):
    def __init__(self, *args, **kwargs):
        super(NameManagerTool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = artellapipe.Tool.config_dict(file_name=file_name)
        tool_config = {
            'name': 'Name Manager',
            'id': 'artellapipe-tools-namemanager',
            'logo': 'namemanager_logo',
            'icon': 'rename',
            'tooltip': 'Tool to manage the nomenclature of the project',
            'tags': ['name', 'manager'],
            'sentry_id': 'https://d50e6953c45b44609a9e88d3bc3064d8@sentry.io/1764141',
            'is_checkable': False,
            'is_checked': False,
            'menu_ui': {'label': 'Name Manager', 'load_on_startup': False, 'color': '', 'background_color': ''},
            'menu': [
                {'label': 'TD',
                 'type': 'menu', 'children': [{'id': 'artellapipe-tools-namemanager', 'type': 'tool'}]}],
            'shelf': [
                {'name': 'TD',
                 'children': [{'id': 'artellapipe-tools-namemanager', 'display_label': False, 'type': 'tool'}]}
            ]
        }
        base_tool_config.update(tool_config)

        return base_tool_config


class NameManagerToolset(artellapipe.Toolset, object):
    ID = TOOL_ID

    def __init__(self, *args, **kwargs):
        super(NameManagerToolset, self).__init__(*args, **kwargs)

    def contents(self):

        from artellapipe.tools.namemanager.widgets import namemanager

        name_manager = namemanager.NameManager(
            project=self._project, config=self._config, settings=self._settings, parent=self)
        return [name_manager]
