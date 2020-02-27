# -*- coding: utf-8 -*-
"""
logging services module.
"""

from pyrin.application.services import get_component
from pyrin.logging import LoggingPackage


def get_all_loggers():
    """
    gets a dictionary containing all available loggers.
    it returns a shallow copy of loggers dict.

    :returns: dict(str name: Logger instance)

    :rtype: dict
    """

    return get_component(LoggingPackage.COMPONENT_NAME).get_all_loggers()


def should_be_wrapped(logger):
    """
    gets a value indication that given logger should be wrapped.

    note that we should not wrap sqlalchemy and alembic loggers,
    because it does not affect on sqlalchemy loggers and they
    never have request info in emitted logs, I don't know the reason.
    but wrapping them actually has a side effect which leads to some errors.
    so we do not wrap them in the first place.

    :param Logger logger: logger to check should it be wrapped.

    :rtype: bool
    """

    return get_component(LoggingPackage.COMPONENT_NAME).should_be_wrapped(logger)


def reload_configs(**options):
    """
    reloads all logging configurations from config file.
    """

    return get_component(LoggingPackage.COMPONENT_NAME).reload_configs(**options)


def wrap_all_loggers():
    """
    wraps all available loggers into an adapter.
    normally, this method should not be called manually.
    """

    get_component(LoggingPackage.COMPONENT_NAME).wrap_all_loggers()


def get_logger(name, **options):
    """
    gets the logger based on input parameters.

    :param str name: logger name to get.

    :returns: specified logger.

    :rtype: Logger
    """

    return get_component(LoggingPackage.COMPONENT_NAME).get_logger(name, **options)


def debug(msg, *args, **kwargs):
    """
    emits a log with debug level.

    :param str msg: log message.
    """

    return get_component(LoggingPackage.COMPONENT_NAME).debug(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    """
    emits a log with info level.

    :param str msg: log message.
    """

    return get_component(LoggingPackage.COMPONENT_NAME).info(msg, *args, **kwargs)


def warning(msg, *args, **kwargs):
    """
    emits a log with warning level.

    :param str msg: log message.
    """

    return get_component(LoggingPackage.COMPONENT_NAME).warning(msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    """
    emits a log with error level.

    :param str msg: log message.
    """

    return get_component(LoggingPackage.COMPONENT_NAME).error(msg, *args, **kwargs)


def exception(msg, *args, **kwargs):
    """
    emits a log with error level and exception information.

    :param str msg: log message.
    """

    return get_component(LoggingPackage.COMPONENT_NAME).exception(msg, *args, **kwargs)


def critical(msg, *args, **kwargs):
    """
    emits a log with critical level.

    :param str msg: log message.
    """

    return get_component(LoggingPackage.COMPONENT_NAME).critical(msg, *args, **kwargs)
