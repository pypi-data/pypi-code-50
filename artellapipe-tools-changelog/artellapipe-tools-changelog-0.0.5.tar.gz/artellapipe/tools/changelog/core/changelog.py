#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool that shows generic changelog for Artella project
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import artellapipe

# Defines ID of the tool
TOOL_ID = 'artellapipe-tools-changelog'

# We skip the reloading of this module when launching the tool
no_reload = True


class ChangelogTool(artellapipe.Tool, object):
    def __init__(self, *args, **kwargs):
        super(ChangelogTool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = artellapipe.Tool.config_dict(file_name=file_name)
        tool_config = {
            'name': 'Changelog',
            'id': 'artellapipe-tools-changelog',
            'logo': 'changelog_logo',
            'icon': 'document',
            'tooltip': 'Tool that shows changelog of the different versions',
            'tags': ['changelog'],
            'sentry_id': 'https://780f09885fe84358a3d54f5f475a82fc@sentry.io/1764084',
            'is_checkable': False,
            'is_checked': False,
            'menu_ui': {'label': 'Changelog', 'load_on_startup': False, 'color': '', 'background_color': ''},
            'menu': [
                {'label': 'General',
                 'type': 'menu', 'children': [{'id': 'artellapipe-tools-changelog', 'type': 'tool'}]}],
            'shelf': [
                {'name': 'General',
                 'children': [{'id': 'artellapipe-tools-changelog', 'display_label': False, 'type': 'tool'}]}
            ]
        }
        base_tool_config.update(tool_config)

        return base_tool_config


class ChangelogToolset(artellapipe.Toolset, object):
    ID = TOOL_ID

    def __init__(self, *args, **kwargs):
        super(ChangelogToolset, self).__init__(*args, **kwargs)

    def contents(self):

        from artellapipe.tools.changelog.widgets import changelog

        changelog_widget = changelog.ArtellaChangelog(
            project=self._project, config=self._config, settings=self._settings, parent=self)
        return [changelog_widget]
