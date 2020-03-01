"""Top-level package for PyKeyMapper."""

__author__ = """Samuel Luen-English"""
__email__ = "sluenenglish@gmail.com"
__version__ = "0.1.3"

from logging import NullHandler

from .events import *
from .modifiers.custom_modifier import CustomModifier
from .modifiers.existing_modifier import ExistingModifier
from .utils import *
from .runner import run_mapper
from . import premade

logging.getLogger(__name__).addHandler(NullHandler())
