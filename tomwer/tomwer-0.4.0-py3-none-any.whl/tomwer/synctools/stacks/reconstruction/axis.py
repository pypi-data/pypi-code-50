# coding: utf-8
###########################################################################
# Copyright (C) 2016-2019 European Synchrotron Radiation Facility
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
#############################################################################

__authors__ = ["H.Payno"]
__license__ = "MIT"
__date__ = "03/05/2019"


from tomwer.core.process.reconstruction.axis import AxisProcess
from tomwer.core.process.reconstruction.axis.axis import NoAxisUrl
from tomwer.core.process.reconstruction.axis.mode import AxisMode
from tomwer.core.scan.scanbase import TomoBase
from tomwer.core.settings import get_lbsram_path, isOnLbsram
from tomwer.core.utils import isLowOnMemory
from ..processingstack import FIFO, ProcessingThread
from silx.gui import qt
import logging

_logger = logging.getLogger(__name__)


class AxisProcessThreaded(AxisProcess, FIFO):
    """Implementation of the `.AxisProcess` but having a stack for treating
    scans and making computation in threads"""

    def __init__(self, axis_params):
        AxisProcess.__init__(self, axis_params=axis_params)
        FIFO.__init__(self)
        assert self._axis_params is not None

    def _process_computation(self, scan):
        assert isinstance(scan, TomoBase)
        mode = self._axis_params.mode
        if not self._axis_params.use_sinogram and mode in (AxisMode.manual, AxisMode.read):
            # If mode is read or manual the position_value is not computed and
            # we will keep the actual one (should have been defined previously)
            self._end_computation(scan=scan)
        elif isOnLbsram() and isLowOnMemory(get_lbsram_path()) is True:
            # if computer is running into low memory on lbsram skip it
            mess = 'low memory, skip axis calculation', scan.path
            _logger.processSkipped(mess)
            scan.axis_params.value = None
            # TODO: all process
            self.scan_ready(scan=scan)
        elif not self._axis_params.use_sinogram and not mode in self.RADIO_CALCULATIONS_METHODS:
            _logger.warning('no method defined to compute', mode)
            self._process_next()
        else:
            scan.axis_params.value = '...'
            self._axis_params.value = '...'
            assert self._axis_params.value == '...'
            self._scan_currently_computed = scan
            self._computationThread.init(scan=scan,
                                         axis_params=self._axis_params)
            # need to manage connect before starting it because
            self._computationThread.finished.connect(self._end_threaded_computation)

            self._computationThread.start()

    def _process(self, scan):
        return AxisProcess.process(self, scan)

    def _end_computation(self, scan):
        """
        callback when the computation thread is finished

        :param scan: pass if no call to '_computationThread is made'
        """
        assert isinstance(scan, TomoBase)
        assert self._axis_params is not None
        # copy result computed on scan on the AxisProcess reconsparams
        self._axis_params.value = scan.axis_params.value  # noqa
        FIFO._end_computation(self, scan)

    def _end_threaded_computation(self):
        assert self._scan_currently_computed is not None
        self._axis_params.value = self._computationThread.center_of_rotation
        self._computationThread.finished.disconnect(self._end_threaded_computation)
        FIFO._end_threaded_computation(self)

    def _create_processing_thread(self) -> qt.QThread:
        return _ProcessingThread()

    def stop(self):
        self.queue.clear()
        self._computationThread.blockSignals(True)
        self._computationThread.wait()


class _ProcessingThread(ProcessingThread):
    """
    Thread use to execute the processing of the axis position
    """
    def __init__(self):
        ProcessingThread.__init__(self)
        self._scan = None
        self._axis_params = None
        """function pointer to know which function to call for the axis
        calculation"""
        self.__patch = {}
        """Used to patch some calculation method (for test purpose)"""

    def init(self, scan, axis_params):
        self._scan = scan
        self._axis_params = axis_params

    def run(self):
        self.sigComputationStarted.emit()
        axis = AxisProcess(axis_params=self._axis_params)
        axis = self.apply_patch(axis=axis)
        try:
            axis.process(self._scan)
        except NoAxisUrl as e:
            self.center_of_rotation = None
            _logger.error(str(e))
        except Exception as e:
            _logger.error(str(e))
            self.center_of_rotation = None
        else:
            self.center_of_rotation = self._scan.axis_params.value

    def patch_calc_method(self, mode, function):
        self.__patch[mode] = function

    def apply_patch(self, axis):
        for mode, patch_fct in self.__patch.items():
            if mode in AxisMode:
                axis.RADIO_CALCULATIONS_METHODS[mode] = patch_fct
        return axis
