# -*- coding: utf-8 -*-
"""
| ----------------------------------------------------------------------------------------------------------------------
| Date                : September 2018
| Copyright           : (C) 2018 by Ann Crabbé (KU Leuven)
| Email               : ann.crabbe@kuleuven.be
|
| This program is free software; you can redistribute it and/or modify it under the terms of the GNU
| General Public License as published by the Free Software Foundation; either version 3 of the
| License, or any later version.
| ----------------------------------------------------------------------------------------------------------------------
"""
import os
import sys
import tempfile
from osgeo import gdal
from qgis.gui import QgsFileWidget
from qgis.core import QgsRasterLayer, QgsProject, QgsMapLayerProxyModel, QgsProviderRegistry
from qgis.utils import iface
from qgis.PyQt.uic import loadUi
from qgis.PyQt.QtWidgets import QDialog, QFileDialog, QDialogButtonBox
from mesma.io import EmittingStream
from mesma.io.imports import import_band_names
from mesma.io.operators import ShadeNormalisationOperator, GUIProgressBar
from mesma.gui.logo_gui import LogoWidget
from mesma.sitepackages.hubdc.applier import Applier, ApplierInputRaster, ApplierOutputRaster


class ShadeNormalisationWidget(QDialog):
    """ QDialog to interactively set up the Shade Normalisation input and output. """

    def __init__(self):
        super(ShadeNormalisationWidget, self).__init__()
        loadUi(os.path.join(os.path.dirname(__file__), 'shade_normalisation.ui'), self)
        sys.stdout = EmittingStream(self.tabWidget)
        sys.stderr = EmittingStream(self.tabWidget)

        # Logo
        self.logoLayout.addWidget(LogoWidget(parent=self.logoWidget))

        # image
        self.inputComboBox.setFilters(QgsMapLayerProxyModel.RasterLayer)
        self.inputAction.triggered.connect(self._image_browse)
        self.inputButton.setDefaultAction(self.inputAction)

        # output
        self.outputFileWidget.setStorageMode(QgsFileWidget.SaveFile)
        self.outputFileWidget.lineEdit().setPlaceholderText('[Create temporary layer]')
        self.outputFileWidget.lineEdit().setReadOnly(True)

        # Open in QGIS?
        try:
            iface.activeLayer
        except AttributeError:
            self.openInQGIS.setChecked(False)
            self.openInQGIS.setDisabled(True)

        # run or cancel
        self.OKClose.button(QDialogButtonBox.Ok).setText("Run")
        self.OKClose.accepted.connect(self._run_shade_normalisation)
        self.OKClose.rejected.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def _image_browse(self):
        """ Browse for an image raster file. """

        path = QFileDialog.getOpenFileName(filter=QgsProviderRegistry.instance().fileRasterFilters())[0]

        if len(path) > 0:
            gdal.UseExceptions()
            try:
                layer = QgsRasterLayer(path, os.path.basename(path), 'gdal')
                assert layer.isValid()
            except AssertionError:
                print("'" + path + "' not recognized as a supported file format.", file=sys.stderr)
                return

            QgsProject.instance().addMapLayer(layer, True)
            self.inputComboBox.setLayer(layer)

    def _run_shade_normalisation(self):
        """ Read all parameters and pass them on to the ShadeNormalisationOperator. """

        # Image chosen?
        try:
            image_path = self.inputComboBox.currentLayer().source()
        except AttributeError:
            print("Select a MESMA Fractions image as input.", file=sys.stderr)
            return

        # Shade band present?
        band_names, shade_band_index = import_band_names(image_path)

        if not shade_band_index:
            print("No band found with the name 'shade_fraction'. Already normalized or not a MESMA Fractions image.")
            return

        # Only temp file possible when result is opened in QGIS
        output_path = self.outputFileWidget.filePath()
        if not self.openInQGIS.isChecked() and len(output_path) == 0:
            print("If you won't open the result in QGIS, you must select an output file.", file=sys.stderr)
            return

        if len(output_path) == 0:
            basename, extension = os.path.splitext(os.path.basename(image_path))
            output_path = os.path.join(tempfile.gettempdir(), basename + "_normalized" + extension)

        # set up the applier
        applier = Applier()
        applier.controls.setProgressBar(GUIProgressBar(q_progress_bar=self.progressBar))
        applier.inputRaster.setRaster(key='raster', value=ApplierInputRaster(filename=image_path))
        applier.outputRaster.setRaster(key='fractions', value=ApplierOutputRaster(filename=output_path))

        # apply shade normalisation
        applier.apply(operatorType=ShadeNormalisationOperator, band_names=band_names, shade_band=shade_band_index)
        print("Done.")

        if self.openInQGIS.isChecked():
            new_layer = QgsRasterLayer(output_path, "Normalized Fractions")
            QgsProject.instance().addMapLayer(new_layer, True)


def _run():
    from qgis.core import QgsApplication
    app = QgsApplication([], True)
    app.initQgis()

    z = ShadeNormalisationWidget()
    z.show()

    app.exec_()


if __name__ == '__main__':
    _run()
