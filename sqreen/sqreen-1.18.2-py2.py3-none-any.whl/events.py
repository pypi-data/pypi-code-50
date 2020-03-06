# -*- coding: utf-8 -*-
# Copyright (c) 2016, 2017, 2018, 2019 Sqreen. All rights reserved.
# Please refer to our terms for more information:
#
#     https://www.sqreen.io/terms.html
#
""" Sqreen attack event helpers and placeholder
"""
import traceback
from logging import getLogger

from .config import CONFIG
from .remote_exception import traceback_formatter
from .sanitizer import sanitize_attacks, sanitize_exceptions, sanitize_request

LOGGER = getLogger(__name__)


def get_context_payload():
    """ Return attack payload dependent on the context, right now stacktrace.
    """
    return {
        "context": {
            "backtrace": list(traceback_formatter(traceback.extract_stack()))
        }
    }


class Attack(object):
    def __init__(self, payload, rule_name):
        self.payload = payload
        self.rule_name = rule_name

    def to_dict(self):
        result = {}
        rule_payload = self.payload.get("rule", {})
        request_payload = self.payload.get("request", {})
        local_payload = self.payload.get("local", {})
        if "name" in rule_payload:
            result["rule_name"] = rule_payload["name"]
        if "rulespack_id" in rule_payload:
            result["rulespack_id"] = rule_payload["rulespack_id"]
        if "test" in rule_payload:
            result["test"] = rule_payload["test"]
        if "infos" in self.payload:
            result["infos"] = self.payload["infos"]
        if "time" in local_payload:
            result["time"] = local_payload["time"]
        if "remote_ip" in request_payload:
            result["client_ip"] = request_payload["remote_ip"]
        if "request" in self.payload:
            result["request"] = self.payload["request"]
        if "params" in self.payload:
            result["params"] = self.payload["params"]
        if "context" in self.payload:
            result["context"] = self.payload["context"]
        if "headers" in self.payload:
            result["headers"] = self.payload["headers"]
        return result


class RequestRecord(object):
    """Request record objects."""

    VERSION = "20171208"

    def __init__(self, payload):
        self.payload = payload

    def to_dict(self):
        """Export the record as a dict object."""
        result = {"version": self.VERSION}
        sensitive_values = None

        if "request" in self.payload:
            request_dict = self.payload["request"]
            result["request"] = request_dict
            if "client_ip" in request_dict:
                result["client_ip"] = request_dict.pop("client_ip")
        else:
            result["request"] = {}
        if "params" in self.payload:
            result["request"]["parameters"] = self.payload["params"]
        if "headers" in self.payload:
            result["request"]["headers"] = self.payload["headers"]

        if CONFIG["STRIP_SENSITIVE_DATA"]:
            sanitized_request, sensitive_values = sanitize_request(result["request"])
            result["request"] = sanitized_request

        if "response" in self.payload:
            result["response"] = self.payload["response"]

        if "observed" in self.payload:
            observed_dict = self.payload["observed"]
            result["observed"] = observed_dict
            rulespack = None
            attacks = observed_dict.get("attacks", [])
            for attack_dict in attacks:
                rulespack = attack_dict.pop("rulespack_id", None) or rulespack
            if attacks and sensitive_values:
                observed_dict["attacks"] = list(sanitize_attacks(attacks, sensitive_values))
            exceptions = observed_dict.get("sqreen_exceptions", [])
            for exc_dict in exceptions:
                payload_dict = exc_dict.pop("exception", None)
                if payload_dict:
                    exc_dict["message"] = payload_dict["message"]
                    exc_dict["klass"] = payload_dict["klass"]
                rulespack = exc_dict.pop("rulespack_id", None) or rulespack
            if exceptions and sensitive_values:
                observed_dict["sqreen_exceptions"] = list(sanitize_exceptions(exceptions, sensitive_values))
            if rulespack:
                result["rulespack_id"] = rulespack
            if "observations" in observed_dict:
                result["observed"]["observations"] = [
                    {"category": cat, "key": key, "value": value, "time": time}
                    for (cat, time, key, value) in observed_dict[
                        "observations"
                    ]
                ]
            if "sdk" in observed_dict:
                result["observed"]["sdk"] = [
                    {"name": entry[0], "time": entry[1], "args": entry[2:]}
                    for entry in observed_dict["sdk"]
                ]
        if "local" in self.payload:
            result["local"] = self.payload["local"]
        return result
