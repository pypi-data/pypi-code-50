import logging

_logger = None


def get_logger() -> logging.Logger:
    global _logger
    if not _logger:
        FORMAT = '%(levelname)-8s: %(message)s'
        logging.basicConfig(level=logging.INFO,
                            format=FORMAT)

        _logger = logging.getLogger(__name__)

    return _logger
