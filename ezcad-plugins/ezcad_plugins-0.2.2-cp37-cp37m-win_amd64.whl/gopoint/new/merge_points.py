# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = _("New point from merging points")
    sig_start = Signal(str, str)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        text = _("Input Points")
        default = _("points separated by comma")
        self.inputPoints = self.create_lineedit(text, default=default)
        self.layout.addWidget(self.inputPoints)

        text = _("Output Point")
        self.newPoint = self.create_lineedit(text)
        self.layout.addWidget(self.newPoint)

        action = self.create_action()
        self.layout.addWidget(action)

    def apply(self):
        inputNames = self.inputPoints.edit.text()
        object_name = self.newPoint.edit.text()
        self.sig_start.emit(inputNames, object_name)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
