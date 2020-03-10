#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Juelich Supercomputing Centre (JSC).
# Distributed under the terms of the Modified BSD License.

import pytest

from ..remoterenderer import RemoteRenderer

def test_example_creation_blank():
    w = RemoteRenderer()
    assert w.sessionURL == 'ws://localhost:8080/ws'
    assert w.authKey == 'wslink-secret'
    assert w.viewID == '-1'
