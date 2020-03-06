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

__authors__ = ["H. Payno"]
__license__ = "MIT"
__date__ = "04/03/2019"


from Orange.widgets import widget, gui
from Orange.widgets.settings import Setting
from orangecontrib.tomwer.orange.settings import CallbackSettingsHandler
from Orange.widgets.widget import Input, Output
from tomwer.synctools.stacks.reconstruction.axis import AxisProcessThreaded
from tomwer.synctools.axis import QAxisRP
from tomwer.gui.reconstruction.axis import AxisWindow
from tomwer.core.scan.scanbase import TomoBase
from tomwer.core.process.reconstruction.axis.mode import AxisMode
from silx.gui import qt

import logging

logger = logging.getLogger(__name__)


class AxisOW(widget.OWWidget, AxisProcessThreaded):
    """
    Widget used to defined the center of rotation axis to be used for a
    reconstruction.

    :param bool _connect_handler: True if we want to store the modifications
                      on the setting. Need for unit test since
                      keep alive qt widgets.
    """
    name = "center of rotation calculation"
    id = "orange.widgets.tomwer.axis"
    description = "use to compute the center of rotation"
    icon = "icons/axis.png"
    priority = 14
    category = "esrfWidgets"
    keywords = ["tomography", "axis", "tomwer", "reconstruction", "rotation",
                "position", "ftseries"]

    want_main_area = True
    resizing_enabled = True
    allows_cycle = True
    compress_signal = False

    settingsHandler = CallbackSettingsHandler()

    sigScanReady = qt.Signal()
    """Signal emitted when a scan is ready"""
    if qt._qt.BINDING == 'PyQt4':
        sigComputationStarted = qt.Signal()
        """need redefinition for pyqt4"""
        sigComputationEnded = qt.Signal()
        """need redefinition for pyqt4"""
    _rpSetting = Setting(dict())
    "AxisRP store as dict"

    class Inputs:
        data_in = Input(name=AxisProcessThreaded.inputs[0].name,
                        type=AxisProcessThreaded.inputs[0].type,
                        doc=AxisProcessThreaded.inputs[0].doc,)
        data_recompute_axis = Input(name=AxisProcessThreaded.inputs[1].name,
                                    type=AxisProcessThreaded.inputs[1].type,
                                    doc=AxisProcessThreaded.inputs[1].doc,)

    assert len(AxisProcessThreaded.outputs) == 1
    class Outputs:
        data_out = Output(name=AxisProcessThreaded.outputs[0].name,
                          type=AxisProcessThreaded.outputs[0].type,
                          doc=AxisProcessThreaded.outputs[0].doc,)


    def __init__(self, parent=None, _connect_handler=True):
        self.__lastAxisProcessParamsCache = None
        self.__scan = None
        self.__skip_exec = False
        self._n_skip = 0
        recons_params = QAxisRP()
        if self._rpSetting != dict():
            try:
                recons_params.load_from_dict(self._rpSetting)
            except Exception as e:
                logger.error('fail to load reconstruction settings:', str(e))

        widget.OWWidget.__init__(self, parent)
        AxisProcessThreaded.__init__(self, axis_params=recons_params)

        self._widget = AxisWindow(parent=self, axis_params=recons_params)

        self._layout = gui.vBox(self.mainArea, self.name).layout()
        self._layout.setContentsMargins(0, 0, 0, 0)

        self._layout.addWidget(self._widget)

        if _connect_handler:
            self.settingsHandler.addCallback(self._updateSettingsVals)

        # connect Signal / Slot
        self._widget.sigComputationRequested.connect(self.__compute)
        self._widget.sigApply.connect(self.__validate)
        self._widget.sigAxisEditionLocked.connect(self.__lockReconsParams)
        self.sigComputationStarted.connect(self._startProcessing)
        self.sigComputationEnded.connect(self._endProcessing)
        # connect sinogram calculation signal
        self._widget._sinogramAxis.sigSinoLoadStarted.connect(self._startProcessing)
        self._widget._sinogramAxis.sigSinoLoadEnded.connect(self._endProcessing)

        # expose API
        self.setLocked = self._widget.setLocked
        self.getAxis = self._widget.getAxis

    def _startProcessing(self, *args, **kwargs):
        self._widget._disableForProcessing()
        self.processing_state(scan=self._scan_currently_computed, working=True)

    def _endProcessing(self):
        self.processing_state(scan=self._scan_currently_computed, working=False)
        self._widget._enableForProcessing()

    def __compute(self):
        if self.__scan:
            if self._axis_params.mode is not AxisMode.manual:
                r1, r2 = self.get_inputs_urls(self.__scan)
                if r1 is None:
                    self._informNoProjFound(self.__scan)
                    return

            self.__lastAxisProcessParamsCache = self.recons_params.to_dict()
            # copy url which are specific to the scan
            self._axis_params.axis_url_1 = self.__scan.axis_params.axis_url_1
            self._axis_params.axis_url_2 = self.__scan.axis_params.axis_url_2
            self.__scan.axis_params.sinogram_line = self._axis_params.sinogram_line
            self.__scan.axis_params.calculation_input_type = self._axis_params.calculation_input_type
            self.__scan.axis_params.sinogram_subsampling = self._axis_params.sinogram_subsampling
            return self.compute(self.__scan, wait=False)

    def __validate(self):
        """Validate the current scan and move the scan to the next process.
        The Axis will process the next scan in the stack.
        """
        if self.__scan:
            # if parameters have changed since last processing,
            # reprocess axis method
            if self.recons_params.to_dict() != self.__lastAxisProcessParamsCache:
                r1, r2 = self.get_inputs_urls(self.__scan)
                if r1 is None:
                    self._informNoProjFound(self.__scan)
                    return

                self.compute(scan=self.__scan, wait=True)

            self.accept()
            self.scan_ready(scan=self.__scan)
        self.hide()

    def __lockReconsParams(self, lock):
        self.lock_position_value(lock)

    def scan_ready(self, scan):
        assert isinstance(scan, TomoBase)
        self._process_end(scan, scan.axis_params.value)

        self.Outputs.data_out.send(scan)
        self.sigScanReady.emit()
        self._process_next()

    def _process(self, scan=None):
        """overwrite for updating gui"""
        # if the widget is locked then we are in a mode which does not
        # require any computation, just a copy of the axis position and not
        # any user interaction.
        if self.isLocked():
            self.__scan = scan
            self.__validate()
        else:
            self.__scan = scan
            if not self.__skip_exec:
                self.activateWindow()
                self.raise_()
                self.show()
            else:
                self._n_skip += 1
                return super()._process(scan=scan)

    def _informNoProjFound(self, scan):
        msg = qt.QMessageBox(self)
        msg.setIcon(qt.QMessageBox.Warning)
        text = "Unable to find url to compute the axis of `%s`" % scan.path or 'no path given'
        text += ", please select them from the `axis input` tab"
        msg.setText(text)
        msg.exec_()

    def _updateSettingsVals(self):
        self._rpSetting = self._axis_params.to_dict()

    def _skip_exec(self, b):
        """util function used for unit test. If activate, skip the call to
        self.exec() in process"""
        self.__skip_exec = b

    @property
    def recons_params(self):
        return self._axis_params

    def _instanciateReconsParams(self):
        return QAxisRP()

    def _lock_axis_controls(self, lock):
        """

        :param bool lock: lock the axis controls to avoid modification of the
                          requested options, method... of the axis calculation
                          when this value is under calculation.
        """
        self._widget.setLocked(lock)

    def isLocked(self):
        return self._widget.isLocked()

    @Inputs.data_in
    def process(self, scan):
        if scan is None:
            return

        if self.isLocked():
            if scan.axis_params is None:
                scan.axis_params = QAxisRP()
            scan.axis_params.copy(self._axis_params, copy_axis_url=False)
            self.scan_ready(scan)
        else:
            self._widget.setScan(scan=scan)

            if self._axis_params.mode is not AxisMode.manual:
                r1, r2 = self.get_inputs_urls(scan)
                if r1 is None:
                    self.__scan = scan
                    self._informNoProjFound(scan)
                    return
            self.add(scan)

    @Inputs.data_recompute_axis
    def reprocess(self, scan):
        """Recompute the axis for scan"""
        # for now The behavior for reprocessing is the sama as for processing
        self.process(scan=scan.instance)

    def close(self):
        logger.info('close AxisOW')
        self.stop()
        super(AxisOW, self).close()

    def processing_state(self, scan, working: bool) -> None:
        # default orange version don't have Processing.
        try:
            if working:
                self.processing_info('processing %s' % scan.path if scan else '')
            else:
                self.Processing.clear()
        except Exception:
            pass
