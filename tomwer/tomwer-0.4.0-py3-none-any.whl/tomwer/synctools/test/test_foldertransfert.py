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


from tomwer.synctools.datatransfert import FolderTransfert
from tomwer.core.scan.scanfactory import ScanFactory
from tomwer.core.utils import rebaseParFile
from tomwer.core.utils.scanutils import MockEDF
from tomwer.test.utils import UtilsTest

from silx.gui.utils.testutils import TestCaseQt
from glob import glob
import unittest
import os
import tempfile
import shutil
import logging

logging.disable(logging.INFO)


class TestFolderTransfert(TestCaseQt):
    """
    Test that the folder transfert process is valid
    """

    def setUp(self):
        TestCaseQt.setUp(self)
        self.sourcedir = tempfile.mkdtemp()
        self.n_file = 10
        MockEDF.fastMockAcquisition(self.sourcedir, n_radio=self.n_file)
        self.scan = ScanFactory.create_scan_object(self.sourcedir)
        assert(os.path.isdir(self.sourcedir))
        self.targettedir = tempfile.mkdtemp()
        assert(os.path.isdir(self.targettedir))

        self.folderTrans = FolderTransfert()
        self.folderTrans.turn_off_print = True
        self.folderTrans.setDestDir(self.targettedir)
        self.folderTrans._copying = False

        self.outputdir = os.path.join(self.targettedir, os.path.basename(self.sourcedir))

    def tearDown(self):
        if os.path.isdir(self.sourcedir):
            shutil.rmtree(self.sourcedir)
        if os.path.isdir(self.targettedir):
            shutil.rmtree(self.targettedir)
        TestCaseQt.tearDown(self)

    def testMoveFiles(self):
        """
        simple test that files are moved
        """
        self.folderTrans.process(self.scan,
                                 move=True,
                                 noRsync=True)


        self.assertTrue(os.path.isdir(self.outputdir))
        self.assertTrue(self.checkDataCopied())

    def testCopyFiles(self):
        """
        Simple test that file are copy and deleted
        """
        self.folderTrans.process(self.scan,
                                 move=False,
                                 noRsync=True)

        self.assertTrue(self.checkDataCopied())

    def testMoveFilesForce(self):
        """
        Test the force option of folderTransfert
        """
        assert(not os.path.isdir(self.outputdir))
        assert(os.path.isdir(self.scan.path))
        self.folderTrans.process(self.scan,
                                 move=True,
                                 force=False,
                                 noRsync=True)

        MockEDF.fastMockAcquisition(self.sourcedir, n_radio=self.n_file)
        with self.assertRaises(shutil.Error):
            self.assertRaises(
                self.folderTrans.process(self.scan,
                                         move=True,
                                         force=False,
                                         noRsync=True))

        self.folderTrans.process(self.scan,
                                 move=True,
                                 force=True,
                                 noRsync=True)
        self.assertTrue(self.checkDataCopied())

    def testCopyFilesForce(self):
        """
        Test the force option for the copy files process
        """
        assert(not os.path.isdir(self.outputdir))
        os.mkdir(self.outputdir)
        assert(os.path.isdir(self.outputdir))
        self.folderTrans.process(self.scan,
                                 move=False,
                                 force=False,
                                 noRsync=True)
        self.assertTrue(self.checkDataCopied())

        MockEDF.fastMockAcquisition(self.sourcedir, n_radio=self.n_file)
        self.assertTrue(self.scan.path == self.sourcedir)
        with self.assertRaises(FileExistsError):
            self.assertRaises(
                self.folderTrans.process(self.scan,
                                         move=False,
                                         force=False,
                                         noRsync=True))

        self.folderTrans.process(self.scan,
                                 move=False,
                                 force=True,
                                 noRsync=True)
        self.assertTrue(self.checkDataCopied())

    def checkDataCopied(self):
        outputFiles = os.listdir(self.outputdir)
        inputFile = glob(self.sourcedir)
        # +2 because .info and .xml are count
        return (len(inputFile) == 0) and (len(outputFiles) == (self.n_file+2)) and \
            (not os.path.isdir(self.sourcedir))


class TestPreTransfert(unittest.TestCase):
    """Test the pretransfert actions"""
    def setUp(self):
        unittest.TestCase.setUp(self)
        folderDataset = UtilsTest.getDataset('scan_3_')
        self.tmpdir = tempfile.mkdtemp()
        self.outputfolder = tempfile.mkdtemp()
        scan_path = os.path.join(self.tmpdir, 'scan_3_')
        shutil.copytree(src=folderDataset, dst=scan_path)
        self.scan = ScanFactory.create_scan_object(scan_path=scan_path)
        self.folderTrans = FolderTransfert()
        self.folderTrans.turn_off_print = True
        self.folderTrans._copying = False
        self.folderTrans.setDestDir(self.outputfolder)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        for _dir in (self.tmpdir, self.outputfolder):
            if os.path.exists(_dir):
                shutil.rmtree(_dir)

    def testParFile(self):
        """Make sure the scan_3_.par is correctly updated when moved
        """
        parDict = self.getParDict(os.path.join(self.scan.path, 'scan_3_.par'))
        assert parDict['file_prefix'] == '/data/visitor/mi1226/id19/nemoz/henri/scan_3_/scan_3_'
        assert parDict['ff_prefix'] == '/data/visitor/mi1226/id19/nemoz/henri/scan_3_/refHST'
        rebaseParFile(os.path.join(self.scan.path, 'scan_3_.par'),
                      oldfolder='/data/visitor/mi1226/id19/nemoz/henri/scan_3_',
                      newfolder=self.scan.path)
        parDict = self.getParDict(os.path.join(self.scan.path, 'scan_3_.par'))
        self.assertTrue(parDict['file_prefix'] == os.path.join(self.scan.path, 'scan_3_'))
        self.assertTrue(parDict['ff_prefix'] == os.path.join(self.scan.path, 'refHST'))
        self.folderTrans.process(scan=self.scan, move=False, force=True,
                                 noRsync=True)
        parDict = self.getParDict(os.path.join(self.outputfolder, 'scan_3_', 'scan_3_.par'))
        self.assertTrue(parDict['file_prefix'] == os.path.join(self.outputfolder, 'scan_3_', 'scan_3_'))
        self.assertTrue(parDict['ff_prefix'] == os.path.join(self.outputfolder, 'scan_3_', 'refHST'))

    @staticmethod
    def getParDict(_file):
        assert os.path.isfile(_file)
        ddict = {}
        f = open(_file, "r")
        lines = f.readlines()
        for line in lines:
            if not '=' in line:
                continue
            l = line.rstrip().replace(' ', '')
            l = l.split('#')[0]
            key, value = l.split('=')
            ddict[key.lower()] = value
        return ddict


def suite():
    test_suite = unittest.TestSuite()
    for ui in (TestFolderTransfert, TestPreTransfert):
        test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(ui))
    return test_suite


if __name__ == '__main__':
    unittest.main(defaultTest="suite")
