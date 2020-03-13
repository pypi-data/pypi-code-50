#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool to handle bugs and requests for the different tools of the pipeline
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import artellapipe

# Defines ID of the tool
TOOL_ID = 'artellapipe-tools-bugtracker'

# We skip the reloading of this module when launching the tool
no_reload = True


class BugTrackerTool(artellapipe.Tool, object):
    def __init__(self, *args, **kwargs):
        super(BugTrackerTool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = artellapipe.Tool.config_dict(file_name=file_name)
        tool_config = {
            'name': 'Bug Tracker',
            'id': 'artellapipe-tools-bugtracker',
            'logo': 'bugtracker_logo',
            'icon': 'bugtracker',
            'tooltip': 'Tool to handle bugs and requests for the different tools of the pipeline',
            'tags': ['error', 'bug', 'report'],
            'sentry_id': 'https://9d2160bb725a4fbcacb4d72aa9df6eaf@sentry.io/1797903',
            'is_checkable': False,
            'is_checked': False,
            'menu_ui': {'label': 'Bug Tracker', 'load_on_startup': False, 'color': '', 'background_color': ''},
            'menu': [
                {'label': 'General',
                 'type': 'menu', 'children': [{'id': 'artellapipe-tools-bugtracker', 'type': 'tool'}]}],
            'shelf': [
                {'name': 'General',
                 'children': [{'id': 'artellapipe-tools-bugtracker', 'display_label': False, 'type': 'tool'}]}
            ]
        }
        base_tool_config.update(tool_config)

        return base_tool_config


class BugTrackerToolset(artellapipe.Toolset, object):
    ID = TOOL_ID

    def __init__(self, *args, **kwargs):

        self._tool = kwargs.pop('tool', None)
        self._traceback = kwargs.pop('traceback', None)

        super(BugTrackerToolset, self).__init__(*args, **kwargs)

    def contents(self):

        from artellapipe.tools.bugtracker.widgets import bugtracker

        bug_tracker = bugtracker.ArtellaBugTracker(
            project=self._project, config=self._config, settings=self._settings, parent=self,
            tool=self._tool, traceback=self._traceback)
        return [bug_tracker]
