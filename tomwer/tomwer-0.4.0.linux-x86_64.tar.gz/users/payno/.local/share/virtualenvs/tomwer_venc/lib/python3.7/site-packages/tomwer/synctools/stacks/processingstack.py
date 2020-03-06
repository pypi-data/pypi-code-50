# coding: utf-8
###########################################################################
# Copyright (C) 2016 European Synchrotron Radiation Facility
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
"""Define some processing stack"""

__authors__ = ["H.Payno"]
__license__ = "MIT"
__date__ = "08/01/2020"


from queue import Queue
from silx.gui import qt


class ProcessingThread(qt.QThread):
    """Class for running some processing"""

    sigComputationStarted = qt.Signal()
    """Signal emitted when a computation is started"""


class FIFO(Queue):
    """Processing Queue with a First In, First Out behavior"""

    sigComputationStarted = qt.Signal()
    """Signal emitted when a computation is started"""
    sigComputationEnded = qt.Signal()
    """Signal emitted when a computation is ended"""

    def __init__(self):
        Queue.__init__(self)
        self._computationThread = self._create_processing_thread()
        assert isinstance(self._computationThread, ProcessingThread)
        self._computationThread = self._create_processing_thread()
        self._computationThread.sigComputationStarted.connect(self._start_threaded_computation)
        """scan process by the thread"""
        self._scan_currently_computed = None
        """Scan computed currently"""

    def add(self, scan):
        """"""
        Queue.put(self, scan)
        if self.can_process_next():
            self._process_next()

    def _process(self, scan):
        raise NotImplementedError('Virtual class')

    def _process_next(self):
        if Queue.empty(self):
            return

        scan = Queue.get(self)
        self._process(scan)

    def can_process_next(self):
        """
        :return: True if the computation thread is ready to compute
        a new axis position
        :rtype: bool
        """
        return not self._computationThread.isRunning()

    def _end_computation(self, scan):
        """
        callback when the computation thread is finished

        :param scan: pass if no call to '_computationThread is made'
        """
        self.sigComputationEnded.emit()
        if self.can_process_next():
            self._process_next()

    def _create_processing_thread(self) -> ProcessingThread:
        raise NotImplementedError('Virtual class')

    def is_computing(self):
        """Return True if processing thread is running (mean that computation
        is on going)"""
        return self._computationThread.isRunning()

    def wait_computation_finished(self):
        """
        Wait until the computation is finished
        """
        if self._computationThread.isRunning():
            self._computationThread.wait()

    def _start_threaded_computation(self, *args, **kwargs):
        self.sigComputationStarted.emit()

    def _end_threaded_computation(self):
        self._end_computation(scan=self._scan_currently_computed)
