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
__date__ = "22/03/2018"

import logging
import unittest
from tomwer.gui.qtapplicationmanager import QApplicationManager
from orangecontrib.tomwer.test.utils import OrangeWorflowTest
from tomwer.test.utils import UtilsTest
from tomwer.test.utils import skip_gui_test

app = QApplicationManager()
logging.disable(logging.INFO)


@unittest.skipIf(skip_gui_test(), reason='skip gui test')
@unittest.skip('Fail on CI...')
class TestScanListSampleMovedWorkflow(OrangeWorflowTest):
    """Make sure the sample moved is correctly connecting to the orange-canvas
    and that it will display requested scans
    """

    def setUp(self):
        super(TestScanListSampleMovedWorkflow, self).setUp()
        dataset = 'D2_H2_T2_h_'
        self.dataTestDir = UtilsTest.getDataset(dataset)

    def tearDow(self):
        super(TestScanListSampleMovedWorkflow, self).tearDow()

    @classmethod
    def setUpClass(cls):
        OrangeWorflowTest.setUpClass()
        # create widgets
        cls.nodeScanList = cls.addWidget(cls,
                                         'orangecontrib.tomwer.widgets.control.DataListOW.DataListOW')
        cls.nodeSampleMoved = cls.addWidget(cls,
                                            'orangecontrib.tomwer.widgets.visualization.SampleMovedOW.SampleMovedOW')
        cls.processOrangeEvents(cls)

        cls.link(cls, cls.nodeScanList, "data", cls.nodeSampleMoved, "data")
        cls.processOrangeEvents(cls)

        cls.scanListWidget = cls.getWidgetForNode(cls, cls.nodeScanList)
        cls.sampleMovedWidget = cls.getWidgetForNode(cls, cls.nodeSampleMoved)

    @classmethod
    def tearDownClass(cls):
        for node in (cls.nodeScanList, cls.nodeSampleMoved):
            cls.removeNode(cls, node)
        OrangeWorflowTest.tearDownClass()

    def test(self):
        self.assertTrue(len(self.sampleMovedWidget._mainWidget._images) is 0)

        self.scanListWidget.add(self.dataTestDir)
        self.scanListWidget._sendList()
        app.processEvents()
       

def suite():
    test_suite = unittest.TestSuite()
    for ui in (TestScanListSampleMovedWorkflow,):
        test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(ui))
    return test_suite


if __name__ == '__main__':
    unittest.main(defaultTest="suite")
