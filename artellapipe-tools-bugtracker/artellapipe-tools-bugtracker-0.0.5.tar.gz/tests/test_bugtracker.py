#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains tests for artellapipe-tools-bugtracker
"""

import pytest

from artellapipe.tools.bugtracker import __version__


def test_version():
    assert __version__.__version__
