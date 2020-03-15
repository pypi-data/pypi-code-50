#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from setuptools import find_packages, setup

NAME = 'scriptgen'
VERSION = '0.0.2'
DESCRIPTION = 'A collection of script generation helpers and templates.'
HOME = Path(__file__).parent
README = (HOME / 'README.md').read_text()
CHANGELOG = (HOME / 'CHANGELOG.md').read_text()
AUTHOR = 'Elmer Nocon, fopoon'
AUTHOR_EMAIL = 'elmernocon@gmail.com'
LICENSE = 'MIT'
PLATFORMS = 'Any'
URL = 'https://github.com/Fopoon/scriptgen'
DOWNLOAD_URL = 'https://pypi.org/project/scriptgen/'
CLASSIFIERS = [
    'Development Status :: 1 - Planning',
    'License :: OSI Approved :: MIT License',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'Operating System :: Unix',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3 :: Only',
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description='\n\n'.join([README, CHANGELOG]),
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    platforms=PLATFORMS,
    url=URL,
    download_url=DOWNLOAD_URL,
    classifiers=CLASSIFIERS,

    packages=find_packages(
        exclude=[
            "tests",
            "tests.*",
            "*.tests.*",
            "*.tests"
        ]
    ),
)

