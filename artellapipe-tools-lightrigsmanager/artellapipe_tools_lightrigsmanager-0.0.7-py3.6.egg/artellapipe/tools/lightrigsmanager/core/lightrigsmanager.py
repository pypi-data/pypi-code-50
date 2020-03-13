#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool to easily import light rigs into DCC scenes
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import artellapipe

# Defines ID of the tool
TOOL_ID = 'artellapipe-tools-lightrigsmanager'

# We skip the reloading of this module when launching the tool
no_reload = True


class LightRigsManagerTool(artellapipe.Tool, object):
    def __init__(self, *args, **kwargs):
        super(LightRigsManagerTool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = artellapipe.Tool.config_dict(file_name=file_name)
        tool_config = {
            'name': 'Light Rigs Manager',
            'id': 'artellapipe-tools-lightrigsmanager',
            'logo': 'lightrigsmanager_logo',
            'icon': 'idea',
            'tooltip': 'Tool to easily import light rigs into DCC scenes',
            'tags': ['light', 'light rig'],
            'sentry_id': 'https://5382260e62d448b881a24ea95f70ef4f@sentry.io/1764569',
            'is_checkable': False,
            'is_checked': False,
            'import_order': ['widgets', 'core'],
            'menu_ui': {'label': 'Light Rigs Manager', 'load_on_startup': False, 'color': '', 'background_color': ''},
            'menu': [
                {'label': 'Lighting',
                 'type': 'menu', 'children': [{'id': 'artellapipe-tools-lightrigsmanager', 'type': 'tool'}]}],
            'shelf': [
                {'name': 'Lighting',
                 'children': [{'id': 'artellapipe-tools-lightrigsmanager', 'display_label': False, 'type': 'tool'}]}
            ]
        }
        base_tool_config.update(tool_config)

        return base_tool_config


class LightRigsManagerToolset(artellapipe.Toolset, object):
    ID = TOOL_ID

    def __init__(self, *args, **kwargs):
        super(LightRigsManagerToolset, self).__init__(*args, **kwargs)

    def contents(self):

        from artellapipe.tools.lightrigsmanager.widgets import lightrigsmanager

        lights_rig_manager = lightrigsmanager.ArtellaLightRigManager(
            project=self._project, config=self._config, settings=self._settings, parent=self)
        return [lights_rig_manager]
