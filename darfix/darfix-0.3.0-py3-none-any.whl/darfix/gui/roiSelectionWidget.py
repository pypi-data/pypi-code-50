# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016-2017 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ###########################################################################*/


__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "06/12/2019"

# import os

import logging
import numpy

from silx.gui import qt
from silx.gui.colors import Colormap
from silx.gui.plot.StackView import StackViewMainWindow
from silx.gui.plot.items.roi import RectangleROI
from silx.gui.plot.tools.roi import RegionOfInterestManager, RegionOfInterestTableWidget

import darfix
from darfix.core.roi import apply_3D_ROI


_logger = logging.getLogger(__file__)


class ROISelectionWidget(qt.QWidget):
    """
    Widget that allows the user to pick a ROI in any image of the dataset.
    """
    sigComputed = qt.Signal(list, list)

    def __init__(self, parent=None):
        qt.QWidget.__init__(self, parent)

        self.roi = None

        self.setLayout(qt.QVBoxLayout())
        self._sv = StackViewMainWindow()
        _buttons = qt.QDialogButtonBox(parent=self)
        self._okB = _buttons.addButton(_buttons.Ok)
        self._applyB = _buttons.addButton(_buttons.Apply)
        self._resetB = _buttons.addButton(_buttons.Reset)

        self._applyB.clicked.connect(self.applyRoi)
        self._okB.clicked.connect(self.apply)
        self._resetB.clicked.connect(self.resetStack)

        self._sv.setColormap(Colormap(name=darfix.config.DEFAULT_COLORMAP_NAME,
                                      normalization='linear',
                                      vmin=None,
                                      vmax=None))
        self.layout().addWidget(self._sv)
        self.layout().addWidget(_buttons)

        plot = self._sv.getPlot()
        self._roiManager = RegionOfInterestManager(plot)
        self._roiTable = RegionOfInterestTableWidget()
        self._roiTable.setRegionOfInterestManager(self._roiManager)

        self._roi = RectangleROI()
        self._roi.setLabel('ROI')
        self._roi.setGeometry(origin=(0, 0), size=(10, 10))
        self._roi.setEditable(True)
        self._roiManager.addRoi(self._roi)
        self._roiTable.setColumnHidden(4, True)

        # Add the region of interest table and the buttons to a dock widget
        widget = qt.QWidget()
        layout = qt.QVBoxLayout()
        widget.setLayout(layout)
        layout.addWidget(self._roiTable)

        def roiDockVisibilityChanged(visible):
            """Handle change of visibility of the roi dock widget.

            If dock becomes hidden, ROI interaction is stopped.
            """
            if not visible:
                self._roiManager.stop()

        dock = qt.QDockWidget('Image ROI')
        dock.setWidget(widget)
        dock.visibilityChanged.connect(roiDockVisibilityChanged)
        plot.addTabbedDockWidget(dock)

    def setDataset(self, dataset):
        """
        Dataset setter. Saves the dataset and updates the stack with the dataset
        data.

        :param Dataset dataset: dataset to be used in the widget.
        """
        self.dataset = dataset
        self.setStack(dataset.data)

    def setStack(self, *arg, **kwargs):
        """
        Sets the data passed as arguments in the stack.
        Mantains the current frame showed in the view.
        """
        first_frame_shape = self.dataset.data[0].shape
        self.setRoi(center=(first_frame_shape[1] / 2, first_frame_shape[0] / 2),
                    size=(first_frame_shape[1] / 5, first_frame_shape[0] / 5))
        nframe = self._sv.getFrameNumber()
        self._sv.setStack(*arg, **kwargs)
        self._sv.setFrameNumber(nframe)

    def setRoi(self, roi=None, origin=None, size=None, center=None):
        """
        Sets a region of interest of the stack of images.

        :param RectangleROI roi: A region of interest.
        :param Tuple origin: If a roi is not provided, used as an origin for the roi
        :param Tuple size: If a roi is not provided, used as a size for the roi.
        :param Tuple center: If a roi is not provided, used as a center for the roi.
        """
        if roi is not None and (size is not None or center is not None or origin is not None):
            _logger.warning("Only using provided roi, the rest of parameters are omitted")

        if roi is not None:
            self._roi = roi
        else:
            self._roi.setGeometry(origin=origin, size=size, center=center)

    def getRoi(self):
        """
        Returns the roi selected in the stackview.

        :rtype: silx.gui.plot.items.roi.RectangleROI
        """
        return self._roi

    def applyRoi(self):
        """
        Function to apply the region of interest at the data of the dataset
        and show the new data in the stack. Dataset data is not yet replaced.
        A new roi is created in the middle of the new stack.
        """
        self.roi = RectangleROI()
        self.roi.setGeometry(origin=self.getRoi().getOrigin(), size=self.getRoi().getSize())
        frames = apply_3D_ROI(self._sv.getStack()[0], size=numpy.flip(self.roi.getSize()),
                              center=numpy.flip(self.roi.getCenter()))

        self.setStack(frames)
        self.resetROI()

    def apply(self):
        """
        Function that replaces the dataset data with the data shown in the stack of images.
        If the stack has a roi applied, it applies the same roi to the dark frames of the dataset.
        Signal emitted with the roi parameters.
        """
        self.dataset.data = self._sv.getStack()[0]
        if self.roi:
            if len(self.dataset.dark_frames):
                self.dataset.dark_frames = apply_3D_ROI(self.dataset.dark_frames,
                                                        self.roi.getSize() / 2, numpy.flip(self.roi.getCenter()))
            self.sigComputed.emit(self.roi.getOrigin().tolist(), self.roi.getSize().tolist())
        else:
            self.sigComputed.emit([], [])

    def resetROI(self):
        """
        Sets the region of interest in the middle of the stack, with size 1/5 of the image.
        """
        frame_shape = numpy.array(self._sv.getStack()[0][0].shape)
        center = numpy.flip(frame_shape) / 2
        size = numpy.flip(frame_shape) / 5
        self.setRoi(center=center, size=size)

    def resetStack(self):
        """
        Restores stack with the dataset data.
        """
        self.roi = None
        self.setStack(self.dataset.data)

    def clearStack(self):
        """
        Clears stack.
        """
        self._okB.setEnabled(False)
        self._sv.setStack(None)
        self._roi.setGeometry(origin=(0, 0), size=(10, 10))
