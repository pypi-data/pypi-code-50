#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from .config import g_config
from .py4j_util import LocalJvmBridge


class Session(object):
    _current_session = None
    _g = None
    _global_idx = 0

    def __init__(self, name=None, **kwargs):
        self._batch_sinks = []
        self._stream_ops = []
        self._table_dict = dict()
        self._udf_dict = dict()
        self._jvm_bridge = LocalJvmBridge.inst()
        self._config = g_config
        pass

    def __enter__(self):
        assert Session._current_session is None
        Session._current_session = self
        return self

    def __exit__(self, *args, **kwargs):
        assert Session._current_session is self
        Session._current_session = None
        pass

    @classmethod
    def inst(cls):
        if Session._current_session is None:
            if Session._g is None:
                Session._g = Session('global')
            return Session._g
        return Session._current_session
