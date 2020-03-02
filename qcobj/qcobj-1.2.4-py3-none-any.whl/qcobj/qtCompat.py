""" The main initialization of our PySide2/PyQt5 Package.

    Warning:
        This module tries to import PySide2 if available,
        otherwise defaults to PyQt5 for the GUI.
        To change this behaviour set *TRY_PYSIDE* to False.


    :Author:
        - 2009-2011 Nicola Creati
        - 2009-2020 Roberto Vidmar

    :Copyright: 2011-2020
              Nicola Creati <ncreati@inogs.it>
              Roberto Vidmar <rvidmar@inogs.it>

    :License: MIT/X11 License (see :download:`license.txt
                               <../../license.txt>`)
"""
TRY_PYSIDE = True

try:
    if not TRY_PYSIDE:
        raise ImportError()
    import PySide2.QtCore as _QtCore
    import PySide2.QtGui as _QtGui
    import PySide2.QtWidgets as _QtWidgets
    USES_PYSIDE = True
except ImportError:
    import PyQt5.QtCore as _QtCore
    import PyQt5.QtGui as _QtGui
    import PyQt5.QtWidgets as _QtWidgets
    USES_PYSIDE = False
finally:
    QtWidgets = _QtWidgets
    QtCore = _QtCore
    QtGui = _QtGui

if USES_PYSIDE:
    Signal = QtCore.Signal
    Slot = QtCore.Slot
    Property = QtCore.Property

    def getOpenFileName(*args, **kargs):
        """ Wrap to PySide QtWidgets.QFileDialog.getOpenFileName
        """
        pn, selectedFilter = QtWidgets.QFileDialog.getOpenFileName(*args, **kargs)
        return pn

    def getOpenFileNames(*args, **kargs):
        """ Wrap to PySide QtWidgets.QFileDialog.getOpenFileNames
        """
        pn, selectedFilter = QtWidgets.QFileDialog.getOpenFileNames(*args, **kargs)
        return pn

    def getSaveFileName(*args, **kargs):
        """ Wrap to PySide QtWidgets.QFileDialog.getSaveFileName
        """
        pn, selectedFilter = QtWidgets.QFileDialog.getSaveFileName(*args, **kargs)
        return pn
else:
    Signal = QtCore.pyqtSignal
    Slot = QtCore.pyqtSlot
    Property = QtCore.pyqtProperty

    def getOpenFileName(*args, **kargs):
        """ Wrap to PyQt4 QtWidgets.QFileDialog.getOpenFileName
        """
        return QtWidgets.QFileDialog.getOpenFileName(*args, **kargs)

    def getOpenFileNames(*args, **kargs):
        """ Wrap to PyQt4 QtWidgets.QFileDialog.getOpenFileNames
        """
        return QtWidgets.QFileDialog.getOpenFileNames(*args, **kargs)

    def getSaveFileName(*args, **kargs):
        """ Wrap to PyQt4 QtWidgets.QFileDialog.getSaveFileName
        """
        return QtWidgets.QFileDialog.getSaveFileName(*args, **kargs)

    QtCore.pyqtRemoveInputHook()

Qt = QtCore.Qt
