#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains manager to handle playblasts in Solstice
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import logging
import contextlib

import tpDcc as tp
from tpDcc.libs.python import decorators

import artellapipe.register
from artellapipe.managers import playblasts

if tp.is_maya():
    import tpDcc.dccs.maya as maya
    from tpDcc.dccs.maya.core import gui, playblast

LOGGER = logging.getLogger()


class MayaPlayblastsManager(playblasts.PlayblastsManager, object):
    def __init__(self):
        super(MayaPlayblastsManager, self).__init__()

    def parse_current_scene(self):
        """
        Parse current Maya scene looking for settings related with play blasts
        :return: dict
        """

        time_control = maya.mel.eval("$gPlayBackSlider = $gPlayBackSlider")

        return {
            'start_frame': maya.cmds.playbackOptions(query=True, minTime=True),
            'end_frame': maya.cmds.playbackOptions(query=True, maxTime=True),
            'width': maya.cmds.getAttr('defaultResolution.width'),
            'height': maya.cmds.getAttr('defaultResolution.height'),
            'compression': maya.cmds.optionVar(query='playblastCompression'),
            'filename': (maya.cmds.optionVar(query='playblastFile') if maya.cmds.optionVar(
                query='playblastSaveToFile') else None),
            'format': maya.cmds.optionVar(query='playblastFormat'),
            'off_scren': (True if maya.cmds.optionVar(query='playblastOffscreen') else False),
            'show_ornaments': (True if maya.cmds.optionVar(query='playblastShowOrnaments') else False),
            'quality': maya.cmds.optionVar(query='playblastQuality'),
            'sound': maya.cmds.timeControl(time_control, query=True, sound=True) or None
        }

    def capture_scene(self, **options):
        path = super(MayaPlayblastsManager, self).capture_scene(options=options)
        path = playblast.fix_playblast_output_path(path)

        return path

    def _generate_playblast(self, **kwargs):
        """
        Implements base PlayblastsManager _generate_playblast_function
        """

        width = int(kwargs.get('width'))
        height = int(kwargs.get('height'))
        compression = kwargs.get('compression', 'H.264')
        format = kwargs.get('format', 'qt')
        percent = kwargs.get('percent', 100)
        quality = kwargs.get('quality', 100)
        viewer = kwargs.get('viewer', None)
        start_time = kwargs.get('start_frame')
        end_time = kwargs.get('end_frame')
        frame = kwargs.get('frame', None)
        if frame:
            start_time = frame
            end_time = frame
        off_screen = kwargs.get('off_screen', False)
        show_ornaments = kwargs.get('show_ornaments', True)
        force_overwrite = kwargs.get('overwrite', True)
        filename = kwargs.get('filename', None)
        raw_frame_numbers = kwargs.get('raw_frame_numbers', False)
        frame_padding = kwargs.get('frame_padding', 4)
        extra_args = kwargs.get('extra_args', {})
        isolate = kwargs.get('isolate', None)
        camera_options = kwargs.get('camera_options', None)
        display_options = kwargs.get('display_options', None)
        viewport_options = kwargs.get('viewport_options', None)
        viewport2_options = kwargs.get('viewport2_options', None)
        camera = kwargs.get('camera', None)

        padding = 10
        with gui.create_independent_panel(
                width=width + padding, height=height + padding, off_screen=off_screen) as panel:
            tp.Dcc.focus(panel)
            with contextlib.nested(
                    applied_viewport_options(viewport_options, panel, self.config),
                    applied_camera_options(camera_options, panel, self.config),
                    applied_display_options(display_options, self.config),
                    applied_viewport2_options(viewport2_options, self.config),
                    gui.disable_inview_messages(),
                    gui.maintain_camera_on_panel(panel=panel, camera=camera),
                    gui.isolated_nodes(nodes=isolate, panel=panel),
                    gui.reset_time()
            ):
                # Only image format supports raw frame numbers
                # so we ignore the state when calling it with a movie
                # format
                if format != "image" and raw_frame_numbers:
                    LOGGER.warning(
                        "Capturing to image format with raw frame numbers is not supported. "
                        "Ignoring raw frame numbers...")
                    raw_frame_numbers = False

        output = maya.cmds.playblast(
            compression=compression,
            format=format,
            percent=percent,
            quality=quality,
            viewer=viewer,
            startTime=start_time,
            endTime=end_time,
            offScreen=off_screen,
            showOrnaments=show_ornaments,
            forceOverwrite=force_overwrite,
            filename=filename,
            widthHeight=[width, height],
            rawFrameNumbers=raw_frame_numbers,
            framePadding=frame_padding,
            **extra_args
        )

        return output


@decorators.Singleton
class ArtellaMayaPlayblastsManagerSingleton(MayaPlayblastsManager, object):
    def __init__(self):
        MayaPlayblastsManager.__init__(self)


@contextlib.contextmanager
def applied_viewport_options(options, panel, config):
    """
    Context manager for applying options to panel
    :param options: dict
    :param panel: str
    :param config:
    """

    viewport_options = config.get('options', 'viewport')
    options = dict(viewport_options, **(options or {}))
    playblast_widgets = maya.cmds.pluginDisplayFilter(query=True, listFilters=True)
    widget_options = dict()

    for widget in playblast_widgets:
        if widget in options:
            widget_options[widget] = options.pop(widget)

    maya.cmds.modelEditor(panel, edit=True, **options)

    for widget, state in widget_options.items():
        maya.cmds.modelEditor(panel, edit=True, pluginObjects=(widget, state))

    yield


@contextlib.contextmanager
def applied_viewport2_options(options, config):
    """
    Context manager for setting viewport 2.0 options
    :param options: dict
    """

    viewport2_options = config.get('options', 'viewport2')
    options = dict(viewport2_options, **(options or {}))
    original = dict()

    for option in options.copy():
        try:
            original[option] = maya.cmds.getAttr('hardwareRenderingGlobals.' + option)
        except ValueError:
            options.pop(option)
    for option, value in options.items():
        maya.cmds.setAttr('hardwareRenderingGlobals.' + option, value)

    try:
        yield
    finally:
        for option, value in original.items():
            maya.cmds.setAttr('hardwareRenderingGlobals.' + option, value)


@contextlib.contextmanager
def applied_display_options(options, config):
    """
    Context manager for setting background color display options
    :param options: dict
    """

    display_options = config.get('options', 'display')
    options = dict(display_options, **(options or {}))
    colors = ['background', 'backgroundTop', 'backgroundBottom']
    preferences = ['displayGradient']
    original = dict()

    for clr in colors:
        original[clr] = maya.cmds.displayRGBColor(clr, query=True) or list()
    for preference in preferences:
        original[preference] = maya.cmds.displayPref(query=True, **{preference: True})
    for clr in colors:
        value = options[clr]
        maya.cmds.displayRGBColor(clr, *value)
    for preference in preferences:
        value = options[preference]
        maya.cmds.displayPref(**{preference: value})

    try:
        yield
    finally:
        for clr in colors:
            maya.cmds.displayRGBColor(clr, *original[clr])
        for preference in preferences:
            maya.cmds.displayPref(**{preference: original[preference]})


@contextlib.contextmanager
def applied_camera_options(options, panel, config):
    """
    Context manager for applying options to camera
    :param options: dict
    :param panel: str
    """

    camera_options = config.get('options', 'camera')
    camera = maya.cmds.modelPanel(panel, query=True, camera=True)
    options = dict(camera_options, **(options or {}))
    old_options = dict()

    for option in options.copy():
        try:
            old_options[option] = tp.Dcc.get_attribute_value(node=camera, attribute_name=option)
        except Exception as e:
            LOGGER.error('Could not get camera attribute for capture: "{}"'.format(option))

    for option, value in options.items():
        tp.Dcc.set_attribute_value(node=camera, attribute_name=option, attribute_value=value)

    try:
        yield
    finally:
        if old_options:
            for option, value in old_options.items():
                tp.Dcc.set_attribute_value(node=camera, attribute_name=option, attribute_value=value)


if tp.is_maya():
    artellapipe.register.register_class('PlayblastsMgr', ArtellaMayaPlayblastsManagerSingleton)
