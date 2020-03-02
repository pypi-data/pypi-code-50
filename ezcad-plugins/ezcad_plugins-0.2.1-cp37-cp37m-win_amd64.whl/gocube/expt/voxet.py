# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = _("Export cube to voxet file")
    sig_start = Signal(str, str, str)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        text = _("Output cube")
        geom = ['Cube']
        self.grabob = self.create_grabob(text, geom=geom)
        self.layout.addWidget(self.grabob)

        text = _("Properties")
        default = _("properties seperated by comma")
        self.properties = self.create_lineedit(text, default=default)
        self.layout.addWidget(self.properties)

        text = _("Voxet name")
        self.file = self.create_browsefile(text, new=True)
        self.layout.addWidget(self.file)

        action = self.create_action()
        self.layout.addWidget(action)

    def apply(self):
        cube_name = self.grabob.lineedit.edit.text()
        prop_names = self.properties.edit.text()
        file_name = self.file.lineedit.edit.text()
        self.sig_start.emit(cube_name, prop_names, file_name)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
