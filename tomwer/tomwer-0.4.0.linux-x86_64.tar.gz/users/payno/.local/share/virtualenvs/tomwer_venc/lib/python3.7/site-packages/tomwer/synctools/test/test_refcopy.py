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
__date__ = "09/02/2018"


import logging
import os
import shutil
import tempfile
import unittest
from xml.etree import ElementTree

import fabio
import numpy
from silx.gui.utils.testutils import TestCaseQt
from tomwer.core.process.reconstruction.darkref.darkrefs import DarkRefs
from tomwer.core.process.reconstruction.darkref.settings import DARKHST_PREFIX, REFHST_PREFIX

from tomwer.core import utils
from tomwer.core.process.reconstruction.darkref.darkrefscopy import DarkRefsCopy
from tomwer.test.utils import UtilsTest, rebaseAcquisition

logging.disable(logging.INFO)


class TestRefCopy(TestCaseQt):
    """
    Test that RefCopy process is correct
    """

    def setUp(self):
        TestCaseQt.setUp(self)
        self.topDir = tempfile.mkdtemp()
        datasetWithRef = 'test10'
        dataTestDir = UtilsTest.getDataset(datasetWithRef)
        self.folderWithRef = os.path.join(self.topDir, datasetWithRef)
        shutil.copytree(dataTestDir, self.folderWithRef)

        datasetWithNoRef = 'test101'
        self.folderWithoutRef = os.path.join(self.topDir, datasetWithNoRef)
        rebaseAcquisition(src=self.folderWithRef, dst=self.folderWithoutRef)
        [os.remove(f) for f in DarkRefs.getRefHSTFiles(self.folderWithoutRef, prefix=REFHST_PREFIX)]
        [os.remove(f) for f in DarkRefs.getDarkHSTFiles(self.folderWithoutRef, prefix=DARKHST_PREFIX)]

        for acqui in (self.folderWithRef, self.folderWithoutRef):
            for _file in os.listdir(acqui):
                if _file.startswith(('refHST', 'dark.edf', 'darkHST')):
                    os.remove(os.path.join(acqui, _file))
                if acqui == self.folderWithoutRef and _file.startswith('ref'):
                    os.remove(os.path.join(acqui, _file))
        # remove darkend file to avoid creation of dark.edf from it
        os.remove(os.path.join(self.folderWithoutRef, 'darkend0000.edf'))

        assert len(DarkRefs.getRefHSTFiles(self.folderWithoutRef, prefix=REFHST_PREFIX)) is 0
        assert len(DarkRefs.getDarkHSTFiles(self.folderWithoutRef, prefix=DARKHST_PREFIX)) is 0
        # create back the dark.edf
        darkProcess = DarkRefs()
        darkProcess.setForceSync(True)
        darkProcess.process(self.folderWithRef)
        del darkProcess
        assert 'dark.edf' in os.listdir(self.folderWithRef)
        assert 'refHST0000.edf' in os.listdir(self.folderWithRef)
        assert 'refHST0020.edf' in os.listdir(self.folderWithRef)
        self.refCopyObj = DarkRefsCopy(reconsparams=None)
        self.refCopyObj.setForceSync(True)

    def tearDown(self):
        shutil.rmtree(self.topDir)
        self.refCopyObj = None
        TestCaseQt.tearDown(self)

    def testAutoMode(self):
        """Check behavior of the auto mode"""
        self.refCopyObj.setModeAuto(True)
        self.refCopyObj.process(self.folderWithRef)
        # TODO : remove permamently the darkHST0000.edf file
        # make sure the refCopy is correctly initialized
        self.assertTrue(self.refCopyObj.hasRefStored() is True)
        self.assertTrue('dark.edf' in self.refCopyObj.worker._getRefList())
        self.assertTrue('refHST0000.edf' in self.refCopyObj.worker._getRefList())
        self.assertTrue(len(self.refCopyObj.worker._getRefList()) is 2)
        # check process is doing the job
        self.refCopyObj.process(self.folderWithoutRef)
        self.assertTrue(len(DarkRefs.getRefHSTFiles(self.folderWithoutRef, prefix=REFHST_PREFIX)) > 0)
        self.assertTrue(len(DarkRefs.getDarkHSTFiles(self.folderWithoutRef, prefix=DARKHST_PREFIX)) > 0)

    def testManualMode(self):
        """Check behavior of the manual mode"""
        self.refCopyObj.setModeAuto(False)
        self.refCopyObj.setRefsFromScan(self.folderWithRef)
        # make sure the refCopy is correctly initialized
        self.assertTrue(self.refCopyObj.hasRefStored() is True)
        self.assertTrue('dark.edf' in self.refCopyObj.worker._getRefList())
        self.assertTrue('refHST0000.edf' in self.refCopyObj.worker._getRefList())
        self.assertTrue(len(self.refCopyObj.worker._getRefList()) is 2)
        # check process is doing the job
        self.refCopyObj.process(self.folderWithoutRef)
        self.assertTrue(len(DarkRefs.getRefHSTFiles(self.folderWithoutRef, prefix=REFHST_PREFIX)) > 0)
        self.assertTrue(len(DarkRefs.getDarkHSTFiles(self.folderWithoutRef, prefix=DARKHST_PREFIX)) > 0)

    def testNormalizationSRCurrent(self):
        """Make sure the srCurrent is taking into account"""
        self.refCopyObj.setModeAuto(False)
        self.refCopyObj.setRefsFromScan(self.folderWithRef)

        self.assertTrue(os.path.isfile(
            os.path.join(self.folderWithRef, 'dark.edf')))
        originalRefData = fabio.open(
            os.path.join(self.folderWithRef, 'refHST0000.edf')).data
        assert utils.getSRCurrent(scan=self.folderWithRef, when='start') == 101.3
        assert utils.getSRCurrent(scan=self.folderWithRef, when='end') == 93.6
        normRefData = fabio.open(
            os.path.join(self.refCopyObj.worker._savedir, 'refHST0000.edf')).data
        self.assertFalse(numpy.array_equal(originalRefData, normRefData))

        # change SRCurrent on the .xml
        infoXml = os.path.join(self.folderWithoutRef, 'test101.xml')
        assert os.path.exists(infoXml)
        xmlTree = ElementTree.parse(infoXml)
        xmlTree.getroot()[0][6].text = '200.36'
        xmlTree.getroot()[0][7].text = '199.63'
        xmlTree.write(infoXml)
        self.refCopyObj.process(self.folderWithoutRef)
        self.assertTrue(
            os.path.isfile(os.path.join(self.folderWithoutRef, 'dark.edf')))
        self.assertTrue(
            os.path.isfile(os.path.join(self.folderWithoutRef, 'refHST0000.edf')))
        copyRefData = fabio.open(
            os.path.join(self.folderWithoutRef, 'refHST0000.edf')).data
        assert utils.getSRCurrent(scan=self.folderWithoutRef, when='start') == 200.36
        assert utils.getSRCurrent(scan=self.folderWithoutRef, when='end') == 199.63
        self.assertFalse(numpy.array_equal(originalRefData, copyRefData))
        self.assertFalse(numpy.array_equal(normRefData, copyRefData))

    def testInverseOperation(self):
        """Make sure we will found back the original flat field reference
        if the process is forced to take the default value for SRCurrent
        two time"""
        self.refCopyObj.setModeAuto(False)
        self.refCopyObj.setRefsFromScan(self.folderWithRef)
        originalRefData = fabio.open(
            os.path.join(self.folderWithRef, 'refHST0000.edf')).data
        self.refCopyObj.process(self.folderWithoutRef)
        copyRefData = fabio.open(
            os.path.join(self.folderWithoutRef, 'refHST0000.edf')).data
        self.assertTrue(originalRefData.shape == copyRefData.shape)
        self.assertTrue(numpy.allclose(originalRefData, copyRefData))


def suite():
    test_suite = unittest.TestSuite()
    for ui in (TestRefCopy, ):
        test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(ui))
    return test_suite


if __name__ == '__main__':
    unittest.main(defaultTest="suite")
