# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from qtpy.QtWidgets import QLabel, QRadioButton, QButtonGroup, QHBoxLayout
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = _("Create Line from Point")
    HELP_BODY = _("For example, closed line is for AOI polygon, and "
        "open line is for arbitrary line through key wells.")
    sig_start = Signal(str, str, bool)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        text = _("Input Point")
        geom = ['Point']
        self.grabob = self.create_grabob(text, geom=geom)
        self.layout.addWidget(self.grabob)

        text = _("Output Line")
        self.line = self.create_lineedit(text)
        self.layout.addWidget(self.line)

        lblClosed = QLabel(_("Closed"))
        rbYes = QRadioButton(_("Yes"))
        rbNo = QRadioButton(_("No"))
        bgClosed = QButtonGroup()
        bgClosed.addButton(rbYes)
        bgClosed.addButton(rbNo)
        hbox = QHBoxLayout()
        hbox.addWidget(lblClosed)
        hbox.addWidget(rbYes)
        hbox.addWidget(rbNo)
        self.layout.addLayout(hbox)

        action = self.create_action()
        self.layout.addWidget(action)

        rbYes.toggled.connect(lambda: self.set_method(rbYes))
        rbNo.toggled.connect(lambda: self.set_method(rbNo))
        rbNo.setChecked(True)

    def set_method(self, rb):
        if rb.isChecked():
            if rb.text() == _("Yes"):
                self.isClosed = True
            elif rb.text() == _("No"):
                self.isClosed = False
            else:
                raise ValueError("unknown value {}".format(rb.text()))

    def load_object(self):
        line_name = self.object.name + '_ln'
        self.line.edit.setText(line_name)

    def apply(self):
        point_name = self.grabob.lineedit.edit.text()
        line_name = self.line.edit.text()
        isClosed = self.isClosed
        self.sig_start.emit(point_name, line_name, isClosed)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
