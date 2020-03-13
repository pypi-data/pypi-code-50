#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains implementation for Assets Shaders Viewer widget
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import os
import logging

from Qt.QtCore import *
from Qt.QtWidgets import *

import tpDcc
from tpDcc.libs.python import osplatform
from tpDcc.libs.qt.core import base, qtutils
from tpDcc.libs.qt.widgets import stack, breadcrumb

import artellapipe
from artellapipe.widgets import assetswidget
from artellapipe.tools.shadersmanager.widgets import shaderexporter

LOGGER = logging.getLogger()


class ArtellaAssetShadersViewer(base.BaseWidget, object):
    def __init__(self, project, parent=None):
        self._project = project
        super(ArtellaAssetShadersViewer, self).__init__(parent=parent)

        self._init()

    def ui(self):
        super(ArtellaAssetShadersViewer, self).ui()

        shader_splitter = QSplitter(Qt.Horizontal)
        shader_splitter.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.main_layout.addWidget(shader_splitter)

        self._assets_viewer = assetswidget.AssetsWidget(
            project=self._project,
            column_count=2,
            parent=self
        )
        self._assets_viewer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self._stack = stack.SlidingStackedWidget()

        no_items_widget = QFrame()
        no_items_widget.setFrameShape(QFrame.StyledPanel)
        no_items_widget.setFrameShadow(QFrame.Sunken)
        no_items_layout = QVBoxLayout()
        no_items_layout.setContentsMargins(0, 0, 0, 0)
        no_items_layout.setSpacing(0)
        no_items_widget.setLayout(no_items_layout)
        no_items_lbl = QLabel()
        no_items_pixmap = tpDcc.ResourcesMgr().pixmap('no_asset_selected')
        no_items_lbl.setPixmap(no_items_pixmap)
        no_items_lbl.setAlignment(Qt.AlignCenter)
        no_items_layout.addItem(QSpacerItem(0, 10, QSizePolicy.Preferred, QSizePolicy.Expanding))
        no_items_layout.addWidget(no_items_lbl)
        no_items_layout.addItem(QSpacerItem(0, 10, QSizePolicy.Preferred, QSizePolicy.Expanding))
        self._asset_shaders_layout = QVBoxLayout()
        self._asset_shaders_layout.setContentsMargins(0, 0, 0, 0)
        self._asset_shaders_layout.setSpacing(0)
        self._assets_shaders_widget = QWidget()
        self._assets_shaders_widget.setLayout(self._asset_shaders_layout)
        self._stack.addWidget(no_items_widget)
        self._stack.addWidget(self._assets_shaders_widget)

        shader_splitter.addWidget(self._assets_viewer)
        shader_splitter.addWidget(self._stack)
        shader_splitter.setSizes([1, 2])

    def setup_signals(self):
        self._assets_viewer.assetAdded.connect(self._on_asset_added)

    def get_shaders_info_widget(self, asset_widget):
        """
        Returns shaders info widget attached to given widget
        :param asset_widget: ArtellaAssetWidget
        :return: AssetsShadersWidget
        """

        return AssetsShadersWidget(asset_widget=asset_widget)

    def show_shaders_info(self, asset_widget):
        """
        Shows Assets Shaders Info Widget UI associated to the given asset widget
        :param asset_widget: ArtellaAssetWidget
        """

        shaders_info_widget = self.get_shaders_info_widget(asset_widget=asset_widget)
        if not shaders_info_widget:
            LOGGER.warning(
                'Asset {} has not an AssetShadersInfo widget associated to it. Skipping ...!'.format(
                    asset_widget.get_name()))
            return

        self._set_asset_shaders_info(shaders_info_widget)

    def _init(self):
        """
        Internal function that checks shaders library validity and initializes shaders viewer properly
        :return:
        """

        self._assets_viewer.update_assets()

    def _setup_asset_signals(self, asset_widget):
        """
        Internal function that sets proper signals to given asset widget
        This function can be extended to add new signals to added items
        :param asset_widget: ArtellaAssetWidget
        """

        asset_widget.clicked.connect(self._on_asset_clicked)

    def _set_asset_shaders_info(self, shaders_info):
        """
        Sets the asset shaders info widget currently being showed
        :param shaders_info: AssetsShadersWidget
        """

        if self._assets_shaders_widget == shaders_info:
            return

        qtutils.clear_layout(self._asset_shaders_layout)

        if shaders_info:
            self._assets_shaders_widget = shaders_info
            self._asset_shaders_layout.addWidget(shaders_info)
            self._stack.slide_in_index(1)

    def _on_asset_added(self, asset_widget):
        """
        Internal callback function that is called when a new asset widget is added to the assets viewer
        :param asset_widget: ArtellaAssetWidget
        """

        if not asset_widget:
            return

        self._setup_asset_signals(asset_widget)

    def _on_asset_clicked(self, asset_widget):
        """
        Internal callback function that is called when an asset button is clicked
        :param asset_widget: ArtellaAssetWidget
        """

        if not asset_widget:
            return

        self.show_shaders_info(asset_widget=asset_widget)


class AssetsShadersWidget(base.BaseWidget, object):
    def __init__(self, asset_widget, parent=None):
        self._asset_widget = asset_widget
        super(AssetsShadersWidget, self).__init__(parent=parent)

        self._init()

    def get_main_layout(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(2, 2, 2, 2)
        main_layout.setSpacing(2)
        main_layout.setAlignment(Qt.AlignTop)

        return main_layout

    def ui(self):
        super(AssetsShadersWidget, self).ui()

        self._title_breadcrumb = breadcrumb.BreadcrumbFrame()
        self._asset_icon_frame = QFrame()
        self._asset_icon_frame.setFrameShape(QFrame.StyledPanel)
        self._asset_icon_frame.setFrameShadow(QFrame.Sunken)
        self._asset_icon_frame.setLineWidth(3)
        self._asset_icon_frame.setStyleSheet('background-color: rgba(60, 60, 60, 100); border-radius:5px;')
        asset_icon_layout = QHBoxLayout()
        asset_icon_layout.setContentsMargins(0, 0, 0, 0)
        asset_icon_layout.setSpacing(0)
        self._asset_icon_frame.setLayout(asset_icon_layout)
        self._asset_icon_lbl = QLabel()
        self._asset_icon_lbl.setAlignment(Qt.AlignCenter)
        self._asset_icon_lbl.setPixmap(tpDcc.ResourcesMgr().pixmap('default'))
        self._asset_toolbar_layout = QVBoxLayout()
        self._asset_toolbar_layout.setContentsMargins(2, 2, 2, 2)
        self._asset_toolbar_layout.setSpacing(5)

        asset_icon_layout.addLayout(self._asset_toolbar_layout)
        asset_icon_layout.addWidget(self._asset_icon_lbl)

        self.main_layout.addWidget(self._title_breadcrumb)
        self.main_layout.addWidget(self._asset_icon_frame)

    def _init(self):
        """
        Internal function that initializes asset info widget
        """

        if not self._asset_widget:
            return

        self._title_breadcrumb.set([self._asset_widget.asset.get_name()])
        thumb_icon = self._asset_widget.get_thumbnail_icon()
        thumb_size = artellapipe.AssetsMgr().config.get('thumb_size')
        self._asset_icon_lbl.setPixmap(
            thumb_icon.pixmap(thumb_icon.availableSizes()[-1]).scaled(thumb_size[0], thumb_size[1], Qt.KeepAspectRatio))

        self._asset_toolbar = self._create_asset_toolbar()
        self._shaders_stack = AssetShadersStack(asset_widget=self._asset_widget)
        self._shaders_stack.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self._asset_toolbar_layout.addWidget(self._asset_toolbar)
        self.main_layout.addWidget(self._shaders_stack)

    def _create_asset_toolbar(self):
        """
        Creates toolbar widget for the asset
        """

        toolbar_widget = QWidget()
        toolbar_widget.setMaximumWidth(40)
        toolbar_layout = QVBoxLayout()
        toolbar_layout.setContentsMargins(2, 2, 2, 2)
        toolbar_layout.setSpacing(5)
        toolbar_widget.setLayout(toolbar_layout)

        artella_btn = QToolButton()
        artella_btn.setText('Artella')
        artella_btn.setIcon(tpDcc.ResourcesMgr().icon('artella'))
        artella_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        view_locally_btn = QToolButton()
        view_locally_btn.setText('Folder')
        view_locally_btn.setIcon(tpDcc.ResourcesMgr().icon('folder'))
        view_locally_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        toolbar_layout.addItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Preferred))
        toolbar_layout.addWidget(artella_btn)
        toolbar_layout.addWidget(view_locally_btn)
        toolbar_layout.addItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Preferred))

        artella_btn.clicked.connect(self._on_open_artella)
        view_locally_btn.clicked.connect(self._on_view_locally)

        return toolbar_widget

    def _on_open_artella(self):
        """
        Internal callback function that is called when the user presses asset Artella button
        """

        if not self._asset_widget:
            return

        self._asset_widget.asset.open_in_artella()

    def _on_view_locally(self):
        """
        Internal callback function that is called when the user presses asset View Locally button
        """

        if not self._asset_widget:
            return

        self._asset_widget.asset.view_locally()


class AssetShadersStack(base.BaseWidget, object):
    def __init__(self, asset_widget, parent=None):
        self._asset_widget = asset_widget
        super(AssetShadersStack, self).__init__(parent=parent)

        self.refresh()

    def ui(self):
        super(AssetShadersStack, self).ui()

        export_icon = tpDcc.ResourcesMgr().icon('export')
        open_folder_icon = tpDcc.ResourcesMgr().icon('folder')

        self._export_btn = QPushButton('Shaders Exporter')
        self._export_btn.setIcon(export_icon)
        self._export_btn.setMinimumWidth(80)
        self._open_folder_btn = QPushButton('Open Shaders Folder')
        self._open_folder_btn.setIcon(open_folder_icon)
        self._open_folder_btn.setMaximumWidth(135)

        buttons_layout = QHBoxLayout()
        buttons_layout.setContentsMargins(0, 0, 0, 0)
        buttons_layout.setSpacing(10)
        buttons_layout.addWidget(self._open_folder_btn)
        buttons_layout.addWidget(self._export_btn)

        self._shaders_stack = stack.SlidingStackedWidget()

        project = self._asset_widget.asset.project
        shaders_viewer_widget = QWidget()
        self._shaders_viewer = artellapipe.ShadersViewer(
            project=project, shaders_path=self._asset_widget.asset.get_shaders_path())
        shaders_viewer_widget.setLayout(self._shaders_viewer)
        no_shaders_widget = QFrame()
        no_shaders_widget.setFrameShape(QFrame.StyledPanel)
        no_shaders_widget.setFrameShadow(QFrame.Sunken)
        no_shaders_layout = QVBoxLayout()
        no_shaders_layout.setContentsMargins(0, 0, 0, 0)
        no_shaders_layout.setSpacing(0)
        no_shaders_widget.setLayout(no_shaders_layout)
        no_shaders_lbl = QLabel()
        no_shaders_pixmap = tpDcc.ResourcesMgr().pixmap('no_shaders_available')
        no_shaders_lbl.setPixmap(no_shaders_pixmap)
        no_shaders_lbl.setAlignment(Qt.AlignCenter)
        no_shaders_layout.addItem(QSpacerItem(0, 10, QSizePolicy.Preferred, QSizePolicy.Expanding))
        no_shaders_layout.addWidget(no_shaders_lbl)
        no_shaders_layout.addItem(QSpacerItem(0, 10, QSizePolicy.Preferred, QSizePolicy.Expanding))
        self._shaders_exporter = shaderexporter.ShaderExporter(project=project)

        self._shaders_stack.addWidget(no_shaders_widget)
        self._shaders_stack.addWidget(shaders_viewer_widget)
        self._shaders_stack.addWidget(self._shaders_exporter)

        self.main_layout.addLayout(buttons_layout)
        self.main_layout.addWidget(self._shaders_stack)

    def setup_signals(self):
        self._export_btn.clicked.connect(self._on_export_shaders)
        self._open_folder_btn.clicked.connect(self._on_open_shaders_folder)
        self._shaders_exporter.exportCanceled.connect(self._on_shaders_export_canceled)

    def refresh(self):
        total_shaders = self._shaders_viewer.count()
        if total_shaders > 0:
            self._shaders_stack.slide_in_index(1)
        else:
            self._shaders_stack.slide_in_index(0)

    def _on_open_shaders_folder(self):
        if not self._asset_widget:
            return

        shaders_path = self._asset_widget.asset.get_shaders_path()
        if not os.path.isdir(shaders_path):
            return

        osplatform.open_folder(shaders_path)

    def _on_export_shaders(self):
        if not self._asset_widget:
            return

        self._shaders_exporter.set_asset(self._asset_widget.asset)

        self._shaders_stack.slide_in_index(2)

    def _on_shaders_export_canceled(self):
        self.refresh()
