# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'del_contact.ui'
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

class Ui_DelUserDialog(object):
    def setupUi(self, DelUserDialog):
        if DelUserDialog.objectName():
            DelUserDialog.setObjectName(u"DelUserDialog")
        DelUserDialog.resize(373, 120)
        DelUserDialog.setMinimumSize(QSize(373, 120))
        DelUserDialog.setMaximumSize(QSize(373, 120))
        self.DelContactLabel = QLabel(DelUserDialog)
        self.DelContactLabel.setObjectName(u"DelContactLabel")
        self.DelContactLabel.setGeometry(QRect(20, 10, 241, 16))
        self.cl_comboBox = QComboBox(DelUserDialog)
        self.cl_comboBox.setObjectName(u"cl_comboBox")
        self.cl_comboBox.setGeometry(QRect(20, 40, 211, 22))
        self.cl_comboBox.setMaxVisibleItems(50)
        self.buttonBox = QDialogButtonBox(DelUserDialog)
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

        self.retranslateUi(DelUserDialog)
        self.buttonBox.rejected.connect(DelUserDialog.reject)

        QMetaObject.connectSlotsByName(DelUserDialog)
    # setupUi

    def retranslateUi(self, DelUserDialog):
        DelUserDialog.setWindowTitle(QCoreApplication.translate("DelUserDialog", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u0430 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.DelContactLabel.setText(QCoreApplication.translate("DelUserDialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u043e\u043d\u0442\u0430\u043a\u0442 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430 \u0434\u043b\u044f \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f:", None))
    # retranslateUi

