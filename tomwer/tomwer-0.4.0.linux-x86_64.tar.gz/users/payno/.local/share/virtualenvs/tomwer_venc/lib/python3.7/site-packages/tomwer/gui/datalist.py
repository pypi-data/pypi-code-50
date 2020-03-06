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

__authors__ = ["C. Nemoz", "H. Payno"]
__license__ = "MIT"
__date__ = "01/12/2016"

import logging
import os
from collections import OrderedDict

from silx.gui import qt

from tomwer.core.process.scanlist import _ScanList
from tomwer.core.scan.scanbase import TomoBase
from tomwer.core.utils import logconfig
from tomwer.gui.qfolderdialog import QScanDialog

logger = logging.getLogger(__name__)


class DataListDialog(qt.QWidget):
    """A simple list of dataset path.

    .. warning: the widget won't check for scan validity and will only
        emit the path to folders to the next widgets

    :param parent: the parent widget
    """
    def __init__(self, parent=None):
        qt.QWidget.__init__(self, parent)
        self.setLayout(qt.QVBoxLayout())
        # add list
        self.datalist = DataList(parent=self)
        self.layout().addWidget(self.datalist)
        # add buttons
        self._buttons = qt.QDialogButtonBox(parent=self)
        self._addButton = qt.QPushButton("Add", parent=self)
        self._buttons.addButton(self._addButton, qt.QDialogButtonBox.ActionRole)
        self._rmButton = qt.QPushButton("Remove", parent=self)
        self._buttons.addButton(self._rmButton, qt.QDialogButtonBox.ActionRole)
        self._rmAllButton = qt.QPushButton("Remove all", parent=self)
        self._buttons.addButton(self._rmAllButton, qt.QDialogButtonBox.ActionRole)

        self._sendButton = qt.QPushButton("Send", parent=self)
        self._buttons.addButton(self._sendButton, qt.QDialogButtonBox.AcceptRole)
        self.layout().addWidget(self._buttons)

        # expose API
        self._sendList = self.datalist._sendList
        self.add = self.datalist.add
        self.remove = self.datalist.remove
        self.setScanIDs = self.datalist.setScanIDs
        self._scheme_title = self.datalist._scheme_title
        self.length = self.datalist.length
        self.selectAll = self.datalist.selectAll
        self.clear = self.datalist.clear

        # connect signal / slot
        self._addButton.clicked.connect(self._callbackAddFolder)
        self._rmButton.clicked.connect(self._callbackRemoveFolder)
        self._rmAllButton.clicked.connect(self._callbackRemoveAllFolders)

    def _callbackAddFolder(self):
        """"""
        dialog = QScanDialog(self, multiSelection=True)

        if not dialog.exec_():
            dialog.close()
            return

        foldersSelected = dialog.filesSelected()
        for folder in foldersSelected:
            assert(os.path.isdir(folder))
            self.add(folder)

    def _callbackRemoveFolder(self):
        """"""
        selectedItems = self.datalist.selectedItems()
        toRemove = []
        if selectedItems is not None and len(selectedItems) > 0:
            for item in selectedItems:
                toRemove.append(item.text())
        for scan in toRemove:
            self.remove(scan)

    def _callbackRemoveAllFolders(self):
        self.datalist.selectAll()
        self._callbackRemoveFolder()


class DataList(_ScanList, qt.QTableWidget):
    def __init__(self, parent):
        _ScanList.__init__(self)
        qt.QTableWidget.__init__(self, parent)
        self.setRowCount(0)
        self.setColumnCount(1)
        self.setSortingEnabled(True)
        self.setHorizontalHeaderLabels(['folder'])
        self.verticalHeader().hide()
        if hasattr(self.horizontalHeader(), 'setSectionResizeMode'):  # Qt5
            self.horizontalHeader().setSectionResizeMode(0,
                                                         qt.QHeaderView.Stretch)
        else:  # Qt4
            self.horizontalHeader().setResizeMode(0, qt.QHeaderView.Stretch)
        self.setAcceptDrops(True)
        self.items = OrderedDict()

    def remove_item(self, item):
        """Remove a given folder
        """
        del self.items[item.text()]
        itemIndex = self.row(item)
        self.takeItem(itemIndex, 0)
        _ScanList.remove(self, item.text())
        self.removeRow(item.row())
        self.setRowCount(self.rowCount() - 1)
        self._update()

    def remove(self, scan):
        if scan is not None and scan in self.items:
            item = self.items[scan]
            itemIndex = self.row(item)
            self.takeItem(itemIndex, 0)
            _ScanList.remove(self, scan)
            del self.items[scan]
            self.removeRow(item.row())
            self.setRowCount(self.rowCount()-1)
            self._update()

    def _update(self):
        list_scan = list(self.items.keys())
        self.clear()
        for scan in list_scan:
            self.add(scan)
        self.sortByColumn(0, self.horizontalHeader().sortIndicatorOrder())

    def add(self, d):
        """Add the folder d in the scan list
        :param d: the path of the directory to add
        :type d: Union[str, TomoBase]
        """
        scan_obj = _ScanList.add(self, d)
        if scan_obj:
            self._addScanIDItem(scan_obj.path)

    def _addScanIDItem(self, d):
        if(not os.path.isdir(d)):
            warning = "Skipping the observation of %s, directory not existing on the system" % d
            logger.info(warning,
                           extra={logconfig.DOC_TITLE: self._scheme_title})
        elif d in self.items:
            warning = "The directory %s is already in the scan list" % d
            logger.info(warning)
        else:
            row = self.rowCount()
            self.setRowCount(row + 1)

            _item = qt.QTableWidgetItem()
            _item.setText(d)
            _item.setFlags(qt.Qt.ItemIsEnabled | qt.Qt.ItemIsSelectable)
            self.setItem(row, 0, _item)

            self.items[d] = _item

    def setScanIDs(self, scanIDs):
        [self._addScanIDItem(item) for item in scanIDs]
        _ScanList.setScanIDs(self, scanIDs)

    def clear(self):
        """Remove all items on the list"""
        self.items = OrderedDict()
        _ScanList.clear(self)
        qt.QTableWidget.clear(self)
        self.setRowCount(0)
        self.setHorizontalHeaderLabels(['folder'])
        if hasattr(self.horizontalHeader(), 'setSectionResizeMode'):  # Qt5
            self.horizontalHeader().setSectionResizeMode(0,
                                                         qt.QHeaderView.Stretch)
        else:  # Qt4
            self.horizontalHeader().setResizeMode(0, qt.QHeaderView.Stretch)

    def dropEvent(self, event):
        if event.mimeData().hasFormat('text/uri-list'):
            for url in event.mimeData().urls():
                self.add(str(url.path()))

    def supportedDropActions(self):
        """Inherited method to redefine supported drop actions."""
        return qt.Qt.CopyAction | qt.Qt.MoveAction

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/uri-list'):
            event.accept()
            event.setDropAction(qt.Qt.CopyAction)
        else:
            qt.QListWidget.dragEnterEvent(self, event)

    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat('text/uri-list'):
            event.setDropAction(qt.Qt.CopyAction)
            event.accept()
        else:
            qt.QListWidget.dragMoveEvent(self, event)



def main():
    app = qt.QApplication([])
    s = DataListDialog()
    s.show()
    app.exec_()


if __name__ == "__main__":
    main()
