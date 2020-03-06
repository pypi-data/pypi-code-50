# -*- coding: utf-8 -*-
# Date: 01.01.2020
# Author: MaximRaduntsev

from PySide2.QtCore import Qt, QFile
from PySide2.QtGui import QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QTabWidget, QMainWindow, QTableWidget, QWidget, \
    QHBoxLayout, QLineEdit, QPushButton, QGroupBox, QHeaderView, \
    QAction, QMessageBox, QTableWidgetItem, QDialog, QFileDialog, QApplication, QVBoxLayout

import ui.connect_window_UIs as connect_window_UIs
import ui.add_user as add_member
import ui.remove_user as del_member
import ui.modify_user as modify_user

from pathlib import Path
from dynaconf import settings
from dynaconf.loaders import yaml_loader as loader
from ipaddress import ip_address

from ui import style


class Main(QMainWindow):
    """
    Класс окна программы
    """

    def __init__(self, database, server):
        super(Main, self).__init__()
        self.database = database
        self.server = server
        self.tabs = QTabWidget(self)
        self.setWindowTitle("Server Manager")
        self.setWindowIcon(QIcon('ui/icons/icon.ico'))
        self.setGeometry(450, 150, 1100, 750)
        # self.setFixedSize(self.size())

        self.tool_bar()
        self.tabs.blockSignals(False)
        self.tabs.currentChanged.connect(self.func_tab_refresh)
        self.setCentralWidget(self.tabs)

        self.history_user_table = QTableWidget(self)
        self.active_user_table = QTableWidget(self)

        self.tab1 = QWidget(self)
        self.tab2 = QWidget(self)

        self.init_ui()
        self.show()

    def init_ui(self):
        """Функция настройки отображения шапок таблиц"""
        header1 = [
            'ID Клиента',
            'Имя Клиента',
            'IP Адрес',
            'Порт',
            'Время подключения']
        tab_name1 = 'Список подключенных клиентов'
        self.base_tab(self.active_user_table, header1, self.tab1, tab_name1)
        self.member_search_entry.setDisabled(True)

        header2 = [
            'Имя Клиента',
            'Последний раз входил',
            'Сообщений отправлено',
            'Сообщений получено']
        tab_name2 = 'История клиентов'
        self.base_tab(self.history_user_table, header2, self.tab2, tab_name2)

    def layout_tab(self, table, tab, tab_name):
        """
        Функция настройки layout
        :param table:
        :param tab:
        :param tab_name:
        :return:
        """
        # self.member_search_text = QLabel("Найти пользователя")
        self.member_search_entry = QLineEdit()
        self.member_search_button = QPushButton("Найти")
        self.member_search_button.clicked.connect(self.search_users)
        self.member_search_button.setStyleSheet(style.search_button_style())

        self.member_main_layout = QHBoxLayout()
        self.member_left_layout = QHBoxLayout()
        self.member_right_layout = QVBoxLayout()
        self.right_top_layout = QVBoxLayout()

        self.member_right_group_box = QGroupBox("Поиск клиентов")
        self.right_top_layout.setContentsMargins(20, 40, 20, 100)
        self.member_right_group_box.setStyleSheet(style.search_box_style())

        self.bottom_group_box = QGroupBox()

        self.right_top_layout.addWidget(self.member_search_entry)
        self.right_top_layout.addWidget(self.member_search_button)
        self.member_right_group_box.setLayout(self.right_top_layout)

        self.member_left_layout.addWidget(table)

        self.member_right_layout.addWidget(self.member_right_group_box, 20)
        self.member_right_layout.addWidget(self.bottom_group_box, 80)

        self.member_main_layout.addLayout(self.member_left_layout, 70)
        self.member_main_layout.addLayout(self.member_right_layout, 30)

        tab.setLayout(self.member_main_layout)

        self.tabs.addTab(tab, tab_name)

    def base_tab(self, table, header, tab, tab_name):
        """
        Базовый tab
        :param table:
        :param header:
        :param tab:
        :param tab_name:
        :return:
        """
        table.setColumnCount(len(header))
        table.setHorizontalHeaderLabels(header)
        table.verticalHeader().hide()
        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.doubleClicked.connect(self.selected_user)
        self.layout_tab(table, tab, tab_name)

    def tool_bar(self):
        """
        Функция настройки и расположения tool bar
        :return:
        """
        self.tb = self.addToolBar('Tool Bar')
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.config_window = QAction(
            QIcon('ui/img/db.png'), 'Настройка БД', self)
        self.tb.addAction(self.config_window)
        self.config_window.triggered.connect(self.func_config_window)
        self.tb.addSeparator()

        self.add_member = QAction(
            QIcon('ui/icons/user_add.ico'),
            'Новый клиент',
            self)
        self.tb.addAction(self.add_member)
        self.add_member.triggered.connect(self.func_add_user)
        self.tb.addSeparator()

        self.del_member = QAction(
            QIcon('ui/icons/user_delete.ico'),
            'Удалить клиента',
            self)
        self.tb.addAction(self.del_member)
        self.del_member.triggered.connect(self.func_del_user)
        self.tb.addSeparator()

        self.tab_refresh = QAction(
            QIcon('ui/icons/brain.ico'), 'Обновить', self)
        self.tb.addAction(self.tab_refresh)
        self.tab_refresh.triggered.connect(self.func_tab_refresh)
        self.tb.addSeparator()

    def func_config_window(self):
        """
        Открытие настроек сервера
        :return:
        """
        self.config_open()

    def func_del_user(self):
        """
        Функция открытия окна удаления пользователя
        :return:
        """
        self.rem_window = del_member.DelUserDialog(self.database, self.server)

    def func_add_user(self):
        """
        Функция открытия окна добавления пользователя
        :return:
        """
        self.new_user = add_member.AddUser(self.database, self.server)

    def selected_user(self):
        """
        Функция открытия окна выбора пользователя
        :return:
        """
        list_user = []
        for i in range(0, 4):
            list_user.append(
                self.history_user_table.item(
                    self.history_user_table.currentRow(),
                    i).text())
        user_name = list_user[0]
        # user_id = list_user[0]
        self.modify_user = modify_user.ModifyUser(self.database, user_name)
        self.modify_user.show()

    def search_users(self):
        """
        Функция открытия окна выбора пользователя
        :return:
        """
        value = self.member_search_entry.text()
        if value == '':
            QMessageBox.information(
                self, 'Warning', 'Запрос не может быть пустым')

        else:
            self.member_search_entry.setText('')
            results = self.database.get_user_by_like(value)
            if not results:
                QMessageBox.warning(self, 'Warning', 'Нет такого клиента')
            else:
                for i in reversed(range(self.history_user_table.rowCount())):
                    self.history_user_table.removeRow(i)

                for row_data in results:
                    row_number = self.history_user_table.rowCount()
                    self.history_user_table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.history_user_table.setItem(
                            row_number, column_number, QTableWidgetItem(
                                self.table_widget_item(data)))

    @staticmethod
    def table_widget_item(data):
        """
        Функция настройки QTableWidgetItem
        :param data:
        :return:
        """
        item = QTableWidgetItem()
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        item.setText(str(data))
        return item

    def config_open(self):
        """Открытие окна настроек сервера"""
        global config_window
        config_window = ConfigWindow(self)

    def display_users(self):
        """Функция таблицы пользователей во вкладке история клиентов """
        for i in reversed(range(self.history_user_table.rowCount())):
            self.history_user_table.removeRow(i)

        members = set(self.database.message_history())
        sorted(members, key=lambda item: item[3])
        for row_data in members:
            row_number = self.history_user_table.rowCount()
            self.history_user_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.history_user_table.setItem(
                    row_number, column_number, QTableWidgetItem(
                        self.table_widget_item(data)))

    def func_tab_refresh(self):
        """Функция обновления таблицы пользователей во вкладке история клиентов """
        self.display_users()


class ConfigWindow(QDialog):
    """Класс окна настроек."""

    def __init__(self, parent):
        """Инициализация."""
        self.parent_gui = parent
        super().__init__()
        self.ui = connect_window_UIs.Ui_ConnectDialog()
        self.ui.setupUi(self)
        # self.ui = self.load_ui_widget("ui/connect_window.ui")
        self.init_ui()

    @staticmethod
    def load_ui_widget(ui_filename):
        """Функция загрузки ui"""
        ui_file = QFile(ui_filename)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        ui = loader.load(ui_file)
        ui_file.close()
        ui.show()
        return ui

    def init_ui(self):
        """Инициализация интерфейса."""
        self.setAttribute(Qt.WA_DeleteOnClose)
        db_def_name = Path(settings.get('DATABASES.SERVER.NAME'))

        def open_file_dialog():
            """Функция обработчик открытия окна выбора папки."""
            global dialog
            dialog = QFileDialog(config_window)
            path_d = dialog.getExistingDirectory()
            if path_d:
                path_d = str(Path(path_d))
                self.ui.db_path_lbl.clear()
                self.ui.db_path_lne.insert(path_d)

        self.ui.db_path_btn.clicked.connect(open_file_dialog)
        self.ui.db_path_lne.insert(str(db_def_name.parent.absolute()))
        self.ui.db_name_lne.insert(str(db_def_name.name))
        self.ui.ip_lne.insert(
            str(ip_address(settings.get('DEFAULT_SERVER_IP'))))
        self.ui.port_lne.insert(str(settings.get('DEFAULT_PORT')))
        self.ui.btn_box.accepted.connect(self.save_server_config)
        self.show()

    def save_server_config(self):
        """Функция сохранения настроек сервера."""
        for_save = dict()
        msg_box = QMessageBox()
        db_path = Path(self.ui.db_path_lne.text())
        db_name = Path(self.ui.db_name_lne.text())
        db = db_path.joinpath(db_name)
        try:
            db = db.relative_to(Path.cwd())
        except Exception:
            pass
        try:
            port = self.parent_gui.port = int(self.ui.port_lne.text())
        except Exception as e:
            return msg_box.warning(config_window, 'Ошибка', str(e))
        # set settings
        settings.set('DEFAULT_SERVER_IP', self.ui.ip_lne.text())
        settings.set('DEFAULT_PORT', port)
        settings.DATABASES.SERVER.NAME = str(db)
        for_save['DEFAULT'] = set_dict = settings.as_dict()
        for_save['DEFAULT']['DATABASES'] = set_dict['DATABASES']

        loader.write(Path('config/server_settings.yaml'), for_save)
        msg_box.information(
            config_window,
            'OK',
            'Настройки успешно сохранены!')


if __name__ == '__main__':
    app = QApplication()
    ex = Main(None, None)
    app.exec_()
