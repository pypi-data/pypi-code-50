# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainClientWindow(object):
    def setupUi(self, MainClientWindow):
        if MainClientWindow.objectName():
            MainClientWindow.setObjectName(u"MainClientWindow")
        MainClientWindow.resize(756, 534)
        MainClientWindow.setMinimumSize(QSize(756, 534))
        self.menu_exit = QAction(MainClientWindow)
        self.menu_exit.setObjectName(u"menu_exit")
        self.menu_add_contact = QAction(MainClientWindow)
        self.menu_add_contact.setObjectName(u"menu_add_contact")
        self.menu_del_contact = QAction(MainClientWindow)
        self.menu_del_contact.setObjectName(u"menu_del_contact")
        self.centralwidget = QWidget(MainClientWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_contacts = QLabel(self.centralwidget)
        self.label_contacts.setObjectName(u"label_contacts")
        self.label_contacts.setGeometry(QRect(10, 0, 101, 16))
        self.btn_add_contact = QPushButton(self.centralwidget)
        self.btn_add_contact.setObjectName(u"btn_add_contact")
        self.btn_add_contact.setGeometry(QRect(10, 450, 121, 31))
        self.btn_remove_contact = QPushButton(self.centralwidget)
        self.btn_remove_contact.setObjectName(u"btn_remove_contact")
        self.btn_remove_contact.setGeometry(QRect(140, 450, 121, 31))
        self.label_history = QLabel(self.centralwidget)
        self.label_history.setObjectName(u"label_history")
        self.label_history.setGeometry(QRect(300, 0, 391, 21))
        self.text_message = QTextEdit(self.centralwidget)
        self.text_message.setObjectName(u"text_message")
        self.text_message.setGeometry(QRect(300, 360, 441, 71))
        self.label_new_message = QLabel(self.centralwidget)
        self.label_new_message.setObjectName(u"label_new_message")
        self.label_new_message.setGeometry(QRect(300, 330, 171, 16))
        self.list_contacts = QListView(self.centralwidget)
        self.list_contacts.setObjectName(u"list_contacts")
        self.list_contacts.setGeometry(QRect(10, 20, 251, 411))
        self.list_messages = QListView(self.centralwidget)
        self.list_messages.setObjectName(u"list_messages")
        self.list_messages.setGeometry(QRect(300, 20, 441, 301))
        self.btn_send = QPushButton(self.centralwidget)
        self.btn_send.setObjectName(u"btn_send")
        self.btn_send.setGeometry(QRect(610, 450, 131, 31))
        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setGeometry(QRect(460, 450, 131, 31))
        MainClientWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainClientWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 756, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainClientWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainClientWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainClientWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.menu_exit)
        self.menu_2.addAction(self.menu_add_contact)
        self.menu_2.addAction(self.menu_del_contact)
        self.menu_2.addSeparator()

        self.retranslateUi(MainClientWindow)
        self.btn_clear.clicked.connect(self.text_message.clear)

        QMetaObject.connectSlotsByName(MainClientWindow)
    # setupUi

    def retranslateUi(self, MainClientWindow):
        MainClientWindow.setWindowTitle(QCoreApplication.translate("MainClientWindow", u"\u0427\u0430\u0442 \u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 alpha release", None))
        self.menu_exit.setText(QCoreApplication.translate("MainClientWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.menu_add_contact.setText(QCoreApplication.translate("MainClientWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u043e\u043d\u0442\u0430\u043a\u0442", None))
        self.menu_del_contact.setText(QCoreApplication.translate("MainClientWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043a\u043e\u043d\u0442\u0430\u043a\u0442", None))
        self.label_contacts.setText(QCoreApplication.translate("MainClientWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043e\u0432:", None))
        self.btn_add_contact.setText(QCoreApplication.translate("MainClientWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u043e\u043d\u0442\u0430\u043a\u0442", None))
        self.btn_remove_contact.setText(QCoreApplication.translate("MainClientWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043a\u043e\u043d\u0442\u0430\u043a\u0442", None))
        self.label_history.setText(QCoreApplication.translate("MainClientWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0439:", None))
        self.label_new_message.setText(QCoreApplication.translate("MainClientWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u0432\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435:", None))
        self.btn_send.setText(QCoreApplication.translate("MainClientWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        self.btn_clear.setText(QCoreApplication.translate("MainClientWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043f\u043e\u043b\u0435", None))
        self.menu.setTitle(QCoreApplication.translate("MainClientWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainClientWindow", u"\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b", None))
    # retranslateUi

