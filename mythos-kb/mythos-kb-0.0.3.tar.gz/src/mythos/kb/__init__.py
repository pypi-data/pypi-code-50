import logging

from .__version__ import __title__, __version__, __description__  # noqa
from .__version__ import __author__, __license__  # noqa
from .__version__ import __copyright__, __url__  # noqa


# Default logging handler to avoid "No handler found" warnings.
logging.getLogger(__title__).addHandler(logging.NullHandler())
