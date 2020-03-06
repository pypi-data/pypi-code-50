# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""
Style setting pages for cube.
"""

from qtpy.QtCore import Qt
from qtpy.QtGui import QColor
from qtpy.QtWidgets import QLabel, QVBoxLayout, QFormLayout, QSplitter, \
    QGroupBox, QPushButton, QColorDialog

from ezcad.config.base import _
from ezcad.utils import icon_manager as ima
from ezcad.widgets.style_page import StylePage
from ezcad.widgets.property_table import PropertyDistribtionTable
from .info_table import dict_vidx_table, dict_vxyz_table, \
    dict_parm_table, dict_sgmt_table


class GraphicsPage(StylePage):
    NAME = _("Graphics")
    ICON = ima.icon('genprefs')

    def setup_page(self):
        cage_group = QGroupBox(_("Cage"))
        lbl_edge_color = QLabel(_("Edge color"))
        btn_ec_palette = QPushButton(_('Palette'))
        btn_ec_palette.clicked.connect(self.edge_color_picker)
        form = QFormLayout()
        form.addRow(lbl_edge_color, btn_ec_palette)
        cage_layout = QVBoxLayout()
        cage_layout.addLayout(form)
        cage_group.setLayout(cage_layout)

        vbox = QVBoxLayout()
        vbox.addWidget(cage_group)
        self.setLayout(vbox)

    def edge_color_picker(self):
        self.edge_qcolor = QColorDialog.getColor(self.edge_qcolor)
        # self.dob.pgCage.setColor(self.edge_qcolor)

    def load_style(self):
        # self.edge_qcolor = self.dob.pgCage.edge_color
        self.edge_qcolor = QColor(255, 0, 0, 255)

    def apply_changes(self):
        pass


class DataInfoPage(StylePage):
    NAME = "Information"
    ICON = ima.icon('DataInformation')

    def setup_page(self):
        nv = self.dob.get_cell_number()
        nv_str = "{:,}".format(nv)  # with thousands separator

        name_label = QLabel(_("Object name"))
        name_value = QLabel(self.dob.name)
        nv_label = QLabel(_('Number of cells'))
        nv_value = QLabel(nv_str)

        form = QFormLayout()
        form.addRow(name_label, name_value)
        form.addRow(nv_label, nv_value)
        vbox = QVBoxLayout()
        vbox.addLayout(form)

        vsplit = QSplitter(Qt.Vertical)

        self.prop_table = PropertyDistribtionTable(self.dob.prop)
        btn_refresh = QPushButton(_('Refresh property table'))
        btn_refresh.clicked.connect(self.refresh_prop_table)
        vsplit.addWidget(btn_refresh)
        vsplit.addWidget(self.prop_table)

        vidx_table = dict_vidx_table(self.dob.dict_vidx)
        vsplit.addWidget(vidx_table)

        vxyz_table = dict_vxyz_table(self.dob.dict_vxyz)
        vsplit.addWidget(vxyz_table)

        parm_table = dict_parm_table(self.dob.dict_parm)
        vsplit.addWidget(parm_table)

        sgmt_table = dict_sgmt_table(self.dob.survey.geometry)
        vsplit.addWidget(sgmt_table)

        vbox.addWidget(vsplit)
        self.setLayout(vbox)

    def load_style(self):
        pass

    def apply_changes(self):
        pass
