#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup, find_packages
import sys
 
setup(
    name="cmutils",
    version="0.1.2",
    author="Chen, Xiong",
    author_email="bearfly1990@163.com",
    description="common utils like read/write file, log",
    long_description=open("README.rst").read(),
    license="MIT",
    url="https://github.com/bearfly1990/PowerScript/tree/master/Python3/mylib/cmutils",
    packages=['cmutils'],
    install_requires=[
        "openpyxl>=3.0.3",
        "colorlog",
        ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
