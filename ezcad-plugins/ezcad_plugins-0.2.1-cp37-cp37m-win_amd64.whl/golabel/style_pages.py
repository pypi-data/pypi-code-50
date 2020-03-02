# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""
Style setting pages for label.
"""

from qtpy.QtCore import Qt
from qtpy.QtGui import QColor
from qtpy.QtWidgets import QLabel, QVBoxLayout, QFormLayout, QGroupBox, \
     QLineEdit, QPushButton, QColorDialog, QFontDialog, QScrollBar
from ezcad.config.base import _
from ezcad.utils import icon_manager as ima
from ezcad.widgets.style_page import StylePage


class GraphicsPage(StylePage):
    NAME = _("Graphics")
    ICON = ima.icon('genprefs')

    def setup_page(self):
        opacity = QLabel(_('Opacity'))
        self.opacity = QScrollBar(Qt.Horizontal)
        self.opacity.setMaximum(255)
        self.opacity.sliderMoved.connect(self.opacity_changed)
        color_picker = QPushButton(_('Pick color'))
        color_picker.clicked.connect(self.color_picker)
        font_picker = QPushButton(_('Pick font'))
        font_picker.clicked.connect(self.font_picker)
        text_layout = QFormLayout()
        text_layout.addRow(opacity, self.opacity)
        text_layout.addRow(color_picker, font_picker)
        text_group = QGroupBox(_("Text"))
        text_group.setLayout(text_layout)

        angle = QLabel(_('Angle'))
        self.angle = QLineEdit()
        anchor = QLabel(_('Anchor'))
        self.anchor = QLineEdit()
        width = QLabel(_('Text Width'))
        border = QLabel(_('Border'))
        fill = QLabel(_('Fill'))
        geom_layout = QFormLayout()
        geom_layout.addRow(angle, self.angle)
        geom_layout.addRow(anchor, self.anchor)
        geom_layout.addRow(width, QLabel(_('TODO')))
        geom_layout.addRow(border, QLabel(_('TODO')))
        geom_layout.addRow(fill, QLabel(_('TODO')))
        geom_group = QGroupBox(_("Geometry"))
        geom_group.setLayout(geom_layout)

        box = QVBoxLayout()
        box.addWidget(text_group)
        box.addWidget(geom_group)
        self.setLayout(box)

    def opacity_changed(self):
        opacity = self.opacity.value()
        self.qcolor.setAlpha(opacity)
        for item in self.dob.pg2d_labels:
            item.setColor(self.qcolor)

    def font_picker(self):
        font, valid = QFontDialog.getFont(self.font)
        if valid:
            self.font = font

    def color_picker(self):
        self.qcolor = QColorDialog.getColor(self.qcolor)

    def load_style(self):
        self.text_style = self.dob.text_style
        self.font = self.text_style['QFont']

        alpha = self.text_style['opacity']
        self.opacity.setValue(alpha)

        r, g, b, a = self.text_style['color']
        self.qcolor = QColor(r, g, b, alpha)  # integers 0-255

        angle = self.text_style['angle']
        self.angle.setText(str(angle))

        x, y = self.text_style['anchor']
        anchor = str(x) + ", " + str(y)
        self.anchor.setText(anchor)

    def apply_changes(self):
        angle = self.angle.text()
        anchor = self.anchor.text()
        opacity = self.opacity.value()
        angle = float(angle)
        self.qcolor.setAlpha(opacity)
        r, g, b, a = self.qcolor.getRgb()
        anchor = [x.strip() for x in anchor.split(',')]
        anchor = [float(x) for x in anchor]

        self.text_style['angle'] = angle
        self.text_style['anchor'] = anchor
        self.text_style['color'] = (r, g, b, opacity)
        self.text_style['opacity'] = opacity
        self.text_style['QColor'] = self.qcolor
        self.text_style['QFont'] = self.font
        self.text_style['font_size'] = self.font.pointSize()
        self.dob.set_text_style(text_style=self.text_style, update_plots=True)


class DataInfoPage(StylePage):
    NAME = "Information"
    ICON = ima.icon('DataInformation')

    def setup_page(self):
        name_label = QLabel(_("Object name"))
        name_value = QLabel(self.dob.name)
        nv_label = QLabel(_('Number of labels'))
        nv_value = QLabel(str(self.dob.n_vertexes))
        form = QFormLayout()
        form.addRow(name_label, name_value)
        form.addRow(nv_label, nv_value)
        box = QVBoxLayout()
        box.addLayout(form)
        self.setLayout(box)

    def load_style(self):
        pass

    def apply_changes(self):
        pass
