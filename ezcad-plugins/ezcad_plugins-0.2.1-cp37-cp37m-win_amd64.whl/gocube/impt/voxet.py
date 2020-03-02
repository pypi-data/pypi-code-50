# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from qtpy.QtWidgets import QTextBrowser, QPushButton, QHBoxLayout
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog
from ezcad.utils.envars import FILTER_ALL_FILES


class Dialog(EasyDialog):
    NAME = _("Load Gocad voext")
    sig_start = Signal(str, str, str)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        filters = "VO files (*.vo)" + FILTER_ALL_FILES
        self.input = self.create_browsefile(_("Voxet file"), filters=filters)
        self.layout.addWidget(self.input)

        text = _("Properties")
        self.prop_names = self.create_lineedit(text, default='DEFAULT')
        self.layout.addWidget(self.prop_names)
        
        text = _("Object name")
        self.object_name = self.create_lineedit(text)
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
        prop_names = self.prop_names.edit.text()
        object_name = self.object_name.edit.text()
        # survey = self.treebase.main.survey
        # Load data in the GUI thread, then call the parent treebase.
        # progress_bar = self.treebase.main.progress_bar
        # dob = load_cube_voxet(fn, survey, object_name, progress_bar)
        # self.treebase.add_item(dob)
        # Cleaner using signal-slot, the dialog GUI do clear simple job.
        self.sig_start.emit(fn, prop_names, object_name)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
