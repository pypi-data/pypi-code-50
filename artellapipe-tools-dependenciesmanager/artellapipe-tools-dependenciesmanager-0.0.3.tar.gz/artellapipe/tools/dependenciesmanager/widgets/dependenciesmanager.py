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

import os
import traceback
import logging.config

from Qt.QtWidgets import *
from Qt.QtCore import *
from Qt.QtGui import *

import tpDcc as tp

from tpDcc.libs.qt.core import qtutils
from tpDcc.libs.qt.widgets import splitters

import artellapipe
from artellapipe.libs import artella
from artellapipe.libs.artella.core import artellalib

LOGGER = logging.getLogger()


class DependenciesManager(artellapipe.ToolWidget, object):

    def __init__(self, project, config, settings, parent, file_path=None):
        self._init_file_path = file_path
        super(DependenciesManager, self).__init__(project=project, config=config, settings=settings, parent=parent)

        self._init()

    def get_main_layout(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(2, 2, 2, 2)
        main_layout.setSpacing(2)
        main_layout.setAlignment(Qt.AlignTop)

        return main_layout

    def ui(self):
        super(DependenciesManager, self).ui()

        self._path_widget = QWidget()
        path_layout = QVBoxLayout()
        path_layout.setContentsMargins(0, 0, 0, 0)
        path_layout.setSpacing(0)
        path_base_layout = QHBoxLayout()
        path_base_layout.setContentsMargins(0, 0, 0, 0)
        path_base_layout.setSpacing(0)
        path_layout.addLayout(path_base_layout)
        self._path_widget.setLayout(path_layout)
        path_lbl = QLabel('Path: ')
        path_lbl.setFixedWidth(30)
        self._folder_path = QLineEdit()
        tip = 'Select folder where files to batch are located'
        self._folder_path.setToolTip(tip)
        self._folder_path.setStatusTip(tip)
        self._folder_path.setContextMenuPolicy(Qt.CustomContextMenu)
        browse_icon = tp.ResourcesMgr().icon('open')
        self._browse_btn = QPushButton()
        self._browse_btn.setFlat(True)
        self._browse_btn.setIcon(browse_icon)
        self._browse_btn.setFixedWidth(30)
        self._browse_btn.setToolTip('Browse Root Folder')
        self._browse_btn.setStatusTip('Browse Root Folder')
        refresh_icon = tp.ResourcesMgr().icon('refresh')
        self._refresh_btn = QPushButton()
        self._refresh_btn.setFlat(True)
        self._refresh_btn.setIcon(refresh_icon)
        path_base_layout.addWidget(path_lbl)
        path_base_layout.addWidget(self._folder_path)
        path_base_layout.addWidget(self._browse_btn)
        path_base_layout.addWidget(splitters.get_horizontal_separator_widget())
        path_base_layout.addWidget(self._refresh_btn)

        self._all_cbx = QCheckBox()
        self._all_cbx.setChecked(True)
        cbx_lyt = QHBoxLayout()
        cbx_lyt.setContentsMargins(0, 0, 0, 0)
        cbx_lyt.setSpacing(0)
        cbx_lyt.addWidget(self._all_cbx)
        cbx_lyt.addItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Preferred))
        self._total_items_lbl = QLabel('')
        cbx_lyt.addItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Preferred))
        cbx_lyt.addWidget(self._total_items_lbl)

        self._files_list = QTreeWidget()
        self._files_list.setColumnCount(3)
        self._files_list.setAlternatingRowColors(True)
        self._files_list.setHeaderLabels(['Path', 'Current Version', 'Latest Version'])
        self._files_list.resizeColumnToContents(0)
        self._files_list.setColumnWidth(1, 120)

        self._progress = self._project.get_progress_bar()
        self._progress.setVisible(False)
        self._progress.setTextVisible(False)
        self._progress_lbl = QLabel('')
        self._progress_lbl.setAlignment(Qt.AlignCenter)

        buttons_layout = QHBoxLayout()
        buttons_layout.setContentsMargins(2, 2, 2, 2)
        buttons_layout.setSpacing(2)

        sync_icon = tp.ResourcesMgr().icon('sync')
        self._sync_btn = QPushButton()
        self._sync_btn.setIcon(sync_icon)
        buttons_layout.addWidget(self._sync_btn)

        self.main_layout.addWidget(self._path_widget)
        self.main_layout.addLayout(splitters.SplitterLayout())
        self.main_layout.addLayout(cbx_lyt)
        self.main_layout.addWidget(self._files_list)
        self.main_layout.addWidget(self._progress)
        self.main_layout.addWidget(self._progress_lbl)
        self.main_layout.addLayout(buttons_layout)

        self._files_list.model().dataChanged.connect(self._on_data_changed)
        self._browse_btn.clicked.connect(self._on_browse)
        self._refresh_btn.clicked.connect(self._on_refresh)
        self._sync_btn.clicked.connect(self._on_sync)
        self._all_cbx.toggled.connect(self._on_toggle_all)

    def _on_refresh(self):
        """
        Internal function that initializes Dependencies Manager UI
        """

        current_path = self._folder_path.text()
        if not current_path or not os.path.isfile(current_path):
            current_path = tp.Dcc.scene_name()
            if not current_path or not os.path.isfile(current_path):
                return False

        if current_path and os.path.isfile(current_path):
            self._on_browse(current_path)

    def _init(self):
        """
        Internal function that is called after launching the tool
        """

        if self._init_file_path and os.path.isfile(self._init_file_path):
            self._folder_path.setText(self._init_file_path)
            self._update_items()

    def _update_items(self):
        """
        Function that refresh all the items
        """

        try:
            self._progress_lbl.setText('Getting dependencies from file... Please wait!')
            self.repaint()
            self._refresh_files()
            self._progress_lbl.setText('Getting dependencies versions ... Please wait!')
            self.repaint()
            self._refresh_versions()
        except Exception as e:
            LOGGER.error(str(e))
            LOGGER.error(traceback.format_exc())
        finally:
            self._progress.setValue(0)
            self._progress_lbl.setText('')
            self._progress.setVisible(False)

    def _refresh_files(self):
        root_path = self._folder_path.text()
        if not root_path:
            return

        self._files_list.clear()

        deps, invalid_deps = artellapipe.DepsMgr().get_dependencies(root_path)

        project_path = self._project.get_path()

        invalid_deps_found = False
        invalid_deps_fixed = False
        if invalid_deps:
            invalid_deps_found = True
            result = qtutils.show_question(
                None, 'Invalid dependencies found',
                'Invalid dependencies paths found in current file. If you continue, dependencies manager will try to '
                'fix them. Are you sure you want to continue?')
            if result == QMessageBox.No:
                return

            artellapipe.DepsMgr().fix_file_paths(root_path)
            deps, invalid_deps = artellapipe.DepsMgr().get_dependencies(root_path)
            if invalid_deps:
                artellapipe.FilesMgr().sync_files(invalid_deps)
                deps, invalid_deps = artellapipe.DepsMgr().get_dependencies(root_path)
                if invalid_deps:
                    qtutils.show_warning(
                        None, 'Invalid dependencies found',
                        'Invalid dependencies paths found in current file.\n\n' + '\n'.join(
                            invalid_deps) + 'Please fix paths manually!')
                    return
                else:
                    invalid_deps_fixed = True
            else:
                invalid_deps_fixed = True

        if invalid_deps_found and invalid_deps_fixed:
            result = qtutils.show_question(
                None, 'File paths updated in file', 'File Paths fixed in the following file: "{}". '
                'Do you want to upload new version of the file to Artella server?'.format(root_path))
            if result == QMessageBox.Yes:
                artellapipe.FilesMgr().upload_working_version(
                    root_path, skip_saving=True, notify=False, comment='DependenciesManager: Fixed paths')

        if deps:
            for file_path, files in deps.items():
                try:
                    rel_path = os.path.relpath(file_path, project_path)
                except Exception:
                    rel_path = file_path
                file_path_item = QTreeWidgetItem()
                file_path_item.setText(0, rel_path)
                file_path_item.path = file_path

                for f in files:
                    try:
                        rel_path = os.path.relpath(f, project_path)
                    except Exception:
                        rel_path = f
                    f_item = QTreeWidgetItem()
                    f_item.setText(0, rel_path)
                    f_item.path = f
                    f_item.latest_path = None
                    f_item.setFlags(f_item.flags() | Qt.ItemIsUserCheckable)
                    f_item.setTextAlignment(1, Qt.AlignCenter)
                    f_item.setTextAlignment(2, Qt.AlignCenter)
                    if self._all_cbx.isChecked():
                        f_item.setCheckState(0, Qt.Checked)
                    else:
                        f_item.setCheckState(0, Qt.Unchecked)
                    file_path_item.addChild(f_item)

                if file_path_item.childCount() > 0:
                    self._files_list.addTopLevelItem(file_path_item)

        self._files_list.expandAll()
        self._files_list.resizeColumnToContents(0)
        self._files_list.resizeColumnToContents(1)
        self._files_list.resizeColumnToContents(2)

    def _refresh_versions(self):
        """
        Internal function that updates working version of selected items
        :return:
        """

        working_folder = artella.config.get('server', 'working_folder')

        try:
            all_items = list(self._all_items())
            self._progress.setVisible(True)
            self._progress.setMinimum(0)
            self._progress.setMaximum(len(all_items) - 1)
            self._progress_lbl.setText('Checking file versions ... Please wait!')
            for i, item in enumerate(all_items):
                self._progress.setValue(i)
                self._progress_lbl.setText('Checking version for: {}'.format(item.text(0)))
                if working_folder in item.path:
                    path_name = os.path.basename(item.path)
                    current_versions = artellalib.get_current_version(item.path)
                    if not current_versions.get(path_name, None):
                        artellapipe.FilesMgr().sync_files([item.path])
                        current_versions = artellalib.get_current_version(item.path)
                    latest_versions = artellalib.get_latest_version(item.path)
                    current_version = current_versions.get(path_name, None)
                    latest_version = latest_versions.get(path_name, None)
                else:
                    root_dir = os.path.dirname(item.path)
                    root_dir_name = os.path.basename(root_dir)
                    item_path = os.path.dirname(root_dir)
                    asset_path = os.path.dirname(item_path)
                    latest_versions = artellalib.get_latest_version(asset_path)
                    current_version = artellalib.split_version(item_path)
                    current_version = current_version[1] if current_version else 0
                    latest_version = latest_versions.get(root_dir_name, None)

                if current_version is None or latest_version is None:
                    for i in range(4):
                        item.setBackgroundColor(i, QColor(160, 50, 40, 100))
                        item.setText(1, 'FILE DOES NOT EXISTS IN ARTELLA SERVER')
                    continue
                item.setText(1, str(current_version))
                item.setText(2, str(latest_version))
                if current_version == latest_version:
                    for i in range(4):
                        item.setBackgroundColor(i, QColor(75, 165, 135, 100))
                        item.setCheckState(0, Qt.Unchecked)
                else:
                    latest_path = item.path.replace(str(current_version).zfill(3), str(latest_version).zfill(3))
                    item.latest_path = latest_path
                    for i in range(4):
                        item.setBackgroundColor(i, QColor(170, 130, 30, 100))
        except Exception as e:
            LOGGER.error(str(e))
            LOGGER.error(traceback.format_exc())
        finally:
            self._progress.setValue(0)
            self._progress_lbl.setText('')
            self._progress.setVisible(False)

    def _checked_items(self):
        """
        Internal function that returns all checked items in the list
        :return: generator
        """

        it = QTreeWidgetItemIterator(self._files_list)
        while it.value():
            item = it.value()
            if item.childCount() == 0 and item.checkState(0) == Qt.Checked:
                yield item
            it += 1

    def _all_items(self):
        """
        Internal function that updates the versions of all items
        :return: generator
        """

        it = QTreeWidgetItemIterator(self._files_list)
        while it.value():
            item = it.value()
            if item.childCount() == 0:
                yield item
            it += 1

    def _on_data_changed(self):
        checked_items = self._checked_items()
        total_checked_items = len(list(checked_items))
        self._total_items_lbl.setText('Total Checked Items: {}'.format(total_checked_items))

    def _on_browse(self, export_path=None):
        stored_path = self.settings().get('upload_path')
        if stored_path and os.path.isdir(stored_path):
            start_directory = stored_path
        else:
            start_directory = self._project.get_path()

        if not export_path or not os.path.isfile(export_path):
            export_path = tp.Dcc.select_file_dialog(
                title='Select Root Path',
                start_directory=start_directory
            )
        if not export_path:
            return

        self.settings().set('upload_path', str(export_path))

        self._folder_path.setText(export_path)

        self._update_items()

    def _on_sync(self):
        current_path = self._folder_path.text()
        if not current_path or not os.path.exists(current_path):
            LOGGER.warning('Selected a scene file to update dependencies of first!')
            return

        checked_items = self._checked_items()
        if not checked_items:
            LOGGER.warning('No Dependencies to Update checked!')
            return

        open_file = True
        result = qtutils.show_question(
            None, 'Updating Dependencies',
            'Do you want to open file after files are synced?')
        if result == QMessageBox.No:
            open_file = False

        working_folder = artella.config.get('server', 'working_folder')

        locked = False
        try:
            self._progress.setVisible(True)
            self._progress_lbl.setText('Updating Dependencies ... Please wait!')
            self.repaint()

            updated = False
            temp_file = current_path + '_temp'

            for item in checked_items:
                if not item.latest_path:
                    LOGGER.warning(
                        'Impossible to update dependency "{}". Latest path was not found ...'.format(item.path))
                    continue
                if working_folder in item.path:
                    folder_to_sync = item.latest_path
                else:
                    folder_to_sync = os.path.dirname(os.path.dirname(item.latest_path))

                split_text = os.path.splitext(folder_to_sync)
                if split_text[-1]:
                    artellapipe.FilesMgr().sync_files([folder_to_sync])
                else:
                    artellapipe.FilesMgr().sync_paths([folder_to_sync], recursive=True)

                if not os.path.exists(folder_to_sync):
                    LOGGER.warning(
                        'Impossible to update dependency "{}". Was impossible to sync latest path: "{}". '
                        'You will need to update the dependency manually'.format(item.path, item.latest_path))
                    continue

                fixed_path = artellapipe.FilesMgr().resolve_path(item.path)
                latest_fixed_path = artellapipe.FilesMgr().resolve_path(item.latest_path)

                updated_file = False
                locked = artellapipe.FilesMgr().lock_file(current_path, notify=False)
                with open(current_path, 'r') as f:
                    with open(temp_file, 'w') as out:
                        out_lines = list()
                        lines = f.readlines()
                        for line in lines:
                            if item.path in line:
                                if self._line_can_be_updated(line):
                                    LOGGER.info('Updating Dependency: {} ----> {}'.format(item.path, item.latest_path))
                                    line = line.replace(item.path, item.latest_path)
                                    updated_file = True
                                    updated = True
                            if fixed_path in line:
                                if self._line_can_be_updated(line):
                                    LOGGER.info('Updating Dependency: {} ----> {}'.format(item.path, item.latest_path))
                                    line = line.replace(fixed_path, latest_fixed_path)
                                    updated_file = True
                                    updated = True
                            out_lines.append(line)
                        out.writelines(out_lines)

                if updated_file and os.access(current_path, os.W_OK):
                    os.remove(current_path)
                    os.rename(temp_file, current_path)

            if os.path.isfile(temp_file):
                os.remove(temp_file)
            if updated and open_file:
                tp.Dcc.open_file(current_path, force=True)

        except Exception as e:
            LOGGER.error(str(e))
            LOGGER.error(traceback.format_exc())
            if locked:
                artellapipe.FilesMgr().unlock_file(current_path, notify=False, warn_user=False)
        finally:
            self._progress.setVisible(False)
            self._progress_lbl.setText('')
            self._update_items()

    def _line_can_be_updated(self, line):
        if '-rdi' in line or '-r' or '-typ' in line or '.cfn' in line or '.fn' in line:
            return True

        return False

    def _on_toggle_all(self, flag):
        it = QTreeWidgetItemIterator(self._files_list)
        while it.value():
            item = it.value()
            if item.childCount() == 0:
                if flag:
                    item.setCheckState(0, Qt.Checked)
                else:
                    item.setCheckState(0, Qt.Unchecked)
            it += 1
