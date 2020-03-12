# -*- coding: utf-8 -*-

"""
Module that contains definitions for asset in Plot Twist
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import logging

import artellapipe.register
from artellapipe.core import defines, asset

LOGGER = logging.getLogger()


class PlotTwistAsset(asset.ArtellaAsset, object):
    def __init__(self, project, asset_data, node=None):
        super(PlotTwistAsset, self).__init__(project=project, asset_data=asset_data, node=node)

    def reference_rig_file(self, file_type, sync=False):
        """
        References rig file of the current asset
        :param file_type:
        :param sync:
        :return:
        """

        return self.reference_file(
            file_type=file_type, namespace=self.get_id(),
            status=defines.ArtellaFileStatus.PUBLISHED, sync=sync)


artellapipe.register.register_class('Asset', PlotTwistAsset)
