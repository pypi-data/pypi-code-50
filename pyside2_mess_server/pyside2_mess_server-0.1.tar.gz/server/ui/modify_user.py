# -*- coding: utf-8 -*-
# Date: 11.02.2020
# Author: MaximRaduntsev

from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, \
    QVBoxLayout, QFormLayout, QFrame, QMessageBox

import ui.style as style


class ModifyUser(QWidget):
    """
    Класс редактора пользователя
    """
    def __init__(self, database, user_name, password=None):
        super().__init__()
        self.database = database
        self.user_name = user_name
        self.password = password
        self.bottom_frame = QFrame()
        self.top_frame = QFrame()
        self.bottom_layout = QFormLayout()
        self.top_layout = QVBoxLayout()
        self.main_layout = QVBoxLayout()
        self.update_btn = QPushButton('Обновить')
        self.password_l_edit = QLineEdit()
        self.name_l_edit = QLineEdit()
        self.text_label = QLabel('Редактировать профиль')
        self.img = QPixmap('ui/img/members.png')
        self.user_img = QLabel()
        self.setWindowTitle('Редактор профиля')
        self.setWindowIcon(QIcon('ui/icons/icon.ico'))
        self.setGeometry(450, 150, 350, 600)
        self.setFixedSize(self.size())
        self.init_ui()
        self.show()

    def init_ui(self):
        """Функция инициализации окна"""
        self.user_details()
        self.widgets()
        self.layouts()

    def user_details(self):
        query = self.database.get_user_by_name(self.user_name)
        self.user_name = query.name
        # self.password = query.name

    def widgets(self):
        self.user_img.setPixmap(self.img)
        self.user_img.setAlignment(Qt.AlignCenter)
        self.text_label.setAlignment(Qt.AlignCenter)

        self.name_l_edit.setText(self.user_name)
        self.password_l_edit.setText(self.password)
        self.update_btn.clicked.connect(self.update_user)

    def layouts(self):
        self.top_frame.setStyleSheet(style.user_top_frame())
        self.bottom_frame.setStyleSheet(style.user_bottom_frame())

        self.top_layout.addWidget(self.text_label)
        self.top_layout.addWidget(self.user_img)
        self.top_frame.setLayout(self.top_layout)

        self.bottom_layout.addRow(QLabel('Имя: '), self.name_l_edit)
        self.bottom_layout.addRow(QLabel('Пароль: '), self.password_l_edit)
        # пока блокирую
        self.password_l_edit.setDisabled(True)
        self.bottom_layout.addRow(QLabel(''), self.update_btn)
        self.bottom_frame.setLayout(self.bottom_layout)

        self.main_layout.addWidget(self.top_frame)
        self.main_layout.addWidget(self.bottom_frame)
        self.setLayout(self.main_layout)

    def update_user(self):
        name = self.name_l_edit.text()
        password = self.password_l_edit.text()

        if name:
            try:
                self.database.user_modify(self.user_name, name)
                QMessageBox.information(
                    self, 'Info', 'Имя пользователя обновлено!')
            except BaseException:
                QMessageBox.warning(
                    self, 'Warning', 'Имя пользователя не обновлено!')
        else:
            QMessageBox.information(self, 'Info', 'Поле не может быть пустым!')
