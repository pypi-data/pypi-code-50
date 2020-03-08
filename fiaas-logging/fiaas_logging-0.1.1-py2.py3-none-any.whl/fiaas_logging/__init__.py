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
from __future__ import absolute_import, unicode_literals

import datetime
import json
import logging
import sys
import threading

LOG_EXTRAS = threading.local()


class FiaasFormatter(logging.Formatter):
    UNWANTED = (
        "msg", "args", "exc_info", "exc_text", "levelno", "created", "msecs", "relativeCreated", "funcName",
        "filename", "lineno", "module")
    RENAME = {
        "levelname": "level",
        "threadName": "thread",
        "name": "logger",
    }

    def format(self, record):
        fields = vars(record).copy()
        fields["@timestamp"] = self.format_time(record)
        fields["@version"] = 1
        fields["LocationInfo"] = self._build_location(fields)
        fields["message"] = record.getMessage()
        fields["extras"] = getattr(record, "extras", {})
        if "exc_info" in fields and fields["exc_info"]:
            fields["throwable"] = self.formatException(fields["exc_info"])
        for original, replacement in self.RENAME.items():
            fields[replacement] = fields.pop(original)
        for unwanted in self.UNWANTED:
            fields.pop(unwanted)
        return json.dumps(fields, default=self._default_json_default)

    @staticmethod
    def format_time(record):
        """ELK is strict about it's timestamp, so use more strict ISO-format"""
        dt = datetime.datetime.fromtimestamp(record.created)
        return dt.isoformat()

    @staticmethod
    def _default_json_default(obj):
        """
        Coerce everything to strings.
        All objects representing time get output as ISO8601.
        """
        if isinstance(obj, (datetime.datetime, datetime.date, datetime.time)):
            return obj.isoformat()
        else:
            return str(obj)

    @staticmethod
    def _build_location(fields):
        return {
            "method": fields["funcName"],
            "file": fields["filename"],
            "line": fields["lineno"],
            "module": fields["module"]
        }


class ExtraFilter(logging.Filter):
    def filter(self, record):
        extras = {}
        for key, value in vars(LOG_EXTRAS).items():
            extras[key] = value
        record.extras = extras
        return 1


def set_extras(**kwargs):
    for key, value in kwargs.items():
        setattr(LOG_EXTRAS, key, value)


def init_logging(debug=False, format="plain"):
    """Set up logging system, according to best practice for cloud

    :param debug: Enable debug logging
    :param format: Select log format. Available options are "json" and "plain".
    """
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    if debug:
        root.setLevel(logging.DEBUG)
    root.addHandler(_create_default_handler(format))


def _create_default_handler(format):
    handler = logging.StreamHandler(sys.stdout)
    handler.addFilter(ExtraFilter())
    if format == "json":
        handler.setFormatter(FiaasFormatter())
    elif format == "plain":
        handler.setFormatter(logging.Formatter("[%(asctime)s|%(levelname)7s] %(message)s [%(name)s|%(threadName)s]"))
    return handler
