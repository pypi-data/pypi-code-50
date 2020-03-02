# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import os
from qtpy.QtCore import Signal
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = _("Create mask by gsurface")
    sig_start = Signal(str, str, str, int)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        text = _("Input cube")
        geom = ['Cube']
        self.grabCube = self.create_grabob(text, geom=geom)
        self.layout.addWidget(self.grabCube)

        text = _("Input gsurface")
        geom = ['Gsurface']
        self.grabGsurf = self.create_grabob(text, geom=geom)
        self.layout.addWidget(self.grabGsurf)

        text = _("Cube property")
        self.cubeProp = self.create_lineedit(text)
        self.layout.addWidget(self.cubeProp)

        text = _("Number of threads")
        ncore = os.cpu_count()
        default = str(ncore)
        self.nthread = self.create_lineedit(text, default=default)
        self.layout.addWidget(self.nthread)

        action = self.create_action()
        self.layout.addWidget(action)

    def apply(self):

        # Assumptions
        # gsurf on the same spatial grid as cube, if not, map gsurf first.
        # gsurf covers the whole cube

        cube_name = self.grabCube.lineedit.edit.text()
        gsurfName = self.grabGsurf.lineedit.edit.text()
        prop_name = self.cubeProp.edit.text()
        nthread = int(self.nthread.edit.text())
        self.sig_start.emit(cube_name, gsurfName, prop_name, nthread)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()

if __name__ == '__main__':
    main()
