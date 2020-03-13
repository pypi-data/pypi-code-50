#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains implementation for Kitsu Login Form
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import logging

from Qt.QtCore import *
from Qt.QtWidgets import *

import tpDcc
from tpDcc.libs.qt.core import qtutils
from tpDcc.libs.qt.widgets import formwidget, lightbox, stack

import artellapipe
from artellapipe.widgets import dialog
from artellapipe.libs.kitsu.widgets import loginwidget
from artellapipe.utils import worker

LOGGER = logging.getLogger()


class KitsuLoginForm(formwidget.FormDialog, object):

    loginAccepted = Signal(str, str, bool)
    loginCancelled = Signal()

    def __init__(self, email='', password='', store_credentials=False, parent=None):
        super(KitsuLoginForm, self).__init__(parent=parent)

        self._valid_fields = False

        self.setMinimumWidth(300)
        self.setMinimumHeight(300)
        self.setMaximumWidth(400)
        self.setMaximumHeight(400)
        self.accept_button().setText('Login')
        self.accept_button().setEnabled(False)

        kitsu_pixmap = tpDcc.ResourcesMgr().pixmap('kitsu', category='icons', theme='color')
        kitsu_icon = QLabel()
        kitsu_icon.setAlignment(Qt.AlignCenter)
        kitsu_icon.setPixmap(kitsu_pixmap)
        self.main_layout.insertWidget(2, kitsu_icon)

        login_form = {
            'title': 'Kitsu Login',
            'description': 'Write your Kitsu credentials',
            'layout': 'vertical',
            'schema': [
                {
                    'name': 'email',
                    'type': 'string',
                    'value': email
                },
                {
                    'name': 'password',
                    'type': 'password',
                    'value': password
                },
                {
                    'name': 'store credentials',
                    'type': 'bool',
                    'value': bool(store_credentials)
                }
            ],
            'validator': self._kitsu_login_validator,
            'accepted': self._kitsu_login_accepted,
            'rejected': self._kitsu_login_cancelled
        }
        self.set_settings(login_form)
        self._form_widget.validate()

    def _kitsu_login_validator(self, **kwargs):
        """
        Internal function that is called each time the user updates the form
        :param kwargs:
        """

        username = kwargs.get('email', None)
        password = kwargs.get('password', None)

        if not username or not password:
            self._valid_fields = False
            self.accept_button().setEnabled(False)
        else:
            self._valid_fields = True
            self.accept_button().setEnabled(True)

    def _kitsu_login_accepted(self, **kwargs):
        """
        Internal callback function that is called when the user presses the login button
        :param kwargs: dict
        """

        username = kwargs.get('email', None)
        password = kwargs.get('password', None)
        store = kwargs.get('store credentials', False)

        self.loginAccepted.emit(username, password, store)

    def _kitsu_login_cancelled(self, **kwargs):
        """
        Internal callback function that is called when the user presses the cancel button
        :param kwargs: dict
        """

        self.loginCancelled.emit()

    def _on_validated(self):
        """
        Overrides base _on_validated FormWidget function
        """

        self._accept_btn.setEnabled(not self._form_widget.has_errors() and self._valid_fields)


class KitsuLoginDialog(dialog.ArtellaDialog, object):

    validLogin = Signal()
    invalidLogin = Signal()

    def __init__(self, project, parent=None):
        super(KitsuLoginDialog, self).__init__(
            name='KitsuLoginDialog',
            title='Kitsu - Login Dialog',
            parent=parent,
            size=(400, 400),
            fixed_size=True,
            project=project
        )

        self._kitsu_worker = worker.Worker(app=QApplication.instance())
        self._kitsu_worker.workCompleted.connect(self._on_kitsu_worker_completed)
        self._kitsu_worker.workFailure.connect(self._on_kitsu_worker_failure)
        self._kitsu_worker.start()

    def ui(self):
        super(KitsuLoginDialog, self).ui()

        self._dragger._button_closed.setVisible(False)
        self._dragger.setVisible(False)
        self.logo_view.setVisible(False)

        self._main_stack = stack.SlidingStackedWidget(parent=self)

        self._login_widget = self._create_login_form()
        self._kitsu_waiter = loginwidget.KitsuLoginWidget()

        self._main_stack.addWidget(self._login_widget)
        self._main_stack.addWidget(self._kitsu_waiter)

        self._lightbox = lightbox.Lightbox(self)
        self._lightbox.set_widget(self._main_stack)
        self._lightbox.show()

        self._lightbox.closed.connect(self.close)

    def setup_signals(self):
        self._main_stack.animFinished.connect(self._on_stack_anim_finished)
        self._login_widget.loginAccepted.connect(self._on_kitsu_login_accepted)
        self._login_widget.loginCancelled.connect(self.close)

    def _create_login_form(self):
        """
        Internal callback function that checks current Kitsu login status
        """

        email = artellapipe.Tracker().email
        password = artellapipe.Tracker().password
        store_credentials = artellapipe.Tracker().store_credentials

        return KitsuLoginForm(email=email, password=password, store_credentials=store_credentials)

    def _start_kitsu_worker(self, new_index=None):
        """
        Internal function that starts new Kitsu worker
        :param new_index: int
        """

        if new_index:
            w = self._main_stack.widget(new_index)
        else:
            w = self._main_stack.currentWidget()
        if w == self._kitsu_waiter:
            self._kitsu_worker.queue_work(self._kitsu_login, {})

    def _kitsu_login(self, *args, **kwargs):
        """
        Internal function that is called by Kitsu Worker to execute login
        :param data:
        :return:
        """

        email = artellapipe.Tracker().email
        password = artellapipe.Tracker().password

        if not email or not password:
            LOGGER.warning('Impossible to login into Kitsu because user and password are not given!')
            return

        valid_login = artellapipe.Tracker().login(email=email, password=password)

        return valid_login

    def _on_stack_anim_finished(self, new_index):
        """
        Internal callback function that is callded when stack anim finished
        :param new_index: int
        """

        self._start_kitsu_worker(new_index=new_index)

    def _on_kitsu_login_accepted(self, email, password, store_credentials):
        """
        Internal callback function that is called when the user successfully log into Kitsu through Kitsu login form
        :param email: variant, str or None
        :param password: variant, str or None
        :param store_credentials: bool
        """

        artellapipe.Tracker().email = email
        artellapipe.Tracker().password = password
        artellapipe.Tracker().store_credentials = store_credentials

        index = self._main_stack.indexOf(self._kitsu_waiter)
        self._main_stack.slide_in_index(index, force=True)

    def _on_kitsu_worker_completed(self, uid, valid_login):
        """
        Internal callback function that is called when Kitsu worker finishes
        :param uid: str
        :param valid_login: bool
        """

        if valid_login:
            if not artellapipe.Tracker().is_logged():
                LOGGER.warning('Something went wrong during Kitsu login')
                return False
            if artellapipe.Tracker().email and artellapipe.Tracker().password:
                store_credentials = bool(artellapipe.Tracker().store_credentials)
                self._project.settings.set('kitsu_store_credentials', store_credentials)
                self.validLogin.emit()
                self.close()
        else:
            qtutils.show_error(
                self, 'Error while logging into Kitsu', 'Kitsu credentials are not valid. Try again please!')
            self._main_stack.slide_in_index(0)
            return False

        return True

    def _on_kitsu_worker_failure(self, uid, msg):
        """
        Internal callback function that is called when Kitsu worker fails
        :param uid: str
        :param msg: str
        """

        artellapipe.Tracker().reset_user_info()
        LOGGER.error('{} | {}'.format(uid, msg))
        self._main_stack.slide_in_index(0)
