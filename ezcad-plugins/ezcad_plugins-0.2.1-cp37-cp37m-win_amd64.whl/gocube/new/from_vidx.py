# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from qtpy.QtWidgets import QLabel, QRadioButton, QButtonGroup, QHBoxLayout
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog


class Dialog(EasyDialog):
    NAME = "New cube from volume indexes"
    sig_start = Signal(dict, str, str, str)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        text = _("New cube")
        self.cube = self.create_lineedit(text)
        self.layout.addWidget(self.cube)

        text = _("Property")
        self.property = self.create_lineedit(text)
        self.layout.addWidget(self.property)

        method = QLabel(_("Property method"))
        rb_zero = QRadioButton(_("zeros"))
        rb_random = QRadioButton(_("random"))
        rb_sum = QRadioButton(_("index sum"))
        bg_method = QButtonGroup()
        bg_method.addButton(rb_zero)
        bg_method.addButton(rb_random)
        bg_method.addButton(rb_sum)
        box = QHBoxLayout()
        box.addWidget(method)
        box.addWidget(rb_zero)
        box.addWidget(rb_random)
        box.addWidget(rb_sum)
        self.layout.addLayout(box)

        self.frame = self.create_cubeframe()
        self.layout.addWidget(self.frame)
        action = self.create_action()
        self.layout.addWidget(action)

        rb_zero.toggled.connect(lambda: self.set_method(rb_zero))
        rb_random.toggled.connect(lambda: self.set_method(rb_random))
        rb_sum.toggled.connect(lambda: self.set_method(rb_sum))
        rb_zero.setChecked(True)

    def set_method(self, rb):
        if rb.isChecked():
            # self.method = rb.text()
            if rb.text() == _("zeros"):
                self.method = "zeros"
            elif rb.text() == _("random"):
                self.method = "random"
            elif rb.text() == _("index sum"):
                self.method = "isum"
            else:
                raise ValueError("unknown value {}".format(rb.text()))

    def apply(self):

        IL_FRST = int(self.frame.le_il_frst.text())
        IL_LAST = int(self.frame.le_il_last.text())
        IL_NCRT = int(self.frame.le_il_ncrt.text())
        XL_FRST = int(self.frame.le_xl_frst.text())
        XL_LAST = int(self.frame.le_xl_last.text())
        XL_NCRT = int(self.frame.le_xl_ncrt.text())
        DP_FRST = int(self.frame.le_dp_frst.text())
        DP_LAST = int(self.frame.le_dp_last.text())
        DP_NCRT = int(self.frame.le_dp_ncrt.text())  # float? 12.5m

        IL_AMNT = int((IL_LAST - IL_FRST) / IL_NCRT + 1)
        XL_AMNT = int((XL_LAST - XL_FRST) / XL_NCRT + 1)
        DP_AMNT = int((DP_LAST - DP_FRST) / DP_NCRT + 1)
        IL_LAST = IL_FRST + IL_NCRT * (IL_AMNT - 1)
        XL_LAST = XL_FRST + XL_NCRT * (XL_AMNT - 1)
        DP_LAST = DP_FRST + DP_NCRT * (DP_AMNT - 1)

        dict_vidx = {
            'IL_FRST': IL_FRST,
            'IL_LAST': IL_LAST,
            'IL_NCRT': IL_NCRT,
            'IL_AMNT': IL_AMNT,
            'XL_FRST': XL_FRST,
            'XL_LAST': XL_LAST,
            'XL_NCRT': XL_NCRT,
            'XL_AMNT': XL_AMNT,
            'DP_FRST': DP_FRST,
            'DP_LAST': DP_LAST,
            'DP_NCRT': DP_NCRT,
            'DP_AMNT': DP_AMNT
        }

        cube_name = self.cube.edit.text()
        prop_name = self.property.edit.text()
        prop_method = self.method
        self.sig_start.emit(dict_vidx, cube_name, prop_name, prop_method)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
