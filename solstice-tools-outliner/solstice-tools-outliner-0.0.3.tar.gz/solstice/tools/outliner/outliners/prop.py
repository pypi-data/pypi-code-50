#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains outliner implementations for Solstice Prop assets
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import logging
from functools import partial

from Qt.QtCore import *
from Qt.QtWidgets import *

import tpDcc

from artellapipe.tools.outliner.widgets import baseoutliner

LOGGER = logging.getLogger()


class SolsticePropsOutliner(baseoutliner.BaseOutliner, object):

    overrideAdded = Signal(object, object)
    overrideRemoved = Signal(object, object)

    def __init__(self, project, parent=None):
        super(SolsticePropsOutliner, self).__init__(project=project, parent=parent)

    def _create_context_menu(self, menu, item):
        replace_icon = tpDcc.ResourcesMgr().icon('replace')
        delete_icon = tpDcc.ResourcesMgr().icon('delete')
        override_add_icon = tpDcc.ResourcesMgr().icon('override_add')
        override_delete_icon = tpDcc.ResourcesMgr().icon('override_delete')
        override_export_icon = tpDcc.ResourcesMgr().icon('save')
        load_shaders_icon = tpDcc.ResourcesMgr().icon('shading_load')
        unload_shaders_icon = tpDcc.ResourcesMgr().icon('shading_unload')
        proxy_icon = tpDcc.ResourcesMgr().icon('low_poly')
        high_icon = tpDcc.ResourcesMgr().icon('high_poly')

        replace_menu = QMenu('Replace by', self)
        replace_menu.setIcon(replace_icon)
        show_replace_menu = self._create_replace_actions(replace_menu, item)
        if show_replace_menu:
            menu.addMenu(replace_menu)

        remove_action = QAction(delete_icon, 'Delete', menu)
        menu.addAction(remove_action)
        menu.addSeparator()

        add_override_menu = QMenu('Add Override', menu)
        add_override_menu.setIcon(override_add_icon)
        valid_override = self._create_add_override_menu(add_override_menu, item)
        if valid_override:
            menu.addMenu(add_override_menu)

        remove_override_menu = QMenu('Remove Override', menu)
        remove_override_menu.setIcon(override_delete_icon)
        has_overrides = self._create_remove_override_menu(remove_override_menu, item)
        if has_overrides:
            menu.addMenu(remove_override_menu)

        save_override_menu = QMenu('Save Overrides', menu)
        save_override_menu.setIcon(override_export_icon)
        export_overrides = self._create_save_override_menu(save_override_menu, item)
        if export_overrides:
            menu.addMenu(save_override_menu)

        if valid_override or has_overrides or export_overrides:
            menu.addSeparator()

        switch_to_proxy = QAction(proxy_icon, 'Switch to Low Res', menu)
        switch_to_high = QAction(high_icon, 'Switch to High Res', menu)
        menu.addAction(switch_to_proxy)
        menu.addAction(switch_to_high)
        menu.addSeparator()

        load_shaders_action = QAction(load_shaders_icon, 'Load Shaders', menu)
        unload_shaders_action = QAction(unload_shaders_icon, 'Unload Shaders', menu)
        menu.addAction(load_shaders_action)
        menu.addAction(unload_shaders_action)

        remove_action.triggered.connect(partial(self._on_remove, item))
        switch_to_proxy.triggered.connect(partial(self._on_switch_to_proxy, item))
        switch_to_high.triggered.connect(partial(self._on_switch_to_high, item))
        load_shaders_action.triggered.connect(partial(self._on_load_shaders, item))
        unload_shaders_action.triggered.connect(partial(self._on_unload_shaders, item))

    def _create_replace_actions(self, replace_menu, item):
        """
        Internal function that creates replacement options for current file
        :param replace_menu: QMenu
        :return: bool
        """

        rig_icon = tpDcc.ResourcesMgr().icon('rig')
        alembic_icon = tpDcc.ResourcesMgr().icon('alembic')
        standin_icon = tpDcc.ResourcesMgr().icon('standin')

        rig_action = QAction(rig_icon, 'Rig', replace_menu)
        gpu_cache_action = QAction(alembic_icon, 'Gpu Cache', replace_menu)
        standin_action = QAction(standin_icon, 'Standin', replace_menu)
        replace_menu.addAction(rig_action)
        replace_menu.addAction(gpu_cache_action)
        replace_menu.addAction(standin_action)

        rig_replace_menu = QMenu()
        rig_action.setMenu(rig_replace_menu)
        rig_root_control_action = QAction('Root Control', replace_menu)
        rig_main_control_action = QAction('Main Control', replace_menu)
        rig_replace_menu.addAction(rig_root_control_action)
        rig_replace_menu.addAction(rig_main_control_action)

        gpu_cache_replace_menu = QMenu()
        gpu_cache_action.setMenu(gpu_cache_replace_menu)
        gpu_cache_root_control_action = QAction('Root Control', replace_menu)
        gpu_cache_main_control_action = QAction('Main Control', replace_menu)
        gpu_cache_replace_menu.addAction(gpu_cache_root_control_action)
        gpu_cache_replace_menu.addAction(gpu_cache_main_control_action)

        standin_replace_menu = QMenu()
        standin_action.setMenu(standin_replace_menu)
        standin_root_control_action = QAction('Root Control', replace_menu)
        standin_main_control_action = QAction('Main Control', replace_menu)
        standin_replace_menu.addAction(standin_root_control_action)
        standin_replace_menu.addAction(standin_main_control_action)

        if item.asset_node.is_rig():
            rig_action.setEnabled(False)
        elif item.asset_node.is_gpu_cache():
            gpu_cache_action.setEnabled(False)
        elif item.asset_node.is_standin():
            standin_action.setEnabled(False)

        rig_root_control_action.triggered.connect(partial(self._on_replace_rig, item, 'root_ctrl'))
        rig_main_control_action.triggered.connect(partial(self._on_replace_rig, item, 'main_ctrl'))
        gpu_cache_root_control_action.triggered.connect(partial(self._on_replace_gpu_cache, item, 'root_ctrl'))
        gpu_cache_main_control_action.triggered.connect(partial(self._on_replace_gpu_cache, item, 'main_ctrl'))
        standin_root_control_action.triggered.connect(partial(self._on_replace_standin, item, 'root_ctrl'))
        gpu_cache_main_control_action.triggered.connect(partial(self._on_replace_standin, item, 'main_ctrl'))

        return replace_menu

    def _on_switch_to_proxy(self, item):
        """
        Internal callback function that is called when Switch to Low Res action is triggered
        :param item:
        """

        item.asset_node.switch_to_proxy()

    def _on_switch_to_high(self, item):
        """
        Internal callback function that is called when Switch to High Res action is triggered
        :param item:
        """

        item.asset_node.switch_to_hires()

    def _on_load_shaders(self, item):
        """
        Internal callback function that is called when Load Shaders context action is triggered
        """

        item.asset_node.load_shaders()

    def _on_unload_shaders(self, item):
        """
        Internal callback function that is called when Unload Shaders context action is triggered
        """

        item.asset_node.unload_shaders()

    def _on_replace_rig(self, item, rig_control=None):
        """
        Internal callback function that is called when an asset is replaced by a rig
        :param item: OutlinerAssetItem
        :param rig_control: str
        """

        valid_replace = item.asset_node.replace_by_rig(rig_control=rig_control)
        if not valid_replace:
            return False

        self.refresh()

        return True

    def _on_replace_gpu_cache(self, item, rig_control=None):
        """
        Internal callback function that is called when an asset is replaced by a rig
        :param item: OutlinerAssetItem
        :param rig_control: str
        """

        valid_replace = item.asset_node.replace_by_gpu_cache(rig_control=rig_control)
        if not valid_replace:
            return False

        self.refresh()

        return True

    def _on_replace_standin(self, item, rig_control=None):
        """
        Internal callback function that is called when an asset is replaced by a rig
        :param item: OutlinerAssetItem
        :param rig_control: str
        """

        valid_replace = item.asset_node.replace_by_standin(rig_control=rig_control)
        if not valid_replace:
            return False

        self.refresh()

        return True
