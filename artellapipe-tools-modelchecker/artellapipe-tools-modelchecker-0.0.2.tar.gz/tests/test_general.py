#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains general tests for artellapipe-tools-modelchecker
"""

import pytest

from artellapipe.tools.modelchecker import __version__


def test_version():
    assert __version__.__version__
