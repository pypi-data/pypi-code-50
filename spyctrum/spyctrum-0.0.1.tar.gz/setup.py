#!/usr/bin/env python3.6
# coding: utf-8
import os
import sys

from __init__ import VERSION

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist')
    os.system('twine upload dist/*')
    sys.exit()

setup(
    name="spyctrum",
    version=VERSION,
    description="Music spectrum analyser written in python",
    author="WORD559",
    author_email="josh.barrass.work@gmail.com",
    url="https://github.com/joshbarrass/spyctrum",
    scripts=[],
    packages=["spyctrum"],
    package_dir={
        "spyctrum": ".",
        },
    install_requires=["numpy", "scipy"],
    keywords="spectrum analyser music",
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        ],
    )
