# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from qtpy.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, \
    QRadioButton, QButtonGroup, QVBoxLayout, QHBoxLayout, QMessageBox
from ezcad.config.base import _
from ezcad.utils.logger import logger
from ..line import Line


class HandPick(QDialog):
    NAME = "New line by hand picking"
    sig_start = Signal()
    sigClose = Signal()
    sigAddLine = Signal(object, bool)

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.currentRow = 0
        self.setup_page()

    def setup_page(self):
        self.setWindowTitle(_(self.NAME))
        vbox = QVBoxLayout()

        lbl_line = QLabel(_("New line"))
        self.le_line = QLineEdit()
        hbox = QHBoxLayout()
        hbox.addWidget(lbl_line)
        hbox.addWidget(self.le_line)
        vbox.addLayout(hbox)

        lblMethod = QLabel(_("Head tail"))
        self.rbOpen = QRadioButton(_("Open"))
        self.rbClosed = QRadioButton(_("Closed"))
        bgSystem = QButtonGroup()
        bgSystem.addButton(self.rbOpen)
        bgSystem.addButton(self.rbClosed)
        hbox = QHBoxLayout()
        hbox.addWidget(lblMethod)
        hbox.addWidget(self.rbOpen)
        hbox.addWidget(self.rbClosed)
        vbox.addLayout(hbox)

        # xlabels = ['ILNO', 'XLNO', 'X', 'Y', 'Z']
        # nrow, ncol = 50, len(xlabels)
        # data = np.zeros((nrow, ncol))
        # self.editor = ArrayEditorWidget(self, data, xlabels=xlabels)
        # TODO use plain text editor
        self.editor.view.resize_to_contents()
        vbox.addWidget(self.editor)

        btn_start = QPushButton(_('Start picking'))
        btn_start.clicked.connect(self.start)
        btn_apply = QPushButton(_('Apply table'))
        btn_apply.clicked.connect(self.apply)
        btn_close = QPushButton(_('Close'))
        btn_close.clicked.connect(self.close)
        btn_help = QPushButton(_('Help'))
        btn_help.clicked.connect(self.show_help)

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(btn_start)
        hbox.addWidget(btn_apply)
        hbox.addWidget(btn_close)
        hbox.addWidget(btn_help)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.rbOpen.toggled.connect(lambda: self.set_method(self.rbOpen))
        self.rbClosed.toggled.connect(lambda: self.set_method(self.rbClosed))
        self.rbClosed.setChecked(True)

    def set_method(self, rb):
        if rb.isChecked():
            if rb.text() == _("Open"):
                self.isClosed = False
            elif rb.text() == _("Closed"):
                self.isClosed = True
            else:
                raise ValueError("unknown value {}".format(rb.text()))

    def start(self):
        self.sig_start.emit()

    def apply(self):
        self.update_line()

    def close(self):
        self.sigClose.emit()
        QDialog.close(self)

    def insert_point(self, point):
        i = self.currentRow
        if i >= self.editor.data.shape[0]:
            logger.error("Too many points. Ask the developer.")
            return
        self.editor.data[i,:] = point
        self.editor.model.reset() # refresh
        self.currentRow += 1
        self.update_line()

    def get_npoints(self):
        """
        Marker is the last nonzero point in the editor table.
        """
        npoints = 0
        data = self.editor.data
        n = data.shape[0]
        for i in range(n):
            j = n - 1 - i
            x = data[j,2]
            if x != 0:
                npoints = j + 1
                break
        return npoints

    def update_line(self):
        """ update line with new points in editor """
        self.editor.accept_changes() # needed for user typed numbers
        np = self.get_npoints()
        logger.info('Number of points = {}'.format(np))
        if np == 1: # NOT a line when only picked one point
            return
        elif np == 2: # initialize the line
            line_name = self.le_line.text()
            dob = Line(line_name)
            dob.set_atom_style()
            dob.set_line_style()
            dob.line_style['colorRGB'] = (0, 255, 0)
            vertexes = self.editor.data[:np, 2:5]
            dob.set_vertexes(vertexes)
            propList = ['X', 'Y', 'Z']
            dob.init_property(propList, vertexes)
            dob.set_connect(dob.make_connect())
            dob.set_segment(dob.make_segment())
            self.sigAddLine.emit(dob, True)
            self.line = dob
        else:
            vertexes = self.editor.data[:np, 2:5]
            dob = self.line
            dob.line_style['closed'] = True if self.isClosed else False
            dob.set_vertexes(vertexes)
            propList = ['X', 'Y', 'Z']
            dob.init_property(propList, vertexes)
            dob.set_connect(dob.make_connect())
            dob.set_segment(dob.make_segment())
            dob.set_pg3d_lines(pos=vertexes)
            dob.update_vs2d()
            dob.update_vs3d()

    def show_help(self):
        QMessageBox.information(self, _('How to use'),
            _("Input name of the new line, click <i>Start picking</i> <br>"
              "The line is not created until 2+ points are picked."))


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = HandPick()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
