#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains general tests for artellapipe-libs-ffmpeg
"""

import pytest

from artellapipe.libs.ffmpeg import __version__


def test_version():
    assert __version__.__version__
