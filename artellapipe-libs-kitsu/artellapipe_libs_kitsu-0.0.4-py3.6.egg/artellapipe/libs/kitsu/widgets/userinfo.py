#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains widget implementation that shows user info for Plot Twist
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import logging

from Qt.QtCore import *
from Qt.QtWidgets import *
from Qt.QtGui import *

import tpDcc
from tpDcc.libs.qt.core import qtutils
from tpDcc.libs.qt.widgets import balloon

import artellapipe
from artellapipe.libs.kitsu.widgets import logindialog

LOGGER = logging.getLogger()


class KitsuUserBalloon(balloon.BalloonDialog, object):
    def __init__(self, user_data, parent=None):
        super(KitsuUserBalloon, self).__init__(parent)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        full_name_lbl = QLabel('{} - {}'.format(user_data.full_name, user_data.role))
        email_lbl = QLabel(user_data.email)
        timezone_lbl = QLabel('{} - {}'.format(user_data.locale, user_data.timezone))

        main_layout.addWidget(full_name_lbl)
        main_layout.addWidget(email_lbl)
        main_layout.addWidget(timezone_lbl)


class KitsuUserInfo(QFrame, object):

    login = Signal()
    logout = Signal()

    def __init__(self, project, parent=None):
        super(KitsuUserInfo, self).__init__(parent=parent)

        self._project = project

        self.ui()

    def ui(self):
        self.main_layout = QHBoxLayout()
        self.main_layout.setAlignment(Qt.AlignTop)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.setLayout(self.main_layout)

        self.setFrameShape(QFrame.Panel)
        self.setFrameShadow(QFrame.Raised)
        self.setLineWidth(1)

        shutdown_icon = tpDcc.ResourcesMgr().icon('shutdown')
        self._kitsu_off_icon = tpDcc.ResourcesMgr().icon('kitsu_off')
        self._kitsu_on_icon = tpDcc.ResourcesMgr().icon('kitsu_on')

        self._kitsu_btn = QPushButton('Kitsu')
        self._kitsu_btn.setIconSize(QSize(50, 50))
        self._kitsu_btn.setFixedHeight(25)
        self._kitsu_btn.setMinimumWidth(90)
        self._kitsu_btn.setFlat(True)

        self._kitsu_logout_btn = QPushButton()
        self._kitsu_logout_btn.setVisible(False)
        self._kitsu_logout_btn.setIcon(shutdown_icon)
        self._kitsu_btn.setFlat(True)

        self.main_layout.addWidget(self._kitsu_btn)
        self.main_layout.addWidget(self._kitsu_logout_btn)

        self._kitsu_btn.clicked.connect(self._on_open_kitsu_login)
        self._kitsu_logout_btn.clicked.connect(self._on_kitsu_logout)

        if self._project:
            self.update_kitsu_status()

    def set_project(self, project):
        self._project = project
        self.update_kitsu_status()

    def try_kitsu_login(self):
        """
        Function that tries to log into Kitsu
        """

        valid_login = artellapipe.Tracker().login()
        if valid_login:
            self._kitsu_login()
            return True

        return False

    def update_kitsu_status(self):
        """
        Synchronizes current Kitsu status between UserInfo and current project
        """

        if not self._project:
            LOGGER.warning('Impossible to update Kitsu Status because Project is not defined!')
            return

        if artellapipe.Tracker().is_logged():
            self._kitsu_btn.setIcon(self._kitsu_on_icon)
            self._kitsu_logout_btn.setVisible(True)
        else:
            self._kitsu_btn.setIcon(self._kitsu_off_icon)
            self._kitsu_logout_btn.setVisible(False)

    def _kitsu_login(self):
        """
        Tries to login into Kitsu
        """

        self.update_kitsu_status()
        self.login.emit()

    def _on_open_kitsu_login(self):
        """
        Internal callback function that is called when the user presses the Kitsu button
        """

        if artellapipe.Tracker().is_logged():
            user_data = artellapipe.Tracker().user_data
            self._ballon = KitsuUserBalloon(user_data=user_data)
            rect_btn = self._kitsu_btn.geometry()
            rect_balloon = self._ballon.geometry()
            pos = QCursor.pos()
            pos.setX(pos.x() - (self._kitsu_btn.width() / 2) - 20)
            rect_balloon.setRect(
                pos.x(), pos.y(), rect_btn.width(), rect_btn.height()
            )
            self._ballon.setGeometry(rect_balloon)
            self._ballon.show()
        else:
            login_dialog = logindialog.KitsuLoginDialog(project=self._project, parent=self.parent())
            login_dialog.validLogin.connect(self._on_kitsu_login)
            # login_dialog.invalidLogin.connect(self._on_kitsu_logout)
            login_dialog.exec_()

    def _on_kitsu_login(self):
        """
        Internal callback function that is called when the user presses the login button
        """

        self._kitsu_login()

    def _on_kitsu_logout(self):
        """
        Internal callback function that is called when the user presses the logout button
        """

        remove_credentials = False
        res = qtutils.show_question(self, 'Kitsu Logout', 'Do you want to remove Kitsu stored credentials?')
        if res == QMessageBox.Yes:
            remove_credentials = True

        valid = artellapipe.Tracker().logout(remove_credentials=remove_credentials)
        if not valid:
            LOGGER.warning('Error while logging out from Kitsu')
            return

        self.update_kitsu_status()
        self.logout.emit()
