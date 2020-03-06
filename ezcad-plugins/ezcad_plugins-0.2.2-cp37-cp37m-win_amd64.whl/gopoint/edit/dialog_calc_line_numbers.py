# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = _("Calculate line numbers")
    HELP_BODY = _("This is applicable to vertex-based objects.<br>")
    sig_start = Signal(str, str, str)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        text = _("Object")
        geom = ['Point', 'Line', 'Tsurface', 'Gsurface']
        self.leObject = self.create_grabob(text, geom=geom)
        self.layout.addWidget(self.leObject)

        text = _("Property I")
        default = _("ILINE_NO")
        self.propi = self.create_lineedit(text, default=default)
        self.layout.addWidget(self.propi)

        text = _("Property J")
        default = _("XLINE_NO")
        self.propj = self.create_lineedit(text, default=default)
        self.layout.addWidget(self.propj)

        action = self.create_action()
        self.layout.addWidget(action)

    def apply(self):
        object_name = self.leObject.lineedit.edit.text()
        piName = self.propi.edit.text()
        pjName = self.propj.edit.text()
        self.sig_start.emit(object_name, piName, pjName)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
