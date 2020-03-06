# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = _("Create Tsurf from Points")
    sig_start = Signal(str, str)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        text = _("Input Point")
        geom = ['Point']
        self.grabob = self.create_grabob(text, geom=geom)
        self.layout.addWidget(self.grabob)

        text = _("Output Tsurf")
        self.tsurf = self.create_lineedit(text)
        self.layout.addWidget(self.tsurf)

        action = self.create_action()
        self.layout.addWidget(action)

    def load_object(self):
        tsurfName = self.object.name + '_ts'
        self.tsurf.edit.setText(tsurfName)

    def apply(self):
        point_name = self.grabob.lineedit.edit.text()
        tsurfName = self.tsurf.edit.text()
        self.sig_start.emit(point_name, tsurfName)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
