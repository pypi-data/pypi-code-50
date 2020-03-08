#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool that allow to rename DCC nodes in an easy way
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from artellapipe.libs.naming.core import naminglib

from tpDcc.tools.renamer.widgets import renamer


class ArtellaRenamerWidget(renamer.RenamerWidget, object):

    NAMING_LIB = naminglib.ArtellaNameLib

    def __init__(self, config, parent):
        super(ArtellaRenamerWidget, self).__init__(config=config, parent=parent)
