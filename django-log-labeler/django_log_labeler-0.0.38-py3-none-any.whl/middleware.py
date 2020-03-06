import time
import logging
import traceback
from django.core.exceptions import ImproperlyConfigured

from .utils import Utils
from django.conf import settings
from log_labeler import local, LOG_LABEL_REQUEST_SETTING, DEFAULT_HEADER_VALUE, \
        MAX_REQUEST_RESPONSE_SIZE, DEFAULT_LOG_LEVEL, \
        NIM_DJANGO_REQUEST_LOG_LEVEL_NAME, LOGGING

logger = logging.getLogger(__name__)


class HeaderToLabelMiddleware(object):
    """
    Provides full logging of requests and responses
    """
    _initial_http_body = None
    _request_start_time = None
    _TRUNCATE_INDICATOR = "---[TRUNCATED]---"
    _REQUEST = "Request"
    _RESPONSE = "Response"
    _ERROR = "Error"

    def __init__(self, get_response=None):
        if not hasattr(settings, LOG_LABEL_REQUEST_SETTING):
            raise ImproperlyConfigured(f"Please set {LOG_LABEL_REQUEST_SETTING}, it is the dictionary of header names and values that need to be appended to the log")

        if not hasattr(settings, MAX_REQUEST_RESPONSE_SIZE):
            raise ImproperlyConfigured(f"Please set {MAX_REQUEST_RESPONSE_SIZE}, it is the value of the max length of the response")

        if not hasattr(settings, DEFAULT_LOG_LEVEL):
            raise ImproperlyConfigured(f"Please set {DEFAULT_LOG_LEVEL}, it is the value of the log level")

        if not hasattr(settings, NIM_DJANGO_REQUEST_LOG_LEVEL_NAME):
            raise ImproperlyConfigured(f"Please set {NIM_DJANGO_REQUEST_LOG_LEVEL_NAME}, it is the value of the header name containing the correlation id")

        if not hasattr(settings, LOGGING):
            raise ImproperlyConfigured(f"Please set {LOGGING}, it is the list of log name whose log level will be updated")

        self.get_response = get_response


    def __get_time_in_milliseconds(self):
        return int(round(time.time() * 1000))

    def __is_debug(self):
        return logger.level != logging.INFO

    def _get_header(self, request, header_name):
        return request.META.get(header_name, DEFAULT_HEADER_VALUE)

    def process_request(self, request):
        self._initial_http_body = request.body
        self._request_start_time = self.__get_time_in_milliseconds()
        log_label_request_settings = getattr(settings, LOG_LABEL_REQUEST_SETTING, dict())

        nim_headers = Utils.get_raw_nim_headers(request)

        log_entry_info = dict(
            type=self._REQUEST,
            nim_headers=nim_headers,
            request_start_time_ms=self._request_start_time,
            method=request.method,
            url=request.build_absolute_uri()
        )

        log_entry_debug = dict(
            type=self._REQUEST,
            nim_headers=nim_headers,
            request_start_time_ms=self._request_start_time,
            request_end_time_ms=self.__get_time_in_milliseconds(),
            method=request.method,
            body=Utils.adjust_string_length(self._initial_http_body, getattr(settings, MAX_REQUEST_RESPONSE_SIZE)),
            url=request.build_absolute_uri()
        )

        for label, header_name in log_label_request_settings.items():
            header_value = self._get_header(request, header_name)
            setattr(local, label, header_value)
            setattr(request, label, header_value)
            log_entry_info[label] = header_value
            log_entry_debug[label] = header_value

        logger.debug('', log_entry_debug)
        logger.info('', log_entry_info)

    def process_response(self, request, response):
        nim_headers = Utils.get_raw_nim_headers(request)
        log_entry = dict(
            type=self._RESPONSE,
            nim_headers=nim_headers,
            request_start_time_ms=self._request_start_time,
            request_end_time_ms=self.__get_time_in_milliseconds(),
            method=request.method,
            body=Utils.adjust_string_length(self._initial_http_body,
                                            getattr(settings, MAX_REQUEST_RESPONSE_SIZE)) if response.status_code < 400 else self._initial_http_body,
            status_code=response.status_code,
            response=Utils.adjust_string_length(response.content,
                                                settings.MAX_REQUEST_RESPONSE_SIZE) if response.status_code < 400 else response.content,
            url=request.build_absolute_uri()
        )

        log_entry_info = dict(
            type=self._RESPONSE,
            nim_headers=nim_headers,
            request_start_time_ms=self._request_start_time,
            request_end_time_ms=self.__get_time_in_milliseconds(),
            status_code=response.status_code,
            method=request.method,
            url=request.build_absolute_uri()
        )

        log_label_request_settings = getattr(settings, LOG_LABEL_REQUEST_SETTING, dict())
        for label in log_label_request_settings:
            log_entry[label] = getattr(request, label)
            log_entry_info[label] = getattr(request, label)

        if response.status_code < 400:
            logger.debug(
                '', extra=log_entry
            )
        else:
            logger.error(
                '', extra=log_entry
            )

        logger.info(
            '', extra=log_entry_info
        )
        return response

    def process_exception(self, request, exception):
        nim_headers = Utils.get_raw_nim_headers(request)
        log_entry = dict(
            type=self._ERROR,
            nim_headers=nim_headers,
            request_start_time_ms=self._request_start_time,
            request_end_time_ms=self.__get_time_in_milliseconds(),
            method=request.method,
            body=Utils.adjust_string_length(self._initial_http_body, getattr(settings, MAX_REQUEST_RESPONSE_SIZE)),
            status_code="500",
            exception=str(exception),
            url=request.build_absolute_uri(),
            stack_trace=traceback.format_exc()
        )

        log_entry_info = dict(
            type=self._ERROR,
            nim_headers=nim_headers,
            request_start_time_ms=self._request_start_time,
            request_end_time_ms=self.__get_time_in_milliseconds(),
            status_code="500",
            method=request.method,
            url=request.build_absolute_uri()
        )

        log_label_request_settings = getattr(settings, LOG_LABEL_REQUEST_SETTING, dict())
        for label in log_label_request_settings:
            log_entry[label] = getattr(request, label)
            log_entry_info[label] = getattr(request, label)

        logger.error(
            '', extra=log_entry
        )
        logger.info(
            '', extra=log_entry_info
        )
        return exception
