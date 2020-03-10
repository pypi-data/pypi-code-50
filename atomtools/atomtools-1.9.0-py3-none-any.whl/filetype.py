"""
analyze chemical input/output filetype
"""


import os
import re
import argparse
import configparser
import modlog
from . import fileutil


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_FILETYPE_REGEXP_CONF = 'default_filetype.conf'
DEFAULT_FILETYPE_REGEXP_CONF = os.path.join(
    BASE_DIR, DEFAULT_FILETYPE_REGEXP_CONF)
REG_ANYSTRING = r'[\s\S]*?'
FILETYPE_SECTION_NAME = 'filetype'
MULTIFRAME_NAME = 'multiframe'

logger = modlog.getLogger(__name__)

global FORMATS_REGEXP, MULTIFRAME
FORMATS_REGEXP, MULTIFRAME = dict(), list()

PARTIAL_LENGTH = 100000


def update_config(path=None):
    global FORMATS_REGEXP, MULTIFRAME
    path = path or DEFAULT_FILETYPE_REGEXP_CONF
    if os.path.exists(path):
        conf = configparser.ConfigParser(delimiters=('='))
        conf.optionxform = str
        conf.read(path)
        FORMATS_REGEXP.update(conf._sections[FILETYPE_SECTION_NAME])
        MULTIFRAME += conf._sections[MULTIFRAME_NAME][MULTIFRAME_NAME].split()


def filetype(fileobj=None):
    """
    >>> filetype("a.gjf")
    gaussian
    >>> filetype("1.gro")
    gromacs
    """
    filename = fileutil.get_absfilename(fileobj)
    if fileutil.is_compressed_file(filename):
        fileobj = fileutil.get_uncompressed_fileobj(filename)
        filename = fileutil.get_uncompressed_filename(filename)
    else:
        filename = fileutil.get_filename(fileobj)
    try:
        content = fileutil.get_file_content(fileobj, size=PARTIAL_LENGTH)
    except TypeError:
        content = None
    if filename is None and content is None:
        return None
    logger.debug("filename: %s, content: %s" % (filename, content))
    for fmt_regexp, fmt_filetype in FORMATS_REGEXP.items():
        name_regexp, content_regexp = (fmt_regexp.split('&&') + [None])[:2]
        logger.debug(f"{name_regexp}, {content_regexp}")
        if filename and re.match(re.compile(name_regexp.strip()), filename) or filename is None:
            if content and content_regexp:
                if not content_regexp.startswith('^'):
                    content_regexp = REG_ANYSTRING + content_regexp.strip()
                if not content_regexp.endswith('$'):
                    content_regexp = content_regexp.strip() + REG_ANYSTRING
                logger.debug("content_regexp: " + content_regexp)
                if re.match(re.compile(content_regexp.strip()), content):
                    return fmt_filetype
            else:
                return fmt_filetype
    logger.warning(f"filename: {filename} parse fail")
    return None


def list_supported_formats():
    return list(FORMATS_REGEXP.values())


def support_multiframe(ftype):
    if ftype in MULTIFRAME:
        return True
    return False


update_config()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str)
    args = parser.parse_args()
    logger = modlog.getLogger("Atomtools: Filetype", 'normal', 'FILETYPE_LOGLEVEL')
    print(filetype(args.filename))
