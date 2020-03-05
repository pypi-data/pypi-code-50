#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='x-atp-api',
    version='0.0.1',
    keywords=['x', 'atp', 'api', 'test'],
    description='Interface test program for X automated test platform',
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
    ],
    url='https://github.com/hekaiyou/x-atp-api',
    author="HeKaiYou",
    author_email="hekaiyou@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=['sweetest']
)
