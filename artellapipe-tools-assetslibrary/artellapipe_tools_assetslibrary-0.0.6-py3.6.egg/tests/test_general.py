#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains general tests for artellapipe-tools-assetslibrary
"""

import pytest

from artellapipe.tools.assetslibrary import __version__


def test_version():
    assert __version__.__version__
