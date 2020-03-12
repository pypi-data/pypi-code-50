#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains general tests for plottwist-libs-pyblish
"""

import pytest

from plottwist.libs.pyblish import __version__


def test_version():
    assert __version__.__version__
