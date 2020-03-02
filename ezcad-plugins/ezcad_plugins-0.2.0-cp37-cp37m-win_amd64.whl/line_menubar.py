# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import os
import sys
if os.path.realpath(os.path.dirname(__file__)) not in sys.path:
    sys.path.append(os.path.realpath(os.path.dirname(__file__)))

from ezcad.config.base import _
from ezcad.widgets.mode_switch import PluginMenuBar
from ezcad.utils.qthelpers import MENU_SEPARATOR, create_action, add_actions
from goline.bartender import Bartender


class LineMenuBar(PluginMenuBar):
    NAME = "Line Menubar"

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
            self.act_new_coord,
            self.act_new_from_point,
            MENU_SEPARATOR,
            self.act_new_by_picking,
        ]
        self.edit_menu_actions = [
            self.act_translate_xyz,
            self.act_flip_depth,
            self.act_copy_property,
        ]
        self.gate_menu_actions = [
            self.act_import_gocad_pline,
            self.act_import_csv,
            MENU_SEPARATOR,
            self.act_export_csv,
        ]

        add_actions(self.new_menu, self.new_menu_actions)
        add_actions(self.edit_menu, self.edit_menu_actions)
        add_actions(self.gate_menu, self.gate_menu_actions)

    def make_actions(self):
        self.act_new_coord = create_action(self, _('From coordinates'),
            triggered=self.bartender.new_from_coord)
        self.act_new_from_point = create_action(self, _('From point'),
            triggered=self.bartender.new_from_point)
        self.act_new_by_picking = create_action(self, _('Hand picking'),
            triggered=self.bartender.new_by_picking)
        self.act_translate_xyz = create_action(self, _('Translate XYZ'),
            triggered=self.bartender.object_translate_xyz)
        self.act_flip_depth = create_action(self, _('Flip depth'),
            triggered=self.bartender.object_flip_depth)
        self.act_copy_property = create_action(self, _('Copy property'),
            triggered=self.bartender.open_copy_property)
        self.act_import_gocad_pline = create_action(self,
            _('Import Gocad Pline file (.pl)'),
            triggered=self.bartender.import_gocad_pline)
        self.act_import_csv = create_action(self, _('Import CSV file'),
            triggered=self.bartender.import_csv)
        self.act_export_csv = create_action(self, _('Export CSV file'),
            triggered=self.bartender.export_csv)
