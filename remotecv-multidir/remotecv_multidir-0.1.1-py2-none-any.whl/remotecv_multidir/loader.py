# coding: utf-8

from remotecv.utils import config

import urllib2
import re
import os
import json
from os.path import join, exists, abspath
from six.moves.urllib.parse import unquote

import logging

logger = logging.getLogger('remotecv_multidir.loader')
loglevel = getattr(logging, config.log_level.upper())
if not isinstance(loglevel, int):
    raise ValueError('Invalid config.log_level: %s' % config.log_level)
logger.setLevel(loglevel)


# The list of paths where the File Loader will try to find images
REMOTECV_MULTIDIR_LOADER_DIRS = json.loads(os.environ.get('REMOTECV_MULTIDIR_LOADER_DIRS', '[]'))


def load_sync(path):
    """
    Loads image from a list of directories
    :param string path: Path to load
    """
    for idx, next_dir in enumerate(REMOTECV_MULTIDIR_LOADER_DIRS):

        file_path = join(next_dir.rstrip('/'), path.lstrip('/'))
        file_path = abspath(file_path)

        inside_root_path = file_path.startswith(abspath(next_dir))

        if inside_root_path:
            
            # keep backwards compatibility, try the actual path first
            # if not found, unquote it and try again
            found = exists(file_path)
            if not found:
                file_path = unquote(file_path)
                found = exists(file_path)

            if found:
                with open(file_path, 'rb') as f:
                    image = f.read()

                    logger.debug('Read file {0}'.format(file_path))
                    return image

        logger.debug('File {0} not found in {1}'.format(path, next_dir))
        # else loop and try next directory
    
    if not REMOTECV_MULTIDIR_LOADER_DIRS:
        logger.error('No paths set in environment var REMOTECV_MULTIDIR_LOADER_DIRS')

    # no file found
    raise Exception("No image found for %s" % path)
