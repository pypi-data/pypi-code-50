# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""
GUI, from two coordinate systems: XY and IL/XL
"""

from qtpy.QtCore import Signal
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = _("New survey from two coordinate systems")
    sig_start = Signal(str, float, float, float, float, float, float, int, int,
                      int, int)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        # type of unit, drop down menu, English or Metric
        # Reference XY, how to use?

        text = _("Name")
        self.name = self.create_lineedit(text)
        
        text = _("X of origin")
        self.xOrigin = self.create_lineedit(text, wrap=False)
        text = _("Y of origin")
        self.yOrigin = self.create_lineedit(text, wrap=False)
        text = _("X of far end of first inline")
        self.xInlineEnd = self.create_lineedit(text, wrap=False)
        text = _("Y of far end of first inline")
        self.yInlineEnd = self.create_lineedit(text, wrap=False)
        text = _("X of far end of first crossline")
        self.xCrosslineEnd = self.create_lineedit(text, wrap=False)
        text = _("Y of far end of first crossline")
        self.yCrosslineEnd = self.create_lineedit(text, wrap=False)

        text = _("Minimum inline number")
        self.ilMin = self.create_lineedit(text, wrap=False)
        text = _("Maximum inline number")
        self.ilMax = self.create_lineedit(text, wrap=False)
        text = _("Minimum crossline number")
        self.xlMin = self.create_lineedit(text, wrap=False)
        text = _("Maximum crossline number")
        self.xlMax = self.create_lineedit(text, wrap=False)

        self.layout.addWidget(self.name)
        self.layout.addWidget(self.xOrigin)
        self.layout.addWidget(self.yOrigin)
        self.layout.addWidget(self.xInlineEnd)
        self.layout.addWidget(self.yInlineEnd)
        self.layout.addWidget(self.xCrosslineEnd)
        self.layout.addWidget(self.yCrosslineEnd)
        self.layout.addWidget(self.ilMin)
        self.layout.addWidget(self.ilMax)
        self.layout.addWidget(self.xlMin)
        self.layout.addWidget(self.xlMax)

        action = self.create_action()
        self.layout.addWidget(action)

    def apply(self):
        name = self.name.edit.text()
        xOrigin = float(self.xOrigin.edit.text())
        yOrigin = float(self.yOrigin.edit.text())
        xInlineEnd = float(self.xInlineEnd.edit.text())
        yInlineEnd = float(self.yInlineEnd.edit.text())
        xCrosslineEnd = float(self.xCrosslineEnd.edit.text())
        yCrosslineEnd = float(self.yCrosslineEnd.edit.text())
        ilMin = int(self.ilMin.edit.text())
        ilMax = int(self.ilMax.edit.text())
        xlMin = int(self.xlMin.edit.text())
        xlMax = int(self.xlMax.edit.text())
        self.sig_start.emit(name, xOrigin, yOrigin, xInlineEnd, yInlineEnd,
            xCrosslineEnd, yCrosslineEnd, ilMin, ilMax, xlMin, xlMax)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
