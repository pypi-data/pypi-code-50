# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""
This widget toggles images display, similar to the Seismic Compare
in SeisSpace. This is a basic function in seismic data processing,
such as PMDC when we need flip back-n-forth before-n-after results.

It is named Face Change, as in the Sichuan Opera Face. It is written in
the train to Tibet, after my short and memorable stay in Sichuan. 2019/6/18.
"""

from qtpy.QtCore import Signal
from qtpy.QtWidgets import (QTableWidget, QHBoxLayout, QPushButton,
    QComboBox, QTableWidgetItem)
from ezcad.config.base import _
from ezcad.widgets.ezdialog import EasyDialog
from ezcad.utils.envars import SECTION_TYPES


class Dialog(EasyDialog):
    NAME = _("Face change")
    HELP_BODY = _("To be done<br>")
    sig_start = Signal(bool, str, str, str, float, float, float, float)

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent=parent, set_tree=True, set_db=True)
        self.setup_page()
        self.currentRow = 0

    def setup_page(self):
        nrow = 2 # need to handle more than 2
        columnNames = ['Cube', 'Property', 'Sec-type', 'Sec-no',
            'Clip min', 'Clip max', 'Colorbar', 'Opacity']
        ncol = len(columnNames)
        self.table = QTableWidget()
        self.table.setRowCount(nrow)
        self.table.setColumnCount(ncol)
        self.table.setHorizontalHeaderLabels(columnNames)
        self.layout.addWidget(self.table)

        text = _("Cube")
        geom = ['Cube']
        self.cube = self.create_grabob(text, geom=geom)
        btnLoad = QPushButton(_('Load'))
        btnLoad.clicked.connect(self.load_object)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.cube)
        hbox.addWidget(btnLoad)
        self.layout.addLayout(hbox)
        
        self.resize(900, 200)
        self.table.currentCellChanged.connect(self.current_cell_changed)

    def current_cell_changed(self, row, col):
        if self.currentRow != row:
            self.current_row_changed(row)

    def current_row_changed(self, row):
        # Turn off the section corresponding to the old row
        # Turn on the section corresponding to the new row
        self.oldRow = self.currentRow
        self.currentRow = row
        self.turn_off()
        self.turn_on()
        
    def turn_off(self):
        if self.oldRow == -1:
            return
        vals = self.get_row_values(self.oldRow)
        if vals is None:
            return
        cube_name, prop_name, secType, secno, clipmin, clipmax, alpha = vals
        self.sig_start.emit(False, cube_name, prop_name, secType, secno,
            clipmin, clipmax, alpha)

    def turn_on(self):
        vals = self.get_row_values(self.currentRow)
        if vals is None:
            return
        cube_name, prop_name, secType, secno, clipmin, clipmax, alpha = vals
        self.sig_start.emit(True, cube_name, prop_name, secType, secno,
            clipmin, clipmax, alpha)

    def get_row_values(self, row):
        if self.table.item(row, 0) is None: # blank row
            return None
        cube_name = self.table.item(row, 0).text()
        prop_name = self.table.cellWidget(row, 1).currentText()
        secType = self.table.cellWidget(row, 2).currentText()
        secno = float(self.table.item(row, 3).text())
        clipmin = float(self.table.item(row, 4).text())
        clipmax = float(self.table.item(row, 5).text())
        alpha = float(self.table.item(row, 7).text())
        return (cube_name, prop_name, secType, secno, clipmin, clipmax, alpha)
        
    def load_object(self):
        """ Insert cube to the current row of the table """
        name = self.cube.lineedit.edit.text()
        row = self.table.currentRow()
        
        self.table.setItem(row, 0, QTableWidgetItem(name))
        
        dob = self.database[name]
        propList = list(dob.prop.keys())
        prop_name = dob.current_property
        index = propList.index(prop_name)
        combo = QComboBox()
        combo.addItems(propList)
        combo.setCurrentIndex(index)
        self.table.setCellWidget(row, 1, combo)
        
        index = 0
        combo = QComboBox()
        combo.addItems(SECTION_TYPES)
        combo.setCurrentIndex(index)
        self.table.setCellWidget(row, 2, combo)
        
        sectype = SECTION_TYPES[index]
        secno = dob.section_number[sectype]
        clipmin, clipmax = dob.prop[prop_name]['colorClip']
        cg = dob.prop[prop_name]['colorGradient']
        alpha = cg['ticks'][0][1][3]
        
        self.table.setItem(row, 3, QTableWidgetItem(str(secno)))
        self.table.setItem(row, 4, QTableWidgetItem(str(clipmin)))
        self.table.setItem(row, 5, QTableWidgetItem(str(clipmax)))
        self.table.setItem(row, 7, QTableWidgetItem(str(alpha)))

        # TODO
        # table.setCellWidget(row, 6, colorbar)
        # make clip, cbar, opacity cells editable and sync to dob and colorbar editor


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Dialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
