# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = _("Cross plot properties")
    sig_start = Signal(str, str, str)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        text = _("Input Point")
        geom = ['Point']
        self.grabob = self.create_grabob(text, geom=geom)
        self.layout.addWidget(self.grabob)

        text = _("Property X")
        self.propX = self.create_combobox(text)
        self.layout.addWidget(self.propX)

        text = _("Property Y")
        self.propY = self.create_combobox(text)
        self.layout.addWidget(self.propY)

        action = self.create_action()
        self.layout.addWidget(action)

    def apply(self):
        point_name = self.grabob.lineedit.edit.text()
        px_name = self.propX.combobox.currentText()
        py_name = self.propY.combobox.currentText()
        self.sig_start.emit(point_name, px_name, py_name)

    def load_object(self):
        propList = list(self.object.prop.keys())
        self.propX.combobox.clear()
        self.propX.combobox.addItems(propList)
        self.propY.combobox.clear()
        self.propY.combobox.addItems(propList)

        if self.object.xplot_prop is None:
            prop_name = self.object.current_property
            index = propList.index(prop_name)
            self.propX.combobox.setCurrentIndex(index)
            self.propY.combobox.setCurrentIndex(index)
        else:
            px_name, py_name = self.object.xplot_prop
            idX = propList.index(px_name)
            idY = propList.index(py_name)
            self.propX.combobox.setCurrentIndex(idX)
            self.propY.combobox.setCurrentIndex(idY)

    def closeEvent(self, event):
        # TODO restore self.point.pg2d
        # what if did several point objects?
        print("closing dialog")
        super(Dialog, self).closeEvent(event)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
