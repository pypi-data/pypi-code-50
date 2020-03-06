# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from qtpy.QtWidgets import QTextEdit, QLabel
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = _("Export ASCII file")
    sig_start = Signal(str, str, list, list, str, str)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        self.output = self.create_browsefile(_("File"), new=True)
        self.layout.addWidget(self.output)

        text = _("Object")
        geom = ['Point']
        self.grabob = self.create_grabob(text, geom=geom)
        self.layout.addWidget(self.grabob)

        text = _("Properties")
        self.props = self.create_lineedit(text, default='X, Y, Z')
        self.layout.addWidget(self.props)

        text = _("Formats")
        self.formats = self.create_lineedit(text, default='%.18e')
        self.layout.addWidget(self.formats)

        text = _("Delimiter")
        self.delim = self.create_lineedit(text, default='comma')
        self.layout.addWidget(self.delim)

        lbHeader = QLabel(_("Header lines"))
        self.layout.addWidget(lbHeader)
        self.textEdit = QTextEdit(self)
        self.textEdit.setFontFamily("monospace")
        self.layout.addWidget(self.textEdit)

        action = self.create_action()
        self.layout.addWidget(action)

    def apply(self):
        fn = self.output.lineedit.edit.text()
        object_name = self.grabob.lineedit.edit.text()
        props = self.props.edit.text()
        props = props.split(',')
        props = [p.strip() for p in props]
        formats = self.formats.edit.text()
        formats = formats.split(',')
        formats = [f.strip() for f in formats]
        delimiter = self.delim.edit.text().lower()
        headers = self.textEdit.toPlainText()
        self.sig_start.emit(fn, object_name, props, formats, delimiter, headers)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
