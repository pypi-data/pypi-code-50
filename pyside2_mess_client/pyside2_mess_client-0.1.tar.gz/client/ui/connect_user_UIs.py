# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connect_user.ui'
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

class Ui_ConnectionDialog(object):
    def setupUi(self, ConnectionDialog):
        if ConnectionDialog.objectName():
            ConnectionDialog.setObjectName(u"ConnectionDialog")
        ConnectionDialog.resize(359, 149)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConnectionDialog.sizePolicy().hasHeightForWidth())
        ConnectionDialog.setSizePolicy(sizePolicy)
        ConnectionDialog.setMaximumSize(QSize(370, 160))
        icon = QIcon()
        icon.addFile(u"ico/user_add.ico", QSize(), QIcon.Normal, QIcon.Off)
        ConnectionDialog.setWindowIcon(icon)
        self.verticalLayout_3 = QVBoxLayout(ConnectionDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.vLayout_0 = QVBoxLayout()
        self.vLayout_0.setObjectName(u"vLayout_0")
        self.vLayout_1 = QVBoxLayout()
        self.vLayout_1.setSpacing(6)
        self.vLayout_1.setObjectName(u"vLayout_1")
        self.vLayout_1.setContentsMargins(0, 0, 0, 0)
        self.label_name = QLabel(ConnectionDialog)
        self.label_name.setObjectName(u"label_name")
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)

        self.vLayout_1.addWidget(self.label_name)

        self.name_ledit = QLineEdit(ConnectionDialog)
        self.name_ledit.setObjectName(u"name_ledit")

        self.vLayout_1.addWidget(self.name_ledit)


        self.vLayout_0.addLayout(self.vLayout_1)

        self.vLayout_2 = QVBoxLayout()
        self.vLayout_2.setObjectName(u"vLayout_2")
        self.label_password = QLabel(ConnectionDialog)
        self.label_password.setObjectName(u"label_password")
        sizePolicy.setHeightForWidth(self.label_password.sizePolicy().hasHeightForWidth())
        self.label_password.setSizePolicy(sizePolicy)

        self.vLayout_2.addWidget(self.label_password)

        self.pass_ledit = QLineEdit(ConnectionDialog)
        self.pass_ledit.setObjectName(u"pass_ledit")
        self.pass_ledit.setEchoMode(QLineEdit.Password)

        self.vLayout_2.addWidget(self.pass_ledit)


        self.vLayout_0.addLayout(self.vLayout_2)


        self.verticalLayout_3.addLayout(self.vLayout_0)

        self.hLayout_0 = QHBoxLayout()
        self.hLayout_0.setSpacing(6)
        self.hLayout_0.setObjectName(u"hLayout_0")
        self.hLayout_0.setContentsMargins(0, 0, 0, 0)
        self.spacer1 = QSpacerItem(131, 31, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hLayout_0.addItem(self.spacer1)

        self.okButton = QPushButton(ConnectionDialog)
        self.okButton.setObjectName(u"okButton")

        self.hLayout_0.addWidget(self.okButton)

        self.cancelButton = QPushButton(ConnectionDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.hLayout_0.addWidget(self.cancelButton)

        self.spacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hLayout_0.addItem(self.spacer2)


        self.verticalLayout_3.addLayout(self.hLayout_0)


        self.retranslateUi(ConnectionDialog)
        # self.okButton.clicked.connect(ConnectionDialog.accept)
        # self.cancelButton.clicked.connect(ConnectionDialog.reject)

        QMetaObject.connectSlotsByName(ConnectionDialog)
    # setupUi

    def retranslateUi(self, ConnectionDialog):
        ConnectionDialog.setWindowTitle(QCoreApplication.translate("ConnectionDialog", u"Connection", None))
        self.label_name.setText(QCoreApplication.translate("ConnectionDialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f:", None))
        self.label_password.setText(QCoreApplication.translate("ConnectionDialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.okButton.setText(QCoreApplication.translate("ConnectionDialog", u"OK", None))
        self.cancelButton.setText(QCoreApplication.translate("ConnectionDialog", u"Cancel", None))
    # retranslateUi

