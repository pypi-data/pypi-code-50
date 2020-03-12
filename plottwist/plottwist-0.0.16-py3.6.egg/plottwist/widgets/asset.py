# -*- coding: utf-8 -*-

"""
Module that contains widgets related with Plot Twist assets
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import logging

import artellapipe.register
from artellapipe.widgets import asset

LOGGER = logging.getLogger()


class PlotTwistAssetWidget(asset.ArtellaAssetWidget, object):
    def __init__(self, asset, text=None, parent=None):
        super(PlotTwistAssetWidget, self).__init__(asset=asset, text=text, parent=parent)


artellapipe.register.register_class('AssetWidget', PlotTwistAssetWidget)
