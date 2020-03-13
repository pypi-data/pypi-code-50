#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool to easily import and reference assets file into DCC scene
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import artellapipe

# Defines ID of the tool
TOOL_ID = 'artellapipe-tools-assetslibrary'

# We skip the reloading of this module when launching the tool
no_reload = True


class AssetsLibraryTool(artellapipe.Tool, object):
    def __init__(self, *args, **kwargs):
        super(AssetsLibraryTool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = artellapipe.Tool.config_dict(file_name=file_name)
        tool_config = {
            'name': 'Assets Library',
            'id': 'artellapipe-tools-assetslibrary',
            'logo': 'assetslibrary_logo',
            'icon': 'assets_library',
            'tooltip': 'Tool to easily import and reference assets file into DCC scene',
            'tags': ['assets', 'library'],
            'sentry_id': 'https://6ce3277bc9d646029e1062bdf7e56f24@sentry.io/1764122',
            'is_checkable': False,
            'is_checked': False,
            'menu_ui': {'label': 'Assets Library', 'load_on_startup': False, 'color': '', 'background_color': ''},
            'menu': [
                {'label': 'Assets',
                 'type': 'menu', 'children': [{'id': 'artellapipe-tools-assetslibrary', 'type': 'tool'}]}],
            'shelf': [
                {'name': 'Assets',
                 'children': [{'id': 'artellapipe-tools-assetslibrary', 'display_label': False, 'type': 'tool'}]}
            ]
        }
        base_tool_config.update(tool_config)

        return base_tool_config


class AssetsLibraryToolset(artellapipe.Toolset, object):
    ID = TOOL_ID

    def __init__(self, *args, **kwargs):
        super(AssetsLibraryToolset, self).__init__(*args, **kwargs)

    def contents(self):

        from artellapipe.tools.assetslibrary.widgets import assetslibrary

        assets_library = assetslibrary.ArtellaAssetsLibrary(
            project=self._project, config=self._config, settings=self._settings, parent=self)
        return [assets_library]
