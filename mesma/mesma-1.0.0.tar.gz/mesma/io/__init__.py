# -*- coding: utf-8 -*-
"""
| ----------------------------------------------------------------------------------------------------------------------
| Date                : March 2020
| Copyright           : (C) 2018 by Ann Crabbé (KU Leuven)
| Email               : ann.crabbe@kuleuven.be
|
| This program is free software; you can redistribute it and/or modify it under the terms of the GNU
| General Public License as published by the Free Software Foundation; either version 3 of the
| License, or any later version.
| ----------------------------------------------------------------------------------------------------------------------
"""
import os
from qgis.PyQt.QtWidgets import QWidget


class EmittingStream:
    """ QObject to catch the terminal output and send it along with pyqtSignal. """

    def __init__(self, tab_widget):

        self.tab_widget = tab_widget
        self.log_index = tab_widget.indexOf(tab_widget.findChild(QWidget, 'tab_log'))
        self.log_widget = tab_widget.findChild(QWidget, 'logBrowser')

    def write(self, text):
        self.log_widget.append(text)
        self.tab_widget.setCurrentIndex(self.log_index)


def check_path(path):
    """ Check if path exists. Skip paths which are in memory

    :param path: the absolute path to the input file
    """
    if path == '':
        raise Exception("Path empty")

    elif not os.path.exists(path):
        raise Exception("Path {} does not exist.".format(path))
