# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from qtpy.QtWidgets import QLabel
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = _("Gsurface calculate normal")
    sig_start = Signal(str)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        text = _("Gsurface")
        geom = ['Gsurface']
        default = _("gsurfaces seperated by comma")
        self.grabob = self.create_grabob(text, default=default, geom=geom)
        self.layout.addWidget(self.grabob)

        lbl_disabled = QLabel(_("Not work yet"))
        self.layout.addWidget(lbl_disabled)

        action = self.create_action()
        self.layout.addWidget(action)

    def apply(self):
        gsurfNames = self.grabob.lineedit.edit.text()
        self.sig_start.emit(gsurfNames)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
