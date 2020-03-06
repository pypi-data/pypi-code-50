# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = _("Subset from property value range")
    HELP_BODY = _("If no limit on minimum value, leave it blank.<br>"
        "If no limit on maximum value, leave it blank.<br>")
    sig_start = Signal(str, str, float, float)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        text = _("Input Point")
        geom = ['Point']
        self.grabob = self.create_grabob(text, geom=geom)
        self.layout.addWidget(self.grabob)

        text = _("Property")
        self.prop = self.create_combobox(text)
        self.layout.addWidget(self.prop)

        text = _("Minimum value")
        self.vmin = self.create_lineedit(text)
        self.layout.addWidget(self.vmin)

        text = _("Maximum value")
        self.vmax = self.create_lineedit(text)
        self.layout.addWidget(self.vmax)

        action = self.create_action()
        self.layout.addWidget(action)

    def apply(self):
        point_name = self.grabob.lineedit.edit.text()
        prop_name = self.prop.combobox.currentText()
        vmin = self.vmin.edit.text().strip()
        vmin = None if len(vmin) == 0 else float(vmin)
        vmax = self.vmax.edit.text().strip()
        vmax = None if len(vmax) == 0 else float(vmax)
        self.sig_start.emit(point_name, prop_name, vmin, vmax)

    def load_object(self):
        propList = list(self.object.prop.keys())
        self.prop.combobox.clear()
        self.prop.combobox.addItems(propList)

        prop_name = self.object.current_property
        index = propList.index(prop_name)
        self.prop.combobox.setCurrentIndex(index)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
