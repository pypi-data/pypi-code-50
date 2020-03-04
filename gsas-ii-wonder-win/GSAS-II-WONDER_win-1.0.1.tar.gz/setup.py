#!/usr/bin/env python3

import io
import os, sys

from setuptools import setup, find_packages

with io.open('about.md', 'r', encoding='utf-8') as f:
    ABOUT = f.read()

MAJOR = 1
MINOR = 0
MICRO = 1
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

AUTHOR = 'Luca Rebuffi, Paolo Scardi, Alberto Flor'
AUTHOR_EMAIL = 'paolo.scardi@unitn.ut'

URL = 'https://github.com/WONDER-project/GSAS-II-WONDER'
DESCRIPTION = 'GSAS-II plugin for WONDER'
LONG_DESCRIPTION = ABOUT
LICENSE = 'GPL3+'

CLASSIFIERS = [
    'Development Status :: 1 - Planning',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Programming Language :: Python :: 3 :: Only'
]

KEYWORDS = [
    'gsas 2',
    'gsas-ii'
]

PACKAGES = find_packages()

PACKAGE_DATA = {
    'GSAS-II-WONDER'        : ['*.dat', 'bin/*.*', 'bindist/*.*'],
}

INSTALL_REQUIRES = sorted(set(
    line.partition('#')[0].strip()
    for line in open(os.path.join(os.path.dirname(__file__), 'requirements.txt'))) - {''})

ENTRY_POINTS = {
    }

from distutils.core import setup

if __name__ == '__main__':

    platform = sys.platform

    if len(sys.argv) >= 3:
        value = sys.argv[2]

        if value == "darwin" or  value.startswith("win") or value.startswith("linux"):
            platform = value
            sys.argv = sys.argv[0:2]

    if platform == "darwin":
        NAME = 'GSAS-II-WONDER_osx'
    elif platform.startswith("win"):
        NAME = 'GSAS-II-WONDER_win'
    elif platform.startswith("linux"):
        NAME = 'GSAS-II-WONDER_linux'

    setup(
        name=NAME,
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        url=URL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license=LICENSE,
        packages=PACKAGES,
        package_data=PACKAGE_DATA,
        keywords=KEYWORDS,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
        namespace_packages=['GSAS-II-WONDER'],
        #namespace_packages=NAMESPACE_PACAKGES,
        #entry_points=ENTRY_POINTS
    )
