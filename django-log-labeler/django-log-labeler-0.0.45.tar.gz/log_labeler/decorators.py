import logging
from functools import wraps
from django.conf import settings
from log_labeler import ALLOWED_DYNAMIC_DEBUG_LEVEL_VALUES, LOG_LABEL_EXCLUDE_LOG_LIST, LOGGING


def process_dynamic_log_level(request):
    if "loggers" in getattr(settings, LOGGING):
        logger_names = list(getattr(settings, LOGGING)["loggers"].keys())
        exclude_log_list = getattr(settings, LOG_LABEL_EXCLUDE_LOG_LIST, list())
        for log_name in logger_names:
            if log_name not in exclude_log_list:
                logger = logging.getLogger(log_name)
                logger.setLevel(settings.DEFAULT_LOG_LEVEL)

        if settings.NIM_DJANGO_REQUEST_LOG_LEVEL_NAME in request.META:
            level_value = request.META.get(settings.NIM_DJANGO_REQUEST_LOG_LEVEL_NAME).upper()
            logger_message = logging.getLogger("django.request")
            if level_value in ALLOWED_DYNAMIC_DEBUG_LEVEL_VALUES:
                for log_name in logger_names:
                    if log_name not in exclude_log_list:
                        logger = logging.getLogger(log_name)
                        logger.setLevel(level_value)
                logger_message.info("The header '{}' has been overwritten to the value {}".format(
                    settings.NIM_DJANGO_REQUEST_LOG_LEVEL_NAME, level_value))
            else:
                logger_message.info("The header '{}' has an invalid value, the values allowed are {}".format(
                    settings.NIM_DJANGO_REQUEST_LOG_LEVEL_NAME, ", ".join(ALLOWED_DYNAMIC_DEBUG_LEVEL_VALUES)))


def dynamic_log_level():
    def _dynamic_log_level(func):  # pragma: no cover
        def dynamic_log_level_logic(*argv, **kwargs):
            if "request" in kwargs:
                request = kwargs["request"]
                process_dynamic_log_level(request)
            elif len(argv) > 1: #The first argument is the Django Rest HTTP request
                request = argv[1]
                process_dynamic_log_level(request)
            return func(*argv, **kwargs)

        return wraps(func)(dynamic_log_level_logic)

    return _dynamic_log_level
