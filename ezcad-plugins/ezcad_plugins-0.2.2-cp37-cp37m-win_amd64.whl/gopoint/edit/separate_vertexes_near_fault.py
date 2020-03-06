# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import os
from qtpy.QtCore import Signal
from qtpy.QtWidgets import QLabel, QRadioButton, QButtonGroup, QHBoxLayout
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = _("Separate vertexes near fault")
    sig_start = Signal(str, str, str, str, float, int)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.method = 'remove'
        self.setup_page()

    def setup_page(self):
        text = _("Input Point")
        geom = ['Point']
        self.grabob = self.create_grabob(text, geom=geom)
        self.layout.addWidget(self.grabob)

        text = _("Faults")
        default = _('point or tsurface separated by comma')
        geom = ['Point', 'Tsurface']
        self.faults = self.create_grabob(text, default=default, geom=geom)
        self.layout.addWidget(self.faults)

        text = _("Output Point")
        self.newPoint = self.create_lineedit(text)
        self.layout.addWidget(self.newPoint)

        text = _("Limit distance")
        self.distance = self.create_lineedit(text, default='1000')
        self.layout.addWidget(self.distance)

        lblMethod = QLabel(_('Separation method'))
        rbRemove = QRadioButton(_('remove'))
        rbKeep = QRadioButton(_('keep'))
        bgMethod = QButtonGroup()
        bgMethod.addButton(rbRemove)
        bgMethod.addButton(rbKeep)
        hbox = QHBoxLayout()
        hbox.addWidget(lblMethod)
        hbox.addWidget(rbRemove)
        hbox.addWidget(rbKeep)
        self.layout.addLayout(hbox)

        text = _("Number of threads")
        ncore = os.cpu_count()
        default = str(ncore)
        self.nthread = self.create_lineedit(text, default=default)
        self.layout.addWidget(self.nthread)

        action = self.create_action()
        self.layout.addWidget(action)

        rbRemove.toggled.connect(lambda: self.set_method(rbRemove))
        rbKeep.toggled.connect(lambda: self.set_method(rbKeep))
        rbRemove.setChecked(True)

    def set_method(self, rb):
        if rb.isChecked():
            if rb.text() == _('remove'):
                self.method = 'remove'
            elif rb.text() == _('keep'):
                self.method = 'keep'
            else:
                raise ValueError("Unknown value")

    def apply(self):
        point_name = self.grabob.lineedit.edit.text()
        faultNames = self.faults.lineedit.edit.text()
        object_name = self.newPoint.edit.text()
        method = self.method
        limitDistance = float(self.distance.edit.text())
        nthread = int(self.nthread.edit.text())
        self.sig_start.emit(point_name, faultNames, object_name, method,
                           limitDistance, nthread)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
