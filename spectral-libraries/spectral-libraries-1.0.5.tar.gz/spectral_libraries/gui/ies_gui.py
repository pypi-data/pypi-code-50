# -*- coding: utf-8 -*-
"""
| ----------------------------------------------------------------------------------------------------------------------
| Date                : August 2018
| Copyright           : (C) 2018 by Ann Crabbé (KU Leuven)
| Email               : ann.crabbe@kuleuven.be
| Acknowledgements    : Translated from VIPER Tools 2.0 (UC Santa Barbara, VIPER Lab).
|                       Dar Roberts, Kerry Halligan, Philip Dennison, Kenneth Dudley, Ben Somers, Ann Crabbé
|
| This program is free software; you can redistribute it and/or modify it under the terms of the GNU
| General Public License as published by the Free Software Foundation; either version 3 of the
| License, or any later version.
| ----------------------------------------------------------------------------------------------------------------------
"""
import os
import sys
import numpy as np
from qgis.gui import QgsFileWidget
from qgis.PyQt.uic import loadUi
from qgis.PyQt.QtWidgets import QDialog, QDialogButtonBox
from spectral_libraries.io.imports import import_square, import_library, import_library_metadata
from spectral_libraries.io.exports import save_ies_metadata
from spectral_libraries.gui import LogoWidget, EmittingStream
from spectral_libraries.scripts.ies import Ies


class IesWidget(QDialog):
    """ QDialog to interactively set up the IES input and output. """

    def __init__(self):
        super(IesWidget, self).__init__()
        loadUi(os.path.join(os.path.dirname(__file__), 'ies.ui'), self)
        sys.stdout = EmittingStream(self.tabWidget)
        sys.stderr = EmittingStream(self.tabWidget)

        # Logo
        self.logoLayout.addWidget(LogoWidget(parent=self.logoWidget))

        # array
        self.browseSquare.lineEdit().setReadOnly(True)
        self.browseSquare.lineEdit().setPlaceholderText('The square array (.sqr) ...')
        self.browseSquare.fileChanged.connect(self._array_browse)

        # metadata
        self.browseMeta.lineEdit().setReadOnly(True)
        self.browseMeta.lineEdit().setPlaceholderText('Spectral Library  file (.sli) ...')
        self.browseMeta.fileChanged.connect(self._meta_browse)

        # forced library
        self.forcedDropDown.checkedItemsChanged.connect(self._select_endmembers)

        # output
        self.browseOut.lineEdit().setReadOnly(True)
        self.browseOut.lineEdit().setPlaceholderText('The output spectral library (.sli) ...')
        self.browseOut.setStorageMode(QgsFileWidget.SaveFile)

        # run or cancel
        self.OKClose.button(QDialogButtonBox.Ok).setText("Run")
        self.OKClose.accepted.connect(self._run_ies)
        self.OKClose.rejected.connect(self.close)

        # widget variables
        self.square = None
        self.spectra_names = None
        self.spectral_library = None
        self.spectral_library_path = None

    def __del__(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def _array_browse(self, path):
        """ Browse for a square array.
        :param path: the absolute path to the square array
        """

        self.square, self.spectra_names = import_square(path)

        # on unsuccessful import:
        if self.square is None:
            self.browseSquare.setFilePath('')
            return

        # find connected metadata file
        lib_path = path[:path.find('_sq.sqr')] + '.sli'
        if os.path.exists(lib_path):
            self.browseMeta.lineEdit().setText(lib_path)

        # add spectra to drop down
        self.forcedDropDown.clear()
        self.forcedDropDown.addItems(self.spectra_names)

        # set default output name
        out_path = path[:path.find('_sq.sqr')] + '_ies.sli'
        if not os.path.exists(out_path):
            self.browseOut.lineEdit().setText(out_path)

    def _meta_browse(self, path):
        """ Browse for metadata and set the drop down.
        :param path: the absolute path to the spectral library
        """
        if path == '':
            return

        self.classDropDown.clear()

        try:
            self.spectral_library = import_library(path)
        except Exception as e:
            print(str(e), file=sys.stderr)
            self.browseMeta.setFilePath('')
            return

        self.spectral_library_path = path

        # add header to drop down
        self.classDropDown.addItems(['Select ...'] + self.spectral_library.fieldNames())

    def _select_endmembers(self):

        count = len(self.forcedDropDown.checkedItems())
        self.forcedLabel.setText(str(count) + " selected")

    def _run_ies(self, test_mode=False):
        """ Read all parameters and pass them on to the SquareArray class. """

        if self.square is None:
            print('Choose a square array.', file=sys.stderr)
            return

        if self.spectral_library is None:
            print('Choose a spectral library file.', file=sys.stderr)
            return

        # Get the class_list
        class_name = self.classDropDown.currentText()
        if class_name == "Select ...":
            print('Choose a metadata class.', file=sys.stderr)
            return
        class_str = import_library_metadata(self.spectral_library, metadata=class_name)
        class_unique, class_list = np.unique(class_str, return_inverse=True)

        if len(class_unique) == 1:
            print('IES requires more than one class, please select another column', file=sys.stderr)
            return

        # Output file
        if self.browseOut.filePath() == '':
            print('Specify an output file.', file=sys.stderr)
            return
        else:
            output_file = self.browseOut.filePath()

        # Forced endmembers
        if self.forcedGroup.isChecked():
            items = self.forcedDropDown.checkedItems()
            if len(items) == 0:
                print('No endmembers selected to forcefully add to the ies process.', file=sys.stderr)
                return
            else:
                forced_list = np.array([self.spectra_names.index(x) for x in items])
                forced_location = self.forcedStep.value()
        else:
            forced_list = None
            forced_location = None

        # Check a RMSE and Constraints band are given
        bands = list(self.square.keys())
        if 'rmse' not in bands:
            print("No 'RMSE' band found in the square array.", file=sys.stderr)
            return
        if 'constraints' not in bands:
            print("No 'Constraints' band found in the square array", file=sys.stderr)
            return

        # Run IES
        ies_selection, ies_metadata = Ies().execute(rmse_band=self.square['rmse'], class_list=class_list,
                                                    constraints_band=self.square['constraints'],
                                                    forced_list=forced_list, forced_location=forced_location,
                                                    summary=True, p=self.progressBar)

        if ies_selection is None:
            return

        # write output library and metadata file
        profiles_list = list(self.spectral_library.profiles())
        fid_attribute_index = profiles_list[0].fieldNameIndex('fid')
        fid_list = [profiles_list[x].attributes()[fid_attribute_index] for x in ies_selection]

        ies_library = self.spectral_library.speclibFromFeatureIDs(fid_list)
        ies_library.exportProfiles(path=output_file)

        save_ies_metadata(metadata=ies_metadata, library_path=self.spectral_library_path,
                          outfile_path=os.path.splitext(output_file)[0] + '_summary.txt',
                          forced_list=forced_list, forced_position=forced_location,
                          class_header=class_name,
                          class_list=class_str,
                          spectra_names=self.spectra_names,
                          selection=ies_selection)
        if not test_mode:
            os.startfile(os.path.splitext(output_file)[0] + '_summary.txt')
        self.progressBar.setValue(100)


def _run():
    from qgis.core import QgsApplication
    app = QgsApplication([], True)
    app.initQgis()

    z = IesWidget()
    z.show()

    app.exec_()


if __name__ == '__main__':
    _run()
