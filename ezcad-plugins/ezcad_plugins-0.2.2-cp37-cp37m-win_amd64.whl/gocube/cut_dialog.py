# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = _("Cube section by arbitrary line")
    sig_start = Signal(str, str, str)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        text = _("Input cube")
        geom = ['Cube']
        self.grabCube = self.create_grabob(text, geom=geom)
        self.layout.addWidget(self.grabCube)

        text = _("Input line")
        geom = ['Line']
        self.grabLine = self.create_grabob(text, geom=geom)
        self.layout.addWidget(self.grabLine)

        text = _("Output section")
        self.section = self.create_lineedit(text)
        self.layout.addWidget(self.section)

        action = self.create_action()
        self.layout.addWidget(action)

    def apply(self):
        cube_name = self.grabCube.lineedit.edit.text()
        line_name = self.grabLine.lineedit.edit.text()
        section_name = self.section.edit.text()
        self.sig_start.emit(cube_name, line_name, section_name)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
