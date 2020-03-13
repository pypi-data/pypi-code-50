#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains manager that handles OCIO setup in Plot Twist
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import logging

import tpDcc as tp
from tpDcc.libs.python import decorators

import artellapipe.register
from artellapipe.managers import ocio

if tp.is_maya():
    import tpDcc.dccs.maya as maya
    from tpDcc.dccs.maya.core import colormanagement

LOGGER = logging.getLogger()


class ArtellaPlotTwistOCIOManager(ocio.ArtellaOCIOManager, object):
    def __init__(self):
        super(ArtellaPlotTwistOCIOManager, self).__init__()

    def init_ocio(self):
        super(ArtellaPlotTwistOCIOManager, self).init_ocio()

        self.set_arnold_renderer()

        if not colormanagement.is_color_management_enabled():
            colormanagement.enable_color_management()
        colormanagement.set_rendering_space('ACEScg')
        colormanagement.set_view_transform('ACES RRT v1.0')

        self.set_arnold_filter('blackman_harris')
        self.set_arnold_filter_width(1.2)
        self.set_arnold_antialiasing(1, 1, 1, 1, 1, 1)
        self.set_arnold_low_light_threshold(0.1)
        self.set_arnold_adaptative_sampling(True, 20, 0.03)

    def set_arnold_renderer(self):
        """
        Sets Arnold renderer as the active one
        """

        tp.Dcc.unlock_attribute('defaultRenderGlobals', 'currentRenderer')
        tp.Dcc.set_string_attribute_value('defaultRenderGlobals', 'currentRenderer', 'arnold')

        # We need to initialize this window to be able to set defaultArnoldRenderOptions
        if maya.cmds.window("unifiedRenderGlobalsWindow", exists=True):
            maya.cmds.deleteUI("unifiedRenderGlobalsWindow")
        maya.mel.eval('unifiedRenderGlobalsWindow;')
        if maya.cmds.window("unifiedRenderGlobalsWindow", exists=True):
            maya.cmds.deleteUI("unifiedRenderGlobalsWindow")

    def set_arnold_filter(self, filter_name):
        """
        Set the filter used by Arnold renderer
        :param filter_name: str, name of the filter used by Arnold
        """

        return tp.Dcc.set_string_attribute_value('defaultArnoldFilter', 'aiTranslator', str(filter_name))

    def set_arnold_filter_width(self, width):
        """
        Sets the widget used by current Arnold renderer filter
        :param width: float
        """

        return tp.Dcc.set_attribute_value('defaultArnoldFilter', 'width', float(width))

    def set_arnold_low_light_threshold(self, value):
        """
        Sets the low light threshold value used by Arnold renderer
        :param value: float
        """

        return tp.Dcc.set_string_attribute_value('defaultArnoldFilter', 'aiTranslator', float(value))

    def set_arnold_progressive_render(self, flag):
        """
        Sets whether Arnold progressive is render is enabled or not
        :param flag: bool
        """

        if tp.Dcc.attribute_exists('defaultArnoldRenderOptions', 'enableProgressiveRender'):
            return tp.Dcc.set_attribute_value('defaultArnoldRenderOptions', 'enableProgressiveRender', bool(flag))

    def set_arnold_antialiasing(self, aa_samples=3, diffuse_samples=2, specular_samples=2, transmission_samples=2,
                                sss_samples=2, volume_indirect_samples=2):
        """
        Sets the samples used by Arnold renderer antialising
        :param aa_samples: int
        :param diffuse_samples: int
        :param specular_samples: int
        :param transmission_samples: int
        :param sss_samples: int
        :param volume_indirect_samples: int
        """

        if aa_samples is not None:
            tp.Dcc.set_attribute_value('defaultArnoldRenderOptions', 'AASamples', int(aa_samples))
        if diffuse_samples is not None:
            tp.Dcc.set_attribute_value('defaultArnoldRenderOptions', 'GIDiffuseSamples', int(diffuse_samples))
        if specular_samples is not None:
            tp.Dcc.set_attribute_value('defaultArnoldRenderOptions', 'GISpecularSamples', int(specular_samples))
        if transmission_samples is not None:
            tp.Dcc.set_attribute_value('defaultArnoldRenderOptions', 'GITransmissionSamples', int(transmission_samples))
        if sss_samples is not None:
            tp.Dcc.set_attribute_value('defaultArnoldRenderOptions', 'GISssSamples', int(sss_samples))
        if volume_indirect_samples is not None:
            tp.Dcc.set_attribute_value('defaultArnoldRenderOptions', 'GIVolumeSamples', int(volume_indirect_samples))

    def set_arnold_adaptative_sampling(self, enabled, max_camera_aa=None, adaptative_threshold=None):
        """
        Sets the adaptative sampling of arnold
        :param enabled: bool
        :param max_camera_aa: int
        :param adaptative_threshold: float
        """

        if not tp.Dcc.attribute_exists('defaultArnoldRenderOptions', 'enableAdaptiveSampling'):
            LOGGER.warning('Adaptive Sampling is not available in your current Arnold version!')
            return

        if max_camera_aa is not None:
            tp.Dcc.set_attribute_value('defaultArnoldRenderOptions', 'AASamplesMax', int(max_camera_aa))
        if adaptative_threshold is not None:
            tp.Dcc.set_attribute_value('defaultArnoldRenderOptions', 'AAAdaptiveThreshold', float(adaptative_threshold))


@decorators.Singleton
class ArtellaPlotTwistOCIOManagerSingleton(ArtellaPlotTwistOCIOManager, object):
    def __init__(self):
        ArtellaPlotTwistOCIOManager.__init__(self)


artellapipe.register.register_class('OCIOMgr', ArtellaPlotTwistOCIOManagerSingleton)
