import sys
import logging
logger = logging.getLogger(__name__)


def handle_exception(e):
    """Function all modules share to handled exceptions.
    Currently error strings (e) are put into the log file as
    an exception.

    :param e: Error message.

    """

    logger.exception(f'Exception...{e}')
    sys.exit()
