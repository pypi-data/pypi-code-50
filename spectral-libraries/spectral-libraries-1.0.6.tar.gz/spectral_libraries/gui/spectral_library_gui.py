# -*- coding: utf-8 -*-
"""
| ----------------------------------------------------------------------------------------------------------------------
| Date                : November 2019
| Copyright           : (C) 2018 by Ann Crabbé (KU Leuven) and Benjamin Jakimow (HU Berlin)
| Email               : ann.crabbe@kuleuven.be
| Acknowledgements    : Extension on QGIS Plugin Support (QPS)
|                       Benjamin Jakimow (HU Berlin) https://bitbucket.org/jakimowb/qgispluginsupport
|
| This program is free software; you can redistribute it and/or modify it under the terms of the GNU
| General Public License as published by the Free Software Foundation; either version 3 of the
| License, or any later version.
| ----------------------------------------------------------------------------------------------------------------------
"""
from qgis.gui import QgsMapCanvas

from spectral_libraries.sitepackages.qps.speclib.core import SpectralProfile as qpsProfile, SpectralLibrary as qpsLib
from spectral_libraries.sitepackages.qps.speclib.gui import SpectralLibraryWidget as qpsWidget
from spectral_libraries.sitepackages.qps.maptools import CursorLocationMapTool as qpsMapTool
from spectral_libraries.sitepackages.qps.utils import SpatialPoint as qpsPoint
from spectral_libraries.sitepackages.qps import initResources
initResources()


class SpectralLibraryWidget(qpsWidget):
    """
    QDialog to interactively work with Spectral Libraries in QGIS.
    """

    def __init__(self, spectral_library: qpsLib = None, map_canvas: QgsMapCanvas = None):
        super(SpectralLibraryWidget, self).__init__(speclib=spectral_library, mapCanvas=map_canvas)

        self.map_tool = None

        self.setMapInteraction(True)
        self.sigLoadFromMapRequest.connect(self.onActivateMapTool)              # pyqtSignal()

    def onActivateMapTool(self):
        """
        Activates a map tool that informs on clicked map locations.
        """
        self.map_tool = qpsMapTool(self.canvas(), showCrosshair=True)
        self.map_tool.sigLocationRequest[qpsPoint, QgsMapCanvas].connect(self.onLocationClicked)
        self.canvas().setMapTool(self.map_tool)

    def onLocationClicked(self, spatial_point: qpsPoint, map_canvas: QgsMapCanvas):
        """
        Reacts on clicks to the QGIS Map canvas
        :param spatial_point: point in SpatialPoint format as defined in the qps package
        :param map_canvas: QgsMapCanvas
        """
        profiles = qpsProfile.fromMapCanvas(map_canvas, spatial_point)
        self.setCurrentProfiles(profiles)


def _run():
    from qgis.core import QgsApplication
    app = QgsApplication([], True)
    app.initQgis()

    z = SpectralLibraryWidget()
    z.show()

    app.exec_()


def _testing():
    from spectral_libraries.sitepackages.qps.testing import start_app
    app = start_app()

    import os
    from qgis.gui import QgisInterface
    from qgis.core import QgsRasterLayer, QgsProject
    from spectral_libraries.sitepackages.qps.testing import QgisMockup

    from qgis.utils import iface
    assert isinstance(iface, QgisInterface)
    if isinstance(iface, QgisMockup):
        iface.ui.show()

    canvas = iface.mapCanvas()
    assert isinstance(canvas, QgsMapCanvas)

    raster_layer = QgsRasterLayer(os.path.join(os.path.dirname(__file__), '../../tests/data/testdata'),
                                  baseName='testdata')
    QgsProject.instance().addMapLayer(raster_layer)

    canvas.setLayers([raster_layer])
    canvas.setDestinationCrs(raster_layer.crs())
    canvas.setExtent(raster_layer.extent())

    widget = SpectralLibraryWidget(map_canvas=canvas)
    widget.show()

    app.exec_()


if __name__ == '__main__':
    _testing()
