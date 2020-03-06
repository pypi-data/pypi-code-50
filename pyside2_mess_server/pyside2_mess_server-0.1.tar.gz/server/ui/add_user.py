# -*- coding: utf-8 -*-
# Date: 09.02.2020
# Author: MaximRaduntsev

from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, \
    QVBoxLayout, QFormLayout, QFrame, QMessageBox
import hashlib
import binascii

from ui import style


class AddUser(QWidget):
    """
    Класс окна добавления пользователя
    """

    def __init__(self, database, server):
        super().__init__()
        self.database = database
        self.server = server

        self.password_l_edit = QLineEdit()
        self.label_conf = QLineEdit()
        self.bottom_frame = QFrame()
        self.top_frame = QFrame()
        self.bottom_layout = QFormLayout()
        self.top_layout = QVBoxLayout()
        self.main_layout = QVBoxLayout()
        self.submit_btn = QPushButton("Добавить")
        self.add_user_img = QLabel()
        self.name_l_edit = QLineEdit()
        self.text_label = QLabel("Добавьте пользователя")
        self.img = QPixmap('ui/img/add_user.png')
        self.setWindowTitle("Добавить клиента")
        self.setWindowIcon(QIcon('ui/icons/user_add.ico'))
        self.setGeometry(450, 150, 350, 550)
        self.setFixedSize(self.size())
        self.messages = QMessageBox()
        self.init_ui()
        self.show()

    def init_ui(self):
        """Функция инициализации окна"""
        self.widgets()
        self.layouts()

    def widgets(self):
        """Функция настройки виджета"""
        self.add_user_img.setPixmap(self.img)
        self.add_user_img.setAlignment(Qt.AlignCenter)
        self.text_label.setAlignment(Qt.AlignCenter)
        self.name_l_edit.setPlaceholderText('Введите имя пользователя')
        self.password_l_edit.setPlaceholderText('Пароль')
        self.label_conf.setPlaceholderText('Подтверждение')
        self.submit_btn.clicked.connect(self.save_data)

    def layouts(self):
        """Функция настройки layouts"""
        self.top_frame.setStyleSheet(style.user_top_frame())
        self.bottom_frame.setStyleSheet(style.user_bottom_frame())

        self.top_layout.addWidget(self.text_label)
        self.top_layout.addWidget(self.add_user_img)
        self.top_frame.setLayout(self.top_layout)
        self.bottom_layout.addRow(QLabel('Логин: '), self.name_l_edit)
        self.bottom_layout.addRow(QLabel('Пароль: '), self.password_l_edit)
        self.password_l_edit.setEchoMode(QLineEdit.Password)
        self.bottom_layout.addRow(QLabel('Подтверждение: '), self.label_conf)
        self.label_conf.setEchoMode(QLineEdit.Password)
        # self.password_l_edit.setDisabled(True)

        self.bottom_layout.addRow(QLabel(''), self.submit_btn)
        self.bottom_frame.setLayout(self.bottom_layout)

        self.main_layout.addWidget(self.top_frame)
        self.main_layout.addWidget(self.bottom_frame)

        self.setLayout(self.main_layout)

    def save_data(self):
        """
        Функция проверки правильности ввода и сохранения в базу
        нового пользователя.
        """
        if not self.name_l_edit.text():
            self.messages.critical(
                self, 'Ошибка', 'Не указано имя пользователя.')
            return
        elif self.password_l_edit.text() != self.label_conf.text():
            self.messages.critical(
                self, 'Ошибка', 'Введённые пароли не совпадают.')
            return
        elif self.database.check_user(self.name_l_edit.text()):
            self.messages.critical(
                self, 'Ошибка', 'Пользователь уже существует.')
            return
        else:
            # Генерируем хэш пароля, в качестве соли будем использовать логин в
            # нижнем регистре.
            passwd_bytes = self.password_l_edit.text().encode('utf-8')
            salt = self.name_l_edit.text().lower().encode('utf-8')
            passwd_hash = hashlib.pbkdf2_hmac(
                'sha512', passwd_bytes, salt, 10000)
            self.database.add_user(
                self.name_l_edit.text(),
                binascii.hexlify(passwd_hash))
            self.messages.information(
                self, 'Успех', 'Пользователь успешно зарегистрирован.')
            # Рассылаем клиентам сообщение о необходимости обновить справичники
            self.server.service_update_lists()
            self.close()
