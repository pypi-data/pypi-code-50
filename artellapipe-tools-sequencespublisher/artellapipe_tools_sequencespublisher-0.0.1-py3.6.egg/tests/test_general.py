#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains general tests for artellapipe-tools-sequencespublisher
"""

import pytest

from artellapipe.tools.sequencespublisher import __version__


def test_version():
    assert __version__.__version__
