#/*##########################################################################
# Copyright (C) 2016-2017 European Synchrotron Radiation Facility
#
# This file is part of the PyMca X-ray Fluorescence Toolkit developed at
# the ESRF by the Software group.
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
#############################################################################*/

__author__ = ["H. Payno"]
__license__ = "MIT"
__date__ = "08/02/2017"

from silx.gui import qt
import logging
import os


_logger = logging.getLogger()


class QScanDialog(qt.QFileDialog):
    """docstring for QFolderDialog"""
    def __init__(self, parent, multiSelection=False):
        qt.QFileDialog.__init__(self, parent)
        self.setFileMode(qt.QFileDialog.ExistingFiles)
        self.setOption(qt.QFileDialog.ShowDirsOnly)
        self.multiSelection = multiSelection
        # check if old data directory exists
        idir = False
        f_cd_last = os.environ['HOME'] + '/.octave/mylastpwd.txt'
        if os.path.isfile(f_cd_last) is True:
            with open(f_cd_last, "r") as fcdl:
                d_cd_last = fcdl.readlines()
                d_cd_last = d_cd_last[0][0:d_cd_last[0].rfind('/')]
                idir = os.path.isdir(d_cd_last)

        if idir is True:
            self.setDirectory(d_cd_last)
        else:
            self.setDirectory('/data')

        if self.multiSelection is True:
            # to make it possible to select multiple directories:
            self.file_view = self.findChild(qt.QListView, 'listView')
            if self.file_view:
                self.file_view.setSelectionMode(
                        qt.QAbstractItemView.MultiSelection)
                self.file_view.setSelectionMode(
                    qt.QAbstractItemView.ExtendedSelection)

            self.f_tree_view = self.findChild(qt.QTreeView)
            if self.f_tree_view:
                self.f_tree_view.setSelectionMode(
                        qt.QAbstractItemView.MultiSelection)
                self.f_tree_view.setSelectionMode(
                    qt.QAbstractItemView.ExtendedSelection)

            btns = self.findChildren(qt.QPushButton)
            if len(btns) is 0:
                _logger.error('Cannot retrieve open button. Multiple selection'
                              ' not available. Might came from an issue '
                              'with some PyQt(5) version. Had this issue '
                              'with PyQt5 5.9.2')
            else:
                self.openBtn = [x for x in btns if 'open' in str(x.text()).lower()][0]
                self.openBtn.clicked.disconnect()
                self.openBtn.hide()
                parent = self.openBtn.parent()
                self.openBtn = qt.QPushButton('Select', parent=parent)
                self.openBtn.clicked.connect(self.openClicked)
                parent.layout().insertWidget(0, self.openBtn)

    def openClicked(self):
        inds = self.f_tree_view.selectionModel().selectedIndexes()
        files = []
        for i in inds:
            if i.column() == 0:
                files.append(os.path.join(str(self.directory().absolutePath()), str(i.data())))
        self.selectedFiles = files
        self.accept()
        self.done(1)

    def filesSelected(self):
        return self.selectedFiles
