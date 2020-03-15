#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains sequences publisher implementation for Artella
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import artellapipe

# Defines ID of the tool
TOOL_ID = 'artellapipe-tools-sequencespublisher'

# We skip the reloading of this module when launching the tool
no_reload = True


class SequencesPublisherTool(artellapipe.Tool, object):
    def __init__(self, *args, **kwargs):
        super(SequencesPublisherTool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = artellapipe.Tool.config_dict(file_name=file_name)
        tool_config = {
            'name': 'Sequences Publisher',
            'id': 'artellapipe-tools-sequencespublisher',
            'logo': 'sequencespublisher_logo',
            'icon': 'sequencespublisher',
            'tooltip': 'Tool that allow layout department to generate shot files from a sequence file (master layout)',
            'tags': ['shots', 'sequencers', 'publisher', 'pyblish'],
            'sentry_id': 'https://40f85d79f6184fbabedecd5b1a0ba14b@sentry.io/1886517',
            'is_checkable': False,
            'is_checked': False,
            'menu_ui': {
                'label': 'Sequences Publisher', 'load_on_startup': False, 'color': '', 'background_color': ''},
            'menu': [
                {'label': 'Layout',
                 'type': 'menu', 'children': [{'id': 'artellapipe-tools-sequencespublisher', 'type': 'tool'}]}],
            'shelf': [
                {'name': 'Layout',
                 'children': [{'id': 'artellapipe-tools-sequencespublisher', 'display_label': False, 'type': 'tool'}]}
            ]
        }
        base_tool_config.update(tool_config)

        return base_tool_config


class SequencesPublisherToolset(artellapipe.Toolset, object):
    ID = TOOL_ID

    def __init__(self, *args, **kwargs):
        super(SequencesPublisherToolset, self).__init__(*args, **kwargs)

    def contents(self):

        from artellapipe.tools.sequencespublisher.widgets import sequencespublisher

        sequences_publisher = sequencespublisher.SequencesPublisher(
            project=self._project, config=self._config, settings=self._settings, parent=self)
        return [sequences_publisher]
