# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_contact.ui'
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

class Ui_AddUserDialog(object):
    def setupUi(self, AddUserDialog):
        if AddUserDialog.objectName():
            AddUserDialog.setObjectName(u"AddUserDialog")
        AddUserDialog.resize(380, 125)
        AddUserDialog.setMinimumSize(QSize(380, 125))
        AddUserDialog.setMaximumSize(QSize(380, 125))
        self.buttonBox = QDialogButtonBox(AddUserDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setEnabled(True)
        self.buttonBox.setGeometry(QRect(260, 10, 101, 91))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMinimumSize(QSize(0, 0))
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.add_user_label = QLabel(AddUserDialog)
        self.add_user_label.setObjectName(u"add_user_label")
        self.add_user_label.setGeometry(QRect(30, 10, 181, 20))
        self.add_user_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.cl_comboBox = QComboBox(AddUserDialog)
        self.cl_comboBox.setObjectName(u"cl_comboBox")
        self.cl_comboBox.setGeometry(QRect(20, 40, 211, 22))
        self.cl_comboBox.setMaxVisibleItems(50)
        self.btn_refresh = QPushButton(AddUserDialog)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setGeometry(QRect(70, 80, 121, 31))

        self.retranslateUi(AddUserDialog)
        self.buttonBox.rejected.connect(AddUserDialog.reject)

        QMetaObject.connectSlotsByName(AddUserDialog)
    # setupUi

    def retranslateUi(self, AddUserDialog):
        AddUserDialog.setWindowTitle(QCoreApplication.translate("AddUserDialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0432 \u0441\u043f\u0438\u0441\u043e\u043a \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043e\u0432", None))
        self.add_user_label.setText(QCoreApplication.translate("AddUserDialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u043e\u043d\u0442\u0430\u043a\u0442 \u0434\u043b\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.btn_refresh.setText(QCoreApplication.translate("AddUserDialog", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a", None))
    # retranslateUi

