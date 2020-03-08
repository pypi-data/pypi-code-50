#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='x-atp-cli',
    version='0.0.5',
    keywords=['x', 'atp', 'test', 'sweetest'],
    description='X 自动化测试平台 命令行客户端',
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
    ],
    url='https://github.com/hekaiyou/x-atp-cli',
    author="HeKaiYou",
    author_email="hekaiyou@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'x-atp-cli = atp.cli:main'
        ]
    },
)
