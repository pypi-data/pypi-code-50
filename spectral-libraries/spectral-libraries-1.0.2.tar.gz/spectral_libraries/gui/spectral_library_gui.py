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
from spectral_libraries.sitepackages.qps.speclib.core import SpectralProfile as qpsProfile, SpectralLibrary as qpsLibrary
from spectral_libraries.sitepackages.qps.speclib.gui import SpectralLibraryWidget as qpsWidget
from spectral_libraries.sitepackages.qps.maptools import CursorLocationMapTool as qpsMapTool
from spectral_libraries.sitepackages.qps.utils import SpatialPoint as qpsPoint
from spectral_libraries.sitepackages.qps.utils import SpatialExtent as qpsExtent
from spectral_libraries.sitepackages.qps import initResources
initResources()


class SpectralLibraryWidget(qpsWidget):
    """
    QDialog to interactively work with Spectral Libraries in QGIS.
    """

    def __init__(self, spectral_library: qpsLibrary = None, map_canvas: QgsMapCanvas = None):
        super(SpectralLibraryWidget, self).__init__(speclib=spectral_library, mapCanvas=map_canvas)

        self.viper_map_tool = None  # will be created later

        self.setMapInteraction(True)
        self.sigLoadFromMapRequest.connect(self.onActivateMapTool)              # pyqtSignal()
        self.sigMapExtentRequested.connect(self.onZoomToSelected)               # pyqtSignal(SpatialExtent)
        self.sigMapCenterRequested.connect(self.onPanToSelected)                # pyqtSignal(SpatialPoint)

    def onZoomToSelected(self, bbox: qpsExtent):
        """
        Zoom to the selected rows in the Spectral Library
        :param bbox: bounding box in SpatialExtent format as defined in the qps package
        """
        crs = self.viper_canvas.mapSettings().destinationCrs()
        new_bbox = bbox.toCrs(crs)
        if isinstance(new_bbox, qpsExtent):
            self.viper_canvas.setExtent(new_bbox)

    def onPanToSelected(self, center: qpsPoint):
        """
        Pan to the selected rows in the Spectral Library
        :param center: point in SpatialPoint format as defined in the qps package
        """
        crs = self.viper_canvas.mapSettings().destinationCrs()
        new_point = center.toCrs(crs)
        if isinstance(new_point, qpsPoint):
            self.viper_canvas.setCenter(new_point)

    def onActivateMapTool(self):
        """
        Activates a map tool that informs on clicked map locations.
        """
        self.viper_map_tool = qpsMapTool(self.viper_canvas)
        self.viper_map_tool.sigLocationRequest[qpsPoint, QgsMapCanvas].connect(self.onLocationClicked)
        self.viper_canvas.setMapTool(self.viper_map_tool)

    def onLocationClicked(self, spatial_point: qpsPoint, map_canvas: QgsMapCanvas):
        """
        Reacts on clicks to the QGIS Map canvas
        :param spatial_point: point in SpatialPoint format as defined in the qps package
        :param map_canvas: QgsMapCanvas
        """
        profiles = qpsProfile.fromMapCanvas(map_canvas, spatial_point)

        # filter & modify profiles here before sending them to a SpectralLibraryWidget
        # e.g. change profile names

        self.setCurrentProfiles(profiles)


def _run():
    from qgis.core import QgsApplication
    from spectral_libraries.sitepackages.qps.testing import QgisMockup

    app = QgsApplication([], True)
    app.initQgis()

    mock = QgisMockup()
    canvas = mock.mapCanvas()
    z = SpectralLibraryWidget(map_canvas=canvas)
    z.show()

    app.exec_()


if __name__ == '__main__':
    _run()
