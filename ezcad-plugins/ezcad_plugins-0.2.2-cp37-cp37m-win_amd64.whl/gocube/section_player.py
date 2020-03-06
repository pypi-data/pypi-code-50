# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from qtpy.QtCore import Qt
from qtpy.QtWidgets import QDialog, QLabel, QLineEdit, QSpinBox, QSlider, \
    QMessageBox, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox

from ezcad.config.base import _
from ezcad.utils.qthelpers import create_toolbutton_help
from ezcad.utils.functions import myprint
from .function import vidx_dict2list


class SectionPlayer(QDialog):
    NAME = "Section player"

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        if parent is not None:
            self.treebase = parent # connection wire to outside world
            self.database = self.treebase.object_data

        self.setup_page()
        self.load_cube()

    def setup_page(self):
        self.setWindowTitle(_(self.NAME))
        vbox = QVBoxLayout()

        lbl_cube = QLabel(_('Cube object'))
        self.le_cube = QLineEdit()
        btn_grab_cube = QPushButton(_('Grab'))
        btn_grab_cube.clicked.connect(self.grab_cube)
        btn_load_cube = QPushButton(_('Load'))
        btn_load_cube.clicked.connect(self.load_cube)

        hbox = QHBoxLayout()
        hbox.addWidget(lbl_cube)
        hbox.addWidget(self.le_cube)
        hbox.addWidget(btn_grab_cube)
        hbox.addWidget(btn_load_cube)
        vbox.addLayout(hbox)

        il_group = self.setup_page_il()
        xl_group = self.setup_page_xl()
        dp_group = self.setup_page_dp()
        vbox.addWidget(il_group)
        vbox.addWidget(xl_group)
        vbox.addWidget(dp_group)

        help_btn = create_toolbutton_help(self, triggered=self.show_help)
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(help_btn)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def setup_page_il(self):
        il_group = QGroupBox(_('Select inline'))
        lbl_il0 = QLabel('First')
        lbl_il1 = QLabel('Last')
        lbl_ils = QLabel('Increment')
        lbl_iln = QLabel('Amount')
        self.le_il0 = QLineEdit()
        self.le_il1 = QLineEdit()
        self.le_ils = QLineEdit()
        self.le_iln = QLineEdit()
        self.sld_il = QSlider(Qt.Horizontal)
        self.sp_il = QSpinBox()
        hbox = QHBoxLayout()
        hbox.addWidget(lbl_il0)
        hbox.addWidget(self.le_il0)
        hbox.addWidget(lbl_il1)
        hbox.addWidget(self.le_il1)
        hbox.addWidget(lbl_ils)
        hbox.addWidget(self.le_ils)
        hbox.addWidget(lbl_iln)
        hbox.addWidget(self.le_iln)
        il_layout = QVBoxLayout()
        il_layout.addLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.sld_il)
        hbox.addWidget(self.sp_il)
        il_layout.addLayout(hbox)
        il_group.setLayout(il_layout)

        self.le_il0.setReadOnly(True)
        self.le_il1.setReadOnly(True)
        self.le_ils.setReadOnly(True)
        self.le_iln.setReadOnly(True)
        self.sld_il.setTracking(False)
        self.sld_il.setTickPosition(QSlider.TicksBelow)
        self.sld_il.setSingleStep(1)
        self.sld_il.valueChanged.connect(self.slider_value_changed_il)
#        self.sp_il.valueChanged.connect(self.spinbox_value_changed_il)
        self.sp_il.editingFinished.connect(self.spinbox_editing_finished_il)

        return il_group

    def setup_page_xl(self):
        xl_group = QGroupBox(_('Select crossline'))
        lbl_xl0 = QLabel('First')
        lbl_xl1 = QLabel('Last')
        lbl_xls = QLabel('Increment')
        lbl_xln = QLabel('Amount')
        self.le_xl0 = QLineEdit()
        self.le_xl1 = QLineEdit()
        self.le_xls = QLineEdit()
        self.le_xln = QLineEdit()
        self.sld_xl = QSlider(Qt.Horizontal)
        self.sp_xl = QSpinBox()
        hbox = QHBoxLayout()
        hbox.addWidget(lbl_xl0)
        hbox.addWidget(self.le_xl0)
        hbox.addWidget(lbl_xl1)
        hbox.addWidget(self.le_xl1)
        hbox.addWidget(lbl_xls)
        hbox.addWidget(self.le_xls)
        hbox.addWidget(lbl_xln)
        hbox.addWidget(self.le_xln)
        xl_layout = QVBoxLayout()
        xl_layout.addLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.sld_xl)
        hbox.addWidget(self.sp_xl)
        xl_layout.addLayout(hbox)
        xl_group.setLayout(xl_layout)

        self.le_xl0.setReadOnly(True)
        self.le_xl1.setReadOnly(True)
        self.le_xls.setReadOnly(True)
        self.le_xln.setReadOnly(True)
        self.sld_xl.setTracking(False)
        self.sld_xl.setTickPosition(QSlider.TicksBelow)
        self.sld_xl.setSingleStep(1)
        self.sld_xl.valueChanged.connect(self.slider_value_changed_xl)
#        self.sp_xl.valueChanged.connect(self.spinbox_value_changed_xl)
        self.sp_xl.editingFinished.connect(self.spinbox_editing_finished_xl)

        return xl_group

    def setup_page_dp(self):
        dp_group = QGroupBox(_('Select depth'))
        lbl_dp0 = QLabel('First')
        lbl_dp1 = QLabel('Last')
        lbl_dps = QLabel('Increment')
        lbl_dpn = QLabel('Amount')
        self.le_dp0 = QLineEdit()
        self.le_dp1 = QLineEdit()
        self.le_dps = QLineEdit()
        self.le_dpn = QLineEdit()
        self.sld_dp = QSlider(Qt.Horizontal)
        self.sp_dp = QSpinBox()
        hbox = QHBoxLayout()
        hbox.addWidget(lbl_dp0)
        hbox.addWidget(self.le_dp0)
        hbox.addWidget(lbl_dp1)
        hbox.addWidget(self.le_dp1)
        hbox.addWidget(lbl_dps)
        hbox.addWidget(self.le_dps)
        hbox.addWidget(lbl_dpn)
        hbox.addWidget(self.le_dpn)
        dp_layout = QVBoxLayout()
        dp_layout.addLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.sld_dp)
        hbox.addWidget(self.sp_dp)
        dp_layout.addLayout(hbox)
        dp_group.setLayout(dp_layout)

        self.le_dp0.setReadOnly(True)
        self.le_dp1.setReadOnly(True)
        self.le_dps.setReadOnly(True)
        self.le_dpn.setReadOnly(True)
        self.sld_dp.setTracking(False)
        self.sld_dp.setTickPosition(QSlider.TicksBelow)
        self.sld_dp.setSingleStep(1)
        self.sld_dp.valueChanged.connect(self.slider_value_changed_dp)
#        self.sp_dp.valueChanged.connect(self.spinbox_value_changed_dp)
        self.sp_dp.editingFinished.connect(self.spinbox_editing_finished_dp)

        return dp_group

    def grab_cube(self):
        geom = ['Cube']
        self.cube = self.treebase.grab_object(geom)
        self.le_cube.setText(self.cube.name)
        self.load_cube()

    def load_cube(self):
        """
        """
        self.ilno_old = -1
        self.xlno_old = -1
        self.dpno_old = -1

        if len(self.le_cube.text().strip()) == 0 :
            # This is for testing GUI without data cube.
            self.dob = None
            self.il0, self.il1, self.ils, self.iln = 0, 99, 1, 100
            self.xl0, self.xl1, self.xls, self.xln = 0, 99, 1, 100
            self.dp0, self.dp1, self.dps, self.dpn = 0, 99, 1, 100
            self.ilno, self.xlno, self.dpno = self.il0, self.xl0, self.dp0
        else:
            cube_name = self.le_cube.text()
            self.dob = self.database[cube_name]
            listVidx = vidx_dict2list(self.dob.dict_vidx)
            self.il0, self.il1, self.ils, self.iln = listVidx[0:4]
            self.xl0, self.xl1, self.xls, self.xln = listVidx[4:8]
            self.dp0, self.dp1, self.dps, self.dpn = listVidx[8:12]
            self.ilno = self.dob.section_number['iline']
            self.xlno = self.dob.section_number['xline']
            self.dpno = self.dob.section_number['depth']

        self.le_il0.setText(str(self.il0))
        self.le_il1.setText(str(self.il1))
        self.le_ils.setText(str(self.ils))
        self.le_iln.setText(str(self.iln))
        self.sld_il.setRange(0, self.iln-1)
        self.sld_il.setTickInterval(int(self.iln/5))
        sliderValue = (self.ilno - self.il0) / self.ils
        self.sld_il.setValue(sliderValue)
        self.sp_il.setRange(self.il0, self.il1)
        self.sp_il.setSingleStep(self.ils)
        self.sp_il.setValue(self.ilno)

        self.le_xl0.setText(str(self.xl0))
        self.le_xl1.setText(str(self.xl1))
        self.le_xls.setText(str(self.xls))
        self.le_xln.setText(str(self.xln))
        self.sld_xl.setRange(0, self.xln-1)
        self.sld_xl.setTickInterval(int(self.xln/5))
        sliderValue = (self.xlno - self.xl0) / self.xls
        self.sld_xl.setValue(sliderValue)
        self.sp_xl.setRange(self.xl0, self.xl1)
        self.sp_xl.setSingleStep(self.xls)
        self.sp_xl.setValue(self.xlno)

        self.le_dp0.setText(str(self.dp0))
        self.le_dp1.setText(str(self.dp1))
        self.le_dps.setText(str(self.dps))
        self.le_dpn.setText(str(self.dpn))
        self.sld_dp.setRange(0, self.dpn-1)
        self.sld_dp.setTickInterval(int(self.dpn/5))
        sliderValue = (self.dpno - self.dp0) / self.dps
        self.sld_dp.setValue(sliderValue)
        self.sp_dp.setRange(self.dp0, self.dp1)
        self.sp_dp.setSingleStep(self.dps)
        self.sp_dp.setValue(self.dpno)

    def slider_value_changed_il(self, sliderValue):
        """
        """
        self.ilno = self.il0 + self.ils * sliderValue
        self.sp_il.setValue(self.ilno) # sync spinbox
        self.check_ilno()

    def spinbox_value_changed_il(self, spinboxValue):
        """
        """
        self.ilno = spinboxValue
        sliderValue = (self.ilno - self.il0) / self.ils
        self.sld_il.setValue(sliderValue) # sync slider
        self.check_ilno()

    def spinbox_editing_finished_il(self):
        """
        """
        self.ilno = self.sp_il.value()
        sliderValue = (self.ilno - self.il0) / self.ils
        self.sld_il.setValue(sliderValue) # sync slider
        self.check_ilno()

    def slider_value_changed_xl(self, sliderValue):
        """
        """
        self.xlno = self.xl0 + self.xls * sliderValue
        self.sp_xl.setValue(self.xlno) # sync spinbox
        self.check_xlno()

    def spinbox_value_changed_xl(self, spinboxValue):
        """
        """
        self.xlno = spinboxValue
        sliderValue = (self.xlno - self.xl0) / self.xls
        self.sld_xl.setValue(sliderValue) # sync slider
        self.check_xlno()

    def spinbox_editing_finished_xl(self):
        """
        """
        self.xlno = self.sp_xl.value()
        sliderValue = (self.xlno - self.xl0) / self.xls
        self.sld_xl.setValue(sliderValue) # sync slider
        self.check_xlno()

    def slider_value_changed_dp(self, sliderValue):
        """
        """
        self.dpno = self.dp0 + self.dps * sliderValue
        self.sp_dp.setValue(self.dpno) # sync spinbox
        self.check_dpno()

    def spinbox_value_changed_dp(self, spinboxValue):
        """
        """
        self.dpno = spinboxValue
        sliderValue = (self.dpno - self.dp0) / self.dps
        self.sld_dp.setValue(sliderValue) # sync slider
        self.check_dpno()

    def spinbox_editing_finished_dp(self):
        """
        """
        self.dpno = self.sp_dp.value()
        sliderValue = (self.dpno - self.dp0) / self.dps
        self.sld_dp.setValue(sliderValue) # sync slider
        self.check_dpno()

    def check_ilno(self):
        """
        Avoid act twice by slider and spinbox
        """
        if self.ilno != self.ilno_old :
            self.section_changed('iline', self.ilno)
            self.ilno_old = self.ilno

    def check_xlno(self):
        if self.xlno != self.xlno_old :
            self.section_changed('xline', self.xlno)
            self.xlno_old = self.xlno

    def check_dpno(self):
        if self.dpno != self.dpno_old :
            self.section_changed('depth', self.dpno)
            self.dpno_old = self.dpno

    def section_changed(self, section_type, section_number):
        """
        The mechanism is both slider and spinbox changes can trigger action.
        This slot is the ultimate one that calls section replot and move.
        The slider value change will sync the spinbox and call this slot.
        The spinbox value change will sync the slider and call this slot.
        The spin-box updates slider, slider updates spin-box, ...
        This is not infinite loop because only value change fires the update.
        """
        myprint("%s changes to %s %i" % (self.NAME, section_type, section_number))
        if self.dob is not None:
            self.dob.move_section(section_type, section_number)
            #self.treebase.main.current_viewer.update()
            object_name = self.dob.name
            self.treebase.update_cube_secno(object_name, section_type, section_number)

    def show_help(self):
        QMessageBox.information(self, _('How to use'), _(
        "To avoid update when type number in the spinbox, I disconnect its "
        "valueChanged signal and connect the editingFinished signal to the "
        "update slot. You can type number in the spinbox, then hit Enter. "
        "You can change the spinbox value by holding the un/down key in keyboard, "
        "then hit Enter. You can click the up/down arrow in spinbox, then "
        "click any other box (to take away the focus which means editing finished).<br>"))


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = SectionPlayer()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
