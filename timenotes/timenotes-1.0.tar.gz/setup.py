#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: Fan Peilin
# Mail: fanpeilin123@126.com
# Created Time:  2020-3-4 10:01:00
#############################################

from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="timenotes",
    version="1.0",
    description="easy-use tool for record running time",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",

    url="https://github.com/Hamlet-Fansion/timenotes",
    author="Fan Peilin",
    author_email="fanpeilin123@126.com",

    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
