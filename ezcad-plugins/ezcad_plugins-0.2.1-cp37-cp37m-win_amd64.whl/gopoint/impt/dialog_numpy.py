# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from qtpy.QtWidgets import QTextBrowser, QPushButton, QHBoxLayout
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = _("Numpy load text file")
    sig_start = Signal(str, str, str, str, str)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        self.input = self.create_browsefile(_("TXT file"))
        self.layout.addWidget(self.input)

        self.fileComment = self.create_lineedit("Comment", default='#')
        self.layout.addWidget(self.fileComment)

        self.fileDelimiter = self.create_lineedit("Delimiter",
                                                  default='comma')
        self.layout.addWidget(self.fileDelimiter)

        self.columnNames = self.create_lineedit("Column names",
                                                default='X,Y,Z')
        self.layout.addWidget(self.columnNames)

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
        comment = self.fileComment.edit.text()
        delimiter = self.fileDelimiter.edit.text().lower()
        props = self.columnNames.edit.text()
        object_name = self.object_name.edit.text()
        self.sig_start.emit(fn, comment, delimiter, props, object_name)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
