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
__date__ = "07/12/2016"

import logging
import os
import shutil
import tempfile
import unittest

from silx.gui import qt

from orangecontrib.tomwer.widgets.control.DataValidatorOW import \
    DataValidatorOW
from tomwer.gui.qtapplicationmanager import QApplicationManager
from tomwer.core.scan.edfscan import EDFTomoScan
from tomwer.core.scan.scanbase import TomoBase
from tomwer.core.utils.scanutils import MockEDF
from tomwer.test.utils import UtilsTest

_qapp = QApplicationManager()

logging.disable(logging.INFO)


class TestAccumulation(unittest.TestCase):
    """Test that all scans will be validated if many are send and no answer
    is give until all received"""

    NB_SCAN = 10
    """Number of scan to accumulate"""

    N_RADIO = 10
    N_RECONS = 2
    DIM_MOCK_SCAN = 10

    def setUp(self):
        self.scans = []
        for iScan in range(TestAccumulation.NB_SCAN):
            scanID = tempfile.mkdtemp()
            scan = MockEDF.mockScan(scanID=scanID,
                                    nRadio=self.N_RADIO,
                                    nRecons=self.N_RECONS,
                                    nPagRecons=0,
                                    dim=self.DIM_MOCK_SCAN)

            self.scans.append(scan)

        self.scanValidator = DataValidatorOW(None)
        self.scanValidator._warnValManualShow = True
        self.scanValidator.setAttribute(qt.Qt.WA_DeleteOnClose)

    def tearDown(self):
        _qapp.processEvents()
        for f in self.scans:
            if os.path.isdir(f.path):
                shutil.rmtree(f.path)
        self.scanValidator.close()

    def test(self):
        for scan in self.scans:
            self.scanValidator.addScan(scan)

        _qapp.processEvents()

        self.assertTrue(len(self.scanValidator._scansToValidate) == TestAccumulation.NB_SCAN)
        for scanID in self.scans:
            self.scanValidator._validateScan(scanID)
            _qapp.processEvents()
        self.assertTrue(len(self.scanValidator._scansToValidate) == 0)


class TestValidation(unittest.TestCase):
    """Test the validation command"""
    class _ValidationReceiver(qt.QObject):
        def __init__(self):
            qt.QObject.__init__(self)
            self.counter = 0

        def count(self):
            self.counter = self.counter + 1

    class _DataValidatorWidgetPatched(DataValidatorOW):
        """A DataValidatorOW without the Orange send signal process"""
        scanReady = qt.Signal(TomoBase)
        _warnValManualShow = True

        def _validated(self, scan):
            """Callback when the validate button is pushed"""
            assert isinstance(scan, TomoBase)
            if scan is not None:
                self.Outputs.data_out.send(scan)
                self.scanReady.emit(scan)
                del self._scansToValidate[scan.path]

    @classmethod
    def setUpClass(cls):
        cls.rootdir = tempfile.mkdtemp()
        cls.dataSetIDs = 'test10', 'test01'
        cls.scans = []
        for scanID in cls.dataSetIDs:
            dataDir = UtilsTest.getDataset(scanID)
            tmpDir = os.path.join(cls.rootdir, scanID)
            cls.scans.append(tmpDir)
            shutil.copytree(dataDir, tmpDir)
        cls.validationReceiver = TestValidation._ValidationReceiver()

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.rootdir)
        del cls.validationReceiver
        if os.path.isdir(cls.rootdir):
            shutil.rmtree(cls.rootdir)

    def tearDown(self):
        self.scanValidator.close()
        del self.scanValidator
        unittest.TestCase.tearDown(self)

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.scanValidator = TestValidation._DataValidatorWidgetPatched()
        self.scanValidator._warnValManualShow = True
        self.scanValidator.scanReady.connect(self.validationReceiver.count)
        self.validationReceiver.counter = 0
        self.scanValidator.setAttribute(qt.Qt.WA_DeleteOnClose)

    def testAutomaticValidation(self):
        for scan in self.scans:
            self.scanValidator.addScan(EDFTomoScan(scan))

        self.assertTrue(self.validationReceiver.counter == 0)
        self.scanValidator.getValidationWidget('scan to treat').setChecked(False)
        while (_qapp.hasPendingEvents()):
            _qapp.processEvents()
        self.assertTrue(self.validationReceiver.counter == 2)
        self.assertTrue(len(self.scanValidator._scansToValidate) == 0)


def suite():
    test_suite = unittest.TestSuite()
    for ui in (TestAccumulation, TestValidation):
        test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(ui))
    return test_suite


if __name__ == '__main__':
    unittest.main(defaultTest="suite")
