# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Signal
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog
from ..function import vidx_dict2list, vidx_format_dtype


class Dialog(EasyDialog):
    NAME = _("Extract subcube from an existing cube")
    sig_start = Signal(str, str, dict)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        text = _("Existing cube")
        geom = ['Cube']
        self.grabob = self.create_grabob(text, geom=geom)
        self.layout.addWidget(self.grabob)

        text = _("New cube")
        self.newCube = self.create_lineedit(text)
        self.layout.addWidget(self.newCube)

        self.frame = self.create_cubeframe()
        self.layout.addWidget(self.frame)

        action = self.create_action()
        self.layout.addWidget(action)

    def apply(self):
        cube_name = self.grabob.lineedit.edit.text()
        newCubeName = self.newCube.edit.text()

        IL_FRST = int(self.frame.le_il_frst.text())
        IL_LAST = int(self.frame.le_il_last.text())
        IL_NCRT = int(self.frame.le_il_ncrt.text())
        XL_FRST = int(self.frame.le_xl_frst.text())
        XL_LAST = int(self.frame.le_xl_last.text())
        XL_NCRT = int(self.frame.le_xl_ncrt.text())
        DP_FRST = float(self.frame.le_dp_frst.text())
        DP_LAST = float(self.frame.le_dp_last.text())
        DP_NCRT = float(self.frame.le_dp_ncrt.text())

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
            'DP_AMNT': DP_AMNT,
        }
        vidx_format_dtype(dict_vidx)
        self.sig_start.emit(cube_name, newCubeName, dict_vidx)

    def load_object(self):
        self.cube = self.object # assigned by grab object
        listVidx = vidx_dict2list(self.cube.dict_vidx)
        il0, il1, ils, iln = listVidx[0:4]
        xl0, xl1, xls, xln = listVidx[4:8]
        dp0, dp1, dps, dpn = listVidx[8:12]
        self.frame.le_il_frst.setText(str(il0))
        self.frame.le_il_last.setText(str(il1))
        self.frame.le_il_ncrt.setText(str(ils))
        self.frame.le_xl_frst.setText(str(xl0))
        self.frame.le_xl_last.setText(str(xl1))
        self.frame.le_xl_ncrt.setText(str(xls))
        self.frame.le_dp_frst.setText(str(dp0))
        self.frame.le_dp_last.setText(str(dp1))
        self.frame.le_dp_ncrt.setText(str(dps))


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
