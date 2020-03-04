import sys
import logging
from django.conf import settings
from log_labeler import LOG_LABEL_LOGGER_NAME

try:
    unicode
    _unicode = True
except NameError:
    _unicode = False

if hasattr(settings, LOG_LABEL_LOGGER_NAME):
    logger = logging.getLogger(getattr(settings, LOG_LABEL_LOGGER_NAME))
else:
    logger = logging.getLogger(__name__)

class StructlogRawMessageHandler(logging.StreamHandler):
    level = logging.DEBUG
    filters = []
    lock = None
    _name = "StructlogRawMessageHandler"

    def __init__(self, stream=None):
        """
        Initialize the handler.

        If stream is not specified, sys.stderr is used.
        """
        logging.StreamHandler.__init__(self)
        if stream is None:
            stream = sys.stderr
        self.stream = stream

    def emit(self, record):
        logger.log(self.level, record.msg, name=record.name)
