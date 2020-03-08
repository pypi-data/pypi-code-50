#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains implementation for Shader Exporter
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import os
import traceback
import logging
from functools import partial

from Qt.QtCore import *
from Qt.QtWidgets import *

import tpDcc as tp
from tpDcc.libs.qt.core import base

import artellapipe
from artellapipe.core import defines
from artellapipe.utils import exceptions, shader as shader_utils

if tp.is_maya():
    from tpDcc.dccs.maya.core import shader as maya_shader

LOGGER = logging.getLogger()


class ArtellaShaderExportSplash(QSplashScreen, object):
    def __init__(self, *args, **kwargs):
        super(ArtellaShaderExportSplash, self).__init__(*args, **kwargs)

        self.mousePressEvent = self.MousePressEvent
        self._canceled = False

    def MousePressEvent(self, event):
        pass


class ArtellaShaderExporterWidget(base.BaseWidget, object):
    def __init__(self, shader_name, layout='horizontal', asset=None, parent=None):
        self._layout = layout
        self._name = shader_name
        self._asset = asset
        super(ArtellaShaderExporterWidget, self).__init__(parent=parent)

    def get_main_layout(self):
        if self._layout == 'horizontal':
            main_layout = QHBoxLayout()
        else:
            main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(5)
        main_layout.setAlignment(Qt.AlignLeft)

        return main_layout

    def ui(self):
        super(ArtellaShaderExporterWidget, self).ui()

        if tp.Dcc.object_exists(self._name):
            self._shader_swatch = maya_shader.get_shader_swatch(self._name)
            self.main_layout.addWidget(self._shader_swatch)

            if self._layout == 'horizontal':
                v_div_w = QWidget()
                v_div_l = QVBoxLayout()
                v_div_l.setAlignment(Qt.AlignLeft)
                v_div_l.setContentsMargins(0, 0, 0, 0)
                v_div_l.setSpacing(0)
                v_div_w.setLayout(v_div_l)
                v_div = QFrame()
                v_div.setMinimumHeight(30)
                v_div.setFrameShape(QFrame.VLine)
                v_div.setFrameShadow(QFrame.Sunken)
                v_div_l.addWidget(v_div)
                self.main_layout.addWidget(v_div_w)

        shader_lbl = QLabel(self._name)
        self.main_layout.addWidget(shader_lbl)
        if self._layout == 'vertical':
            self.main_layout.setAlignment(Qt.AlignCenter)
            shader_lbl.setAlignment(Qt.AlignCenter)
            shader_lbl.setStyleSheet('QLabel {background-color: rgba(50, 50, 50, 200); border-radius:5px;}')
            shader_lbl.setStatusTip(self.name)
            shader_lbl.setToolTip(self.name)

        do_export_layout = QVBoxLayout()
        do_export_layout.setAlignment(Qt.AlignCenter)
        self.do_export = QCheckBox()
        self.do_export.setChecked(True)
        do_export_layout.addWidget(self.do_export)
        self.main_layout.addLayout(do_export_layout)

    def export(self, new_version=False, comment=None):

        exported_shader = None
        if self.do_export.isChecked():
            if self._asset:
                exported_shader = artellapipe.ShadersMgr().export_asset_shaders(
                    asset=self._asset, shader_swatch=self._shader_swatch,
                    new_version=new_version, comment=comment, shaders_to_export=[self._name])
            else:
                exported_shader = artellapipe.ShadersMgr().export_shader(
                    shader_name=self._name, shader_swatch=self._shader_swatch,
                    new_version=new_version, comment=comment)

        return exported_shader

    @property
    def name(self):
        return self._name


class ShadersDialog(tp.Dialog, object):
    def __init__(self, project, shaders, parent=None):
        self._project = project
        self._shaders = shaders
        super(ShadersDialog, self).__init__(parent=parent)

    def ui(self):
        super(ShadersDialog, self).ui()

        self._shaders_exporter = ShaderExporter(project=self._project, shaders=self._shaders)
        self.main_layout.addWidget(self._shaders_exporter)


class ShaderExporter(base.BaseWidget, object):

    exportFinished = Signal()
    exportCanceled = Signal()

    def __init__(self, project, shaders=None, asset=None, parent=None):
        self._shaders = shaders or list()
        self._asset = asset
        self._project = project

        super(ShaderExporter, self).__init__(parent=parent)

        self.refresh()

    def ui(self):
        super(ShaderExporter, self).ui()

        shaders_layout = QVBoxLayout()
        shaders_layout.setAlignment(Qt.AlignBottom)
        self.main_layout.addLayout(shaders_layout)
        self._shaders_list = QListWidget()
        self._shaders_list.setFlow(QListWidget.LeftToRight)
        self._shaders_list.setSelectionMode(QListWidget.NoSelection)
        self._shaders_list.setStyleSheet('background-color: rgba(50, 50, 50, 150);')
        shaders_layout.addWidget(self._shaders_list)

        refresh_icon = tp.ResourcesMgr().icon('refresh')
        export_icon = tp.ResourcesMgr().icon('export')
        publish_icon = tp.ResourcesMgr().icon('box')
        cancel_icon = tp.ResourcesMgr().icon('delete')

        self.export_shader_mapper_cbx = QCheckBox('Export Shaders Mapping File?')
        self.export_shader_mapper_cbx.setChecked(True)
        self.upload_new_version_cbx = QCheckBox('Upload New Version?')
        self._comment_lbl = QLabel('Comment:')
        self._comment_line = QLineEdit()
        self.refresh_btn = QPushButton()
        self.refresh_btn.setIcon(refresh_icon)
        self.refresh_btn.setMaximumWidth(40)
        self.export_btn = QPushButton('Export')
        self.export_btn.setIcon(export_icon)
        self.publish_btn = QPushButton('Export and Publish')
        self.publish_btn.setEnabled(False)
        self.publish_btn.setIcon(publish_icon)
        self.cancel_btn = QPushButton('Cancel')
        self.cancel_btn.setMaximumWidth(80)
        self.cancel_btn.setIcon(cancel_icon)
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.refresh_btn)
        buttons_layout.addWidget(self.export_btn)
        buttons_layout.addWidget(self.publish_btn)
        buttons_layout.addWidget(self.cancel_btn)
        buttons_layout.setAlignment(Qt.AlignBottom)
        checkboxes_layout = QHBoxLayout()
        checkboxes_layout.addWidget(self.export_shader_mapper_cbx)
        checkboxes_layout.addWidget(self.upload_new_version_cbx)
        checkboxes_layout.addItem(QSpacerItem(10, 0, QSizePolicy.Fixed, QSizePolicy.Preferred))
        checkboxes_layout.addWidget(self._comment_lbl)
        checkboxes_layout.addWidget(self._comment_line)
        self.main_layout.addLayout(checkboxes_layout)
        self.main_layout.addLayout(buttons_layout)

        progress_layout = QHBoxLayout()
        self.main_layout.addLayout(progress_layout)

        self._progress_text = QLabel('Exporting and uploading shaders to Artella ... Please wait!')
        self._progress_text.setAlignment(Qt.AlignCenter)
        self._progress_text.setStyleSheet("QLabel { background-color : rgba(0, 0, 0, 180); color : white; }")
        self._progress_text.setVisible(False)
        font = self._progress_text.font()
        font.setPointSize(10)
        self._progress_text.setFont(font)

        progress_layout.addWidget(self._progress_text)

    def setup_signals(self):
        self.export_btn.clicked.connect(partial(self._on_export_shaders))
        self.publish_btn.clicked.connect(partial(self._on_publish_shaders))
        self.cancel_btn.clicked.connect(self.exportCanceled.emit)
        self.refresh_btn.clicked.connect(self.refresh)

    def set_asset(self, asset):
        self._asset = asset
        asset_shaders = artellapipe.ShadersMgr().get_asset_shaders_to_export(self._asset) or list()
        self._shaders = asset_shaders
        self.refresh()

    def set_shaders(self, shaders):
        self._shaders = shaders
        self.refresh()

    def refresh(self):

        self._open_asset_shaders_file()

        self._shaders_list.clear()

        for shader in self._shaders:
            if shader in shader_utils.IGNORE_SHADERS:
                continue
            shader_item = QListWidgetItem()
            shader_widget = ArtellaShaderExporterWidget(shader_name=shader, layout='vertical', asset=self._asset)
            shader_item.setSizeHint(QSize(120, 120))
            shader_widget.setMinimumWidth(100)
            shader_widget.setMinimumHeight(100)
            self._shaders_list.addItem(shader_item)
            self._shaders_list.setItemWidget(shader_item, shader_widget)

    def export_shaders(self, new_version=False, comment=None):

        exported_shaders = list()

        if self._shaders_list.count() <= 0:
            LOGGER.error('No Shaders To Export. Aborting ....')
            return exported_shaders

        try:
            for i in range(self._shaders_list.count()):
                shader_item = self._shaders_list.item(i)
                shader = self._shaders_list.itemWidget(shader_item)
                self._progress_text.setText('Exporting shader: {0} ... Please wait!'.format(shader.name))
                self.repaint()
                exported_shader = shader.export(new_version=new_version, comment=comment)
                if exported_shader is not None:
                    if type(exported_shader) == list:
                        exported_shaders.extend(exported_shader)
                    else:
                        exported_shaders.append(exported_shader)
                # else:
                #     LOGGER.error('Error while exporting shader: {}'.format(shader.name))
        except Exception as e:
            exceptions.capture_sentry_exception(e)
            LOGGER.error(str(e))
            LOGGER.error(traceback.format_exc())
            return exported_shaders

        if self._asset and self.export_shader_mapper_cbx.isChecked():
            self._progress_text.setText('Exporting Shaders Mapping File ... Please wait!')
            self.repaint()
            artellapipe.ShadersMgr().export_asset_shaders_mapping(
                self._asset, comment=comment, new_version=new_version)

        return exported_shaders

    def publish_shaders(self, comment=None):
        publish_path = self._asset.get_shaders_path(status=defines.ArtellaFileStatus.PUBLISHED, next_version=True)
        if not publish_path:
            LOGGER.warning(
                'Impossible to publish shaders. Was not possible to found publish path. Publish shaders manually.')
            return

        if os.path.isdir(publish_path):
            LOGGER.warning('New Publish Path already exits: "{}". Publish shader manually.'.format(publish_path))
            return

        if not comment:
            comment = 'Shaders Exporter >>> Shaders Published: {}'.format(publish_path)

        # artellalib.publish_asset(publish_path, comment=comment)

        return True

    def _open_asset_shaders_file(self):
        if not self._asset:
            return

        shading_file_type = artellapipe.AssetsMgr().get_shading_file_type()
        file_path = self._asset.get_file(
            file_type=shading_file_type, status=defines.ArtellaFileStatus.WORKING, fix_path=True)
        valid_open = self._asset.open_file(file_type=shading_file_type, status=defines.ArtellaFileStatus.WORKING)
        if not valid_open:
            LOGGER.warning('Impossible to open Asset Shading File: {}'.format(file_path))
            return None

    def _set_widgets_visibility(self, flag):
        self.cancel_btn.setVisible(flag)
        self.export_btn.setVisible(flag)
        self.publish_btn.setVisible(flag)
        self.refresh_btn.setVisible(flag)
        self.export_shader_mapper_cbx.setVisible(flag)
        self.upload_new_version_cbx.setVisible(flag)
        self._comment_lbl.setVisible(flag)
        self._comment_line.setVisible(flag)
        self._progress_text.setVisible(not flag)

    def _on_export_shaders(self):

        self._set_widgets_visibility(False)
        self.repaint()
        try:
            self.export_shaders(
                new_version=self.upload_new_version_cbx.isChecked(),
                comment=self._comment_line.text())
            self.exportFinished.emit()
            LOGGER.info('Shaders exported successfully!')
        finally:
            self._set_widgets_visibility(True)

    def _on_publish_shaders(self):

        raise NotImplementedError('Publish Shaders functionality not implemented!')

        # res = qtutils.show_question(
        #     None, 'Publishing Shaders',
        #     'Are you sure you want to publish asset shaders?\n\nShaders and Mapping files will be re-exported.')
        # if res == QMessageBox.No:
        #     return
        #
        # self._set_widgets_visibility(False)
        # self.repaint()
        # try:
        #     self.export_shaders(
        #         new_version=True,
        #         comment=self._comment_line.text())
        #     LOGGER.info('Shaders exported successfully!')
        #     artellapipe.ShadersMgr().export_asset_shaders_mapping(
        #         self._asset, comment=self._comment_line.text(), new_version=True)
        #     LOGGER.info('Shaders Mapping exported successfully!')
        #     self.publish_shaders(comment=self._comment_line.text())
        #     LOGGER.info('New shaders version published successfully!')
        # finally:
        #     self._set_widgets_visibility(True)
