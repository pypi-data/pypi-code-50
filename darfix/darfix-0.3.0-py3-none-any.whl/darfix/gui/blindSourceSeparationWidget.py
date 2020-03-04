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


__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "07/02/2020"

import numpy

from silx.gui import qt

from darfix.core.blindSourceSeparation import Method, BSS
from .operationThread import OperationThread
from .displayComponentsWidget import DisplayComponentsWidget


class BSSWidget(qt.QMainWindow):
    """
    Widget to apply blind source separation.
    """

    def __init__(self, parent=None):
        qt.QMainWindow.__init__(self, parent)

        # Widget with the type of bss and the number of components to compute
        top_widget = qt.QWidget(self)

        methodLabel = qt.QLabel("Method: ")
        self.methodCB = qt.QComboBox()
        for method in Method.values():
            self.methodCB.addItem(method)
        nComponentsLabel = qt.QLabel("Num comp:")
        self.nComponentsLE = qt.QLineEdit("1")
        self.nComponentsLE.setValidator(qt.QIntValidator())
        self.computeButton = qt.QPushButton("Compute")
        maxNComponentsLabel = qt.QLabel("Max number of components:")
        self.maxNumComp = qt.QLineEdit("")
        self.maxNumComp.setToolTip("For a specific number of components enter an "
                                   "integer, for a\npercentage enter a float between "
                                   "0 (included) and 1 (not included).\n"
                                   "Float 0.5 will take as max number the 50% of "
                                   "the images.\nEmpty text computes all components.")
        self.maxNumComp.setValidator(qt.QDoubleValidator())
        self.detectButton = qt.QPushButton("Detect number of components")
        self.computeButton.setEnabled(False)
        self.detectButton.setEnabled(False)
        layout = qt.QGridLayout()

        layout.addWidget(methodLabel, 0, 0, 1, 1)
        layout.addWidget(self.methodCB, 0, 1, 1, 1)
        layout.addWidget(nComponentsLabel, 0, 2, 1, 1)
        layout.addWidget(self.nComponentsLE, 0, 3, 1, 1)
        layout.addWidget(self.computeButton, 0, 4, 1, 1)
        layout.addWidget(maxNComponentsLabel, 1, 2, 1, 1)
        layout.addWidget(self.maxNumComp, 1, 3, 1, 1)
        layout.addWidget(self.detectButton, 1, 4, 1, 1)

        top_widget.setLayout(layout)

        self.splitter = qt.QSplitter(qt.Qt.Vertical)
        self.splitter.addWidget(top_widget)
        self.setCentralWidget(self.splitter)

        self._displayComponentsWidget = DisplayComponentsWidget()
        self.splitter.addWidget(self._displayComponentsWidget)
        self._displayComponentsWidget.hide()

        self.computeButton.clicked.connect(self._computeBSS)
        self.detectButton.clicked.connect(self._detectComp)

    def hideButton(self):
        self._computeB.hide()

    def showButton(self):
        self._computeB.show()

    def setDataset(self, dataset):
        """
        Dataset setter. Saves the dataset and updates the stack with the dataset
        data

        :param Dataset dataset: dataset
        """
        self.dataset = dataset
        self.BSS = BSS(self.dataset.hi_data)
        self.computeButton.setEnabled(True)
        self.detectButton.setEnabled(True)

    def _computeBSS(self):
        """
        Computes blind source separation with the chosen method.
        """
        self.computeButton.setEnabled(False)
        self.nComponentsLE.setEnabled(False)
        method = Method(self.methodCB.currentText())
        n_comp = int(self.nComponentsLE.text())
        if method == Method.PCA:
            self._thread = OperationThread(self.BSS.PCA)
        elif method == Method.NNICA:
            self._thread = OperationThread(self.BSS.non_negative_ICA)
        elif method == Method.NMF:
            self._thread = OperationThread(self.BSS.NMF)
        elif method == Method.NNICA_NMF:
            self._thread = OperationThread(self.BSS.NNICA_NMF)
        else:
            raise ValueError('BSS method not managed')

        self._thread.setArgs(n_comp)
        self._thread.finished.connect(self._displayComponents)
        self._thread.start()

    def _displayComponents(self):
        self._thread.finished.disconnect(self._displayComponents)
        comp, self.W = self._thread.data
        n_comp = int(self.nComponentsLE.text())
        if comp.shape[0] < n_comp:
            n_comp = comp.shape[0]
            msg = qt.QMessageBox()
            msg.setIcon(qt.QMessageBox.Information)
            msg.setText("Found only {0} components".format(n_comp))
            msg.setStandardButtons(qt.QMessageBox.Ok)
            msg.exec_()
        self.comp = comp.reshape(n_comp, self.dataset.data.shape[1], self.dataset.data.shape[2])
        self._displayComponentsWidget.show()
        self.computeButton.setEnabled(True)
        self.nComponentsLE.setEnabled(True)
        if numpy.any(self.dataset.li_data):
            # If filter data is activated, the matrix W has reduced dimensionality, so reshaping is not possible
            # Create empty array with shape the total number of frames
            W = numpy.zeros((self.dataset.nframes, n_comp))
            # Set actual values of W where threshold of filter is True
            W[self.dataset.threshold] = self.W
            self.W = W
        self._displayComponentsWidget.setComponents(self.comp, self.W, self.dataset.get_dimensions_values())

    def _detectComp(self):
        txt = self.maxNumComp.text()
        if txt != "":
            maxNumComp = float(self.maxNumComp.text())
        else:
            maxNumComp = None
        self.detectButton.setEnabled(False)
        self._thread = OperationThread(self.BSS.PCA)
        self._thread.setArgs(None, maxNumComp)
        self._thread.finished.connect(self._setNumComp)
        self._thread.start()

    def _setNumComp(self):
        self._thread.finished.disconnect(self._setNumComp)
        mean, vecs, vals = self._thread.data
        vals /= numpy.sum(vals)
        components = len(vals[vals > 0.01])
        self.detectButton.setEnabled(True)
        self.nComponentsLE.setText(str(components))
