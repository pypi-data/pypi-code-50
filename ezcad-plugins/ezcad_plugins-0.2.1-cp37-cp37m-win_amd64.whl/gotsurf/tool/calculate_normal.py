# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = _("Tsurface calculate normal")
    sig_start = Signal(str)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        text = _("Tsurface")
        geom = ['Tsurface']
        default = _("tsurfaces separated by comma")
        self.grabob = self.create_grabob(text, default=default, geom=geom)
        self.layout.addWidget(self.grabob)

        action = self.create_action()
        self.layout.addWidget(action)

    def apply(self):
        tsurfNames = self.grabob.lineedit.edit.text()
        self.sig_start.emit(tsurfNames)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
