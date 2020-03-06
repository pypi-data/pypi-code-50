# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = _("Select vertexes inside of polygon")
    sig_start = Signal(str, str)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        text = _("Input Point")
        geom = ['Point']
        self.grabPoint = self.create_grabob(text, geom=geom)
        self.layout.addWidget(self.grabPoint)

        text = _("Polygon")
        geom = ['Line']
        self.grabLine = self.create_grabob(text, geom=geom)
        self.layout.addWidget(self.grabLine)

        action = self.create_action()
        self.layout.addWidget(action)

    def apply(self):
        point_name = self.grabPoint.lineedit.edit.text()
        line_name = self.grabLine.lineedit.edit.text()
        self.sig_start.emit(point_name, line_name)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
