import os
import structlog
import log_labeler
import logging.config
import json_log_formatter

DEFAULT_LOG_LEVEL = os.getenv('LOGGING_LEVEL', 'INFO')

timestamper = structlog.processors.TimeStamper(fmt="iso")

logging.config.dictConfig(
    {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'json': {
                '()': 'json_log_formatter.JSONFormatter',
                'format': '%(message)s'
            }
        },
        'filters': {
            'header_to_label': {
                '()': 'log_labeler.filters.HeaderToLabelFilter',
            }
        },
        'handlers': {
            'django_request': {
                'level': 'DEBUG',
                'class': 'log_labeler.handlers.StructlogRawMessageHandler',
                'formatter': 'json',
                'filters': ['header_to_label'],
            },
            'gunicorn_access': {
                'level': 'DEBUG',
                'class': 'log_labeler.handlers.StructlogRawMessageHandler',
                'formatter': 'json',
                'filters': ['header_to_label'],
            }
        },
        'loggers': {
            'gunicorn.access': {
                'handlers': ['gunicorn_access'],
                'level': DEFAULT_LOG_LEVEL,
                'propagate': False,
                'qualname': 'gunicorn.access'
            },
            'django.request': {
                'handlers': ['django_request'],
                'level': os.getenv('DJANGO_REQUEST_LOG_LEVEL', DEFAULT_LOG_LEVEL),
                'propagate': False,
            },
            'urllib3': {
                'handlers': ['django_request'],
                'level': os.getenv('DJANGO_REQUEST_LOG_LEVEL', DEFAULT_LOG_LEVEL),
                'propagate': False,
            }
        }
    }
)

structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.PositionalArgumentsFormatter(),
        timestamper,
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    context_class=structlog.threadlocal.wrap_dict(dict),
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)


class GunicornLogger(object):
    """
    A stripped down version of https://github.com/benoitc/gunicorn/blob/master/gunicorn/glogging.py to provide structlog logging in gunicorn
    Modified from http://stevetarver.github.io/2017/05/10/python-falcon-logging.html
    """

    def __init__(self, cfg):
        self._error_logger = structlog.get_logger("gunicorn.error")
        self._error_logger.setLevel(logging.INFO)
        self._access_logger = structlog.get_logger("gunicorn.access")
        self._access_logger.setLevel(logging.INFO)
        self.cfg = cfg

    def critical(self, msg, *args, **kwargs) -> None:
        self._error_logger.error(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs) -> None:
        self._error_logger.error(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs) -> None:
        self._error_logger.warning(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs) -> None:
        self._error_logger.info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs) -> None:
        self._error_logger.debug(msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs) -> None:
        self._error_logger.exception(msg, *args, **kwargs)

    def log(self, lvl, msg, *args, **kwargs) -> None:
        self._error_logger.log(lvl, msg, *args, **kwargs)

    def access(self, resp, req, environ, request_time) -> None:
        status = resp.status
        if isinstance(status, str):
            status = status.split(None, 1)[0]

        self._access_logger.info(
            "request",
            method=environ["REQUEST_METHOD"],
            request_uri=environ["RAW_URI"],
            status=status,
            response_length=getattr(resp, "sent", None),
            request_time_seconds="%d.%06d" % (request_time.seconds, request_time.microseconds),
            pid="<%s>" % os.getpid(),
        )

    def reopen_files(self) -> None:
        pass  # we don't support files

    def close_on_exec(self) -> None:
        pass  # we don't support files
