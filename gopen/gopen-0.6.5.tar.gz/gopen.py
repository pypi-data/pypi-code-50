# -*- coding: utf-8 -*-
"""gopen, gread function."""
import logging
from contextlib import contextmanager

import pkg_resources

project_name = 'gopen'
__version__ = pkg_resources.require(project_name)[0].version
__copyright__ = 'Copyright (C) 2019 Simone Marsili'
__license__ = 'BSD 3 clause'
__author__ = 'Simone Marsili (simo.marsili@gmail.com)'
__all__ = ['readable', 'gread']

logger = logging.getLogger(__name__)


@contextmanager
def readable(source, encoding=None):  # pylint: disable=too-many-branches
    """Context manager for readable files.

    Usage:
    >>> import gopen
    >>> with gopen.readable(`source`) as f:
    >>>     <do something with f>
    `source` can be: a file-like object, a valid filename, a file descriptor.
    If `source` is a file-like object, do not close it.
    """
    import six
    import codecs
    import locale

    if encoding is None:
        encoding = locale.getpreferredencoding(False)

    if hasattr(source, 'read'):
        yield source  # yield the handle without closing it
    else:  # set handle or raise an exception
        if isinstance(source, int):  # file descriptor
            try:
                # do not close the file descriptos
                handle = open(source, 'r', encoding=encoding, closefd=False)
            except OSError:
                raise OSError('Cant open file file descriptor %s' % source)
        elif isinstance(source, six.string_types):  # a filename
            try:
                mimetype = _mimetype(source)
            except IOError:
                raise IOError('File: %s not found' % source)
            else:
                try:
                    mimetype = mimetype.split('/')[1]
                except AttributeError:
                    logger.warning(mimetype)
                    raise
                if mimetype in ['gzip', 'x-bzip2']:
                    # compressed
                    if mimetype == 'gzip':
                        import gzip
                        handle = codecs.getreader(encoding)(gzip.open(
                            source, 'r'))
                    elif mimetype == 'x-bzip2':
                        from bz2 import BZ2File
                        handle = codecs.getreader(encoding)(BZ2File(
                            source, 'r'))
                else:
                    handle = open(source, 'r', encoding=encoding)
                    # raise TypeError('Invalid filetype (%s)' % mimetype)
        else:
            raise TypeError('Expected {str, int, file-like}, '
                            'got %s' % type(source))
        yield handle
        handle.close()


def gread(source, encoding=None):
    """Return a generator of lines from source."""
    with readable(source, encoding=encoding) as f:
        for line in f:
            yield line


def _mimetype(source, encoding=False, uncompress=False):
    """Return the mime type of source.

    Parameters
    ----------
    encoding : bool (False)
        If True, codec is returned

    """
    import magic  # pylint: disable=import-error
    mime = magic.Magic(mime=True, mime_encoding=True, uncompress=uncompress)
    result = mime.from_file(source)
    mtype = result.split(';')[0]
    codec = result.split('=')[1]
    if encoding:
        return mtype, codec
    return mtype
