#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool to easily manage to dependencies of DCC files
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import artellapipe

# Defines ID of the tool
TOOL_ID = 'artellapipe-tools-dependenciesmanager'

# We skip the reloading of this module when launching the tool
no_reload = True


class DependenciesManagerTool(artellapipe.Tool, object):
    def __init__(self, *args, **kwargs):
        super(DependenciesManagerTool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = artellapipe.Tool.config_dict(file_name=file_name)
        tool_config = {
            'name': 'Artella Dependencies Manager',
            'id': 'artellapipe-tools-dependenciesmanager',
            'logo': 'dependenciesmanager_logo',
            'icon': 'dependencies',
            'tooltip': 'Tool to easily manage to dependencies of DCC files',
            'tags': ['artella', 'manager', 'files', 'dependencies', 'sync'],
            'sentry_id': 'https://bd40ce7d42d44d9eb0ec6fc4f3f58e1c@sentry.io/1840333',
            'is_checkable': False,
            'is_checked': False,
            'import_order': ['widgets', 'core'],
            'menu_ui': {
                'label': 'Artella Dependencies Manager', 'load_on_startup': False, 'color': '', 'background_color': ''},
            'menu': [
                {'label': 'Artella',
                 'type': 'menu', 'children': [{'id': 'artellapipe-tools-dependenciesmanager', 'type': 'tool'}]}],
            'shelf': [
                {'name': 'Artella',
                 'children': [{'id': 'artellapipe-tools-dependenciesmanager', 'display_label': False, 'type': 'tool'}]}
            ]
        }
        base_tool_config.update(tool_config)

        return base_tool_config


class DependenciesManagerToolset(artellapipe.Toolset, object):
    ID = TOOL_ID

    def __init__(self, *args, **kwargs):
        super(DependenciesManagerToolset, self).__init__(*args, **kwargs)

    def contents(self):

        from artellapipe.tools.dependenciesmanager.widgets import dependenciesmanager

        dependencies_manager = dependenciesmanager.DependenciesManager(
            project=self._project, config=self._config, settings=self._settings, parent=self)
        return [dependencies_manager]
