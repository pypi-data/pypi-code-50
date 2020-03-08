import logging

LOGGING_FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s"
DEFAULT_LOGGING_LEVEL = logging.WARN
LOGGING_LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warn': logging.WARN,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}


def propagate_logging_level_from_request(request):
    """
    Propagates the logging level through the application to enable log level override
    in a Cloud Function.

    Using the following request parameter on the URL will allow the request to have
    a different than standard logging level:

    http://127.0.0.1:5000/logtest?loglev=debug

    :param request: Takes the request object to extract the parameters
    :return: No Return Value
    """
    if 'loglev' not in request.values:
        return

    requested_level = request.values['loglev']
    try:
        _ll = LOGGING_LEVELS[requested_level]
        logging.getLogger().setLevel(_ll)
        logging.getLogger('werkzeug').setLevel(_ll)
        logging.info(f'Set Log Level to {requested_level} {_ll}')
    except KeyError:
        logging.warning(
            f'Requested log level {requested_level} is not available, try {",".join(LOGGING_LEVELS.keys())}')
    except Exception as e:
        logging.error("Failed to get logging level", e)
    return
