# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""
Style setting pages for tri-surface.
"""

from qtpy.QtWidgets import QLabel, QVBoxLayout, QFormLayout, QPushButton
from ezcad.config.base import _
from ezcad.utils import icon_manager as ima
from ezcad.widgets.style_page import StylePage
from ezcad.widgets.property_table import PropertyDistribtionTable
from .grid_table import dict_sidx_table

# The graphics page is the exactly the same as that of the Tsurface,
# because the Gsurface.pg3d is GLSurfacePlotItem, which inherits GLMeshItem,
# and the Tsurface.pg3d is GLMeshItem.
# class GraphicsPage(StylePage):


class DataInfoPage(StylePage):
    NAME = "Information"
    ICON = ima.icon('DataInformation')

    def setup_page(self):
        name_label = QLabel(_("Object name"))
        name_value = QLabel(self.dob.name)
        prop = self.dob.current_property
        prop_array = self.dob.prop[prop]['array2d']
        grid = prop_array.shape
        nv_label = QLabel(_('Number of grids'))
        nv_value = QLabel(str(grid))
        np_label = QLabel(_('Number of properties'))
        np_value = QLabel(str(len(self.dob.prop)))

        form = QFormLayout()
        form.addRow(name_label, name_value)
        form.addRow(nv_label, nv_value)
        form.addRow(np_label, np_value)

        self.prop_table = PropertyDistribtionTable(self.dob.prop)
        refresh = QPushButton(_('Refresh property table'))
        refresh.clicked.connect(self.refresh_prop_table)
        box = QVBoxLayout()
        box.addLayout(form)
        box.addWidget(refresh)
        box.addWidget(self.prop_table)

        table_sidx = dict_sidx_table(self.dob.dict_sidx_ln)
        box.addWidget(table_sidx)
        self.setLayout(box)

    def load_style(self):
        pass

    def apply_changes(self):
        pass
