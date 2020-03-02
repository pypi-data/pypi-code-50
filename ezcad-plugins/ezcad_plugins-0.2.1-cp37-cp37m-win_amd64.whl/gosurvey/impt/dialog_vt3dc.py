# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from qtpy.QtWidgets import QTextBrowser, QPushButton, QHBoxLayout
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog
from ezcad.utils.envars import FILTER_ALL_FILES


class Dialog(EasyDialog):
    NAME = _("Load VT3DC file")
    sig_start = Signal(str, str)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        filters = "DC files (*.dc)" + FILTER_ALL_FILES
        self.input = self.create_browsefile(_("VT3DC file"), filters=filters)
        self.layout.addWidget(self.input)

        self.object_name = self.create_lineedit("Survey name")
        self.layout.addWidget(self.object_name)

        self.preview_lines = self.create_lineedit("Preview lines",
                                                  default='50')
        load = QPushButton(_('Load'))
        load.clicked.connect(self.load_lines)
        box = QHBoxLayout()
        box.addWidget(self.preview_lines)
        box.addWidget(load)
        self.layout.addLayout(box)

        self.text_browser = QTextBrowser(self)
        self.text_browser.setFontFamily("monospace")
        self.layout.addWidget(self.text_browser)

        action = self.create_action()
        self.layout.addWidget(action)

    def load_lines(self):
        filename = self.input.lineedit.edit.text()
        n = int(self.preview_lines.edit.text())
        text = ""
        with open(filename, 'r') as f:
            for i in range(n):
                text += f.readline()  # next(f)
        self.text_browser.setText(text)

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
