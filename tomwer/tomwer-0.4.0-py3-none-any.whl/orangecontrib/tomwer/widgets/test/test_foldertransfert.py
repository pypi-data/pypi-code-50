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
from glob import glob

from silx.gui import qt

from orangecontrib.tomwer.widgets.control.DataTransfertOW import \
    DataTransfertOW
from tomwer.gui.qtapplicationmanager import QApplicationManager
from tomwer.core.scan.scanfactory import ScanFactory
from tomwer.core.utils.scanutils import MockEDF

_qapp = QApplicationManager()

logging.disable(logging.INFO)


class TestFolderTransfertWidget(unittest.TestCase):
    """class testing the DataTransfertOW"""

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.n_file = 10
        self.sourcedir = tempfile.mkdtemp()
        assert os.path.isdir(self.sourcedir)
        self.targettedir = tempfile.mkdtemp()
        assert os.path.isdir(self.targettedir)
        MockEDF.fastMockAcquisition(self.sourcedir, n_radio=self.n_file)
        self.scan = ScanFactory.create_scan_object(self.sourcedir)

        self.folderTransWidget = DataTransfertOW()
        self.folderTransWidget.turn_off_print = True
        self.folderTransWidget.setDestDir(self.targettedir)
        self.folderTransWidget._copying = False

    def tearDown(self):
        self.folderTransWidget.setAttribute(qt.Qt.WA_DeleteOnClose)
        while(_qapp.hasPendingEvents()):
            _qapp.processEvents()
        self.folderTransWidget.close()

        if os.path.isdir(self.sourcedir):
            shutil.rmtree(self.sourcedir)
        if os.path.isdir(self.targettedir):
            shutil.rmtree(self.targettedir)
        self.folderTransWidget = None
        unittest.TestCase.tearDown(self)

    def testMoveFiles(self):
        """
        simple test that files are correctly moved
        """
        self.folderTransWidget.process(self.scan,
                                       move=True,
                                       noRsync=True)

        outputdir = os.path.join(self.targettedir, os.path.basename(self.sourcedir))
        timeout = 1
        while((os.path.isdir(self.sourcedir)) and timeout > 0
              or self.folderTransWidget.isCopying()):
            timeout = timeout - 0.1
            time.sleep(0.1)
            _qapp.processEvents()

        self.assertTrue(os.path.isdir(outputdir))
        self.assertTrue(self.checkDataCopied())

    def testCopyFiles(self):
        """
        Simple test that file are copy and deleted
        """
        self.folderTransWidget.process(self.scan,
                                       move=False,
                                       noRsync=True)

        timeout = 1
        outputdir = os.path.join(self.targettedir, os.path.basename(self.sourcedir))
        while((os.path.isdir(self.sourcedir) and timeout > 0)
              or self.folderTransWidget.isCopying()):
            timeout = timeout - 0.1
            time.sleep(0.1)
            _qapp.processEvents()

        time.sleep(1)

        self.assertTrue(os.path.isdir(outputdir))
        self.assertTrue(self.checkDataCopied())

    def checkDataCopied(self):
        outputdir = os.path.join(self.targettedir, os.path.basename(self.sourcedir))
        outputFiles = os.listdir(outputdir)
        inputFile = glob(self.sourcedir)

        return ((len(inputFile) == 0) and (len(outputFiles) == (self.n_file+2))
                and (not os.path.isdir(self.sourcedir)))


def suite():
    test_suite = unittest.TestSuite()
    for ui in (TestFolderTransfertWidget, ):
        test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(ui))
    return test_suite


if __name__ == '__main__':
    unittest.main(defaultTest="suite")
