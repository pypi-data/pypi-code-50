#!/usr/bin/env python
# -*- coding: utf-8

# Copyright 2017-2019 The FIAAS Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import unicode_literals, absolute_import

import json
import logging
import sys

import mock
import pytest
from callee import InstanceOf, Attrs, List
from six import StringIO

from fiaas_logging import ExtraFilter, set_extras, init_logging, FiaasFormatter, _create_default_handler

TEST_MESSAGE = "This is a test message"


def test_extras_filter():
    set_extras(key1="key1", key2="key2")
    filter = ExtraFilter()
    record = logging.LogRecord("name", "level", "pathname", "lineno", "msg", "args", "exc_info")
    filter.filter(record)
    assert record.extras["key1"] == "key1"
    assert record.extras["key2"] == "key2"


class TestLogSetup(object):
    @pytest.fixture(params=(True, False), ids=("Enable debug", "Disable debug"))
    def debug(self, request):
        yield request.param, logging.DEBUG if request.param else logging.INFO

    @pytest.fixture(params=("plain", "json"))
    def format(self, request):
        yield request.param, FiaasFormatter if request.param == "json" else logging.Formatter

    @staticmethod
    def _describe_stream_handler(formatter):
        return InstanceOf(logging.StreamHandler) & Attrs(stream=sys.stdout,
                                                         filters=List(of=InstanceOf(ExtraFilter)),
                                                         formatter=InstanceOf(formatter, exact=True))

    def test_init_logging(self, debug, format):
        enable_debug, loglevel = debug
        wanted_format, formatter = format
        root = mock.create_autospec(logging.root, name="mock_root_logger", instance=True, spec_set=True)
        root.level = logging.NOTSET

        with mock.patch("fiaas_logging.logging.getLogger") as m:
            def _get(name=None):
                if name is None:
                    return root
                return logging.Logger(name)

            m.side_effect = _get
            init_logging(enable_debug, wanted_format)
        root.addHandler.assert_called_once_with(self._describe_stream_handler(formatter))
        root.setLevel.assert_called_with(loglevel)

    def test_json_log_has_extra(self):
        log = logging.getLogger("test-logger")
        log.setLevel(logging.INFO)
        handler = _create_default_handler("json")
        log_buffer = StringIO()
        handler.stream = log_buffer
        log.addHandler(handler)
        set_extras(one="1", two="2")
        log.info(TEST_MESSAGE)
        log_entry = json.loads(log_buffer.getvalue())
        assert TEST_MESSAGE in log_entry["message"]
        assert log_entry["extras"]["one"] == "1"
        assert log_entry["extras"]["two"] == "2"
