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
"""
contains gui relative to axis calculation using sinogram
"""

__authors__ = ["H. Payno"]
__license__ = "MIT"
__date__ = "14/10/2019"


from silx.gui import qt
from .radioaxis import RadioAxisWindow
from .sinogramaxis import SinogramAxisWindow
from ...utils.scandescription import ScanNameLabel
import logging
from contextlib import ContextDecorator

_logger = logging.getLogger(__file__)


class _AxisTypeSelection(qt.QGroupBox):
    sigSelectionChanged = qt.Signal(str)
    """Signal emitted when the selection changed. Value can be `sinogram` or
    `radio`"""

    def __init__(self, parent):
        qt.QGroupBox.__init__(self, parent=parent)
        self.setTitle('compute center of rotation from')
        self.setLayout(qt.QHBoxLayout())
        self._radioRB = qt.QRadioButton('radios', parent=self)
        self.layout().addWidget(self._radioRB)

        self._sinogramRB = qt.QRadioButton('sinogram', parent=self)
        self.layout().addWidget(self._sinogramRB)

        # Signal / Slot connections
        self._radioRB.toggled.connect(self._selectionChanged)
        self._sinogramRB.toggled.connect(self._selectionChanged)

    def getSelection(self):
        if self._radioRB.isChecked():
            return 'radio'
        else:
            return 'sinogram'

    def setSelection(self, selection):
        if selection == 'radio':
            self._radioRB.setChecked(True)
        elif selection == 'sinogram':
            self._sinogramRB.setChecked(True)
        else:
            raise ValueError('invalid selection given')

    def _selectionChanged(self, *args, **kwargs):
        self.sigSelectionChanged.emit(self.getSelection())


class AxisWindow(qt.QMainWindow):
    """Main widget for the axis calculation"""

    sigComputationRequested = qt.Signal()
    """signal emitted when a computation is requested"""

    sigApply = qt.Signal()
    """signal emitted when the axis reconstruction parameters are validated"""

    sigAxisEditionLocked = qt.Signal(bool)
    """Signal emitted when the status of the reconstruction parameters edition
    change"""

    class _RadioSinoLocker(ContextDecorator):
        """Simple cntextManager for the radio and sinogram axis synchronization"""
        def __init__(self, parent):
            self.__parent = parent
            self.old_radio = None
            self.old_sinogram = None
            self.__locked = False

        def __enter__(self):
            self.old_radio = self.radioAxis.blockSignals(True)
            self.old_sinogram = self.sinogramAxis.blockSignals(True)

        @property
        def radioAxis(self):
            return self.__parent._radioAxis

        @property
        def sinogramAxis(self):
            return self.__parent._sinogramAxis

        def __exit__(self, exc_type, exc_val, exc_tb):
                self.radioAxis.blockSignals(self.old_radio)
                self.sinogramAxis.blockSignals(self.old_sinogram)

        def isLocked(self):
            return self.__locked

        def setLocked(self, locked):
            if locked == self.__locked:
                return
            else:
                self.__locked = locked
                # block widgets signals
                with self:
                    self.radioAxis.setLocked(locked)
                    self.sinogramAxis.setLocked(locked)


    def __init__(self, axis_params, parent=None):
        qt.QMainWindow.__init__(self, parent=parent)
        self.__locker = AxisWindow._RadioSinoLocker(self)
        self._axis_params = axis_params
        self._mainWidget = qt.QWidget()
        self._mainWidget.setLayout(qt.QVBoxLayout())

        self._radioAxis = RadioAxisWindow(parent=self, axis=axis_params)
        self._sinogramAxis = SinogramAxisWindow(parent=self, axis=axis_params)

        # add scan name
        self._scan_label = ScanNameLabel(parent=self)
        self._mainWidget.layout().addWidget(self._scan_label)

        # add selection
        self._selectionGB = _AxisTypeSelection(parent=self)
        self._mainWidget.layout().addWidget(self._selectionGB)

        # add widget for radio and sinogram axis
        self._mainWidget.layout().addWidget(self._radioAxis)
        self._mainWidget.layout().addWidget(self._sinogramAxis)

        self.setCentralWidget(self._mainWidget)

        # connect signal / slots
        self._selectionGB.sigSelectionChanged.connect(self._selectionChanged)
        for widget in self._radioAxis, self._sinogramAxis:
            widget.sigApply.connect(self._applyRequested)
            widget.sigAxisEditionLocked.connect(self.setLocked)
            widget.sigComputationRequested.connect(self._computationRequested)
        self._selectionGB.sigSelectionChanged.connect(self._axisTypeChanged)

        # set up configuration
        if axis_params.use_sinogram:
            selection = 'sinogram'
        else:
            selection = 'radio'
        self._selectionGB.setSelection(selection=selection)
        self._selectionGB._selectionChanged(self._selectionGB.getSelection())

        # expose API
        self.setSelection = self._selectionGB.setSelection
        self.getSelection = self._selectionGB.getSelection

    def getAxis(self):
        return self._axis_params

    def setReconsParams(self, axis_params):
        old = self.blockSignals(True)
        self._axis_params = axis_params
        self._radioAxis.setReconsParams(axis=axis_params)
        self._sinogramAxis.setReconsParams(axis=axis_params)
        self.blockSignals(old)

    def _axisTypeChanged(self, *args, **kwargs):
        self._axis_params.use_sinogram = self._selectionGB.getSelection() == 'sinogram'

    def _disableForProcessing(self, *args, **kwargs):
        self._mainWidget.setEnabled(False)

    def _enableForProcessing(self, *args, **kwargs):
        self._mainWidget.setEnabled(True)

    def setScan(self, scan):
        """
        set the gui for this scan

        :param TomoBase scan:
        """
        self._scan_label.setScan(scan=scan)
        self._radioAxis.setScan(scan=scan)
        self._sinogramAxis.setScan(scan=scan)
        # self._enableSinogramOpt(scan.get_scan_range() == 360)

    def _selectionChanged(self, selection):
        self._radioAxis.setVisible(selection == 'radio')
        self._sinogramAxis.setVisible(selection == 'sinogram')

    def _applyRequested(self) -> None:
        self.sigApply.emit()

    def _computationRequested(self) -> None:
        self.sigComputationRequested.emit()

    def hideLockButtons(self) -> None:
        self._radioAxis._lockLabel.hide()
        self._radioAxis._lockBut.hide()
        self._sinogramAxis._options._lockLabel.hide()
        self._sinogramAxis._options._lockBut.hide()

    def hideApplyButtons(self) -> None:
        self._radioAxis._applyBut.hide()
        self._sinogramAxis._options._applyBut.hide()

    def _enableSinogramOpt(self, b):
        if self._selectionGB.getSelection() == 'sinogram' and not b:
            change_selection_to_radio = True
        else:
            change_selection_to_radio = False
        self._selectionGB._sinogramRB.setEnabled(b)
        self._sinogramAxis.setEnabled(b)
        if change_selection_to_radio:
            self._selectionGB.setSelection('radio')

    def setLocked(self, locked):
        self.__locker.setLocked(locked)

    def isLocked(self):
        return self.__locker.isLocked()

    def setPosition(self, frm: str, value: float) -> None:
        """

        :param frm:
        :type: str
        :param value:
        :type: float

        :raises: ValueError if the frm parameter is not recognized
        """
        if frm == 'radio':
            self._radioAxis.setPosition(value=value)
        elif frm == 'sinogram':
            self._sinogramAxis.setPosition(value=value)
        else:
            raise ValueError('frm parameter value is invalid', frm)
