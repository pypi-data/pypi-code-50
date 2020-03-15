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

import os
import logging

from Qt.QtWidgets import *

import tpDcc
from tpDcc.libs.qt.widgets import stack, splitters

import artellapipe

LOGGER = logging.getLogger()


class SequencesPublisher(artellapipe.PyblishTool, object):

    def __init__(self, project, config, settings, parent):
        super(SequencesPublisher, self).__init__(project=project, config=config, settings=settings, parent=parent)

        self.update_sequences()

        self._publisher_layout.addWidget(self._pyblish_window)

    def ui(self):
        super(SequencesPublisher, self).ui()

        self._stack = stack.SlidingStackedWidget()
        self.main_layout.addWidget(self._stack)

        self._sequences_viewer = artellapipe.SequencesViewer(project=self._project)
        self._stack.addWidget(self._sequences_viewer)

        publisher_widget = QWidget()
        self._publisher_layout = QVBoxLayout()
        self._publisher_layout.setContentsMargins(0, 0, 0, 0)
        self._publisher_layout.setSpacing(2)
        publisher_widget.setLayout(self._publisher_layout)
        self._stack.addWidget(publisher_widget)

        back_icon = tpDcc.ResourcesMgr().icon('back')
        self._back_btn = QPushButton()
        self._back_btn.setIcon(back_icon)
        buttons_layout = QHBoxLayout()
        buttons_layout.setContentsMargins(0, 0, 0, 0)
        buttons_layout.setSpacing(2)
        self._publisher_layout.addLayout(buttons_layout)
        buttons_layout.addWidget(self._back_btn)
        buttons_layout.addItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Preferred))
        self._publisher_layout.addLayout(splitters.SplitterLayout())
        options_layout = QHBoxLayout()
        options_layout.setContentsMargins(0, 0, 0, 0)
        options_layout.setSpacing(2)
        self._publisher_layout.addLayout(options_layout)
        self._upload_new_version_cbx = QCheckBox('Upload New Version')
        os.environ['{}_SEQUENCES_PUBLISHER_NEW_VERSION'.format(self._project.get_clean_name().upper())] = str(False)
        options_layout.addWidget(self._upload_new_version_cbx)
        options_layout.addItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Preferred))

    def setup_signals(self):
        self._sequences_viewer.sequenceAdded.connect(self._on_sequence_added)
        self._stack.animFinished.connect(self._on_stack_anim_finished)
        self._upload_new_version_cbx.toggled.connect(self._on_toggle_upload_new_version)
        self._back_btn.clicked.connect(self._on_back)

    def update_sequences(self, force=False):
        self._sequences_viewer.update_sequences(force=force)

    def _setup_sequence_signals(self, sequence_widget):
        """
        Internal function that sets proper signals to given sequence widget
        This function can be extended to add new signals to added items
        :param sequence_widget: ArtellaSequenceWidget
        """

        sequence_widget.clicked.connect(self._on_sequence_clicked)

    def _on_sequence_added(self, sequence_widget):
        self._setup_sequence_signals(sequence_widget)

    def _on_sequence_clicked(self, sequence_widget):
        if not sequence_widget:
            return
        sequence = sequence_widget.sequence
        if not sequence:
            return

        sequence_name = sequence.get_name()
        sequence = artellapipe.SequencesMgr().find_sequence(sequence_name)
        if not sequence:
            LOGGER.warning('No Sequence found with name "{}" in current project'.format(sequence_name))
            return
        valid_open = sequence.open_master_layout()
        if not valid_open:
            return

        self._stack.slide_in_index(1)

    def _on_stack_anim_finished(self, index):
        if index == 1:
            self._pyblish_window.reset()

    def _on_back(self):
        self._stack.slide_in_index(0)

    def _on_toggle_upload_new_version(self, flag):
        os.environ['{}_SEQUENCES_PUBLISHER_NEW_VERSION'.format(self._project.get_clean_name().upper())] = str(flag)
