# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2017-2019 European Synchrotron Radiation Facility
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
__date__ = "03/05/2019"


from orangecontrib.tomwer.widgets.reconstruction.AxisOW import AxisOW
from tomwer.test.utils import skip_gui_test
from tomwer.test.utils import UtilsTest
from tomwer.core.process.reconstruction.axis.mode import AxisMode
from tomwer.core.settings import mock_lsbram
from tomwer.core.scan.scanfactory import ScanFactory
from tomwer.core import utils
from tomwer.core.utils.scanutils import MockEDF
from silx.gui.utils.testutils import TestCaseQt
from silx.gui import qt
import shutil
import tempfile
import unittest
import time


@unittest.skipIf(skip_gui_test(), reason='skip gui test')
class TestOWAxis(TestCaseQt):
    """Test that the axis widget work correctly"""
    def setUp(self):
        self._window = AxisOW()
        self.recons_params = self._window.recons_params
        self.scan_path = UtilsTest.getDataset("D2_H2_T2_h_")
        self._window.getAxis().mode = AxisMode.global_
        self._window.show()
        self.qWaitForWindowExposed(self._window)

    def tearDown(self):
        self._window.setAttribute(qt.Qt.WA_DeleteOnClose)
        self._window.close()

    def testAxisLock(self):
        """Test behavior when locking the axis position. Could not be included
        in the tomwer/gui because the lock action is only available for the OW
        """
        assert self._window.getAxis().mode is AxisMode.global_
        self.assertFalse(self._window._widget._radioAxis._lockBut.isLocked())
        self.assertTrue(self._window._widget._radioAxis._controlWidget._mainWidget.isEnabled())
        self.mouseClick(self._window._widget._radioAxis._lockBut, qt.Qt.LeftButton)
        self.qapp.processEvents()
        self.assertTrue(self._window._widget._radioAxis._lockBut.isLocked())
        # when the lock button is activated we should automatically switch to
        # the manual mode
        self.assertTrue(self._window.getAxis().mode is AxisMode.manual)
        self.assertFalse(self._window._widget._radioAxis._controlWidget._mainWidget.isEnabled())


@unittest.skipIf(skip_gui_test(), reason='skip gui test')
class TestWindowAxisComputation(TestCaseQt):
    @staticmethod
    def _long_computation(scan):
        time.sleep(5)
        return -1

    """Test that the axis widget work correctly"""
    def setUp(self):
        self._mainWindow = AxisOW()
        self._mainWindow._skip_exec(True)
        self.recons_params = self._mainWindow.recons_params
        self._window = self._mainWindow._widget
        self.scan_path = ScanFactory.create_scan_object(UtilsTest.getDataset("D2_H2_T2_h_"))
        self._mainWindow.show()
        self.qWaitForWindowExposed(self._mainWindow)

    def tearDown(self):
        self._mainWindow.setAttribute(qt.Qt.WA_DeleteOnClose)
        self._mainWindow.close()

    def testFailedComputation(self):
        """Test gui if the axis position fails"""
        self.recons_params.set_position_frm_par_file('not existing',
                                                     force=True)
        self.assertTrue(self.recons_params.mode is AxisMode.read)
        self.assertTrue(self._window._radioAxis.getMode() is AxisMode.read)
        self._mainWindow.process(self.scan_path)
        self.assertTrue(self._window._radioAxis.getMode() is AxisMode.read)
        self.assertTrue(self.recons_params.value is None)
        self.assertTrue(self._window._radioAxis._controlWidget._positionInfoWidget._positionLabel.text() == '?')

    def testLongComputation(self):
        """Test behavior if some time consuming axis computation is made"""
        # monkey patch the method used
        radioAxis = self._mainWindow._widget._radioAxis
        self._mainWindow._computationThread.patch_calc_method(AxisMode.global_, TestWindowAxisComputation._long_computation)  # noqa
        self.recons_params.mode = AxisMode.global_
        self.qapp.processEvents()
        self.assertTrue(radioAxis.getMode() == AxisMode.global_)
        self._mainWindow.process(self.scan_path)
        self.qapp.processEvents()
        # need the data to be loaded from thread and the cor calculation thread
        # to be launch
        time.sleep(0.5)
        self.qapp.processEvents()
        self.assertFalse(radioAxis._controlWidget._mainWidget.isEnabled())
        self.qapp.processEvents()
        self.assertTrue(self._window._radioAxis._controlWidget._positionInfoWidget._positionLabel.text() == '...')

        # then wait for the computation end
        self._mainWindow.wait_computation_finished()
        self.qapp.processEvents()

        # check result is correctly computed
        self.assertTrue(self._window._radioAxis._controlWidget._mainWidget.isEnabled())
        res = self._window._radioAxis._controlWidget._positionInfoWidget._positionLabel.text()
        self.assertTrue(float(res) == -1.0)
        self.assertTrue(self.recons_params.value == -1.0)

    def testComputationSucceed(self):
        """Test gui if the axis position is correctly computed"""
        self.recons_params.mode = AxisMode.manual
        self.recons_params.value = 2.345
        self._mainWindow.process(self.scan_path)
        self.qapp.processEvents()
        self.assertTrue(self._window._radioAxis.getMode() is AxisMode.manual)
        self.assertTrue(self.recons_params.value == 2.345)
        self.assertTrue(self._window._radioAxis._controlWidget._positionInfoWidget._positionLabel.text() == '2.345')


global _computation_res
_computation_res = 0


@unittest.skipIf(skip_gui_test(), reason='skip gui test')
class TestAxisStack(TestCaseQt):
    """Test axis computation of a stack of scan"""

    @staticmethod
    def _test_computation(scan):
        global _computation_res
        _computation_res += 1
        return _computation_res

    def setUp(self):
        # not working due to OW
        # TestCaseQt.setUp(self)
        self._scan1 = MockEDF.mockScan(scanID=tempfile.mkdtemp())
        self._scan2 = MockEDF.mockScan(scanID=tempfile.mkdtemp())
        self._scan3 = MockEDF.mockScan(scanID=tempfile.mkdtemp())
        self._mainWindow = AxisOW()
        self.recons_params = self._mainWindow.recons_params
        self._mainWindow._skip_exec(True)

        global _computation_res
        _computation_res = 0

        self._mainWindow.RADIO_CALCULATIONS_METHODS[
            AxisMode.global_] = TestAxisStack._test_computation  # noqa
        self.recons_params.mode = AxisMode.global_

        self._mainWindow.show()
        self.qWaitForWindowExposed(self._mainWindow)

    def tearDown(self):
        for scan in (self._scan1, self._scan2, self._scan3):
            shutil.rmtree(scan.path)
        utils.mockLowMemory(False)
        mock_lsbram(False)
        self._mainWindow.setAttribute(qt.Qt.WA_DeleteOnClose)
        self._mainWindow.close()
        self._mainWindow = None
        # not working due to OW
        # TestCaseQt.tearDown(self)

    def testLowMemory(self):
        """Make sure the axis computation will be skip if we are in low memory
        """
        utils.mockLowMemory(True)
        mock_lsbram(True)
        for scan in (self._scan1, self._scan2, self._scan3):
            self.qapp.processEvents()
            self._mainWindow.process(scan)

        self.assertTrue(self._scan1.axis_params.value == None)
        self.assertTrue(self._scan2.axis_params.value == None)
        self.assertTrue(self._scan3.axis_params.value == None)

    def testUnlockStack(self):
        """Check that all axis position will be computed properly if we set a
        stack of scan"""
        self._mainWindow.recons_params.value = 1.0
        for scan in (self._scan1, self._scan2, self._scan3):
            self._mainWindow.process(scan)

        for i in range(5):
            self.qapp.processEvents()
            time.sleep(0.2)
            self.qapp.processEvents()

        self.assertTrue(self._scan1.axis_params.value == 1)
        self.assertTrue(self._scan2.axis_params.value == 2)
        self.assertTrue(self._scan3.axis_params.value == 3)

    def testLockStack(self):
        """Check that axis position will be simply copy if we are in a lock
        stack"""
        self.recons_params.mode = AxisMode.manual
        position_value = 0.36
        self.recons_params.value = position_value

        for scan in (self._scan1, self._scan2, self._scan3):
            self._mainWindow.process(scan)

        for i in range(5):
            self.qapp.processEvents()
            time.sleep(0.2)
            self.qapp.processEvents()

        self.assertTrue(self._scan1.axis_params.value == position_value)
        self.assertTrue(self._scan2.axis_params.value == position_value)
        self.assertTrue(self._scan3.axis_params.value == position_value)


def suite():
    test_suite = unittest.TestSuite()
    for ui in (TestOWAxis, TestWindowAxisComputation, TestAxisStack):
        test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(ui))
    return test_suite


if __name__ == '__main__':
    unittest.main(defaultTest="suite")
