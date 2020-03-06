# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import os
import sys
if os.path.realpath(os.path.dirname(__file__)) not in sys.path:
    sys.path.append(os.path.realpath(os.path.dirname(__file__)))

from ezcad.config.base import _
from ezcad.widgets.mode_switch import PluginMenuBar
from ezcad.utils.qthelpers import MENU_SEPARATOR, create_action, add_actions
from gocube.bartender import Bartender


class CubeMenuBar(PluginMenuBar):
    NAME = "Cube Menubar"

    def __init__(self):
        super().__init__()
        self.treebase = None
        self.bartender = None

        self.new_menu = self.addMenu(_("New"))
        self.edit_menu = self.addMenu(_("Edit"))
        self.tool_menu = self.addMenu(_("Tool"))
        self.gate_menu = self.addMenu(_("Gate"))

    def setup(self):
        # call bartender after set treebase
        self.bartender = Bartender(self.treebase)
        self.make_actions()
        self.new_menu_actions = [
            self.act_new_from_vidx,
            MENU_SEPARATOR,
            self.act_extract_subcube,
        ]
        self.edit_menu_actions = [
            self.act_translate_xyz,
            self.act_flip_depth,
            self.act_copy_property,
        ]
        self.tool_menu_actions = [
            self.act_cut_aline_section,
            self.act_property_from_gsurf,
            self.act_mask_by_gsurf,
        ]
        self.gate_menu_actions = [
            self.act_import_voxet,
            self.act_import_segy,
            self.act_import_javaseis,
            self.act_import_zgy,
            self.act_import_parms,
            MENU_SEPARATOR,
            self.act_export_voxet,
            self.act_export_segy,
            self.act_export_javaseis,
            self.act_export_zgy,
            self.act_export_parms,
        ]

        add_actions(self.new_menu, self.new_menu_actions)
        add_actions(self.edit_menu, self.edit_menu_actions)
        add_actions(self.tool_menu, self.tool_menu_actions)
        add_actions(self.gate_menu, self.gate_menu_actions)

    def make_actions(self):
        self.act_new_from_vidx = create_action(self, _('Create from indexes'),
            triggered=self.bartender.new_from_vidx)
        self.act_extract_subcube = create_action(self, _('Extract subcube'),
            triggered=self.bartender.extract_subcube)
        self.act_cut_aline_section = create_action(self,
            _('Cut section by arbitrary line'),
            triggered=self.bartender.cut_aline_section)
        self.act_translate_xyz = create_action(self, _('Translate XYZ'),
            triggered=self.bartender.object_translate_xyz)
        self.act_flip_depth = create_action(self, _('Flip depth'),
            triggered=self.bartender.object_flip_depth)
        self.act_copy_property = create_action(self, _('Copy property'),
            triggered=self.bartender.open_copy_property)
        self.act_property_from_gsurf = create_action(self,
            _('Create property from gsurface'),
            triggered=self.bartender.create_prop_from_gsurf)
        self.act_mask_by_gsurf = create_action(self,
            _('Create property mask by gsurface'),
            triggered=self.bartender.create_mask_by_gsurf)
        self.act_import_voxet = create_action(self, _('Import Voxet'),
            triggered=self.bartender.import_voxet)
        self.act_export_voxet = create_action(self, _('Export Voxet'),
            triggered=self.bartender.export_voxet)
        self.act_import_segy = create_action(self, _('Import Segy'),
            triggered=self.bartender.import_segy)
        self.act_export_segy = create_action(self, _('Export Segy'),
            triggered=self.bartender.export_segy)
        self.act_import_javaseis = create_action(self, _('Import JavaSeis'),
            triggered=self.bartender.import_javaseis)
        self.act_export_javaseis = create_action(self, _('Export JavaSeis'),
            triggered=self.bartender.export_javaseis)
        self.act_import_zgy = create_action(self, _('Import Zgy'),
            triggered=self.bartender.import_zgy)
        self.act_export_zgy = create_action(self, _('Export Zgy'),
            triggered=self.bartender.export_zgy)
        self.act_import_parms = create_action(self, _('Import VTB parms'),
            triggered=self.bartender.import_parms)
        self.act_export_parms = create_action(self, _('Export VTB parms'),
            triggered=self.bartender.export_parms)
