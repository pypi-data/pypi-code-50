"""This root level directives are imported from submodules. They are made
available here as well to keep the number of imports to a minimum for most
applications.
"""
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
__version__ = '3.0.0'

from .base import SquirroClient
from .exceptions import *
from .item_uploader import ItemUploader
from .document_uploader import DocumentUploader
