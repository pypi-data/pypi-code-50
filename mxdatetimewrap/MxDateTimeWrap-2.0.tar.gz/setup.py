# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

setup(
    name='MxDateTimeWrap',
    version='2.0',
    description='Wrap mx.DateTime functions using native datetime',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Sindri (Trackwell hf.)',
    author_email='sindri@trackwell.com',
    url='http://www.trackwell.com/',
    packages=find_packages('.'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Utilities',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'six', 'holidays',
    ]
)
