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
__date__ = "24/01/2017"

import logging
import os
import shutil
import tempfile
import time
import unittest

from silx.gui import qt

from orangecontrib.tomwer.widgets.reconstruction.DarkRefAndCopyOW import \
    DarkRefAndCopyOW
from tomwer.core.process.reconstruction.darkref.dkrf import \
    Method as DkrfMethod
from tomwer.core.scan.scanfactory import ScanFactory
from tomwer.gui.reconstruction.ftserie import FtserieWidget
from tomwer.gui.qtapplicationmanager import QApplicationManager
from tomwer.gui.reconstruction.darkref.darkrefcopywidget import DarkRefAndCopyWidget
from tomwer.synctools.ftseries import QReconsParams
from tomwer.test.utils import UtilsTest

_qapp = QApplicationManager()

logging.disable(logging.INFO)


class TestDarkRefWidget(unittest.TestCase):
    """class testing the DarkRefWidget"""

    def setUp(self):
        unittest.TestCase.setUp(self)
        self._recons_params = QReconsParams()
        self.widget = DarkRefAndCopyOW(parent=None, _connect_handler=False,
                                       reconsparams=self._recons_params.dkrf)

    def tearDown(self):
        self.widget.setAttribute(qt.Qt.WA_DeleteOnClose)
        self.widget.close()

    def testSyncRead(self):
        """Make sure any modification on the self._reconsParams is 
        applied on the GUI"""
        rp = self._recons_params
        self.assertTrue(rp.dkrf['REFSRMV'] is False)
        self.assertFalse(self.widget.widget.mainWidget.tabGeneral._rmOptionCB.isChecked())
        rp.dkrf['REFSRMV'] = True
        self.assertTrue(self.widget.widget.mainWidget.tabGeneral._rmOptionCB.isChecked())

        pattern = self.widget.widget.mainWidget.tabExpert._refLE.text()
        newText = 'popo.*'
        assert(pattern != newText)
        rp.dkrf['RFFILE'] = newText
        self.assertTrue(
            self.widget.widget.mainWidget.tabExpert._refLE.text() == newText)

    def testSyncWrite(self):
        """Test that if we edit through the :class:`DarkRefWidget` then the
        modification are fall back into the self._reconsParams"""
        rp = self._recons_params

        # test patterns
        pattern = self.widget.widget.mainWidget.tabExpert._refLE.text()
        newText = 'popo.*'
        assert(pattern != newText)
        self.widget.widget.mainWidget.tabExpert._refLE.setText(newText)
        self.widget.widget.mainWidget.tabExpert._refLE.editingFinished.emit()
        qt.QApplication.instance().processEvents()
        self.assertTrue(rp.dkrf['RFFILE'] == newText)
        self.widget.widget.mainWidget.tabExpert._darkLE.setText(newText)
        self.widget.widget.mainWidget.tabExpert._darkLE.editingFinished.emit()
        qt.QApplication.instance().processEvents()
        self.assertTrue(rp.dkrf['DKFILE'] == newText)

        # test calc mode
        self.widget.widget.mainWidget.tabGeneral._darkWCB.setMode(DkrfMethod.none)
        self.widget.widget.mainWidget.tabGeneral._refWCB.setMode(DkrfMethod.median)
        self.assertTrue(rp.dkrf['DARKCAL'] == DkrfMethod.none)
        self.assertTrue(rp.dkrf['REFSCAL'] == DkrfMethod.median)

        # test options
        cuRm = self.widget.widget.mainWidget.tabGeneral._rmOptionCB.isChecked()
        self.widget.widget.mainWidget.tabGeneral._rmOptionCB.setChecked(not cuRm)
        self.assertTrue(rp.dkrf['REFSRMV'] == (not cuRm))
        self.assertTrue(rp.dkrf['DARKRMV'] == (not cuRm))

        cuSkip = self.widget.widget.mainWidget.tabGeneral._skipOptionCB.isChecked()
        self.widget.widget.mainWidget.tabGeneral._skipOptionCB.setChecked(not cuSkip)
        # warning : here value of skip and overwrite are of course inverse
        self.assertTrue(rp.dkrf['DARKOVE'] == cuSkip)
        self.assertTrue(rp.dkrf['REFSOVE'] == cuSkip)

    def testBehaviorWithFtserie(self):
        """
        Make sure modification on ftserie 'Dark and flat field' tab are
        correctly take into account in this case they are working on the same
        QReconsParams object
        """
        ftserie = FtserieWidget(recons_params=self._recons_params)

        cuRm = ftserie.getReconsParamSetEditor()._dkRefWidget._qcbRmRef.isChecked()
        cuSkip = ftserie.getReconsParamSetEditor()._dkRefWidget._qcbSkipRef.isChecked()
        calcDK = ftserie.getReconsParamSetEditor()._dkRefWidget._qcbDKMode.getMode()
        calcRef = ftserie.getReconsParamSetEditor()._dkRefWidget._qcbRefMode.getMode()
        patternRef = ftserie.getReconsParamSetEditor()._dkRefWidget._qleRefsPattern.text()
        patternDK = ftserie.getReconsParamSetEditor()._dkRefWidget._qleDKPattern.text()

        # make sure initial status are the same between ftserie and darkref
        dkrfOWMainWidget = self.widget.widget.mainWidget
        self.assertTrue(dkrfOWMainWidget.tabGeneral._rmOptionCB.isChecked() == cuRm)
        self.assertTrue(dkrfOWMainWidget.tabGeneral._skipOptionCB.isChecked() == cuSkip)
        self.assertTrue(dkrfOWMainWidget.tabGeneral._darkWCB.getMode() == calcDK)
        self.assertTrue(dkrfOWMainWidget.tabGeneral._refWCB.getMode() == calcRef)
        self.assertTrue(dkrfOWMainWidget.tabExpert._refLE.text() == patternRef)
        self.assertTrue(dkrfOWMainWidget.tabExpert._darkLE.text() == patternDK)

        # change parameters
        ftserie.getReconsParamSetEditor()._dkRefWidget._qcbRmRef.setChecked(not cuRm)
        ftserie.getReconsParamSetEditor()._dkRefWidget._qcbSkipRef.setChecked(not cuSkip)
        ftserie.getReconsParamSetEditor()._dkRefWidget._qcbDKMode.setMode('none')
        ftserie.getReconsParamSetEditor()._dkRefWidget._qcbRefMode.setMode('average')
        text_ref_pattern = 'toto.*'
        text_dk_pattern = '[maestro]?.'
        ftserie.getReconsParamSetEditor()._dkRefWidget._qleDKPattern.setText(text_dk_pattern)
        ftserie.getReconsParamSetEditor()._dkRefWidget._qleDKPattern.editingFinished.emit()
        qt.QApplication.instance().processEvents()
        ftserie.getReconsParamSetEditor()._dkRefWidget._qleRefsPattern.setText(text_ref_pattern)
        ftserie.getReconsParamSetEditor()._dkRefWidget._qleRefsPattern.editingFinished.emit()
        qt.QApplication.instance().processEvents()

        # check modification are well take into account
        self.assertTrue(dkrfOWMainWidget.tabGeneral._rmOptionCB.isChecked() == (not cuRm))
        self.assertTrue(self._recons_params.dkrf['DARKRMV'] == (not cuRm))
        self.assertTrue(dkrfOWMainWidget.tabGeneral._skipOptionCB.isChecked() == (not cuSkip))
        self.assertTrue(self._recons_params.dkrf['DARKOVE'] == cuSkip)
        self.assertTrue(dkrfOWMainWidget.tabGeneral._darkWCB.getMode() == DkrfMethod.none)
        self.assertTrue(self._recons_params.dkrf['DARKCAL'] == DkrfMethod.none)
        self.assertTrue(dkrfOWMainWidget.tabGeneral._refWCB.getMode() == DkrfMethod.average)
        self.assertTrue(self._recons_params.dkrf['REFSCAL'] == DkrfMethod.average)
        self.assertTrue(self._recons_params.dkrf['DKFILE'] == text_dk_pattern)
        self.assertTrue(self._recons_params.dkrf['RFFILE'] == text_ref_pattern)
        self.assertTrue(dkrfOWMainWidget.tabExpert._refLE.text() == text_ref_pattern)
        self.assertTrue(dkrfOWMainWidget.tabExpert._darkLE.text() == text_dk_pattern)


@unittest.skipIf(UtilsTest.getInternalTestDir('testslicesNemoz6x') is None, "No extra datatset")
class TestID16TestCase(unittest.TestCase):
    """
    class testing the process of the dark ref widget in the case of ID16
    """
    def setUp(self):
        unittest.TestCase.setUp(self)
        datasetDir = UtilsTest.getInternalTestDir('testslicesNemoz6x')
        self._tmpDir = tempfile.mkdtemp()
        self.datasets = []
        for subFolder in ('testslicesNemoz61_1_', 'testslicesNemoz62_1_',
                          'testslicesNemoz63_1_', 'testslicesNemoz64_1_',
                          'testslicesNemoz65_1_'):
            shutil.copytree(os.path.join(datasetDir, subFolder),
                            os.path.join(self._tmpDir, subFolder))
            self.datasets.append(os.path.join(self._tmpDir, subFolder))

        self.recons_params = QReconsParams()
        self.recons_params.dkrf.remove_dark = True
        self.recons_params.dkrf.remove_ref = True
        self.widget = DarkRefAndCopyWidget(parent=None, reconsparams=self.recons_params.dkrf)
        self.widget.setForceSync(True)

    def tearDown(self):
        self.widget.setAttribute(qt.Qt.WA_DeleteOnClose)
        self.widget.close()
        self.widget = None
        shutil.rmtree(self._tmpDir)
        unittest.TestCase.tearDown(self)

    def test(self):
        """make sure the behavior of dark ref is correct for id16b pipeline:
        datasets is composed of :
        
        - testslicesNemoz61_1_: contains original dark and ref. DarkRef should
           process those to generate median ref and dark
        - testslicesNemoz62_1_, testslicesNemoz63_1_, testslicesNemoz64_1_:
           contains no ref or dark orignals or median.
           should copy the one normalized from testslicesNemoz61_1_
        testslicesNemoz65_1_: contains dark median. Should copy ref from 
            testslicesNemoz61_1_
        """
        # check behavior for testslicesNemoz61_1_.
        files = os.listdir(self.datasets[0])
        assert 'darkend0000.edf' in files
        assert 'ref0000_0000.edf' in files
        assert 'ref0000_0050.edf' in files
        assert 'ref0001_0000.edf' in files
        assert 'ref0001_0050.edf' in files
        assert 'refHST0000.edf' not in files
        assert 'refHST0050.edf' not in files
        assert 'dark.edf' not in files

        scan = ScanFactory.create_scan_object(scan_path=self.datasets[0])
        self.widget.process(scan)
        for t in range(8):
            qt.QApplication.instance().processEvents()
            time.sleep(0.5)

        files = os.listdir(scan.path)
        self.assertTrue('dark.edf' in files)
        self.assertTrue('darkend0000.edf' not in files)
        self.assertTrue('ref0000_0000.edf' not in files)
        self.assertTrue('ref0000_0050.edf' not in files)
        self.assertTrue('ref0001_0000.edf' not in files)
        self.assertTrue('ref0001_0050.edf' not in files)
        self.assertTrue('refHST0000.edf' in files)
        self.assertTrue('refHST0050.edf' in files)
        self.assertTrue(self.widget._darkRef.hasRefStored())

        # check behavior for testslicesNemoz62_1_, testslicesNemoz63_1_,
        # testslicesNemoz64_1_.
        for dataset in self.datasets[1:4]:
            files = os.listdir(dataset)
            assert 'darkend0000.edf' not in files
            assert 'ref0000_0000.edf' not in files
            assert 'ref0000_0050.edf' not in files
            assert 'ref0001_0000.edf' not in files
            assert 'ref0001_0050.edf' not in files
            assert 'refHST0000.edf' not in files
            assert 'refHST0050.edf' not in files
            assert 'dark.edf' not in files
            scan = ScanFactory.create_scan_object(scan_path=dataset)
            self.widget.process(scan)
            for t in range(8):
                qt.QApplication.instance().processEvents()
                time.sleep(0.5)

            files = os.listdir(dataset)
            self.assertTrue('darkend0000.edf' not in files)
            self.assertTrue('ref0000_0000.edf' not in files)
            self.assertTrue('ref0000_0050.edf' not in files)
            self.assertTrue('ref0001_0000.edf' not in files)
            self.assertTrue('ref0001_0050.edf' not in files)
            self.assertTrue('refHST0000.edf' in files)
            self.assertTrue('refHST0050.edf' in files)
            self.assertTrue('dark.edf' in files)

        # check behavior for testslicesNemoz65_1_
        dataset = self.datasets[-1]
        files = os.listdir(dataset)
        assert 'darkend0000.edf' not in files
        assert 'ref0000_0000.edf' not in files
        assert 'ref0000_0050.edf' in files
        assert 'ref0001_0000.edf' not in files
        assert 'ref0001_0050.edf' in files
        assert 'refHST0000.edf' not in files
        assert 'refHST0050.edf' not in files
        assert 'dark0000.edf' not in files
        scan = ScanFactory.create_scan_object(scan_path=dataset)
        self.widget.process(scan)
        for t in range(8):
            qt.QApplication.instance().processEvents()
            time.sleep(0.5)

        files = os.listdir(dataset)
        self.assertTrue('darkend0000.edf' not in files)
        self.assertTrue('ref0000_0000.edf' not in files)
        self.assertTrue('ref0000_0050.edf' not in files)
        self.assertTrue('ref0001_0000.edf' not in files)
        self.assertTrue('ref0001_0050.edf' not in files)
        self.assertTrue('refHST0000.edf' in files)
        self.assertTrue('refHST0050.edf' in files)
        self.assertTrue('dark.edf' in files)


def suite():
    test_suite = unittest.TestSuite()
    for ui in (TestDarkRefWidget, TestID16TestCase):
        test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(ui))
    return test_suite


if __name__ == '__main__':
    unittest.main(defaultTest="suite")
