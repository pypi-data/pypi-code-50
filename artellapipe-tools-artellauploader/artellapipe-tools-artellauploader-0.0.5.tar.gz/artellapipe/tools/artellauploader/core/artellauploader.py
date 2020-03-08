#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool to easily upload files into Artella server
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import artellapipe

# Defines ID of the tool
TOOL_ID = 'artellapipe-tools-artellauploader'

# We skip the reloading of this module when launching the tool
no_reload = True


class ArtellUploaderTool(artellapipe.Tool, object):
    def __init__(self, *args, **kwargs):
        super(ArtellUploaderTool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = artellapipe.Tool.config_dict(file_name=file_name)
        tool_config = {
            'name': 'Artella Uploader',
            'id': 'artellapipe-tools-artellauploader',
            'logo': 'artellauploader_logo',
            'icon': 'artella_upload',
            'tooltip': 'Tool to easily upload files into Artella server',
            'tags': ['artella', 'manager', 'files', 'uploader'],
            'sentry_id': 'https://5147c41093e242f59ddc24af9f56c06d@sentry.io/1764690',
            'is_checkable': False,
            'is_checked': False,
            'menu_ui': {'label': 'Artella Uploader', 'load_on_startup': False, 'color': '', 'background_color': ''},
            'menu': [
                {'label': 'Artella',
                 'type': 'menu', 'children': [{'id': 'artellapipe-tools-artellauploader', 'type': 'tool'}]}],
            'shelf': [
                {'name': 'Artella',
                 'children': [{'id': 'artellapipe-tools-artellauploader', 'display_label': False, 'type': 'tool'}]}
            ]
        }
        base_tool_config.update(tool_config)

        return base_tool_config


class ArtellaUploaderToolset(artellapipe.Toolset, object):
    ID = TOOL_ID

    def __init__(self, *args, **kwargs):
        super(ArtellaUploaderToolset, self).__init__(*args, **kwargs)

    def contents(self):
        from artellapipe.tools.artellauploader.widgets import artellauploadertool

        artella_uploader = artellauploadertool.ArtellaUploader(
            project=self._project, config=self._config, settings=self._settings, parent=self)
        return [artella_uploader]
