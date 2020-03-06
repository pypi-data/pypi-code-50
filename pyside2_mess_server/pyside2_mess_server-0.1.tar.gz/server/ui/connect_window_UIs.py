# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connect_window.ui'
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

class Ui_ConnectDialog(object):
    def setupUi(self, ConnectDialog):
        if ConnectDialog.objectName():
            ConnectDialog.setObjectName(u"ConnectDialog")
        ConnectDialog.resize(400, 273)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConnectDialog.sizePolicy().hasHeightForWidth())
        ConnectDialog.setSizePolicy(sizePolicy)
        ConnectDialog.setMinimumSize(QSize(400, 200))
        ConnectDialog.setMaximumSize(QSize(500, 300))
        icon = QIcon()
        icon.addFile(u"ui/icons/db.png", QSize(), QIcon.Normal, QIcon.Off)
        ConnectDialog.setWindowIcon(icon)
        ConnectDialog.setSizeGripEnabled(True)
        ConnectDialog.setModal(True)
        self.gridLayout = QGridLayout(ConnectDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.hlLayout_1 = QHBoxLayout()
        self.hlLayout_1.setObjectName(u"hlLayout_1")
        self.db_name_lbl = QLabel(ConnectDialog)
        self.db_name_lbl.setObjectName(u"db_name_lbl")
        self.db_name_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.hlLayout_1.addWidget(self.db_name_lbl)

        self.db_name_lne = QLineEdit(ConnectDialog)
        self.db_name_lne.setObjectName(u"db_name_lne")

        self.hlLayout_1.addWidget(self.db_name_lne)

        self.hlLayout_1.setStretch(0, 2)
        self.hlLayout_1.setStretch(1, 3)

        self.gridLayout.addLayout(self.hlLayout_1, 1, 0, 1, 1)

        self.vlLayout_1 = QVBoxLayout()
        self.vlLayout_1.setSpacing(0)
        self.vlLayout_1.setObjectName(u"vlLayout_1")
        self.db_path_lbl = QLabel(ConnectDialog)
        self.db_path_lbl.setObjectName(u"db_path_lbl")

        self.vlLayout_1.addWidget(self.db_path_lbl)

        self.hlLayout_2 = QHBoxLayout()
        self.hlLayout_2.setObjectName(u"hlLayout_2")
        self.db_path_lne = QLineEdit(ConnectDialog)
        self.db_path_lne.setObjectName(u"db_path_lne")

        self.hlLayout_2.addWidget(self.db_path_lne)

        self.db_path_btn = QPushButton(ConnectDialog)
        self.db_path_btn.setObjectName(u"db_path_btn")

        self.hlLayout_2.addWidget(self.db_path_btn)

        self.hlLayout_2.setStretch(0, 3)
        self.hlLayout_2.setStretch(1, 1)

        self.vlLayout_1.addLayout(self.hlLayout_2)


        self.gridLayout.addLayout(self.vlLayout_1, 0, 0, 1, 1)

        self.vlLayout_2 = QVBoxLayout()
        self.vlLayout_2.setSpacing(0)
        self.vlLayout_2.setObjectName(u"vlLayout_2")
        self.hlLayout_3 = QHBoxLayout()
        self.hlLayout_3.setSpacing(6)
        self.hlLayout_3.setObjectName(u"hlLayout_3")
        self.ip_lbl = QLabel(ConnectDialog)
        self.ip_lbl.setObjectName(u"ip_lbl")

        self.hlLayout_3.addWidget(self.ip_lbl)

        self.ip_lne = QLineEdit(ConnectDialog)
        self.ip_lne.setObjectName(u"ip_lne")
        self.ip_lne.setInputMask(u"000.000.000.000;_")

        self.hlLayout_3.addWidget(self.ip_lne)

        self.hlLayout_3.setStretch(0, 2)
        self.hlLayout_3.setStretch(1, 3)

        self.vlLayout_2.addLayout(self.hlLayout_3)

        self.info_lbl = QLabel(ConnectDialog)
        self.info_lbl.setObjectName(u"info_lbl")

        self.vlLayout_2.addWidget(self.info_lbl)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlLayout_2.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.vlLayout_2, 3, 0, 1, 1)

        self.btn_box = QDialogButtonBox(ConnectDialog)
        self.btn_box.setObjectName(u"btn_box")
        self.btn_box.setOrientation(Qt.Horizontal)
        self.btn_box.setStandardButtons(QDialogButtonBox.Close|QDialogButtonBox.Save)
        self.btn_box.setCenterButtons(False)

        self.gridLayout.addWidget(self.btn_box, 4, 0, 1, 1)

        self.hlLayout_4 = QHBoxLayout()
        self.hlLayout_4.setObjectName(u"hlLayout_4")
        self.port_lbl = QLabel(ConnectDialog)
        self.port_lbl.setObjectName(u"port_lbl")

        self.hlLayout_4.addWidget(self.port_lbl)

        self.port_lne = QLineEdit(ConnectDialog)
        self.port_lne.setObjectName(u"port_lne")

        self.hlLayout_4.addWidget(self.port_lne)

        self.hlLayout_4.setStretch(0, 2)
        self.hlLayout_4.setStretch(1, 3)

        self.gridLayout.addLayout(self.hlLayout_4, 2, 0, 1, 1)

        QWidget.setTabOrder(self.db_path_lne, self.db_path_btn)
        QWidget.setTabOrder(self.db_path_btn, self.db_name_lne)
        QWidget.setTabOrder(self.db_name_lne, self.ip_lne)

        self.retranslateUi(ConnectDialog)
        self.btn_box.accepted.connect(ConnectDialog.accept)
        self.btn_box.rejected.connect(ConnectDialog.reject)

        QMetaObject.connectSlotsByName(ConnectDialog)
    # setupUi

    def retranslateUi(self, ConnectDialog):
        ConnectDialog.setWindowTitle(QCoreApplication.translate("ConnectDialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0435\u0440\u0432\u0435\u0440\u0430", None))
        self.db_name_lbl.setText(QCoreApplication.translate("ConnectDialog", u"\u0418\u043c\u044f \u0444\u0430\u0439\u043b\u0430 \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445:", None))
        self.db_name_lne.setPlaceholderText(QCoreApplication.translate("ConnectDialog", u"\u0418\u043c\u044f \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.db_path_lbl.setText(QCoreApplication.translate("ConnectDialog", u"\u041f\u0443\u0442\u044c \u0434\u043e \u0444\u0430\u0439\u043b\u0430 \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445:", None))
        self.db_path_lne.setPlaceholderText(QCoreApplication.translate("ConnectDialog", u"\u041f\u0443\u0442\u044c \u043d\u0430 \u0434\u0438\u0441\u043a\u0435 \u043a \u0431\u0430\u0437\u0435 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.db_path_btn.setText(QCoreApplication.translate("ConnectDialog", u"\u041e\u0431\u0437\u043e\u0440...", None))
        self.ip_lbl.setText(QCoreApplication.translate("ConnectDialog", u"\u0421 \u043a\u0430\u043a\u043e\u0433\u043e IP \u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u043c \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u044f", None))
        self.info_lbl.setText(QCoreApplication.translate("ConnectDialog", u" \u043e\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u044d\u0442\u043e \u043f\u043e\u043b\u0435 \u043f\u0443\u0441\u0442\u044b\u043c, \u0447\u0442\u043e\u0431\u044b\n"
" \u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0442\u044c \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u044f \u0441 \u043b\u044e\u0431\u044b\u0445 \u0430\u0434\u0440\u0435\u0441\u043e\u0432.", None))
        self.port_lbl.setText(QCoreApplication.translate("ConnectDialog", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u043e\u0440\u0442\u0430 \u0434\u043b\u044f \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u0439:", None))
        self.port_lne.setPlaceholderText(QCoreApplication.translate("ConnectDialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u043e\u0440\u0442", None))
    # retranslateUi

