#!usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: setup.py
"""
Foo setup script.

"""

from setuptools import setup, find_packages

PACKAGE_NAME = '{{: Package name :}}'
URL = '{{: Git repository URL :}}'
DESCRIPTION = '{{: Package description :}}'
__author__ = '{{: Author :}}'
__email__ = '{{: Email :}}'

with open('requirements.txt') as fobj:
    REQUIREMENTS = [l.strip() for l in fobj.readlines()]

setup(
    name=PACKAGE_NAME,
    url=URL,
    description=DESCRIPTION,
    author=__author__,
    author_email=__email__,
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    install_requires=REQUIREMENTS,
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
    ],
)
