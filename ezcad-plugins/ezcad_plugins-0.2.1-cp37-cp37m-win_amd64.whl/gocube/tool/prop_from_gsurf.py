# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import os
from qtpy.QtCore import Signal
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = _("Create property from gsurface")
    sig_start = Signal(str, str, str, int)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        text = _("Input cube")
        geom = ['Cube']
        self.grabob = self.create_grabob(text, geom=geom)
        self.layout.addWidget(self.grabob)

        text = _("Input gsurfaces")
        default = _("gsurfaces seperated by comma")
        self.gsurfs = self.create_lineedit(text, default=default)
        self.layout.addWidget(self.gsurfs)

        text = _("Gsurface properties")
        default = _("properties seperated by comma")
        self.gsurfProps = self.create_lineedit(text, default=default)
        self.layout.addWidget(self.gsurfProps)

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
        # gsurfs do not cross.

        cube_name = self.grabob.lineedit.edit.text()
        gsurfNames = self.gsurfs.edit.text()
        prop_names = self.gsurfProps.edit.text()
        nthread = int(self.nthread.edit.text())
        self.sig_start.emit(cube_name, gsurfNames, prop_names, nthread)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
