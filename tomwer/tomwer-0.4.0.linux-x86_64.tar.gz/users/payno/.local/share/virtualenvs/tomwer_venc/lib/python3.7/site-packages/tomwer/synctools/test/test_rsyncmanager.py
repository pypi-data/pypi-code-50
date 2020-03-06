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
__date__ = "17/01/2018"


import filecmp
import logging
import os
import shutil
import tempfile
import unittest

from tomwer.synctools.rsyncmanager import RSyncManager
from tomwer.test.utils import UtilsTest

logging.disable(logging.INFO)


@unittest.skipIf(RSyncManager().canUseRSync() is False, "Rsync is missing")
class TestRSyncManager(unittest.TestCase):
    """Check that the RSyncManager is correctly synchronizing folders.
    """

    def setUp(self):
        self.topSrcFolder = tempfile.mkdtemp()
        self.topTargetFolder = tempfile.mkdtemp()

        self.dataSetID = 'test01'
        self.dataDir = UtilsTest.getDataset(self.dataSetID)
        self.sourceFolder = os.path.join(self.topSrcFolder, self.dataSetID)
        shutil.copytree(src=os.path.join(self.dataDir),
                        dst=self.sourceFolder)

    def tearDown(self):
        shutil.rmtree(self.topSrcFolder)
        shutil.rmtree(self.topTargetFolder)

    def testSyncFolder(self):
        """Test that a simple sync between two folders are valid"""
        self.assertTrue(len(os.listdir(self.topTargetFolder)) is 0)
        manager = RSyncManager()
        manager.syncFolder(source=self.sourceFolder,
                           target=self.topTargetFolder,
                           block=True,
                           delete=False)
        targetFolder = os.path.join(self.topTargetFolder, self.dataSetID)
        self.assertTrue(len(os.listdir(targetFolder)) == len(os.listdir(self.sourceFolder)))
        self.assertTrue(filecmp.dircmp(targetFolder, self.sourceFolder))
        self.assertTrue(os.path.isdir(self.sourceFolder))

    def testSyncFolderDelete(self):
        """Test that a simple sync between two folders are valid ans source
        folder is correctly deleted"""
        self.assertTrue(len(os.listdir(self.topTargetFolder)) is 0)
        manager = RSyncManager()
        manager.syncFolder(source=self.sourceFolder,
                           target=self.topTargetFolder,
                           block=True,
                           delete=True)
        targetFolder = os.path.join(self.topTargetFolder, self.dataSetID)
        self.assertTrue(len(os.listdir(targetFolder)) == len(os.listdir(self.dataDir)))
        self.assertTrue(filecmp.dircmp(targetFolder, self.sourceFolder))
        self.assertFalse(os.path.isdir(self.sourceFolder))


def suite():
    test_suite = unittest.TestSuite()
    for ui in (TestRSyncManager, ):
        test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(ui))
    return test_suite


if __name__ == '__main__':
    unittest.main(defaultTest="suite")
