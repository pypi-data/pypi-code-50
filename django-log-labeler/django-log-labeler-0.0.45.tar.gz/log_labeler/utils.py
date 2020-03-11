import re
import math
import time
from django.conf import settings
from log_labeler import LOG_LABEL_OBFUSCATE

class Utils:
    @classmethod
    def get_nim_headers(cls, request):
        NIM_HEADER_REG_EXP = r"^HTTP\_NIM\_"
        HTTP_REG_EXP = r"^HTTP\_"
        nim_headers = dict()
        for key, value in request.META.items():
            if re.match(NIM_HEADER_REG_EXP, key):
                transformed_key = re.sub(HTTP_REG_EXP, "", key).replace("_", "-")
                nim_headers[transformed_key] = value

        return nim_headers

    @classmethod
    def get_all_headers(cls, request):
        headers = dict()
        for key, value in request.META.items():
            headers[key] = value

        return headers

    @classmethod
    def get_header_by_name(cls, request, header_name, default_value):
        return request.META.get(header_name, default_value)

    @classmethod
    def adjust_string_length(cls, value, max_length):
        TRUNCATE_INDICATOR = "---[TRUNCATED]---"
        if isinstance(value, bytes):
            value = value.decode("UTF-8")
        output = value

        if max_length and max_length.upper() != "OFF":
            max_length = int(max_length)
            value = value
            length = len(value)
            if length > max_length:
                extra_chars = int(math.floor((length - max_length) / 2))
                middle = int(math.floor(length / 2))
                output = "".join([value[:middle - extra_chars], TRUNCATE_INDICATOR, value[middle + extra_chars:]])
        return output

    @classmethod
    def get_time_in_milliseconds(cls):
        return int(round(time.time() * 1000))

    @classmethod
    def obfuscate_headers(cls, headers):
        _headers = headers.copy()
        log_label_obfuscate = getattr(settings, LOG_LABEL_OBFUSCATE, dict())
        if "headers" in log_label_obfuscate:
            for header_name in log_label_obfuscate["headers"]:
                if header_name in _headers:
                    _headers[header_name] = "[--HIDDEN--]"

        return _headers

    @classmethod
    def obfuscate_body(cls, body):
        log_label_obfuscate = getattr(settings, LOG_LABEL_OBFUSCATE, dict())
        if "body" in log_label_obfuscate:
            for pattern, replacement in log_label_obfuscate["body"].items():
                if re.search(pattern, body):
                    body = re.sub(pattern, replacement, body)

        return body

    @classmethod
    def obfuscate_response(cls, response):
        log_label_obfuscate = getattr(settings, LOG_LABEL_OBFUSCATE, dict())
        if "response" in log_label_obfuscate:
            for pattern, replacement in log_label_obfuscate["response"].items():
                if re.search(pattern, response):
                    response = re.sub(pattern, replacement, response)

        return response
