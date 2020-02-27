#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from setuptools import setup
import re
import os
import sys
import codecs

name = 'django-log-labeler'
package = 'log_labeler'
description = 'Django middleware and log filter to attach a unique ID to every log message generated as part of a request'
url = 'https://psbl102zatcrh.vodacom.corp/nimble-backend/Vodacom-Django-Log-Labeler/'
author = 'Hermann'
author_email = 'hermann.ntsamo@vcontractor.co.za'
license = 'BSD'
install_requires = ["django>=1.9.2", "django-structlog==1.3.5", "requests==2.22.0", "twine==3.1.1"]

with codecs.open('README.md', encoding='utf-8') as f:
    readme = f.read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    args = {'version': get_version(package)}
    print("You probably want to also tag the version now:")
    print("  git tag -a %(version)s -m 'version %(version)s'" % args)
    print("  git push --tags")
    sys.exit()


setup(
    name=name,
    version='0.0.15',
    url=url,
    license=license,
    description=description,
    long_description=readme,
    long_description_content_type='text/markdown',
    author=author,
    author_email=author_email,
    packages=get_packages(package),
    package_data=get_package_data(package),
    install_requires=install_requires
)
