#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool that allow artists to load assets into DCC scenes
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import os
import time
import logging
import traceback
from functools import partial

from Qt.QtCore import *
from Qt.QtWidgets import *
from Qt.QtGui import *

import tpDcc as tp
from tpDcc.libs.qt.core import qtutils, base
from tpDcc.libs.qt.widgets import splitters, stack, buttons

import artellapipe
from artellapipe.core import defines
from artellapipe.widgets import waiter
from artellapipe.utils import worker, exceptions

LOGGER = logging.getLogger()


class ArtellaAssetsLibraryWidget(QWidget, object):
    def __init__(self, project, supported_files=None, parent=None):

        self._supported_files = supported_files if supported_files else dict()
        self._project = project
        self._cache = dict()

        self._artella_worker = worker.Worker(app=QApplication.instance())
        self._artella_worker.workCompleted.connect(self._on_artella_worker_completed)
        self._artella_worker.workFailure.connect(self._on_artella_worker_failed)
        self._artella_worker.start()

        super(ArtellaAssetsLibraryWidget, self).__init__(parent=parent)

        self.ui()
        self.resize(150, 800)

        self._menu = self._create_contextual_menu()

        self._start_refresh()

    def showEvent(self, event):
        super(ArtellaAssetsLibraryWidget, self).showEvent(event)

    def ui(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.setLayout(self.main_layout)

        self._main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        self._main_widget.setLayout(main_layout)
        self.main_layout.addWidget(self._main_widget)

        self._stack = stack.SlidingStackedWidget()
        main_layout.addWidget(self._stack)

        no_assets_widget = QWidget()
        no_assets_layout = QVBoxLayout()
        no_assets_layout.setContentsMargins(2, 2, 2, 2)
        no_assets_layout.setSpacing(2)
        no_assets_widget.setLayout(no_assets_layout)
        no_assets_frame = QFrame()
        no_assets_frame.setFrameShape(QFrame.StyledPanel)
        no_assets_frame.setFrameShadow(QFrame.Sunken)
        no_assets_frame_layout = QHBoxLayout()
        no_assets_frame_layout.setContentsMargins(2, 2, 2, 2)
        no_assets_frame_layout.setSpacing(2)
        no_assets_frame.setLayout(no_assets_frame_layout)
        no_assets_layout.addWidget(no_assets_frame)
        no_assets_found_label = QLabel()
        no_assets_found_pixmap = tp.ResourcesMgr().pixmap('no_assets_found')
        no_assets_found_label.setPixmap(no_assets_found_pixmap)
        no_assets_frame_layout.addItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Preferred))
        no_assets_frame_layout.addWidget(no_assets_found_label)
        no_assets_frame_layout.addItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Preferred))

        loading_waiter = waiter.ArtellaWaiter()

        viewer_widget = QWidget()
        viewer_layout = QVBoxLayout()
        viewer_layout.setContentsMargins(2, 2, 2, 2)
        viewer_layout.setSpacing(2)
        viewer_widget.setLayout(viewer_layout)

        self._stack.addWidget(no_assets_widget)
        self._stack.addWidget(viewer_widget)
        self._stack.addWidget(loading_waiter)

        self._assets_viewer = artellapipe.AssetsViewer(
            project=self._project,
            column_count=2,
            parent=self
        )
        self._assets_viewer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self._top_layout = QHBoxLayout()
        self._top_layout.setContentsMargins(0, 0, 0, 0)
        self._top_layout.setSpacing(2)
        self._top_layout.setAlignment(Qt.AlignCenter)
        viewer_layout.addLayout(self._top_layout)

        self._categories_menu_layout = QHBoxLayout()
        self._categories_menu_layout.setContentsMargins(0, 0, 0, 0)
        self._categories_menu_layout.setSpacing(5)
        self._categories_menu_layout.setAlignment(Qt.AlignTop)
        self._top_layout.addLayout(self._categories_menu_layout)

        self._categories_btn_grp = QButtonGroup(self)
        self._categories_btn_grp.setExclusive(True)

        viewer_layout.addWidget(self._assets_viewer)

        self._supported_types_layout = QHBoxLayout()
        self._supported_types_layout.setContentsMargins(2, 2, 2, 2)
        self._supported_types_layout.setSpacing(2)
        self._supported_types_layout.setAlignment(Qt.AlignTop)
        viewer_layout.addLayout(self._supported_types_layout)

        self._supported_types_btn_grp = QButtonGroup(self)
        self._supported_types_btn_grp.setExclusive(True)

        self._sync_to_latest = QCheckBox('Sync to Latest Version')
        self._sync_to_latest.setChecked(True)
        self._fit_camera_cbx = QCheckBox('Fit Camera')
        self._fit_camera_cbx.setChecked(False)
        viewer_layout.addLayout(splitters.SplitterLayout())
        checkboxes_layout = QHBoxLayout()
        checkboxes_layout.setContentsMargins(5, 5, 5, 5)
        checkboxes_layout.setSpacing(2)
        viewer_layout.addLayout(checkboxes_layout)
        checkboxes_layout.addWidget(self._sync_to_latest)
        checkboxes_layout.addWidget(self._fit_camera_cbx)
        checkboxes_layout.addItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Preferred))
        viewer_layout.addLayout(splitters.SplitterLayout())

        self._assets_viewer.assetAdded.connect(self._on_asset_added)
        self._stack.animFinished.connect(self._on_stack_anim_finished)

    def contextMenuEvent(self, event):
        if not self._menu or self._stack.currentIndex() != 1:
            return
        self._menu.exec_(event.globalPos())

    def refresh(self, *args, **kwargs):
        """
        Function that refresh all the data of the assets library
        """

        self.update_assets_cache()
        self.update_cache()

    def update_assets_cache(self):
        """
        Function that updates assets viewer internal cache
        """

        self._assets_viewer.update_cache(force=True)

    def update_cache(self, force=False):
        """
        Function that updates the cache of the library
        """

        if self._cache and not force:
            return self._cache

        # If Artella server is slow, this process can take quite a lot of time. We detect this and disable
        # Artella server calls if necessary
        disable_artella_checks = False

        for i in range(self._assets_viewer.rowCount()):
            for j in range(self._assets_viewer.columnCount()):
                item = self._assets_viewer.cellWidget(i, j)
                if not item:
                    continue
                asset_widget = item.containedWidget
                asset_file = asset_widget.asset.get_file(
                    'rig', status=defines.ArtellaFileStatus.PUBLISHED, must_exist=False)
                asset_name = asset_widget.asset.get_name()
                if asset_file and os.path.exists(asset_file):
                    continue

                if asset_name not in self._cache:
                    self._cache[asset_name] = {
                        'item': item,
                        'has_label': False,
                        'has_sync_button': False,
                        'sync_button': None,
                        'label': None
                    }

                    if disable_artella_checks:
                        self._cache[asset_name]['has_label'] = False
                        self._cache[asset_name]['has_sync_button'] = False
                    else:
                        start_time = time.time()
                        if not asset_widget.asset.is_published('rig'):
                            self._cache[asset_name]['has_label'] = True
                        else:
                            self._cache[asset_name]['has_sync_button'] = True
                        end_time = time.time() - start_time
                        if end_time > 10:
                            artellapipe.logger.warning('Artella server is slow. Artella checks will be skip ...')
                            disable_artella_checks = True

        if disable_artella_checks:
            for asset_name, asset_data in self._cache.items():
                asset_data['has_label'] = False
                asset_data['has_sync_button'] = False

        return self._cache

    def update_assets_status(self, force=False):
        """
        Updates widgets icon depending of the availability of the asset
        """

        if not self._cache or force:
            self.update_cache(force=force)
        if not self._cache:
            return

        for asset_name, asset_data in self._cache.items():
            item = self._cache[asset_name]['item']
            has_label = self._cache[asset_name]['has_label']
            has_sync_button = self._cache[asset_name]['has_sync_button']
            if has_label:
                self._cache[asset_name]['label'] = self._create_not_published_label(item)
            if has_sync_button:
                self._cache[asset_name]['sync_button'] = self._create_sync_button(item)

    def update_asset_categories(self, asset_categories=None):
        """
        Updates current categories with the given ones
        :param asset_categories: list(str)
        """

        if not asset_categories:
            asset_categories = self._get_asset_categories()

        for btn in self._categories_btn_grp.buttons():
            self._categories_btn_grp.removeButton(btn)

        qtutils.clear_layout(self._categories_menu_layout)

        all_asset_categories = [defines.ArtellaFileStatus.ALL]
        all_asset_categories.extend(asset_categories)
        for category in all_asset_categories:
            new_btn = QPushButton(category)
            new_btn.setMinimumWidth(QFontMetrics(new_btn.font()).width(category) + 10)
            new_btn.setIcon(tp.ResourcesMgr().icon(category.lower()))
            new_btn.setCheckable(True)
            self._categories_menu_layout.addWidget(new_btn)
            self._categories_btn_grp.addButton(new_btn)
            if category == defines.ArtellaFileStatus.ALL:
                new_btn.setIcon(tp.ResourcesMgr().icon('home'))
                new_btn.setChecked(True)
            new_btn.toggled.connect(partial(self._change_category, category))

    def update_supported_types(self):
        """
        Updates current supported types
        """

        for btn in self._supported_types_btn_grp.buttons():
            self._supported_types_btn_grp.removeButton(btn)

        qtutils.clear_layout(self._supported_types_layout)

        if not self._supported_files:
            LOGGER.warning('No Supported Files for AssetsLibrary!')
            return

        total_buttons = 0
        for supported_file in self._supported_files:
            for type_name, file_info in supported_file.items():
                new_btn = QPushButton(type_name.title())
                new_btn.setIcon(tp.ResourcesMgr().icon(type_name.lower().replace(' ', '')))
                new_btn.setCheckable(True)
                new_btn.file_info = file_info
                self._supported_types_layout.addWidget(new_btn)
                self._supported_types_btn_grp.addButton(new_btn)
                if total_buttons == 0:
                    new_btn.setChecked(True)
                total_buttons += 1

    def _start_refresh(self):
        """
        Internal function that slides to loading assets stack widget and initializes the refresh operation
        in background
        """

        self._stack.slide_in_index(2)

    def _change_category(self, category, flag):
        """
        Internal function that is called when the user presses an Asset Category button
        :param category: str
        """

        if flag:
            self._assets_viewer.change_category(category=category)

    def _setup_asset_signals(self, asset_widget):
        """
        Internal function that sets proper signals to given asset widget
        This function can be extended to add new signals to added items
        :param asset_widget: ArtellaAssetWidget
        """

        asset_widget.clicked.connect(self._on_asset_clicked)
        asset_widget.startSync.connect(self._on_start_asset_sync)

    def _create_sync_button(self, item):
        """
        Internal function that creates a sync button
        :param item: ArtellaAssetWidget
        """

        sync_icon = tp.ResourcesMgr().icon('sync')
        sync_hover_icon = tp.ResourcesMgr().icon('sync_hover')
        sync_btn = buttons.HoverButton(icon=sync_icon, hover_icon=sync_hover_icon)
        sync_btn.setStyleSheet('background-color: rgba(0, 0, 0, 150);')
        sync_btn.setIconSize(QSize(50, 50))
        sync_btn.move(item.width() * 0.5 - sync_btn.width() * 0.5, item.height() * 0.5 - sync_btn.height() * 0.5)
        sync_btn.setParent(item.containedWidget)

        asset_widget = item.containedWidget
        sync_btn.clicked.connect(partial(self._on_sync_asset, asset_widget))

        return sync_btn

    def _create_not_published_label(self, item):
        """
        Internal function that creates not published label
        """

        not_published_pixmap = tp.ResourcesMgr().pixmap('asset_not_published')
        not_published_lbl = QLabel()
        not_published_lbl.move(9, 9)
        not_published_lbl.setFixedSize(65, 65)
        not_published_lbl.setPixmap(not_published_pixmap)
        not_published_lbl.setParent(item.containedWidget)

        return not_published_lbl

    def _create_contextual_menu(self):
        """
        Returns custom contextual menu
        :return: QMenu
        """

        new_menu = QMenu(self)
        get_thumbnails_action = QAction(tp.ResourcesMgr().icon('picture'), 'Update Thumbnails', new_menu)
        refresh_action = QAction(tp.ResourcesMgr().icon('refresh'), 'Refresh', new_menu)
        get_thumbnails_action.triggered.connect(self._on_update_thumbnails)
        refresh_action.triggered.connect(self.refresh)

        new_menu.addAction(get_thumbnails_action)
        new_menu.addAction(refresh_action)

        return new_menu

    def _get_asset_categories(self):
        """
        Returns a list with the asset categories supported
        :return: list(str)
        """

        return artellapipe.AssetsMgr().get_asset_categories()

    def _on_update_thumbnails(self):
        """
        Internal callback function that is called when Update Thumbnails action is triggered
        """

        self._assets_viewer.update_assets_thumbnails(force=True)

    def _on_asset_added(self, asset_widget):
        """
        Internal callback function that is called when a new asset widget is added to the assets viewer
        :param asset_widget: ArtellaAssetWidget
        """

        if not asset_widget:
            return

        self._setup_asset_signals(asset_widget)

    def _on_stack_anim_finished(self, index):
        """
        Internal callback function that is called when stack animation finish
        """

        if index == 2:
            self._artella_worker.queue_work(self.refresh, {})

    def _on_asset_clicked(self, asset_widget):
        """
        Internal callback function that is called when an asset button is clicked
        :param asset_widget: ArtellaAssetWidget
        """

        if not asset_widget:
            return

        for btn in self._supported_types_btn_grp.buttons():
            if btn.isChecked():
                try:
                    file_info = btn.file_info
                    if not file_info:
                        LOGGER.warning('Impossible to load asset file!')
                        return
                    for file_type, extensions in file_info.items():
                        if not extensions:
                            LOGGER.warning(
                                'No Extension defined for File Type "{}" in artellapipe.tools.assetslibrary '
                                'configuration file!'.format(file_type))
                            continue
                        for extension, operation in extensions.items():
                            if operation == 'reference':
                                res = asset_widget.asset.import_file(
                                    extension=extension, file_type=file_type, sync=self._sync_to_latest.isChecked(),
                                    reference=True, status=defines.ArtellaFileStatus.PUBLISHED)
                            else:
                                res = asset_widget.asset.import_file(
                                    extension=extension, file_type=file_type, sync=self._sync_to_latest.isChecked(),
                                    reference=False, status=defines.ArtellaFileStatus.PUBLISHED)
                            if res:
                                if self._fit_camera_cbx.isChecked():
                                    try:
                                        tp.Dcc.select_object(res)
                                        if tp.Dcc.selected_nodes():
                                            tp.Dcc.fit_view(True)
                                        tp.Dcc.clear_selection()
                                    except Exception as exc:
                                        LOGGER.warning(
                                            'Impossible to fit camera view to referenced objects | {}!'.format(exc))
                except Exception as e:
                    LOGGER.warning('Impossible to load asset file!')
                    LOGGER.error('{} | {}'.format(e, traceback.format_exc()))
                finally:
                    return

    def _on_sync_asset(self, asset_widget):
        """
        Internal callback function that is called when refresh button of an asset widget is pressed
        """

        if not asset_widget:
            return

        asset_widget.asset.sync_latest_published_files(None, True)

        asset_name = asset_widget.asset.get_name()
        asset_file = asset_widget.asset.get_file('rig', status=defines.ArtellaFileStatus.PUBLISHED)
        if asset_file and os.path.exists(asset_file):
            if asset_name in self._cache:
                if self._cache[asset_name]['sync_button']:
                    self._cache[asset_name]['sync_button'].setParent(None)
                    qtutils.safe_delete_later(self._cache[asset_name]['sync_button'])
                if self._cache[asset_name]['label']:
                    self._cache[asset_name]['label'].setParent(None)
                    qtutils.safe_delete_later(self._cache[asset_name]['label'])

    def _on_start_asset_sync(self, asset, file_type, sync_type):
        """
        Internal callback function that is called when an asset needs to be synced
        :param asset: ArtellaAsset
        :param file_type: str
        :param sync_type: str
        """

        if not asset:
            return

        asset.sync(file_type, sync_type)

    def _on_artella_worker_completed(self, uid, asset_widget):
        """
        Internal callback function that is called when worker finishes its job
        """

        total_assets = len(self._assets_viewer.get_assets())
        if total_assets > 0:
            self.update_asset_categories()
            self.update_supported_types()
            self.update_assets_status()
            self._stack.slide_in_index(1)
        else:
            self._stack.slide_in_index(0)

    def _on_artella_worker_failed(self, uid, msg, trace):
        """
        Internal callback function that is called when the Artella worker fails
        :param uid: str
        :param msg: str
        :param trace: str
        """

        error_msg = '{} | {} | {}'.format(uid, msg, trace)
        LOGGER.error(error_msg)
        exceptions.capture_message(error_msg)


class ArtellaAssetsLibrary(artellapipe.ToolWidget, object):

    LIBRARY_WIDGET = ArtellaAssetsLibraryWidget

    def __init__(self, project, config, settings, parent):
        super(ArtellaAssetsLibrary, self).__init__(project=project, config=config, settings=settings, parent=parent)

    def ui(self):
        super(ArtellaAssetsLibrary, self).ui()

        supported_files = self.config.get('supported_files')
        self._library_widget = self.LIBRARY_WIDGET(project=self._project, supported_files=supported_files)
        self.main_layout.addWidget(self._library_widget)

        artellapipe.Tracker().logged.connect(self._on_valid_login)
        artellapipe.Tracker().unlogged.connect(self._on_valid_unlogin)

    def _on_valid_login(self):
        """
        Internal callback function that is called anytime user log in into Tracking Manager
        """

        self._library_widget._start_refresh()

    def _on_valid_unlogin(self):
        """
        Internal callback function that is called anytime user unlog from Tracking Manager
        """

        self._library_widget._stack.slide_in_index(0)
