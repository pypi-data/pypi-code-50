#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains model checker implementation for Artella
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import artellapipe


class ArtellaModelChecker(artellapipe.PyblishTool, object):

    def __init__(self, project, config, settings, parent):

        super(ArtellaModelChecker, self).__init__(project=project, config=config, settings=settings, parent=parent)
