#!/usr/bin/env python

from __future__ import absolute_import
import sys

# from distutils.core import setup
from setuptools import setup, find_packages
from os import path
import io
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "EyesLibrary"))

exec(compile(open("EyesLibrary/version.py").read(), "EyesLibrary/version.py", "exec"))

with io.open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="robotframework-eyeslibrarysel3",
    version="v2.2",
    description="Visual verification testing library for Robot Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Chris Hunter",
    author_email="<hunter.james.chris@gmail.com>",
    download_url="https://github.com/chunter4/EyesLibrary/archive/v2.2.tar.gz",
    license="Apache License 2.0",
    keywords="robotframework testing testautomation eyes-selenium selenium appium visual-verification",
    platforms="any",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Framework :: Robot Framework :: Library",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Quality Assurance",
    ],
    install_requires=[
        "robotframework > 3.0, < 4",
        "eyes-selenium >= 3.16.2, < 4",
        "six > 1.0.0, < 2",
        "robotframework-seleniumlibrary",
        "robotframework-appiumlibrary",
    ],
    packages=find_packages(exclude=["tests", "docs"]),
)
