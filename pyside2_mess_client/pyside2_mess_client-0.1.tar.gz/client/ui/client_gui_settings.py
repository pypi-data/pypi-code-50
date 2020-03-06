#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 31.01.2020 19:13
# @Author: MaximRaduntsev
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDialog, qApp, QApplication
from PySide2.QtCore import Qt

from log.client_log_config import logger
from ui.connect_user_UIs import Ui_ConnectionDialog
from ui.add_contact_UIs import Ui_AddUserDialog
from ui.del_contact_UIs import Ui_DelUserDialog


class UserNameDialog(QDialog):
    """
    Класс реализующий стартовый диалог с запросом логина и пароля
    пользователя.
    """

    def __init__(self):
        super(UserNameDialog, self).__init__()
        self.ui = Ui_ConnectionDialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('ui/icons/icon.ico'))
        self.ok_pressed = False
        self.initUI()

    def initUI(self):
        """
        Стартовый диалог с выбором имени пользователя
        """
        self.ui.okButton.clicked.connect(self.click)
        self.ui.cancelButton.clicked.connect(qApp.exit)
        self.show()

    def click(self):
        """
        Обработчик кнопки ОК, если поле вводе не пустое,
        ставим флаг и завершаем приложение.
        """
        if self.ui.name_ledit.text() and self.ui.pass_ledit.text():
            self.ok_pressed = True
            qApp.exit()


class AddContactDialog(QDialog):
    """
    Диалог выбора контакта для добавления
    """

    def __init__(self, transport, database):
        super().__init__()
        self.ui = Ui_AddUserDialog()
        self.transport = transport
        self.database = database
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('ui/icons/user_add.ico'))
        self.selector = self.ui.cl_comboBox
        self.initUI()

    def initUI(self):
        """
        Обработка нажатия кнопки "Добавить контакт" главного окна
        Вызывает окно для ввода имени контакта
        """
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setModal(True)
        # Заполняем список возможных контактов
        self.possible_contacts_update()
        # Назначаем действие на кнопку обновить
        self.ui.btn_refresh.clicked.connect(self.update_possible_contacts)

        self.ui.buttonBox.rejected.connect(self.close)
        # self.show()

    def possible_contacts_update(self):
        """Заполняем список возможных контактов разницей между всеми пользователями"""
        self.selector.clear()
        # множества всех контактов и контактов клиента
        contacts_list = set(self.database.get_contacts())
        users_list = set(self.database.get_users())
        # Удалим сами себя из списка пользователей, чтобы нельзя было добавить
        # самого себя
        users_list.remove(self.transport.account_name)
        # Добавляем список возможных контактов
        self.selector.addItems(users_list - contacts_list)

    def update_possible_contacts(self):
        """
        Обновлялка возможных контактов. Обновляет таблицу известных пользователей,
        затем содержимое предполагаемых контактов
        """
        try:
            self.transport.user_list_update()
        except OSError:
            pass
        else:
            logger.debug('Обновление списка пользователей с сервера выполнено')
            self.possible_contacts_update()


class DelContactDialog(QDialog):
    """
    Диалог выбора контакта для удаления
    """

    def __init__(self, database):
        super(DelContactDialog, self).__init__()
        self.ui = Ui_DelUserDialog()
        self.database = database
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('ui/icons/user_delete.ico'))
        self.selector = self.ui.cl_comboBox
        self.initUI()

    def initUI(self):
        """
        Обработка нажатия кнопки "Удалить контакт" главного окна
        Вызывает окно для ввода имени контакта
        """
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setModal(True)

        # заполнитель контактов для удаления
        self.selector.addItems(sorted(self.database.get_contacts()))

        self.ui.buttonBox.rejected.connect(self.close)


if __name__ == '__main__':
    app = QApplication([])
    dial = UserNameDialog()
    app.exec_()
