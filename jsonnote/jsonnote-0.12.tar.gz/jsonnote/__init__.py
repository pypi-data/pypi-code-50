import logging

logger = logging.getLogger(__name__)
console = logging.StreamHandler()
logger.addHandler(console)

from jsonnote.src.jsonnote import jsonnote as jsonnote

__version__ = '0.12'
