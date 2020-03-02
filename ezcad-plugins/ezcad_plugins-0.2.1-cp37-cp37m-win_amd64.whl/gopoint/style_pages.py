# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""
Style setting pages for point.

Improve from StyleEditor
no need to redo the plot and colorBar items, just set and update.
no need the signal and slot for add new plot, replace/remove old plot.
"""

# Standard library imports
import copy

# Third party imports
from qtpy.QtCore import Qt
from qtpy.QtGui import QColor
from qtpy.QtWidgets import QLabel, QComboBox, QVBoxLayout, QFormLayout, \
    QRadioButton, QHBoxLayout, QGroupBox, QPushButton, QColorDialog, \
    QScrollBar, QSpinBox, QButtonGroup

# Local imports
from ezcad.config.base import _
from ezcad.utils import icon_manager as ima
from ezcad.utils.plotting import atom_symbols
from ezcad.widgets.style_page import StylePage
from ezcad.widgets.property_table import PropertyDistribtionTable


class GraphicsPage(StylePage):
    NAME = _("Atom Graphics")
    ICON = ima.icon('genprefs')

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.opacity = QScrollBar(Qt.Horizontal)
        self.colorLabel = QLabel(_('Monocolor'))
        self.colorVary = QRadioButton(_('vary'))
        self.colorMono = QRadioButton(_('single'))
        self.symbol = QComboBox()
        self.size = QSpinBox()
        self.qtColor = None

    def setup_page(self):
        size = QLabel(_('Size'))
        # self.size.setRange(0, 10)
        symbol = QLabel(_('Symbol'))

        coloring = QLabel(_('Coloring'))
        bgMethod = QButtonGroup()
        bgMethod.addButton(self.colorMono)
        bgMethod.addButton(self.colorVary)
        hbMethod = QHBoxLayout()
        hbMethod.addWidget(self.colorMono)
        hbMethod.addWidget(self.colorVary)

        palette = QPushButton(_('Palette'))
        palette.clicked.connect(self.atom_color_picker)

        opacity = QLabel(_('Opacity'))
        self.opacity.setMaximum(255)
        # self.opacity.sliderMoved.connect(self.atom_opacity_changed)

        form = QFormLayout()
        form.addRow(size, self.size)
        form.addRow(symbol, self.symbol)
        form.addRow(coloring, hbMethod)
        form.addRow(self.colorLabel, palette)
        form.addRow(opacity, self.opacity)

        group = QGroupBox(_("Atom"))
        group.setLayout(form)

        box = QVBoxLayout()
        box.addWidget(group)
        self.setLayout(box)

    # def atom_opacity_changed(self):
    #     # pg.PlotDataItem.setAlpha < setOpacity
    #     # Is it inherited from QtGui.QGraphicsItem.setOpacity(float)?
    #
    #     atomOpacity = self.opacity.value()
    #     atomOpacityFloat = atomOpacity / 255.0  # scale to float 0.0-1.0
    #     self.pg2d.setAlpha(atomOpacityFloat, True)
    #     # self.pg2d.update()  # unnecessary
    #
    #     # Below is another way, put alpha in color RGBA, set brush.
    #     # self.qtColor.setAlpha(atomOpacity)
    #     # self.pg2d.setSymbolBrush(self.qtColor)
    #     # self.pg2d.updateItems() # necessary?
    #
    #     # update 3D plot
    #     self.qtColor.setAlpha(atomOpacity)
    #     color = self.qtColor.getRgbF()
    #     self.pg3d.setData(color=color)

    def atom_color_picker(self):
        self.qtColor = QColorDialog.getColor(self.qtColor)
        # print(self.qtColor.getRgb())  # (r, g, b, 255)
        self.colorLabel.setStyleSheet("QWidget { background-color: %s}" %
            self.qtColor.name())

    def load_style(self):
        if self.dob.atom_style is None:
            self.dob.set_atom_style()
        style = self.dob.atom_style

        self.size.setValue(style['size'])
        index = atom_symbols.index(style['symbol'])
        self.symbol.addItems(atom_symbols)
        self.symbol.setCurrentIndex(index)

        coloring = style['coloring']
        if coloring == 1:
            self.colorMono.setChecked(True)
        else:
            self.colorVary.setChecked(True)

        alpha = style['opacity']
        self.opacity.setValue(alpha)
        r, g, b, a = style['face_color']
        self.qtColor = QColor(r, g, b, alpha)  # integers 0-255

    def apply_changes(self):
        symbol = self.symbol.currentText()
        size = self.size.value()
        alpha = self.opacity.value()
        r, g, b, a = self.qtColor.getRgb()
        if self.colorMono.isChecked():
            coloring = 1
        else:
            coloring = 2
        style = copy.deepcopy(self.dob.atom_style)
        style['symbol'] = symbol
        style['size'] = size
        style['coloring'] = coloring
        style['face_color'] = (r, g, b, alpha)
        style['opacity'] = alpha
        # save style to object in memory
        self.dob.set_atom_style(atom_style=style, update_plots=True)


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
