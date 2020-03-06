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
__date__ = "05/04/2019"


import unittest
import tempfile
import shutil
import os
from tomwer.core.utils.scanutils import MockEDF
from tomwer.core.scan.scanbase import TomoBase
from tomwer.core.process.datatransfert import FolderTransfert


class TestDataTransfertIO(unittest.TestCase):
    """Test inputs and outputs types of the handler functions"""

    def setUp(self):
        self.origin_folder = tempfile.mkdtemp()
        self.scan_folder = os.path.join(self.origin_folder, 'scan_toto')
        os.mkdir(self.scan_folder)
        self.output_folder = tempfile.mkdtemp()

        self.scan = MockEDF.mockScan(scanID=self.scan_folder,
                                     nRadio=10,
                                     nRecons=1,
                                     nPagRecons=4,
                                     dim=10)
        self.transfert_process = FolderTransfert()
        self.transfert_process.setDestDir(self.output_folder)

    def tearDown(self):
        shutil.rmtree(self.origin_folder)
        shutil.rmtree(self.output_folder)

    def testInputOutput(self):
        """Test that io using TomoBase instance work"""
        for input_type in (dict, TomoBase):
            for _input in FolderTransfert.inputs:
                for return_dict in (True, False):
                    if os.path.exists(self.output_folder):
                        shutil.rmtree(self.output_folder)
                        os.mkdir(self.output_folder)

                    self.scan = MockEDF.mockScan(scanID=self.scan_folder,
                                                 nRadio=10,
                                                 nRecons=1,
                                                 nPagRecons=4,
                                                 dim=10)

                    with self.subTest(handler=_input.handler,
                                      return_dict=return_dict,
                                      input_type=input_type):
                        input_obj = self.scan
                        if input_obj is dict:
                            input_obj = input_obj.to_dict()
                        self.transfert_process._set_return_dict(return_dict)
                        out = getattr(self.transfert_process, _input.handler)(input_obj)
                        if return_dict:
                            self.assertTrue(isinstance(out, dict))
                        else:
                            self.assertTrue(isinstance(out, TomoBase))


def suite():
    test_suite = unittest.TestSuite()
    for ui in (TestDataTransfertIO, ):
        test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(ui))
    return test_suite
