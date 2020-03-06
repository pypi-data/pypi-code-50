# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from qtpy.QtWidgets import QTextBrowser, QPushButton, QHBoxLayout
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog
from ezcad.utils.envars import FILTER_ALL_FILES


class Dialog(EasyDialog):
    NAME = _("Load Gocad pline file")
    sig_start = Signal(str, str, str)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        filters = "PLine files (*.pl)" + FILTER_ALL_FILES
        self.input = self.create_browsefile(_("Gocad pline file"),
                                            filters=filters)
        self.layout.addWidget(self.input)

        default = "column number, name; default 3,X;4,Y;5,Z"
        self.columns = self.create_lineedit("Columns", default=default)
        self.columns.setEnabled(False)
        self.layout.addWidget(self.columns)

        self.object_name = self.create_lineedit("Object name")
        self.layout.addWidget(self.object_name)

        self.previewLines = self.create_lineedit("Preview lines", default='50')
        btnLoad = QPushButton(_('Load'))
        btnLoad.clicked.connect(self.load_lines)
        hbox = QHBoxLayout()
        hbox.addWidget(self.previewLines)
        hbox.addWidget(btnLoad)
        self.layout.addLayout(hbox)

        self.textBrowser = QTextBrowser(self)
        self.textBrowser.setFontFamily("monospace")
        self.layout.addWidget(self.textBrowser)

        action = self.create_action()
        self.layout.addWidget(action)

    def load_lines(self):
        filename = self.input.lineedit.edit.text()
        nlines = int(self.previewLines.edit.text())
        text = ""
        with open(filename, 'r') as f:
            for i in range(nlines):
                text += f.readline() # next(f)
        self.textBrowser.setText(text)

    def apply(self):
        fn = self.input.lineedit.edit.text()
        # columns = self.columns.edit.text()
        columns = "3,X;4,Y;5,Z"
        object_name = self.object_name.edit.text()
        self.sig_start.emit(fn, columns, object_name)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
