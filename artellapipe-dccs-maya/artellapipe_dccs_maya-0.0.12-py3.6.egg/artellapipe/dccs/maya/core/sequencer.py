#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains functions and classes to handle Maya sequencer
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import os
import logging

import tpDcc.dccs.maya as maya

LOGGER = logging.getLogger()


class SequencerShotExporter(object):
    def __init__(self, anim_curves):
        super(SequencerShotExporter, self).__init__()

        self._anim_curves = anim_curves

    def export_shot_animation_curves(self, export_file_path, start_frame, end_frame,
                                     sequencer_least_key, sequencer_great_key, **kwargs):
        """
        Exports given shot animation curves in the given path and in the given frame range
        :param export_file_path: str, file path to export animation curves information into
        :param start_frame: int, start frame to export animation from
        :param end_frame: int, end frame to export animation until
        :param args:
        :param kwargs:
        :return:
        """

        from tpDcc.dccs.maya.core import animation

        animation.load_maya_animation_import_export_plugin()

        maya.cmds.select(self._anim_curves)
        export_anim_dir = os.path.dirname(export_file_path)
        if not os.path.isdir(export_anim_dir):
            LOGGER.error('Animation export directory does not exists!: {}'.format(export_anim_dir))
            return None

        frames_range = str(int(start_frame)), str(int(end_frame))
        frames = (start_frame, end_frame)

        precision = kwargs.get('precision', 17)
        int_value = kwargs.get('int_value', 17)
        node_names = kwargs.get('node_names', 1)
        verbose_units = kwargs.get('verbose_units', 0)
        which_range = kwargs.get('which_range', 2)
        options = kwargs.get('options', 'curve')
        option = kwargs.get('option', 'curve')
        hierarchy = kwargs.get('hierarchy', 'none')
        control_points = kwargs.get('control_points', 0)
        shapes = kwargs.get('shapes', 1)
        shape = kwargs.get('shape', 1)
        help_pictures = kwargs.get('help_pictures', 1)
        use_channel_box = kwargs.get('use_channel_box', 0)
        copy_key_cmd = kwargs.get('copy_key_cmd', '-animation objects ')

        export_options = 'precision={};intValue={};nodeNames={};verboseUnits={};whichRange={};'.format(
            precision, int_value, node_names, verbose_units, which_range)
        export_options += 'range={0}:{0};'.format(frames_range)
        export_options += 'options={};hierarchy={};controlPoints={};shapes={};helpPictures={};'.format(
            options, hierarchy, control_points, shapes, help_pictures
        )
        export_options += 'useChannelBox={};copyKeyCmd={}'.format(
            use_channel_box, copy_key_cmd
        )
        export_options += '-time >%s:%s> -float >%s:%s> ' % (frames_range + frames_range)
        export_options += '-option {} -hierarchy {} -controlPoints {} -shape {} '.format(
            option, hierarchy, control_points, shape
        )

        # We force first and last frame keys to be tangents
        fixed_start_end_tangents = kwargs.get('fixed_start_end_tangents', True)
        if fixed_start_end_tangents:
            animation.convert_start_end_frame_anim_curve_tangents_to_fixed(self._anim_curves, frames)

        # We insert keys on frames if they does not exist yet
        insert_remove_keys = animation.InsertRemoveAnimCurveKeys(
            anim_curves=self._anim_curves, start_frame=start_frame, end_frame=end_frame,
            sequence_least_key=sequencer_least_key, sequence_great_key=sequencer_great_key)

        insert_missing_keys = kwargs.get('insert_missing_keys', True)
        if insert_missing_keys:
            insert_remove_keys.insert_missing_keys()

        maya.cmds.file(export_file_path, force=True, options=export_options, typ='animExport', pr=True, es=True)

        if insert_missing_keys:
            insert_remove_keys.remove_inserted_keys()

        return True

    def import_shot_animation_curves(
            self, import_file_path, start_frame, end_frame, sequence_start_frame, sequence_end_frame,
            first_frame=False, **kwargs):
        """
        Imports given shot animation curves in the given path and in the given frame range
        :param import_file_path: str, file path to export animation curves information into
        :param start_frame: int, start frame to export animation from
        :param end_frame: int, end frame to export animation until
        :param first_frame: bool
        :return:
        """

        from tpDcc.dccs.maya.core import animation

        if not os.path.isfile(import_file_path):
            LOGGER.error('Animation file to import does not exists! "{}"'.format(import_file_path))
            return

        all_keyframes = sorted(maya.cmds.keyframe(self._anim_curves, query=True, timeChange=True))
        zero_k = all_keyframes[0]
        animation.key_all_anim_curves_in_frames(zero_k, self._anim_curves)
        LOGGER.info(
            'Set temp key on ALL "{}" animation curve nodes on frame "{}"'.format(self._anim_curves, zero_k))

        range_to_delete = (zero_k + 1, all_keyframes[-1])

        animation.delete_keys_from_animation_curves_in_range(
            range_to_delete=range_to_delete, anim_curves=self._anim_curves)
        LOGGER.info('Deleted animation before importing shot specific one on range: {}'.format(range_to_delete))

        animation.load_maya_animation_import_export_plugin()

        maya.cmds.select(self._anim_curves)

        frames = (start_frame, end_frame)

        target_time = kwargs.get('target_itme', 2)
        copies = kwargs.get('copies', 1)
        option = kwargs.get('option', None)
        if not option:
            option = 'fitReplace' if first_frame else 'scaleReplace'
        pictures = kwargs.get('pictures', 0)
        connect = kwargs.get('connect', 0)

        init_frame = start_frame
        last_frame = end_frame
        if first_frame:
            last_frame = start_frame + 1

        import_options = ';targetTime={};time={}:{};'.format(target_time, init_frame, last_frame)
        import_options += 'copies={};option={};pictures={};connect={};'.format(copies, option, pictures, connect)

        maya.cmds.file(import_file_path, i=True, mergeNamespacesOnClash=False, options=import_options, typ='animImport',
                       rpr='IM', pr=True, ignoreVersion=True, loadReferenceDepth='all')

        # We force first and last frame keys to be tangents
        fixed_start_end_tangents = kwargs.get('fixed_start_end_tangents', True)
        if fixed_start_end_tangents:
            animation.convert_start_end_frame_anim_curve_tangents_to_fixed(self._anim_curves, frames)

        if first_frame:
            second_frame = start_frame + 1
            key_exists = maya.cmds.keyframe(self._anim_curves, query=True, time=(second_frame, second_frame))
            if key_exists is not None:
                maya.cmds.cutKey(self._anim_curves, time=(second_frame, second_frame), clear=True)

        # all_anim_keys = animation.get_all_keyframes_in_anim_curves(self._anim_curves)
        # first_frame = all_anim_keys[0]
        # last_frame = all_anim_keys[-1]
        # if first_frame < sequence_start_frame:
        #     cut_end_frame = sequence_start_frame - 1
        #     maya.cmds.cutKey(self._anim_curves, time=(first_frame, cut_end_frame), clear=True)
        # if last_frame > sequence_end_frame:
        #     cust_start_frame = sequence_end_frame + 1
        #     maya.cmds.cutKey(self._anim_curves, time=(cust_start_frame, last_frame), clear=True)

        return True
