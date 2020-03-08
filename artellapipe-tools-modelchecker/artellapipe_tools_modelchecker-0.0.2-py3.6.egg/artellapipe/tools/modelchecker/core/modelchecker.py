#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool to execute modeling checks for geometry
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import artellapipe

# Defines ID of the tool
TOOL_ID = 'artellapipe-tools-modelchecker'

# We skip the reloading of this module when launching the tool
no_reload = True


class ModelCheckerTool(artellapipe.Tool, object):
    def __init__(self, *args, **kwargs):
        super(ModelCheckerTool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = artellapipe.Tool.config_dict(file_name=file_name)
        tool_config = {
            'name': 'Model Checker',
            'id': 'artellapipe-tools-modelchecker',
            'logo': 'modelchecker_logo',
            'icon': 'modelchecker',
            'tooltip': 'Tool to execute modeling checks for geometry',
            'tags': ['model', 'checker', 'pyblish'],
            'sentry_id': 'https://6633e9b4b4c7418fb7b22efc86f0309f@sentry.io/1832212',
            'is_checkable': False,
            'is_checked': False,
            'menu_ui': {
                'label': 'Model Checker', 'load_on_startup': False, 'color': '', 'background_color': ''},
            'menu': [
                {'label': 'Modeling',
                 'type': 'menu', 'children': [{'id': 'artellapipe-tools-modelchecker', 'type': 'tool'}]}],
            'shelf': [
                {'name': 'Modeling',
                 'children': [{'id': 'artellapipe-tools-modelchecker', 'display_label': False, 'type': 'tool'}]}
            ]
        }
        base_tool_config.update(tool_config)

        return base_tool_config


class ModelCheckerToolset(artellapipe.Toolset, object):
    ID = TOOL_ID

    def __init__(self, *args, **kwargs):
        super(ModelCheckerToolset, self).__init__(*args, **kwargs)

    def contents(self):

        from artellapipe.tools.modelchecker.widgets import modelchecker

        model_checker = modelchecker.ArtellaModelChecker(
            project=self._project, config=self._config, settings=self._settings, parent=self)
        return [model_checker]
