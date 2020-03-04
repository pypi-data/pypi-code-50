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
from weakref import WeakValueDictionary
from functools import partial

from qgis.core import QgsProject
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QWidget, QMenu

from spectral_libraries.gui.spectral_library_gui import SpectralLibraryWidget
from spectral_libraries.gui.square_array_gui import SquareArrayWidget
from spectral_libraries.gui.ies_gui import IesWidget
from spectral_libraries.gui.ear_masa_cob_gui import EarMasaCobWidget
from spectral_libraries.gui.cres_gui import CresWidget
from spectral_libraries.resources_rc import qInitResources as viperResources
viperResources()


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
        self.menu = QMenu(title='Spectral Libraries', parent=self.iface.rasterMenu())
        self.menu.setIcon(QIcon(':/profile'))
        self.iface.rasterMenu().addMenu(self.menu)

        # Add an empty toolbar
        self.toolbar = self.iface.addToolBar('Spectral Library Tools')

        # Reference to all open Library Widgets
        self.opened_widgets = WeakValueDictionary()
        self.count = 0

        # Action when layer is removed (for spectral libraries)
        QgsProject.instance().layerWillBeRemoved[str].connect(self.remove_widget)

    def add_action(self, icon_path: str, text: str, callback: callable, enabled_flag: bool = True,
                   status_tip: str = None, add_to_toolbar = True, parent: QWidget = None) -> QAction:
        """ Add a toolbar item to the toolbar.

        :param icon_path: can be a resource path (e.g. ':/plugins/foo/bar.png') or a normal file system path
        :param text: text to be displayed on the menu item
        :param callback: function to be called when the action is triggered
        :param enabled_flag: flag indicating if the action should be enabled by default
        :param status_tip: optional text to show in a popup when mouse pointer hovers over the action
        :param add_to_toolbar: set to False if you do not want to add action to toolbar
        :param parent: parent widget for the new action
        :returns: The action that was created. Note that the action is also added to self.actions list
        """
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        self.menu.addAction(action)
        self.actions.append(action)

        return action

    def initGui(self):
        """ Create the menu entries and toolbar icons inside the QGIS GUI """

        self.add_action(icon_path=':/profile',
                        text='Create Library',
                        callback=self.start_library_widget,
                        add_to_toolbar=True,
                        status_tip='Create Library',
                        parent=self.iface.mainWindow())

        self.add_action(icon_path=':/cube',
                        text='Square Array',
                        callback=partial(self.run, 'square'),
                        add_to_toolbar=True,
                        status_tip='Square Array',
                        parent=self.iface.mainWindow())

        self.add_action(icon_path=':/iteration',
                        text='IES',
                        callback=partial(self.run, 'ies'),
                        add_to_toolbar=True,
                        status_tip='IES',
                        parent=self.iface.mainWindow())

        self.add_action(icon_path=':/average',
                        text="Ear, Masa, Cob",
                        callback=partial(self.run, 'emc'),
                        add_to_toolbar=True,
                        status_tip="Ear, Masa, Cob",
                        parent=self.iface.mainWindow())

        self.add_action(icon_path=':/percentage',
                        text='CRES',
                        callback=partial(self.run_show, 'cres'),
                        add_to_toolbar=False,
                        status_tip='CRES',
                        parent=self.iface.mainWindow())

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        self.iface.rasterMenu().removeAction(self.menu.menuAction())

        for action in self.actions:
            self.iface.removeToolBarIcon(action)

        # remove the toolbar
        del self.toolbar

    @staticmethod
    def run(name: str):
        switcher = {
            'square': SquareArrayWidget(),
            'emc': EarMasaCobWidget(),
            'ies': IesWidget(),
        }

        widget = switcher[name]
        widget.show()
        widget.exec_()

    @staticmethod
    def run_show(name: str):
        switcher = {
            'cres': CresWidget()
        }

        widget = switcher[name]
        widget.show()

    def start_library_widget(self, *args, **kwds):

        self.count += 1

        for key in self.opened_widgets.keys():
            old_widget = self.opened_widgets[key]
            if not old_widget.isVisible():
                old_widget.show()

        new_widget = SpectralLibraryWidget(map_canvas=self.iface.mapCanvas())

        new_library = new_widget.speclib()
        new_library.setName("Spectral Library " + str(self.count))
        new_library_id = new_library.id()

        QgsProject.instance().addMapLayer(new_library)
        self.opened_widgets[new_library_id] = new_widget

        new_widget.show()

        """
        Adding a Spectral Library as a vector layer is simple but problematic:
        When a user removes a speclib from the QGIS layer tree, it will be deleted by the QgsLayerTreeRegistryBridge. 
        This ends in an ugly RuntimeError:  "wrapped C/C++ object of type SpectralLibrary has been deleted" 
        """

    def remove_widget(self, layer_id: str):

        if layer_id in self.opened_widgets.keys():
            widget = self.opened_widgets.pop(layer_id)
            if isinstance(widget, SpectralLibraryWidget):
                widget.close()
                del widget
