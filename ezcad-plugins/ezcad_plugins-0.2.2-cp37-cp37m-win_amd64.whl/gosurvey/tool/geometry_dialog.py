# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""
Dialog for view survey geometry parameters.
"""

from qtpy.QtWidgets import QDialog, QLabel, QGroupBox, QLineEdit, \
    QFormLayout, QVBoxLayout, QMessageBox
from ezcad.config.base import _


class GeometryDialog(QDialog):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.parent = parent
        self.survey = self.parent.survey
        if not hasattr(self.survey, 'binning'):
            QMessageBox.critical(self, _("Error"),
                        _("None survey geometry has been loaded yet."))
            return
        self.setup_page()

    def setup_page(self):
        self.setWindowTitle(_("Survey geometry"))

        binning_group = QGroupBox(_("Binning parameters"))

        list_label = ['X of origin', 'Y of origin',
                      'Azimuth of inlines',
                      'Minimum inline number', 'Maximum inline number',
                      'Number of inlines', 'Distance between inlines',
                      'Azimuth of crosslines',
                      'Minimum crossline number', 'Maximum crossline number',
                      'Number of crosslines', 'Distance between crosslines',
                      'X of the first inline end', 'Y of the first inline end',
                      'X of the first crossline end', 'Y of the first crossline end',
                      'X of the last inline end', 'Y of the last inline end']

        list_key = ['x_origin', 'y_origin',
                    'azimuth_iline',
                    'ilno_min', 'ilno_max',
                    'il_amnt', 'il_dist',
                    'azimuth_xline',
                    'xlno_min', 'xlno_max',
                    'xl_amnt', 'xl_dist',
                    'x_filend', 'y_filend',
                    'x_fxlend', 'y_fxlend',
                    'x_lilend', 'y_lilend']

        list_dtype = ['float', 'float',
                      'float',
                      'int', 'int',
                      'int', 'float',
                      'float',
                      'int', 'int',
                      'int', 'float',
                      'float', 'float',
                      'float', 'float',
                      'float', 'float']

        # TODO change 3 lists to 1 dictionary

        binning_layout = QFormLayout()

        for i in range(len(list_label)):
            label = QLabel(_(list_label[i]))
            if self.survey is not None:
                value = self.survey.binning[list_key[i]]
            else:
                value = 0
            if list_dtype[i] == 'float':
                value = round(value, 2)
            if list_dtype[i] == 'int':
                value = int(value)

            line = QLineEdit(str(value))
            line.setReadOnly(True)
            binning_layout.addRow(label, line)

        binning_group.setLayout(binning_layout)

        vbox = QVBoxLayout()
        vbox.addWidget(binning_group)
        self.setLayout(vbox)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = GeometryDialog()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
