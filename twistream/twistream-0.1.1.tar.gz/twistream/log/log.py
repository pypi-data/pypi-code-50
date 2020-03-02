import logging
import os

# get root logger
ROOT_LOG = logging.getLogger('twistream')
ROOT_LOG.setLevel(logging.INFO)

# Console logger
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
ROOT_LOG.addHandler(stream_handler)

LOG_LEVELS = {
    'ERROR': logging.ERROR,
    'WARN': logging.WARN,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG
}


def get_logger():
    return ROOT_LOG


def set_level(level):
    ROOT_LOG.setLevel(level)
    for h in ROOT_LOG.handlers:
        h.setLevel(level)


def init_logger_file(log_file, log_level='INFO', create_file=True):
    """ Append a FileHandler to the root logger.
    :param str log_file: Path to the log file
    :param str log_level: Logging level
    :param bool create_file: Create login file if not present
    """
    log_base_path = os.path.dirname(log_file)
    if not os.path.exists(log_base_path):
        os.mkdir(log_base_path)

    log_level = LOG_LEVELS[log_level] if log_level in LOG_LEVELS.keys() else logging.INFO

    ROOT_LOG.setLevel(log_level)

    file_handle = logging.FileHandler(log_file)
    file_handle.setLevel(log_level)
    file_handle.setFormatter(formatter)
    ROOT_LOG.addHandler(file_handle)


init_logger_file(os.path.join(os.environ['HOME'], '.twistream', 'twistream.log'))
