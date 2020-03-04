from . import  (QtPrintSupport, QtWidgets, QtGui)
import os

class Shared:
    debugging = int(os.getenv('MUSICRAFT_DBG', 0))

def dbg_print(*pp, **kw):
    if Shared.debugging:
        print(*pp, **kw)


class Printer(QtPrintSupport.QPrinter):
    pageSize = QtPrintSupport.QPrinter.A4

    def __init__(self):
        dbg_print ("Printer.__init__")
        QtPrintSupport.QPrinter.__init__(self, QtPrintSupport.QPrinter.HighResolution)
        self.setPageSize(self.pageSize)
        dbg_print ("!Printer.__init__")


class WithMenu(object):
    menuTag = None

    def __init__(self):
        self.printer = Printer()
        self.compositeName = 'temp'  # under review, like so much!
        self.menu = QtWidgets.QMenu(self.menuTag)
        if not (self.menuTag and self.menuItems()):
            return
        for tag, shortcut, func in self.menuItems():
            action = self.myQAction(tag, shortcut=shortcut, triggered=func)
            self.menu.addAction(action)
        Shared.raft.menuBar().addMenu(self.menu)

    def menuItems(self):
        return [
        ]

    def myQAction(self, menuText, shortcut=None, triggered=None, enabled=None,
                  checkable=None, checked=None):
        action = QtWidgets.QAction(menuText, self)
        if shortcut:
            action.setShortcut(shortcut)
        if triggered:
            action.triggered.connect(triggered)
        if enabled is not None:
            action.setEnabled(enabled)
        if checkable is not None:
            action.setCheckable(checkable)
        if checked is not None:
            action.setChecked(checked)
        return action

    def printAll(self, toPDF=False):
        # fileName = self.compositeName +'.pdf'
        fileName = os.path.splitext(Shared.raft.editBook.activeEdit.fileName)[0] + '.pdf'
        print(fileName)
        if toPDF:
            files = QtWidgets.QFileDialog.getSaveFileName(self,
                "write PDF to file", fileName, '*.pdf')
            fileName = files[0]
            if not fileName:
                return
        self.printer.setDocName(fileName)
        self.printer.setOutputFileName(toPDF and fileName or '')
        self.renderAll(QtGui.QPainter(self.printer))

    def renderAll(self, painter):
        self.scene().render(painter)

    def printAllToPDF(self):
        self.printAll(toPDF=True)

