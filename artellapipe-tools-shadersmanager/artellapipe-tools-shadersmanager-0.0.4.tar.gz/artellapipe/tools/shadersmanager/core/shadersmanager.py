# -*- coding: utf-8 -*-

"""
Tool to export/import shader files
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from tpDcc.libs.qt.core import base
from tpDcc.libs.qt.widgets import tabs

import artellapipe
from artellapipe.tools.shadersmanager.widgets import shaderslibrary, assetsviewer

# Defines ID of the tool
TOOL_ID = 'artellapipe-tools-shadersmanager'

# We skip the reloading of this module when launching the tool
no_reload = True


class ShadersManagerTool(artellapipe.Tool, object):
    def __init__(self, *args, **kwargs):
        super(ShadersManagerTool, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls, file_name=None):
        base_tool_config = artellapipe.Tool.config_dict(file_name=file_name)
        tool_config = {
            'name': 'Shaders Manager',
            'id': 'artellapipe-tools-shadersmanager',
            'logo': 'shadersmanager_logo',
            'icon': 'shading',
            'tooltip': 'Tool to manage all shaders for an Artella project',
            'tags': ['artella', 'manager', 'shaders'],
            'sentry_id': 'https://45368b556716471f8c8ee52dde7ea088@sentry.io/1764720',
            'is_checkable': False,
            'is_checked': False,
            'import_order': ['widgets', 'core'],
            'menu_ui': {'label': 'Shaders Manager', 'load_on_startup': False, 'color': '', 'background_color': ''},
            'menu': [
                {'label': 'Shading',
                 'type': 'menu', 'children': [{'id': 'artellapipe-tools-shadersmanager', 'type': 'tool'}]}],
            'shelf': [
                {'name': 'Shading',
                 'children': [{'id': 'artellapipe-tools-shadersmanager', 'display_label': False, 'type': 'tool'}]}
            ]
        }
        base_tool_config.update(tool_config)

        return base_tool_config


class ShadersManagerToolset(artellapipe.Toolset, object):

    ID = TOOL_ID

    def __init__(self, *args, **kwargs):
        super(ShadersManagerToolset, self).__init__(*args, **kwargs)

    def contents(self):
        shaders_widget = ShadersWidget(project=self._project, config=self._config, settings=self._settings, parent=self)

        return [shaders_widget]


class ShadersWidget(artellapipe.ToolWidget, object):
    def __init__(self, project, config, settings, parent=None):
        super(ShadersWidget, self).__init__(project=project, config=config, settings=settings, parent=parent)

    def ui(self):
        super(ShadersWidget, self).ui()

        tab = tabs.TearOffTabWidget()
        self.main_layout.addWidget(tab)
        tab.setTabsClosable(False)

        self._shaders_library = shaderslibrary.ArtellaShadersLibrary(project=self._project)
        self._assets_viewer = assetsviewer.ArtellaAssetShadersViewer(project=self._project)

        tab.addTab(self._assets_viewer, 'Assets')
        tab.addTab(self._shaders_library, 'Library')
