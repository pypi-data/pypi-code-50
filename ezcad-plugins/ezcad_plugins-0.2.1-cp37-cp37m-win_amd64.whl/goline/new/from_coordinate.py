# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from qtpy.QtWidgets import QTextEdit, QLabel, QRadioButton, QButtonGroup, \
    QHBoxLayout
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = _("New line from coordinates")
    sig_start = Signal(str, str, str, str, str)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        text = _("New line")
        self.newLine = self.create_lineedit(text)
        self.layout.addWidget(self.newLine)

        text = _("Comment")
        self.comment = self.create_lineedit(text, default='#')
        self.layout.addWidget(self.comment)
        
        text = _("Delimiter")
        self.delimiter = self.create_lineedit(text, default='comma')
        self.layout.addWidget(self.delimiter)
        
        lblSystem = QLabel(_("Coordinate system"))
        rbXy = QRadioButton(_("X,Y"))
        rbLn = QRadioButton(_("ILNO,XLNO"))
        bgSystem = QButtonGroup()
        bgSystem.addButton(rbXy)
        bgSystem.addButton(rbLn)
        hbox = QHBoxLayout()
        hbox.addWidget(lblSystem)
        hbox.addWidget(rbXy)
        hbox.addWidget(rbLn)
        self.layout.addLayout(hbox)

        text = _("# Insert X, Y, Z, Connect")
        self.textEdit = QTextEdit(text, self)
        self.layout.addWidget(self.textEdit)

        action = self.create_action()
        self.layout.addWidget(action)

        rbXy.toggled.connect(lambda: self.set_method(rbXy))
        rbLn.toggled.connect(lambda: self.set_method(rbLn))
        rbXy.setChecked(True)
        
    def set_method(self, rb):
        if rb.isChecked():
            if rb.text() == _("X,Y"):
                self.method = 'xy'
            elif rb.text() == _("ILNO,XLNO"):
                self.method = 'ln'
            else:
                raise ValueError("unknown value {}".format(rb.text()))

    def apply(self):
        object_name = self.newLine.edit.text()
        comment = self.comment.edit.text()
        delimiter = self.delimiter.edit.text().lower()
        method = self.method
        text = self.textEdit.toPlainText()
        self.sig_start.emit(object_name, comment, delimiter, method, text)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
