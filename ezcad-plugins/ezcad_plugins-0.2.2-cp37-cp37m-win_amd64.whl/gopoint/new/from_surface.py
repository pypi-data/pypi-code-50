# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = _("New point from surface vertexes")
    sig_start = Signal(str, str)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        text = _("Input surface")
        default = _("tsurface or gsurface")
        geom = ['Tsurface', 'Gsurface']
        self.grabob = self.create_grabob(text, default=default, geom=geom)
        self.layout.addWidget(self.grabob)

        text = _("Output Point")
        self.newPoint = self.create_lineedit(text)
        self.layout.addWidget(self.newPoint)

        # TODO checkbox with and w/o properties

        action = self.create_action()
        self.layout.addWidget(action)

    def apply(self):
        surfName = self.grabob.lineedit.edit.text()
        object_name = self.newPoint.edit.text()
        self.sig_start.emit(surfName, object_name)

    def load_object(self):
        point_name = self.object.name + '_pt'
        self.newPoint.edit.setText(point_name)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
