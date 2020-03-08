#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool to rename DCC objects in an easy way
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import artellapipe

# Defines ID of the tool
TOOL_ID = 'artellapipe-tools-renamer'

# We skip the reloading of this module when launching the tool
no_reload = True


class RenamerTool(artellapipe.Tool, object):
    def __init__(self, *args, **kwargs):
        super(RenamerTool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = artellapipe.Tool.config_dict(file_name=file_name)
        tool_config = {
            'name': 'Renamer',
            'id': 'artellapipe-tools-renamer',
            'logo': 'renamer_logo',
            'icon': 'renamer',
            'tooltip': 'Tool to rename DCC objects in an easy way',
            'tags': ['renamer', 'dcc'],
            'sentry_id': 'https://0e351be2ec4d4360980db9b85980e176@sentry.io/1864142',
            'is_checkable': False,
            'is_checked': False,
            'menu_ui': {'label': 'Renamer', 'load_on_startup': False, 'color': '', 'background_color': ''},
            'menu': [
                {'label': 'General',
                 'type': 'menu', 'children': [{'id': 'artellapipe-tools-renamer', 'type': 'tool'}]}],
            'shelf': [
                {'name': 'General',
                 'children': [{'id': 'artellapipe-tools-renamer', 'display_label': False, 'type': 'tool'}]}
            ]
        }
        base_tool_config.update(tool_config)

        return base_tool_config


class RenamerToolset(artellapipe.Toolset, object):
    ID = TOOL_ID

    def __init__(self, *args, **kwargs):
        super(RenamerToolset, self).__init__(*args, **kwargs)

    def contents(self):

        from artellapipe.tools.renamer.widgets import renamer

        renamer_widget = renamer.ArtellaRenamerWidget(
            config=self._config, parent=self)
        return [renamer_widget]
