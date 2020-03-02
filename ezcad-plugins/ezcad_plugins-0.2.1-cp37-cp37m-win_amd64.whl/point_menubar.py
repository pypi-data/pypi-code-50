# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import os
import sys
if os.path.realpath(os.path.dirname(__file__)) not in sys.path:
    sys.path.append(os.path.realpath(os.path.dirname(__file__)))

from ezcad.config.base import _
from ezcad.widgets.mode_switch import PluginMenuBar
from ezcad.utils.qthelpers import MENU_SEPARATOR, create_action, add_actions
from gopoint.bartender import Bartender


class PointMenuBar(PluginMenuBar):
    NAME = "Point Menubar"

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
            self.act_new_random,
            self.act_new_coord,
            MENU_SEPARATOR,
            self.act_new_xyz_from_existing_point,
            self.act_new_from_surf,
            self.act_merge_points,
            MENU_SEPARATOR,
            self.act_new_from_prop_value_range,
        ]
        self.edit_menu_actions = [
            self.act_translate_xyz,
            # self.act_separate_vertexes_near_fault,
            self.act_flip_depth,
            MENU_SEPARATOR,
            self.act_copy_property,
            self.act_calc_line_numbers,
            MENU_SEPARATOR,
            self.act_crop_by_polygon,
            self.act_clip_by_prop_value_range,
        ]
        self.tool_menu_actions = [self.act_cross_plot]
        self.gate_menu_actions = [
            self.act_import_gocad_vset,
            self.act_import_chd,
            self.act_import_numpy,
            self.act_import_csv_file,
            # self.act_import_csv_files,
            MENU_SEPARATOR,
            self.act_export_ascii,
        ]

        add_actions(self.new_menu, self.new_menu_actions)
        add_actions(self.edit_menu, self.edit_menu_actions)
        add_actions(self.tool_menu, self.tool_menu_actions)
        add_actions(self.gate_menu, self.gate_menu_actions)

    def make_actions(self):
        self.act_new_random = create_action(self, _('From random numbers'),
            triggered=self.bartender.new_from_random_numbers)
        self.act_new_coord = create_action(self, _('From coordinates'),
            triggered=self.bartender.new_from_coord)
        self.act_new_xyz_from_existing_point = create_action(self,
            _('New XYZ from existing point'),
            triggered=self.bartender.new_from_existing_point)
        self.act_new_from_prop_value_range = create_action(self,
            _('Subset from property value range'),
            triggered=self.bartender.subset_from_prop_range)
        self.act_crop_by_polygon = create_action(self,
            _('Crop by polygon'),
            triggered=self.bartender.crop_by_polygon)
        self.act_clip_by_prop_value_range = create_action(self,
            _('Clip by property value range'),
            triggered=self.bartender.clip_by_prop_range)
        self.act_merge_points = create_action(self,
            _('From merging points'),
            triggered=self.bartender.merge_points)
        self.act_new_from_surf = create_action(self,
            _('From surface vertexes'),
            triggered=self.bartender.new_from_surf)
        self.act_translate_xyz = create_action(self, _('Translate XYZ'),
            triggered=self.bartender.object_translate_xyz)
        # self.act_separate_vertexes_near_fault = create_action(self,
        #     _('Separate vertexes near fault'),
        #     triggered=self.bartender.separate_vertexes_near_fault)
        self.act_flip_depth = create_action(self, _('Flip depth'),
            triggered=self.bartender.object_flip_depth)
        self.act_copy_property = create_action(self, _('Copy property'),
            triggered=self.bartender.open_copy_property)
        self.act_calc_line_numbers = create_action(self,
            _('Calculate line numbers'),
            triggered=self.bartender.calc_line_numbers)
        self.act_cross_plot = create_action(self, _('Cross plot'),
            triggered=self.bartender.cross_plot)

        self.act_import_gocad_vset = create_action(self,
            _('Import Gocad VSet file (.vs)'),
            triggered=self.bartender.import_gocad_vset)
        self.act_import_chd = create_action(self,
            _('Import SeisSpace header dump'),
            triggered=self.bartender.import_chd)
        # self.act_import_sdt = create_action(self,
        #     _('Import Space delimited txt'),
        #     triggered=self.bartender.import_sdt)
        self.act_import_numpy = create_action(self,
            _('Import Numpy load text'),
            triggered=self.bartender.import_numpy)
        self.act_import_csv_file = create_action(self, _('Import CSV file'),
            triggered=self.bartender.import_csv)
        # self.act_import_csv_files = create_action(self, _('CSV files'),
        #     triggered=self.bartender.import_csv_files)
        self.act_export_ascii = create_action(self, _('Export ASCII file'),
            triggered=self.bartender.export_ascii)
