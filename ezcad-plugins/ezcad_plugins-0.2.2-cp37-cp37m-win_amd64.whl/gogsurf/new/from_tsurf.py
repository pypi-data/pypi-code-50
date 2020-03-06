# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from qtpy.QtWidgets import QLabel, QLineEdit, QGroupBox, QGridLayout, \
    QRadioButton, QHBoxLayout, QButtonGroup
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = _("Create Gsurf from Tsurf")
    sig_start = Signal(str, str, dict, str)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page_input()
        self.setup_page_output()

    def setup_page_input(self):
        text = _("Input Tsurf")
        geom = ['Tsurface']
        self.grabob = self.create_grabob(text, geom=geom)
        self.layout.addWidget(self.grabob)

    def setup_page_output(self):
        text = _("Output Gsurf")
        self.gsurf = self.create_lineedit(text)
        self.layout.addWidget(self.gsurf)

        lblMethod = QLabel(_('Interpolation method'))
        rbNearest = QRadioButton(_('nearest'))
        rbLinear = QRadioButton(_('linear'))
        rbCubic = QRadioButton(_('cubic'))
        bgMethod = QButtonGroup()
        bgMethod.addButton(rbNearest)
        bgMethod.addButton(rbLinear)
        bgMethod.addButton(rbCubic)
        hbox = QHBoxLayout()
        hbox.addWidget(lblMethod)
        hbox.addWidget(rbNearest)
        hbox.addWidget(rbLinear)
        hbox.addWidget(rbCubic)
        self.layout.addLayout(hbox)

        ln_group = QGroupBox(_('Output gsurf range (in LN domain)'))
        lbl_iline = QLabel(_("Iline first, last, step"))
        self.le_il_frst = QLineEdit()
        self.le_il_last = QLineEdit()
        self.le_il_ncrt = QLineEdit()
        lbl_xline = QLabel(_("Xline first, last, step"))
        self.le_xl_frst = QLineEdit()
        self.le_xl_last = QLineEdit()
        self.le_xl_ncrt = QLineEdit()
        ln_layout = QGridLayout()
        ln_layout.addWidget(lbl_iline, 0, 0)
        ln_layout.addWidget(self.le_il_frst, 0, 1)
        ln_layout.addWidget(self.le_il_last, 0, 2)
        ln_layout.addWidget(self.le_il_ncrt, 0, 3)
        ln_layout.addWidget(lbl_xline, 1, 0)
        ln_layout.addWidget(self.le_xl_frst, 1, 1)
        ln_layout.addWidget(self.le_xl_last, 1, 2)
        ln_layout.addWidget(self.le_xl_ncrt, 1, 3)
        ln_group.setLayout(ln_layout)

        xy_group = QGroupBox(_('Output gsurf range (in XY domain)'))

        self.layout.addWidget(ln_group)
        self.layout.addWidget(xy_group)

        action = self.create_action()
        self.layout.addWidget(action)

        rbNearest.toggled.connect(lambda: self.set_method(rbNearest))
        rbLinear.toggled.connect(lambda: self.set_method(rbLinear))
        rbCubic.toggled.connect(lambda: self.set_method(rbCubic))
        rbLinear.setChecked(True)

    def load_object(self):
        gsurfName = self.object.name + '_gs'
        self.gsurf.edit.setText(gsurfName)

    def set_method(self, rb):
        if rb.isChecked():
            if rb.text() == _('linear'):
                self.method = 'linear'
            elif rb.text() == _('nearest'):
                self.method = 'nearest'
            elif rb.text() == _('cubic'):
                self.method = 'cubic'
            else:
                raise ValueError("Unknown value")

    def apply(self):
        tsurfName = self.grabob.lineedit.edit.text()
        gsurfName = self.gsurf.edit.text()
        method = self.method

        IL_FRST = int(self.le_il_frst.text())
        IL_LAST = int(self.le_il_last.text())
        IL_NCRT = int(self.le_il_ncrt.text())
        XL_FRST = int(self.le_xl_frst.text())
        XL_LAST = int(self.le_xl_last.text())
        XL_NCRT = int(self.le_xl_ncrt.text())

        IL_AMNT = int((IL_LAST - IL_FRST) / IL_NCRT + 1)
        XL_AMNT = int((XL_LAST - XL_FRST) / XL_NCRT + 1)
        IL_LAST = IL_FRST + IL_NCRT * (IL_AMNT - 1)
        XL_LAST = XL_FRST + XL_NCRT * (XL_AMNT - 1)

        dict_sidx_ln = {}
        dict_sidx_ln['IL_FRST'] = IL_FRST
        dict_sidx_ln['IL_LAST'] = IL_LAST
        dict_sidx_ln['IL_NCRT'] = IL_NCRT
        dict_sidx_ln['IL_AMNT'] = IL_AMNT
        dict_sidx_ln['XL_FRST'] = XL_FRST
        dict_sidx_ln['XL_LAST'] = XL_LAST
        dict_sidx_ln['XL_NCRT'] = XL_NCRT
        dict_sidx_ln['XL_AMNT'] = XL_AMNT

        self.sig_start.emit(tsurfName, gsurfName, dict_sidx_ln, method)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
