#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Utility module that contains useful utilities and classes related with FFMpeg
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import os
import fileseq
import logging

import ffmpeg
from ffmpeg import nodes

from tpDcc.libs.python import python

from artellapipe.libs import ffmpeg as ffmpeg_lib

LOGGER = logging.getLogger()


def launch_stream(ffmpeg_stream, overwrite=True):
    """
    Executes all the FFMpeg operations of the given FFMpeg stream
    :param ffmpeg_stream: ffmpeg.nodes.Stream
    :param overwrite: bool
    """

    if not ffmpeg_stream:
        LOGGER.warning('Given FFMpeg stream to store is not valid! Aborting stream launch operation ...')
        return

    ffmpeg_executable = ffmpeg_lib.get_ffmpeg_executable()
    if not ffmpeg_executable or not os.path.isfile(ffmpeg_executable):
        return

    ffmpeg.run(ffmpeg_stream, cmd=ffmpeg_executable, overwrite_output=overwrite, quiet=True)


def get_file_input(input_file, check_file_path=True, **kwargs):
    """
    Returns FFMpeg input of the given file
    :param input_file: str or ffmpeg.nodes.FilterableStream
    :return:
    """

    if input_file and isinstance(input_file, (str, unicode)):
        if check_file_path:
            if os.path.isfile(input_file):
                return ffmpeg.input(input_file, **kwargs)
        else:
            return ffmpeg.input(input_file, **kwargs)
    elif isinstance(input_file, nodes.FilterableStream):
        return input_file
    else:
        LOGGER.warning('Given video file "{}" is not valid!'.format(input_file))

    return None


def save_to_file(ffmpeg_stream, output_path, run_stream=False, overwrite=True):
    """
    Stores given FFMpeg stream object into given output path
    :param ffmpeg_stream: ffmpeg.nodes.Stream
    :param output_path: str
    :param run_stream: bool
    :param overwrite: bool
    """

    if not ffmpeg_stream:
        LOGGER.warning('Given FFMpeg stream to store is not valid! Aborting stream store operation ...')
        return

    save = ffmpeg.output(ffmpeg_stream, output_path, loglevel='quiet')
    if not run_stream:
        return save

    launch_stream(save, overwrite=overwrite)


def draw_text(input_file, text, x=0, y=0, font_color=None, font_file=None, font_size=16, escape_text=False):
    input_file = get_file_input(input_file)
    if not font_color:
        font_color = 'white'
    new_text = ffmpeg.drawtext(
        input_file, text, x=x, y=y, fontcolor=font_color, fontfile=font_file, fontsize=font_size,
        escape_text=escape_text)

    return new_text


def overlay_inputs(input_1, input_2, x=0, y=0):
    """
    Function that overlays input_1 on top of input_2
    :param input_1: str or ffmpeg.nodes.FilterableStream
    :param input_2: str or ffmpeg.nodes.FilterableStream
    :param x: int
    :param y: int
    :return: ffmpeg.nodes.FilterableStream
    """
    stream_1 = get_file_input(input_1)
    stream_2 = get_file_input(input_2)
    if not stream_1 or not stream_2:
        return False

    overlay = ffmpeg.overlay(stream_1, stream_2, x=x, y=y)

    return overlay


def draw_timestamp_on_video(
        video_file, text=None, x=0, y=0, font_color=None, font_file=None, font_size=16, escape_text=False,
        timecode='00:00:00:00', timecode_rate=24):
    input_file = get_file_input(video_file)
    if not font_color:
        font_color = 'white'
    if text is None:
        text = ''
    draw_text = ffmpeg.drawtext(
        input_file, text, timecode=timecode, x=x, y=y, fontcolor=font_color, fontfile=font_file, fontsize=font_size,
        escape_text=escape_text, timecode_rate=timecode_rate)

    return draw_text


def create_video_from_sequence_file(
        file_in_sequence, output_file, sequence_number_padding=2, framerate=24,
        video_codec='libx264', run_stream=True):
    if not file_in_sequence or not os.path.isfile(file_in_sequence):
        return None

    sequence = fileseq.findSequenceOnDisk(file_in_sequence)
    frame_fill = str(sequence.zfill()).zfill(sequence_number_padding)
    frame_file = sequence.frame("#")
    frame_file = frame_file.replace('.#.', '.%{}d.'.format(frame_fill))

    sequence_input = get_file_input(
        frame_file, check_file_path=False, start_number=sequence.start(), framerate=framerate)

    output = ffmpeg.output(
        sequence_input, output_file, vcodec=video_codec, framerate=framerate)
    if not run_stream:
        return output

    launch_stream(output)


def create_video_from_list_of_files(list_of_files, output_file, framerate=24, video_codec='libx264', run_stream=True):
    list_of_files = [get_file_input(input_file) for input_file in list_of_files]
    if not list_of_files:
        return None

    concatenate = ffmpeg.concat(*list_of_files)
    output = ffmpeg.output(concatenate, output_file, vcodec=video_codec, framerate=framerate)
    if not run_stream:
        return output

    launch_stream(output)


def run_multiples_outputs_at_once(outputs_to_run, max_operations=15):
    """
    Run all the given outputs at once
    :param outputs_to_run: list
    :param max_operations: int
    :return:
    """

    operations_to_run = list()
    current_op = 0
    for op in outputs_to_run:
        operations_to_run.append(op)
        current_op += 1
        if current_op >= max_operations:
            merge = ffmpeg.merge_outputs(*operations_to_run)
            try:
                launch_stream(merge)
            except Exception as exc:
                for opt_to_run in operations_to_run:
                    launch_stream(opt_to_run)
            python.clear_list(operations_to_run)
            current_op = 0

    if operations_to_run:
        merge = ffmpeg.merge_outputs(*operations_to_run)
        try:
            launch_stream(merge)
        except Exception as exc:
            for opt_to_run in operations_to_run:
                launch_stream(opt_to_run)


def scale_video(video_file, new_width=None, new_height=None):
    if new_width is None and new_height is None:
        LOGGER.warning('Impossible to scale video because no given new dimensiones are valid!')
        return False

    video_input = get_file_input(video_file)
    if not video_input:
        return False

    raise NotImplementedError()
