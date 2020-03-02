# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import os
import sys
if os.path.realpath(os.path.dirname(__file__)) not in sys.path:
    sys.path.append(os.path.realpath(os.path.dirname(__file__)))

from ezcad.config.base import _
from ezcad.widgets.mode_switch import PluginMenuBar
from ezcad.utils.qthelpers import MENU_SEPARATOR, create_action, add_actions
from gosurvey.bartender import Bartender


class SurveyMenuBar(PluginMenuBar):
    NAME = "Survey Menubar"

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
            self.act_new_vt3,
        ]
        self.tool_menu_actions = [
            self.act_view_survey,
        ]
        self.gate_menu_actions = [
            self.act_import_vt3dc,
            self.act_import_sgmt,
            MENU_SEPARATOR,
            self.act_export_vt3dc,
        ]

        add_actions(self.new_menu, self.new_menu_actions)
        add_actions(self.tool_menu, self.tool_menu_actions)
        add_actions(self.gate_menu, self.gate_menu_actions)

    def make_actions(self):
        self.act_new_vt3 = create_action(self, _("From 3 vertices"),
            triggered=self.bartender.new_from_vt3)
        self.act_view_survey = create_action(self, _("View survey"),
            triggered=self.bartender.view_survey)
        self.act_import_vt3dc = create_action(self, _("Import vt3dc file"),
            triggered=self.bartender.import_vt3dc)
        self.act_import_sgmt = create_action(self, _("Import sgmt file"),
            triggered=self.bartender.import_sgmt)
        self.act_export_vt3dc = create_action(self, _("Export vt3dc file"),
            triggered=self.bartender.export_vt3dc)
