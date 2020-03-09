__version__ = "6.0.19"

import logging

logging.basicConfig()
logger = logging.getLogger("zuper-commons")
logger.setLevel(logging.DEBUG)

logger.info(f"zuper-commons {__version__}")
