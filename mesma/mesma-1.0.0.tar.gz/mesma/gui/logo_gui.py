# -*- coding: utf-8 -*-
"""
| ----------------------------------------------------------------------------------------------------------------------
| Date                : September 2018
| Copyright           : (C) 2018 by Ann Crabbé (KU Leuven)
| Email               : ann.crabbe@kuleuven.be
| Acknowledgements    : VIPER and LUMOS logo's created for free at logomakr.com
|
| This program is free software; you can redistribute it and/or modify it under the terms of the GNU
| General Public License as published by the Free Software Foundation; either version 3 of the
| License, or any later version.
| ----------------------------------------------------------------------------------------------------------------------
"""
from qgis.PyQt.QtGui import QPixmap
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QWidget, QLabel, QHBoxLayout
from mesma.resources import qInitResources
qInitResources()


class LogoWidget(QWidget):
    """ QWidget with the project's logo. To be placed above each widget/dialog. """

    def __init__(self, parent=None):
        super(LogoWidget, self).__init__(parent=parent)

        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignHCenter)

        lumos = QLabel(self)
        lumos.setPixmap(QPixmap(':/lumos_full'))
        layout.addWidget(lumos)

        viper = QLabel(self)
        viper.setPixmap(QPixmap(':/viper_full'))
        layout.addWidget(viper)


def _run():
    from qgis.core import QgsApplication
    app = QgsApplication([], True)
    app.initQgis()

    z = LogoWidget()
    z.show()
    app.exec_()


if __name__ == '__main__':
    _run()
