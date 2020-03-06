# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""
Style setting pages for tri-surface.
"""

from qtpy.QtCore import Qt
from qtpy.QtGui import QColor
from qtpy.QtWidgets import QLabel, QVBoxLayout, QFormLayout, QCheckBox, \
    QGroupBox, QPushButton, QScrollBar, QColorDialog
from ezcad.config.base import _
from ezcad.utils import icon_manager as ima
from ezcad.widgets.style_page import StylePage
from ezcad.widgets.property_table import PropertyDistribtionTable


class GraphicsPage(StylePage):
    NAME = _("Tsurface Graphics")
    ICON = ima.icon('genprefs')

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.face_opacity = QScrollBar(Qt.Horizontal)
        self.face_pure = QCheckBox(_("Triangle faces use pure color"))
        self.draw_face = QCheckBox(_("Draw triangle faces"))
        self.draw_edge = QCheckBox(_("Draw triangle edges"))
        self.gb_face = QGroupBox(_("Triangle faces color selector"))
        self.gb_edge = QGroupBox(_("Triangle edges color selector"))
        self.face_color = None
        self.edge_color = None

    def setup_page(self):
        color = QLabel(_("Color"))
        face_palette = QPushButton(_('Palette'))
        face_palette.clicked.connect(self.face_color_picker)

        opacity = QLabel(_("Opacity"))
        self.face_opacity.setMaximum(255)
        self.face_opacity.sliderMoved.connect(self.face_opacity_changed)

        form = QFormLayout()
        form.addRow(color, face_palette)
        form.addRow(opacity, self.face_opacity)
        self.gb_face.setLayout(form)

        shader = QLabel(_("Shader TODO"))
        smooth = QLabel(_("Smooth TODO"))

        edge_color_label = QLabel(_("Color"))
        edge_palette = QPushButton(_('Palette'))
        edge_palette.clicked.connect(self.edge_color_picker)
        edge_layout = QFormLayout()
        edge_layout.addRow(edge_color_label, edge_palette)
        self.gb_edge.setLayout(edge_layout)

        box = QVBoxLayout()
        box.addWidget(self.face_pure)
        box.addWidget(self.draw_edge)
        box.addWidget(self.draw_face)
        box.addWidget(shader)
        box.addWidget(smooth)
        box.addWidget(self.gb_face)
        box.addWidget(self.gb_edge)
        self.setLayout(box)

        self.face_pure.stateChanged.connect(self.switch_mesh_color)
        self.draw_edge.stateChanged.connect(self.set_draw_edges)
        self.draw_face.stateChanged.connect(self.set_draw_faces)

    def switch_mesh_color(self):
        if self.face_pure.isChecked():
            # mesh color by pure color
            self.gb_face.setEnabled(True)
            self.set_mesh_pure_color()
        else:
            # mesh color by vertexes or faces
            self.gb_face.setEnabled(False)
            self.dob.update_plots_by_prop()

    def set_draw_faces(self):
        if self.draw_face.isChecked():
            draw_face = True
        else:
            draw_face = False
        self.dob.set_draw_faces(draw_face)

    def set_draw_edges(self):
        if self.draw_edge.isChecked():
            draw_edge = True
        else:
            draw_edge = False
        self.dob.set_draw_edges(draw_edge)

    def edge_color_picker(self):
        self.edge_color = QColorDialog.getColor(self.edge_color)
        color = self.edge_color.getRgb()
        self.dob.set_edge_pure_color(color)

    def face_color_picker(self):
        self.face_color = QColorDialog.getColor(self.face_color)
        self.set_mesh_pure_color()

    def face_opacity_changed(self):
        # TODO opacity not work, why?
        opacity = self.face_opacity.value()
        self.face_color.setAlpha(opacity)
        self.set_mesh_pure_color()

    def set_mesh_pure_color(self):
        color = self.face_color.getRgb()
        self.dob.set_mesh_pure_color(color)

    def load_style(self):
        r, g, b, a = self.dob.surf_style['face_color']
        self.face_color = QColor(r, g, b, a)  # integers 0-255
        self.face_opacity.setValue(a)

        r, g, b, a = self.dob.surf_style['edge_color']
        self.edge_color = QColor(r, g, b, a)  # integers 0-255

        self.face_pure.setChecked(self.dob.surf_style['face_pure'])
        self.draw_edge.setChecked(self.dob.surf_style['draw_edge'])
        self.draw_face.setChecked(self.dob.surf_style['draw_face'])

    def apply_changes(self):
        pass


class DataInfoPage(StylePage):
    NAME = "Information"
    ICON = ima.icon('DataInformation')

    def setup_page(self):
        name_label = QLabel(_("Object name"))
        name_value = QLabel(self.dob.name)
        nv_label = QLabel(_('Number of vertexes'))
        nv_value = QLabel(str(self.dob.n_vertexes))
        np_label = QLabel(_('Number of properties'))
        np_value = QLabel(str(len(self.dob.prop)))
        nt = self.dob.triangles['ijk'].shape[0]
        nt_label = QLabel(_('Number of triangles'))
        nt_value = QLabel(str(nt))

        form = QFormLayout()
        form.addRow(name_label, name_value)
        form.addRow(nv_label, nv_value)
        form.addRow(np_label, np_value)
        form.addRow(nt_label, nt_value)

        self.prop_table = PropertyDistribtionTable(self.dob.prop)
        refresh = QPushButton(_('Refresh property table'))
        refresh.clicked.connect(self.refresh_prop_table)

        box = QVBoxLayout()
        box.addLayout(form)
        box.addWidget(refresh)
        box.addWidget(self.prop_table)
        self.setLayout(box)

    def load_style(self):
        pass

    def apply_changes(self):
        pass


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = GraphicsPage()
    test.setup_page()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
