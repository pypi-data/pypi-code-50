# -*- coding: utf-8 -*-
# Copyright (c) 2016, 2017, 2018, 2019 Sqreen. All rights reserved.
# Please refer to our terms for more information:
#
#     https://www.sqreen.io/terms.html
#
"""Sanitizer used to remove sensitive data from our payload"""

import json
import logging
import re

from . import config
from .utils import Iterable, Mapping, flatten, is_string, is_unicode

LOGGER = logging.getLogger(__name__)

MASK = '<Redacted by Sqreen>'

SENSITIVE_KEYS = frozenset([k.strip() for k in config.CONFIG["STRIP_SENSITIVE_KEYS"].split(',')])
LOGGER.debug("Using sensitive keys %s", ", ".join(SENSITIVE_KEYS))
try:
    SENSITIVE_REGEX = re.compile(config.CONFIG["STRIP_SENSITIVE_REGEX"])
except re.error:
    SENSITIVE_REGEX = re.compile(config.CONFIG_DEFAULT_VALUE["STRIP_SENSITIVE_REGEX"])
    LOGGER.warning("Invalid regexp configuration: %s", config.CONFIG["STRIP_SENSITIVE_REGEX"])
finally:
    LOGGER.debug("Using sensitive regex %s", SENSITIVE_REGEX.pattern)


def sanitize_request(data, sensitive_keys=SENSITIVE_KEYS,
                     sensitive_regex=SENSITIVE_REGEX):
    """
    Sanitize sensitive data from an object. Return a 2-tuple with a sanitized
    copy of the data and a list of values that were sanitized.
    """
    sensitive_data = set()

    if is_string(data):
        if not is_unicode(data):
            data = data.decode("utf-8", errors="replace")
        if sensitive_regex.match(data):
            sensitive_data.add(data)
            data = MASK
        return data, sensitive_data

    elif isinstance(data, Mapping):
        new_data = {}
        for k, v in data.items():
            if k in sensitive_keys:
                new_data[k] = MASK
                if is_string(v):
                    sensitive_data.add(v)
                elif isinstance(v, Iterable):
                    keys, values = flatten(v)
                    sensitive_data.update(keys)
                    sensitive_data.update(values)
            else:
                ret_data, child_sensitive_data = sanitize_request(
                    v, sensitive_keys=sensitive_keys, sensitive_regex=sensitive_regex)
                new_data[k] = ret_data
                sensitive_data.update(child_sensitive_data)
        return new_data, sensitive_data

    elif isinstance(data, Iterable):
        new_data = []
        for v in data:
            ret_data, child_sensitive_data = sanitize_request(
                v, sensitive_keys=sensitive_keys, sensitive_regex=sensitive_regex)
            new_data.append(ret_data)
            sensitive_data.update(child_sensitive_data)
        return new_data, sensitive_data

    return data, sensitive_data


def sanitize_attacks(attacks, sensitive_values):
    """
    Sanitize sensitive data from a list of attacks. Return the sanitized
    attacks.
    """
    for attack in attacks:
        infos = attack.get("infos")
        if infos is None:
            continue

        waf_data = infos.get("waf_data")
        if waf_data is not None:
            try:
                if isinstance(waf_data, bytes):
                    waf_data = waf_data.decode("utf-8", errors="replace")
                waf_data = json.loads(waf_data)
                assert isinstance(waf_data, list)
            except (UnicodeDecodeError, ValueError, AssertionError):
                waf_data = []

            sensitive_values = {values.lower() for values in sensitive_values}
            new_waf_data = []
            for item in waf_data:
                filters = item.get("filter")
                if filters is not None:
                    for filter_item in filters:
                        resolved_value = filter_item.get("resolved_value")
                        if resolved_value is not None \
                                and resolved_value.lower() in sensitive_values:
                            filter_item["match_status"] = MASK
                            filter_item["resolved_value"] = MASK
                new_waf_data.append(item)

            infos["waf_data"] = json.dumps(new_waf_data, separators=(",", ":"))
        else:
            attack["infos"], _ = sanitize_request(infos)

        yield attack


def sanitize_exceptions(exceptions, sensitive_values):
    """
    Sanitize sensitive data from a list of exceptions. Return the sanitized
    exceptions.
    """
    for exc in exceptions:
        infos = exc.get("infos")
        if infos is not None:
            # We know the request contains PII, never send args
            # TODO more fine grained filtering
            args = infos.get("args")
            if args is not None and sensitive_values:
                infos.pop("args", None)

            waf_infos = infos.get("waf")
            if waf_infos is not None and sensitive_values:
                waf_infos.pop("args", None)

        yield exc
