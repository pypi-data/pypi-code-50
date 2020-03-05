"""
docstring_ignore
--------------------------------------------------------
Date                : March 2020
Copyright           : (C) 2020 by Ann Crabbé (KU Leuven)
Email               : ann.crabbe@kuleuven.be
Acknowledgements    : Translated from VIPER Tools 2.0 (UC Santa Barbara, VIPER Lab)
                      Dar Roberts, Kerry Halligan, Philip Dennison, Kenneth Dudley, Ben Somers, Ann Crabbé

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation; either version 3 of the License, or any later version.
--------------------------------------------------------
docstring_ignore
"""
from os import path
from functools import partial

from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QWidget, QMenu

from mesma.gui.mesma_gui import MesmaWidget
from mesma.gui.mesma_visualisation_gui import ModelVisualizationWidget
from mesma.gui.shade_normalisation_gui import ShadeNormalisationWidget
from mesma.gui.hard_classification_gui import HardClassificationWidget
from mesma.resources_rc import qInitResources as Resources
Resources()


class MesmaPlugin:
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

        # Add an empty menu to the Raster Menu
        self.main_menu = QMenu(title='MESMA', parent=self.iface.rasterMenu())
        self.main_menu.setIcon(QIcon(':/mesma'))
        self.iface.rasterMenu().addMenu(self.main_menu)

        # Add an empty toolbar
        self.toolbar = self.iface.addToolBar('MESMA')

    def add_action(self, icon_path: str, text: str, callback: callable, enabled_flag: bool = True,
                   add_to_toolbar: bool = False, status_tip: str = None, parent: QWidget = None) -> QAction:
        """ Add a toolbar item to the toolbar.

        :param icon_path: can be a resource path (e.g. ':/plugins/foo/bar.png') or a normal file system path
        :param text: text to be displayed on the menu item
        :param callback: function to be called when the action is triggered
        :param enabled_flag: flag indicating if the action should be enabled by default
        :param add_to_toolbar: bool indicating whether or not to add this action to the toolbar
        :param status_tip: optional text to show in a popup when mouse pointer hovers over the action
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

        self.main_menu.addAction(action)
        self.actions.append(action)

        return action

    def initGui(self):
        """ Create the menu entries and toolbar icons inside the QGIS GUI """

        # use strings in the callback and not methods itself (eg "MesmaWidget()") to not initialize the widget at boot
        self.add_action(icon_path=':/mesma',
                        text='MESMA',
                        callback=partial(self.run, 'mesma'),
                        add_to_toolbar=True,
                        status_tip='MESMA',
                        parent=self.iface.mainWindow())

        self.add_action(icon_path=':/mesma-vis',
                        text='MESMA Visualisation',
                        callback=partial(self.run_show, 'vis'),
                        add_to_toolbar=True,
                        status_tip='MESMA Visualisation',
                        parent=self.iface.mainWindow())

        self.add_action(icon_path=':/histogram',
                        text='Soft to Hard Classification',
                        callback=partial(self.run, 'hc'),
                        add_to_toolbar=True,
                        status_tip='Soft to Hard Classification',
                        parent=self.iface.mainWindow())

        self.add_action(icon_path=':/shade',
                        text='Shade Normalisation',
                        callback=partial(self.run, 'shade'),
                        add_to_toolbar=True,
                        status_tip='Shade Normalisation',
                        parent=self.iface.mainWindow())

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        self.iface.rasterMenu().removeAction(self.main_menu.menuAction())

        for action in self.actions:
            self.iface.removeToolBarIcon(action)

        # remove the toolbar
        del self.toolbar

    @staticmethod
    def run(plugin: str):
        switcher = {
            'mesma': MesmaWidget(),
            'hc': HardClassificationWidget(),
            'shade': ShadeNormalisationWidget()
        }

        widget = switcher[plugin]
        widget.show()
        widget.exec_()

    @staticmethod
    def run_show(plugin: str):
        switcher = {
            'vis': ModelVisualizationWidget()
        }

        widget = switcher[plugin]
        widget.show()
