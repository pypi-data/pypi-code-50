#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool to generate static snow meshes for Solstice
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import artellapipe

# Defines ID of the tool
TOOL_ID = 'solstice-tools-snowgenerator'

# We skip the reloading of this module when launching the tool
no_reload = True


class SnowGeneratorTool(artellapipe.Tool, object):
    def __init__(self, *args, **kwargs):
        super(SnowGeneratorTool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = artellapipe.Tool.config_dict(file_name=file_name)
        tool_config = {
            'name': 'Snow Generator',
            'id': 'solstice-tools-snowgenerator',
            'logo': 'snowgenerator_logo',
            'icon': 'snowgenerator',
            'help_url': 'https://solstice-short-film.github.io/solstice-docs/pipeline/pipeline/tools/snowgenerator/',
            'kitsu_login': False,
            'tooltip': 'Tool to generate static snow meshes for Solstice',
            'tags': ['solstice', 'snow', 'generator'],
            'sentry_id': 'https://32d16a6960cd413fad0a4be211e6972b@sentry.io/1764702',
            'is_checkable': False,
            'is_checked': False,
            'menu_ui': {'label': 'Snow Generator', 'load_on_startup': False, 'color': '', 'background_color': ''},
            'menu': [
                {'label': 'Modeling',
                 'type': 'menu', 'children': [{'id': 'solstice-tools-snowgenerator', 'type': 'tool'}]}],
            'shelf': [
                {'name': 'Modeling',
                 'children': [{'id': 'solstice-tools-snowgenerator', 'display_label': False, 'type': 'tool'}]}
            ]
        }
        base_tool_config.update(tool_config)

        return base_tool_config


class SnowGeneratorToolset(artellapipe.Toolset, object):
    ID = TOOL_ID

    def __init__(self, *args, **kwargs):
        super(SnowGeneratorToolset, self).__init__(*args, **kwargs)

    def contents(self):

        from solstice.tools.snowgenerator.widgets import snowgenerator

        snow_generator = snowgenerator.SolsticeSnowGenerator(
            project=self._project, config=self._config, settings=self._settings, parent=self)
        return [snow_generator]
