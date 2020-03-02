# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import os.path as osp
from qtpy.QtCore import Signal
from qtpy.QtWidgets import QTextBrowser, QPushButton, QHBoxLayout
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = _("Load JavaSeis dataset")
    sig_start = Signal(str, str)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        text = _("JavaSeis dataset")
        self.input = self.create_browsedir(text)
        self.layout.addWidget(self.input)

        text = _("Object name")
        self.object_name = self.create_lineedit(text)
        self.layout.addWidget(self.object_name)

        self.previewLines = self.create_lineedit("Preview lines", default='80')
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
        fileProp = osp.join(filename, 'FileProperties.xml')
        nlines = int(self.previewLines.edit.text())
        text = ""
        with open(fileProp, 'r') as f:
            for i in range(nlines):
                text += f.readline() # next(f)
        self.textBrowser.setText(text)

    def apply(self):
        fn = self.input.lineedit.edit.text()
        object_name = self.object_name.edit.text()
        self.sig_start.emit(fn, object_name)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
