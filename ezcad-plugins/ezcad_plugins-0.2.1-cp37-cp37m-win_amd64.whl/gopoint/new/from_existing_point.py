# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = _("New point from existing point")
    sig_start = Signal(str, str, str, str, str)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        text = _("Input Point")
        geom = ['Point']
        self.grabob = self.create_grabob(text, geom=geom)
        self.layout.addWidget(self.grabob)

        text = _("Output Point")
        self.newPoint = self.create_lineedit(text)
        self.layout.addWidget(self.newPoint)

        text = _("Property X")
        self.propX = self.create_combobox(text)
        self.layout.addWidget(self.propX)

        text = _("Property Y")
        self.propY = self.create_combobox(text)
        self.layout.addWidget(self.propY)

        text = _("Property Z")
        self.propZ = self.create_combobox(text)
        self.layout.addWidget(self.propZ)

        action = self.create_action()
        self.layout.addWidget(action)

    def apply(self):
        point_name = self.grabob.lineedit.edit.text()
        px_name = self.propX.combobox.currentText()
        py_name = self.propY.combobox.currentText()
        pz_name = self.propZ.combobox.currentText()
        object_name = self.newPoint.edit.text()
        self.sig_start.emit(point_name, px_name, py_name, pz_name, object_name)

    def load_object(self):
        inputName = self.object.name
        outputName = inputName + "_new"
        self.newPoint.edit.setText(outputName)

        propList = list(self.object.prop.keys())
        propList.sort()
        self.propX.combobox.clear()
        self.propX.combobox.addItems(propList)
        self.propY.combobox.clear()
        self.propY.combobox.addItems(propList)
        self.propZ.combobox.clear()
        self.propZ.combobox.addItems(propList)

        prop_name = self.object.current_property
        index = propList.index(prop_name)
        self.propX.combobox.setCurrentIndex(index)
        self.propY.combobox.setCurrentIndex(index)
        self.propZ.combobox.setCurrentIndex(index)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
