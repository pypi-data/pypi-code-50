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
from osgeo import gdal
from qgis.gui import QgsFileWidget
from qgis.core import QgsProviderRegistry, QgsMapLayerProxyModel, QgsRasterLayer, QgsProject, QgsField
from qgis.PyQt.uic import loadUi
from qgis.PyQt.QtCore import QVariant
from qgis.PyQt.QtWidgets import QDialog, QFileDialog, QDialogButtonBox
from spectral_libraries.io.imports import import_square, import_library, import_library_metadata
from spectral_libraries.gui import LogoWidget, EmittingStream
from spectral_libraries.scripts.ear_masa_cob import EarMasaCob


class EarMasaCobWidget(QDialog):
    """ QDialog to interactively set up the Ear/Masa/Cob input and output. """

    def __init__(self):
        super(EarMasaCobWidget, self).__init__()
        loadUi(os.path.join(os.path.dirname(__file__), 'ear_masa_cob.ui'), self)
        sys.stdout = EmittingStream(self.tabWidget)
        sys.stderr = EmittingStream(self.tabWidget)
        sys.stderr = EmittingStream(self.tabWidget)

        # Logo
        self.logoLayout.addWidget(LogoWidget(parent=self.logoWidget))

        # array
        excluded_providers = [p for p in QgsProviderRegistry.instance().providerList() if p not in ['gdal']]
        self.arrayComboBox.setExcludedProviders(excluded_providers)
        self.arrayComboBox.setFilters(QgsMapLayerProxyModel.RasterLayer)
        self.arrayComboBox.layerChanged.connect(self._array_select)
        self.arrayAction.triggered.connect(self._array_browse)
        self.arrayButton.setDefaultAction(self.arrayAction)

        # csv
        self.browseCSV.lineEdit().setReadOnly(True)
        self.browseCSV.lineEdit().setPlaceholderText('Spectral Library file (.sli) ...')
        self.browseCSV.fileChanged.connect(self._meta_browse)

        # output
        self.browseOut.lineEdit().setReadOnly(True)
        self.browseOut.lineEdit().setPlaceholderText('The Spectral Library output file (.sli) ...')
        self.browseOut.setStorageMode(QgsFileWidget.SaveFile)

        # run or cancel
        self.OKClose.button(QDialogButtonBox.Ok).setText("Run")
        self.OKClose.accepted.connect(self._run_ear_masa_cob)
        self.OKClose.rejected.connect(self.close)

        # widget variables
        self.square = None
        self.spectra_names = None
        self.spectral_library = None
        self.library_path = None

    def __del__(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def _array_browse(self):
        """ Browse for a square array. """

        path = QFileDialog.getOpenFileName(filter="Square Array (*.sqr);;All Files (*)")[0]

        if len(path) > 0:
            self.set_array(path)

    def set_array(self, path):

        gdal.UseExceptions()
        try:
            layer = QgsRasterLayer(path, os.path.basename(path), 'gdal')
            assert layer.isValid()
        except (AssertionError, Exception):
            print("'" + path + "' not recognized as a supported file format.", file=sys.stderr)
            return

        QgsProject.instance().addMapLayer(layer, True)
        self.arrayComboBox.setLayer(layer)

    def _array_select(self):
        """ Select an array from the Combo Box. """

        current_layer = self.arrayComboBox.currentLayer()
        if current_layer is None:
            return

        path = current_layer.source()

        self.square, self.spectra_names = import_square(path)

        # on unsuccessful import:
        if self.square is None:
            self.browseSquare.setFilePath('')
            return

        # find connected library file
        meta_path = path[:path.find('_sq.sqr')] + '.sli'
        if os.path.exists(meta_path):
            self.browseCSV.lineEdit().setText(meta_path)

    def _meta_browse(self, path):
        """ Browse for Spectral Library and set the drop down.
        :param path: the absolute path to the spectral library
        """
        if path == '':
            return

        self.classDropDown.clear()

        try:
            self.spectral_library = import_library(path)
        except Exception as e:
            print(str(e), file=sys.stderr)
            self.browseCSV.setFilePath('')
            return

        fields = self.spectral_library.fieldNames()
        if "EAR" in fields or "MASA" in fields or "InCOB" in fields or "OutCOB" in fields or "COBI" in fields:
            print("Metadata already contains EMC results ('EAR', 'MASA', 'InCOB', 'OutCOB' or 'COBI'). "
                  "Remove or rename fields.", file=sys.stderr)
            self.browseCSV.setFilePath('')
            return

        self.library_path = path

        # add header to drop down
        self.classDropDown.addItems(['Select ...'] + fields)

        # set default output name
        out_path = path[:path.find('.sli')] + '_emc.sli'
        if not os.path.exists(out_path):
            self.browseOut.lineEdit().setText(out_path)

    def _run_ear_masa_cob(self):
        """ Read all parameters and pass them on to the SquareArray class. """

        if self.square is None:
            print('Choose a Square Array.', file=sys.stderr)
            return

        if self.spectral_library is None:
            print('Choose a Spectral Library.', file=sys.stderr)
            return

        if self.browseOut.filePath() == '':
            print('Set the output path.', file=sys.stderr)
            return

        # Get the class_list
        class_name = self.classDropDown.currentText()
        if class_name == "Select ...":
            print('Choose a metadata class.', file=sys.stderr)
            return
        class_list = import_library_metadata(self.spectral_library, class_name)

        # Check a Spectral Angle, RMSE and Constraints band are given
        bands = list(self.square.keys())
        if 'spectral angle' not in bands:
            print("No 'Spectral Angle' band found in the square array.", file=sys.stderr)
            return
        if 'rmse' not in bands:
            print("No 'RMSE' band found in the square array.", file=sys.stderr)
            return

        # Run EMC
        if 'constraints' not in bands:
            result = EarMasaCob().execute(spectral_angle_band=self.square['spectral angle'],
                                          rmse_band=self.square['rmse'],
                                          class_list=class_list)
        else:
            result = EarMasaCob().execute(spectral_angle_band=self.square['spectral angle'],
                                          rmse_band=self.square['rmse'],
                                          constraints_band=self.square['constraints'],
                                          class_list=class_list)

        # append metadata to spectral library
        self.spectral_library.startEditing()
        self.spectral_library.addAttribute(QgsField(name="EAR", type=QVariant.Double))
        self.spectral_library.addAttribute(QgsField(name="MASA", type=QVariant.Double))
        if 'constraints' in bands:
            self.spectral_library.addAttribute(QgsField(name="InCOB", type=QVariant.Int))
            self.spectral_library.addAttribute(QgsField(name="OutCOB", type=QVariant.Int))
            self.spectral_library.addAttribute(QgsField(name="COBI", type=QVariant.Double))
        self.spectral_library.commitChanges()

        # add extra attribute data
        self.spectral_library.startEditing()

        fields = self.spectral_library.fields()
        ear_index = fields.indexFromName("EAR")
        masa_index = fields.indexFromName("MASA")
        profiles = self.spectral_library.profiles()
        for (profile, ear, masa) in zip(profiles, result[0], result[1]):
            self.spectral_library.changeAttributeValue(profile.id(), ear_index, ear)
            self.spectral_library.changeAttributeValue(profile.id(), masa_index, masa)

        if 'constraints' in bands:
            cob_in_index = fields.indexFromName("InCOB")
            cob_out_index = fields.indexFromName("OutCOB")
            cob_ratio_index = fields.indexFromName("COBI")
            profiles = self.spectral_library.profiles()         # again  because iterator
            for (profile, ci, co, cr) in zip(profiles, result[2], result[3], result[4]):
                self.spectral_library.changeAttributeValue(profile.id(), cob_in_index, ci)
                self.spectral_library.changeAttributeValue(profile.id(), cob_out_index, co)
                self.spectral_library.changeAttributeValue(profile.id(), cob_ratio_index, cr)

        # Export to new library
        self.spectral_library.exportProfiles(self.browseOut.filePath())

        self.progressBar.setValue(100)


def _run():
    from qgis.core import QgsApplication
    app = QgsApplication([], True)
    app.initQgis()

    z = EarMasaCobWidget()
    z.show()

    app.exec_()


if __name__ == '__main__':
    _run()
