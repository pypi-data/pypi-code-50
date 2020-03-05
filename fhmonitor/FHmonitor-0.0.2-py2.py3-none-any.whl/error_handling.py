import logging
logger = logging.getLogger(__name__)


def handle_exception(e):
    """Function all modules share to handled exceptions.
    Currently functions are put into the log file as
    an excption.

    :param e: Error message.

    """

    logger.exception(f'Exception...{e}')
