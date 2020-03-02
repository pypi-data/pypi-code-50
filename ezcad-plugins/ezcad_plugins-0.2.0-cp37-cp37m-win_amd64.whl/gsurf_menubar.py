# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import os
import sys
if os.path.realpath(os.path.dirname(__file__)) not in sys.path:
    sys.path.append(os.path.realpath(os.path.dirname(__file__)))

from ezcad.config.base import _
from ezcad.widgets.mode_switch import PluginMenuBar
from ezcad.utils.qthelpers import MENU_SEPARATOR, create_action, add_actions
from gogsurf.bartender import Bartender


class GsurfaceMenuBar(PluginMenuBar):
    NAME = "Gsurface Menubar"

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
            self.act_new_from_point,
            self.act_new_from_tsurf,
        ]
        self.edit_menu_actions = [
            self.act_translate_xyz,
            self.act_flip_depth,
            self.act_copy_property,
        ]
        self.tool_menu_actions = []
        self.gate_menu_actions = [
            self.act_import_npz,
            MENU_SEPARATOR,
            self.act_export_npz,
        ]

        add_actions(self.new_menu, self.new_menu_actions)
        add_actions(self.edit_menu, self.edit_menu_actions)
        add_actions(self.tool_menu, self.tool_menu_actions)
        add_actions(self.gate_menu, self.gate_menu_actions)

    def make_actions(self):
        self.act_new_from_point = create_action(self, _('New from Point'),
            triggered=self.bartender.new_from_point)
        self.act_new_from_tsurf = create_action(self, _('New from Tsurf'),
            triggered=self.bartender.new_from_tsurf)
        self.act_translate_xyz = create_action(self, _('Translate XYZ'),
            triggered=self.bartender.object_translate_xyz)
        self.act_flip_depth = create_action(self, _('Flip depth'),
            triggered=self.bartender.object_flip_depth)
        self.act_copy_property = create_action(self, _('Copy property'),
            triggered=self.bartender.open_copy_property)
        self.act_import_npz = create_action(self,
            _('Import Numpy npz file'),
            triggered=self.bartender.import_npz)
        self.act_export_npz = create_action(self,
            _('Export Numpy npz file'),
            triggered=self.bartender.export_npz)
