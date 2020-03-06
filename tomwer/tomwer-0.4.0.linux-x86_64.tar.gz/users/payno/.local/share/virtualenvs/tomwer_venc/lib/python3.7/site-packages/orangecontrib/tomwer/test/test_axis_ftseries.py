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
"""contains test for relation between axis and ftseries"""


__authors__ = ["H. Payno"]
__license__ = "MIT"
__date__ = "23/10/2019"


import unittest
from orangecontrib.tomwer.test.utils import OrangeWorflowTest
from tomwer.test.utils import skip_gui_test
from tomwer.core.utils.scanutils import MockEDF
from silx.gui.utils.testutils import SignalListener
import tempfile
import shutil
import time
import os


TIMEOUT_TEST = 10

@unittest.skipIf(skip_gui_test(), reason='skip gui test')
@unittest.skip('Fail on CI...')
class TestAxisFtseries(OrangeWorflowTest):
    """
    Create the following workflow:
    datawatcherOW -> axisOW -> ftseriesOW
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.nodeDataWatcher = cls.addWidget(cls,
                                        'orangecontrib.tomwer.widgets.control.DataWatcherOW.DataWatcherOW')
        cls.nodeAxis = cls.addWidget(cls,
                                     'orangecontrib.tomwer.widgets.reconstruction.AxisOW.AxisOW')
        cls.nodeFTSerie = cls.addWidget(cls,
                                        'orangecontrib.tomwer.widgets.reconstruction.FtseriesOW.FtseriesOW')

        # Let Orange process events (node creations)
        cls.processOrangeEvents(cls)

        # linking the workflow
        cls.link(cls,
                 cls.nodeDataWatcher, "data",
                 cls.nodeAxis, "data")
        cls.link(cls,
                 cls.nodeAxis, "data",
                 cls.nodeFTSerie, "data")

        # Let Orange process events (node creations)
        cls.processOrangeEvents(cls)

        # getting the widgets
        cls.datawatcherWidget = cls.getWidgetForNode(cls, cls.nodeDataWatcher)
        cls.axisWidget = cls.getWidgetForNode(cls, cls.nodeAxis)
        cls.ftserieWidget = cls.getWidgetForNode(cls, cls.nodeFTSerie)

    @classmethod
    def tearDownClass(cls):
        for node in (cls.nodeAxis, cls.nodeFTSerie, cls.nodeDataWatcher):
            cls.removeNode(cls, node)
        cls.app.processEvents()
        del cls.nodeFTSerie
        del cls.nodeAxis
        del cls.nodeDataWatcher
        super().tearDownClass()

    def setUp(self) -> None:
        super().setUp()
        self.root_dir = tempfile.mkdtemp()
        self.scan_1_path = tempfile.mkdtemp(dir=self.root_dir)
        self.scan_2_path = tempfile.mkdtemp(dir=self.root_dir)
        self.scan_3_path = tempfile.mkdtemp(dir=self.root_dir)
        self.scan_dirs = [
            self.scan_1_path,
            self.scan_2_path,
            self.scan_3_path,
        ]

        self.mocks = []
        for scan_dir in self.scan_dirs:
            mock = MockEDF(scan_path=scan_dir, n_radio=20, n_ini_radio=20)
            assert os.path.exists(scan_dir)
            self.mocks.append(mock)

        # set up axis, ftseries and data watcher
        self.datawatcherWidget.setFolderObserved(self.root_dir)
        assert os.path.exists(self.root_dir)
        self.axisWidget._axis_params.mode = 'manual'
        self.ftserieWidget._ftserie.dry_run = True
        # self.ftserieWidget._ftserie.reconsStack.dry_run = True
        self.ftserieWidget.recons_params.axis.do_axis_correction = True
        self.ftserieWidget.recons_params.axis.use_tomwer_axis = True
        self.ftserieWidget.recons_params.axis.use_old_tomwer_axis = False

        self.axisWidget._skip_exec(True)

        # create listeners
        self.axisListener = SignalListener()
        self.ftseriesListener = SignalListener()

        # signal / slot connection
        self.axisWidget.sigScanReady.connect(self.axisListener)
        self.ftserieWidget.sigScanReady.connect(self.ftseriesListener)

    def tearDown(self) -> None:
        shutil.rmtree(self.root_dir)
        super().tearDown()

    def testAxisConsequence(self):
        """
        scenario:
        1. scan1 is detected, axis should wait for an answer, then the axis is
           computed but not locked, ftseries should use the axis value computed.
        2. scan2 is detected, axis should wait for an answer, then axis is
           computed and lock this time, ftseries should use the axis value
           computed.
        3. scan3 is detected, it should pass directly through axis and the
           cor value set and used by ftseries
        """
        assert os.path.exists(self.scan_1_path)
        assert os.path.exists(self.scan_2_path)
        assert os.path.exists(self.scan_3_path)

        def _wait(timeout):
            timeout = timeout - 0.1
            self.app.processEvents()
            self.processOrangeEventsStack()
            time.sleep(0.1)
            return timeout

        def getCORFrmFile(file_path):
            assert os.path.exists(file_path)
            with open(file_path) as fd:
                v = fd.readline()
                try:
                    v = float(v)
                except:
                    v = None
                finally:
                    return v

        # 1.
        self.datawatcherWidget.startObservation()
        self.axisWidget._axis_params.value = 12.0
        self.mocks[0].end_acquisition()

        # wait until we can validate
        timeout = TIMEOUT_TEST
        while timeout > 0 and self.axisWidget._n_skip == 0:
            timeout = _wait(timeout)
        if timeout < 0:
            raise TimeoutError('axis never ended calculation')
        validate_btn = self.axisWidget._widget._radioAxis._applyBut
        validate_btn.click()

        # wait until the axis windows expose (so scan should have been received)
        timeout = TIMEOUT_TEST
        while timeout > 0 and self.axisListener.callCount() < 1:
            timeout = _wait(timeout)
        if timeout < 0:
            raise TimeoutError('axis was never validated')

        timeout = TIMEOUT_TEST
        while timeout > 0 and self.ftseriesListener.callCount() < 1:
            timeout = _wait(timeout)
        if timeout < 0:
            raise TimeoutError('ftserie never ended recosntruction')

        scan_1_correct_file = os.path.join(self.scan_1_path, 'correct.txt')
        self.assertTrue(os.path.exists(scan_1_correct_file))
        self.assertEqual(getCORFrmFile(scan_1_correct_file), 12.0)

        # 2.
        self.axisWidget._axis_params.value = -6.369
        self.mocks[1].end_acquisition()

        # wait until we can validate
        timeout = TIMEOUT_TEST
        while timeout > 0 and self.axisWidget._n_skip == 1:
            timeout = _wait(timeout)
        if timeout < 0:
            raise TimeoutError('axis never ended calculation')
        validate_btn = self.axisWidget._widget._radioAxis._applyBut
        validate_btn.click()

        # wait until the axis windows expose (so scan should have been received)
        timeout = TIMEOUT_TEST
        while timeout > 0 and self.axisListener.callCount() < 2:
            timeout = _wait(timeout)
        if timeout < 0:
            raise TimeoutError('axis was never validated')

        timeout = TIMEOUT_TEST
        while timeout > 0 and self.ftseriesListener.callCount() < 2:
            timeout = _wait(timeout)
        if timeout < 0:
            raise TimeoutError('ftserie never ended recosntruction')
        scan_2_correct_file = os.path.join(self.scan_2_path, 'correct.txt')
        self.assertTrue(os.path.exists(scan_2_correct_file))
        self.assertEqual(getCORFrmFile(scan_2_correct_file), -6.369)

        # 3.
        # lock the result
        self.axisWidget._lock_axis_controls(True)
        self.mocks[2].end_acquisition()

        # wait until the axis windows expose (so scan should have been received)
        timeout = TIMEOUT_TEST
        while timeout > 0 and self.axisListener.callCount() < 3:
            timeout = _wait(timeout)
        if timeout < 0:
            raise TimeoutError('axis was never validated')

        timeout = TIMEOUT_TEST
        while timeout > 0 and self.ftseriesListener.callCount() < 3:
            timeout = _wait(timeout)
        if timeout < 0:
            raise TimeoutError('ftserie never ended recosntruction')
        scan_3_correct_file = os.path.join(self.scan_3_path, 'correct.txt')
        self.assertTrue(os.path.exists(scan_3_correct_file))
        self.assertEqual(getCORFrmFile(scan_3_correct_file), -6.369)


def suite():
    test_suite = unittest.TestSuite()
    for ui in (TestAxisFtseries, ):
        test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(ui))
    return test_suite
