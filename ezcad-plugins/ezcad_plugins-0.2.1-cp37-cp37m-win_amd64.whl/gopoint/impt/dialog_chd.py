# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from qtpy.QtWidgets import QTextBrowser, QPushButton, QHBoxLayout
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog
from ezcad.utils.envars import FILTER_ALL_FILES


class Dialog(EasyDialog):
    NAME = _("Load SeisSpace Header Dump file")
    HELP_BODY = _("Read the text file from SeisSpace tool Chv Header Dump.<br>"
        "CHV_HDR_DUMP $Revision: 20070726.0 $<br>"
        "Select header list mode: List<br>")
    sig_start = Signal(str, str, int)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        filters = "TXT files (*.txt)" + FILTER_ALL_FILES
        self.input = self.create_browsefile(_("TXT file"), filters=filters)
        self.layout.addWidget(self.input)

        text = _("Object name")
        self.object_name = self.create_lineedit(text)
        self.layout.addWidget(self.object_name)

        self.preview_lines = self.create_lineedit("Preview lines", default='50')
        self.skip_lines = self.create_lineedit("Skip lines", default='-1')
        btnLoad = QPushButton(_('Load'))
        btnLoad.clicked.connect(self.load_lines)
        hbox = QHBoxLayout()
        hbox.addWidget(self.preview_lines)
        hbox.addWidget(btnLoad)
        hbox.addWidget(self.skip_lines)
        self.layout.addLayout(hbox)

        self.textBrowser = QTextBrowser(self)
        self.textBrowser.setFontFamily("monospace")
        self.layout.addWidget(self.textBrowser)

        action = self.create_action()
        self.layout.addWidget(action)

    def load_lines(self):
        filename = self.input.lineedit.edit.text()
        nlines = int(self.preview_lines.edit.text())
        text = ""
        with open(filename, mode='r', encoding='utf-8', errors='ignore') as f:
            for i in range(nlines):
                text += f.readline() # next(f)
        self.textBrowser.setText(text)

    def apply(self):
        fn = self.input.lineedit.edit.text()
        object_name = self.object_name.edit.text()
        skip_lines = int(self.skip_lines.edit.text())
        self.sig_start.emit(fn, object_name, skip_lines)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
