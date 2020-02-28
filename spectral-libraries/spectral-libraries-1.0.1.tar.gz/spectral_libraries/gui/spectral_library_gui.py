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
from .sitepackages.qps.speclib.spectrallibraries import SpectralProfile as qpsProfile
from .sitepackages.qps.speclib.spectrallibraries import SpectralLibraryWidget as qpsWidget
from .sitepackages.qps.maptools import CursorLocationMapTool as qpsMapTool
from .sitepackages.qps.utils import SpatialPoint as qpsPoint
from .sitepackages.qps.utils import SpatialExtent as qpsExtent
from .sitepackages.qps import initResources
initResources()


class SpectralLibraryWidget(qpsWidget):

    def __init__(self, *args, **kwds):
        super(SpectralLibraryWidget, self).__init__(*args, **kwds)

        from qgis.utils import iface
        self.viper_canvas = iface.mapCanvas()
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

    def onLocationClicked(self, spatialPoint: qpsPoint, mapCanvas: QgsMapCanvas):
        """
        Reacts on clicks to the QGIS Map canvas
        :param spatialPoint: point in SpatialPoint format as defined in the qps package
        :param mapCanvas: QgsMapCanvas
        """
        profiles = qpsProfile.fromMapCanvas(mapCanvas, spatialPoint)

        # filter & modify profiles here before sending them to a SpectralLibraryWidget
        # e.g. change profile names

        self.setCurrentProfiles(profiles)


# THIS WORKS ONLY WITH A QGIS INTERFACE. NOT STAND ALONE
#
# def _testing():
#     import os
#     from qgis.gui import QgisInterface
#     from qgis.core import QgsRasterLayer, QgsProject
#     from vipertools.sitepackages.qps.testing import initQgisApplication, QgisMockup
#     app = initQgisApplication()
#
#     from qgis.utils import iface
#     assert isinstance(iface, QgisInterface)
#     if isinstance(iface, QgisMockup):
#         iface.ui.show()
#
#     canvas = iface.mapCanvas()
#     assert isinstance(canvas, QgsMapCanvas)
#
#     raster_layer = QgsRasterLayer(os.path.join(os.path.dirname(__file__), '../../tests/testdata/testdata'))
#     QgsProject.instance().addMapLayer(raster_layer)
#
#     canvas.setLayers([raster_layer])
#     canvas.setDestinationCrs(raster_layer.crs())
#     canvas.setExtent(raster_layer.extent())
#
#     widget = SpectralLibraryWidget()
#     widget.show()
#
#     app.exec_()
#
#
# if __name__ == '__main__':
#     _testing()
