#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Library that extends tpNameIt library functionality to support paths templates
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from tpDcc.libs.python import decorators
from tpDcc.libs.nameit.core import namelib

from artellapipe.libs import naming


@decorators.Singleton
class ArtellaNameLib(namelib.NameLib, object):
    def __init__(self):
        namelib.NameLib.__init__(self)
        self.naming_file = naming.config.get_path()

        self.init_naming_data()
