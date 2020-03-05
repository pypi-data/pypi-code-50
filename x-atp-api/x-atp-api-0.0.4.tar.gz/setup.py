#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='x-atp-api',
    version='0.0.4',
    keywords=['x', 'atp', 'api', 'test'],
    description='Interface test program for X automated test platform',
    long_description='X automated test platform',
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
    install_requires=['sweetest'],
    entry_points={
        'console_scripts': [
            'x-atp-api = atp.api:main'
        ]
    },
)
