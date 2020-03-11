# vim: set ft=python fileencoding=utf-8 tw=72 fdm=indent nowrap:
"""
    pynfact.struri
    ~~~~~~~~~~~~~~

    URI strings manipulation functions.

    :copyright: (c) 2012-2020, J. A. Corbal
    :license: MIT
"""
import unidecode
import re
import os


def slugify(unslugged, separator='-'):
    """Slugs a string.

    :param unslugged: String to slugify
    :type unslugged: str
    :param separator: Character used to separate words
    :type separator: str
    :return: Slugged string
    :rtype: str
    """
    return re.sub(r'\W+', separator,
                  unidecode.unidecode(unslugged).strip().lower())


def link_to(name, prefix='', makedirs=True, justdir=False, index='index.html'):
    """Makes a link relative path in terms of the build.

    :param name: Filename with slugified name (extension will be removed)
    :type name: str
    :param prefix: Prefix directory to preppend the file (valid dir. names)
    :type prefix: str
    :param makedirs: If true make all needed directories
    :type makedirs: bool
    :param justdir: If true return only the link dir
    :type justdir: bool
    :param index: Default name of file
    :type index: str
    :return: Link path to a 'index.html' page
    :rtype: str
    """
    dirname = os.path.splitext(name)[0]
    path = os.path.join(prefix, slugify(dirname), index)
    if makedirs:
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
    return os.path.dirname(path) if justdir else path


def strip_html_tags(text):
    """Strips HTML tags in string.

    :param text: String containing HTML code
    :type text: str
    :return: String without HTML tags
    :rtype:str
    """
    return re.sub('<[^<]+?>', '', text)

