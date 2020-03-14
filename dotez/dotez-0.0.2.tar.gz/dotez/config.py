import os
import logging
import sys

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_LOCS = [os.path.join('~', '.config', 'dotez.conf'),
               os.path.join('~', '.dotez.conf'),
               os.path.join(PACKAGE_DIR, 'example.conf')]

DEFAULT_CONFIG = {
    'includes': [
        '.bashrc',
        '.profile',
    ],
    'ignores': ['*.tmp'],
    'dotez_data_dir': '~/dotez/',
}

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger('dotez')
