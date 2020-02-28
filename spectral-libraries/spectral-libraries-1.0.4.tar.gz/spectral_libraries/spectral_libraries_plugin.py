"""
docstring_ignore
--------------------------------------------------------
Date                : March 2020
Copyright           : (C) 2018 by Ann Crabbé (KU Leuven)
Email               : ann.crabbe@kuleuven.be
Acknowledgements    : Translated from VIPER Tools 2.0 (UC Santa Barbara, VIPER Lab)
                      Dar Roberts, Kerry Halligan, Philip Dennison, Kenneth Dudley, Ben Somers, Ann Crabbé

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation; either version 3 of the License, or any later version.
--------------------------------------------------------
docstring_ignore
"""
from os import path
from qgis.core import QgsProject
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QWidget, QMenu
from weakref import WeakValueDictionary
from functools import partial
from spectral_libraries.gui.spectral_library_gui import SpectralLibraryWidget
from spectral_libraries.gui.square_array_gui import SquareArrayWidget
from spectral_libraries.gui.ies_gui import IesWidget
from spectral_libraries.gui.ear_masa_cob_gui import EarMasaCobWidget
from spectral_libraries.gui.cres_gui import CresWidget
# from spectral_libraries.resources import qInitResources as viperResources
# viperResources()


class SpectralLibrariesPlugin:
    """ QGIS Plugin Implementation """

    def __init__(self, iface):
        """
        :param QgsInterface iface: the interface instance which provides the hook to manipulate the QGIS GUI at run time
        """
        # Save reference to the QGIS interface
        self.iface = iface

        # initialize plugin directory
        self.plugin_dir = path.dirname(__file__)

        # List of actions added by this plugin
        self.actions = []

        from .sitepackages.qps import initAll
        initAll()


        # Add an empty menu to the Raster Menu
        self.main_menu = QMenu(title='Spectral Libraries', parent=self.iface.rasterMenu())
        self.main_menu.setIcon(QIcon(':/profile'))
        self.lib_menu = QMenu(title='Spectral Library Creation', parent=self.main_menu)
        self.lib_menu.setIcon(QIcon(':/profile'))
        self.opt_menu = QMenu(title='Spectral Library Optimization', parent=self.main_menu)
        self.opt_menu.setIcon(QIcon(':/library'))
        self.main_menu.addMenu(self.lib_menu)
        self.main_menu.addMenu(self.opt_menu)
        self.iface.rasterMenu().addMenu(self.main_menu)

        # Add an empty toolbar
        self.toolbar = self.iface.addToolBar('Spectral Libraries')

        # Weak Reference for all open Library Widgets
        self.openLibraryWidgets = WeakValueDictionary()

        # Action when layer is removed (for spectral libraries)
        QgsProject.instance().layerWillBeRemoved[str].connect(self.removeLayer)

    def add_action(self, icon_path: str, text: str, callback: callable, enabled_flag: bool = True,
                   add_to_menu: str = None, add_to_toolbar: bool = False, status_tip: str = None,
                   whats_this: str = None, parent: QWidget = None) -> QAction:
        """ Add a toolbar item to the toolbar.

        :param icon_path: can be a resource path (e.g. ':/plugins/foo/bar.png') or a normal file system path
        :param text: text to be displayed on the menu item
        :param callback: function to be called when the action is triggered
        :param enabled_flag: flag indicating if the action should be enabled by default
        :param add_to_menu: str indicating in which submenu the action should be added ['lib', 'opt', 'mesma', 'post']
        :param add_to_toolbar: bool indicating whether or not to add this action to the toolbar
        :param status_tip: optional text to show in a popup when mouse pointer hovers over the action
        :param whats_this: optional text to show in the status bar when the mouse pointer hovers over the action
        :param parent: parent widget for the new action
        :returns: The action that was created. Note that the action is also added to self.actions list
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu == 'lib':
            self.lib_menu.addAction(action)
        if add_to_menu == 'opt':
            self.opt_menu.addAction(action)

        self.actions.append(action)

        return action

    def initGui(self):
        """ Create the menu entries and toolbar icons inside the QGIS GUI """

        self.add_action(icon_path=':/profile',
                        text='Create Library',
                        callback=self.startLibraryWidget,
                        add_to_menu='lib',
                        add_to_toolbar=True,
                        status_tip='Create Library',
                        parent=self.iface.mainWindow())

        self.add_action(icon_path=':/cube',
                        text='Square Array',
                        callback=partial(self.run, SquareArrayWidget()),
                        add_to_menu='opt',
                        add_to_toolbar=False,
                        status_tip='Square Array',
                        parent=self.iface.mainWindow())

        self.add_action(icon_path=':/iteration',
                        text='IES',
                        callback=partial(self.run, IesWidget()),
                        add_to_menu='opt',
                        add_to_toolbar=False,
                        status_tip='IES',
                        parent=self.iface.mainWindow())

        self.add_action(icon_path=':/average',
                        text="Ear, Masa, Cob",
                        callback=partial(self.run, EarMasaCobWidget()),
                        add_to_menu='opt',
                        add_to_toolbar=False,
                        status_tip="Ear, Masa, Cob",
                        parent=self.iface.mainWindow())

        self.add_action(icon_path=':/percentage',
                        text='CRES',
                        callback=partial(self.run_show, CresWidget()),
                        add_to_menu='opt',
                        add_to_toolbar=False,
                        status_tip='CRES',
                        parent=self.iface.mainWindow())

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        self.iface.rasterMenu().removeAction(self.main_menu.menuAction())

        for action in self.actions:
            self.iface.removeToolBarIcon(action)

        # remove the toolbar
        del self.toolbar

    @staticmethod
    def run(widget):
        widget.show()
        widget.exec_()

    @staticmethod
    def run_show(widget):
        widget.show()

    def startLibraryWidget(self, *args, **kwds):
        widget = SpectralLibraryWidget()
        widget.show()

        """
        Adding a Spectral Library as a vector layer is simple but problematic:
        When a user removes a speclib from the QGIS layer tree, it will be deleted by the QgsLayerTreeRegistryBridge. 
        This ends in an ugly RuntimeError:  "wrapped C/C++ object of type SpectralLibrary has been deleted" 
        """

        # solution part 1: close the SpectralLibraryWidget when the speclib layer is removed from the layer list
        QgsProject.instance().addMapLayer(widget.speclib())
        self.openLibraryWidgets[widget.speclib().id()] = widget

        # solution part 2: remove the speclib layer from the layer list if the SpectralLibraryWidget is closed
        # to be done

    def removeLayer(self, layerId: str):

        if layerId in self.openLibraryWidgets.keys():
            widget = self.openLibraryWidgets[layerId]

            QgsProject.instance().removeMapLayer(widget.speclib())

            if isinstance(widget, SpectralLibraryWidget):
                widget.close()

            del widget


