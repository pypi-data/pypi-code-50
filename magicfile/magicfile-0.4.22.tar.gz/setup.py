#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os

from setuptools import setup, find_packages


def read(file_name):
    """Read a text file and return the content as a string."""
    with io.open(os.path.join(os.path.dirname(__file__), file_name),
                 encoding='utf-8') as f:
        return f.read()

setup(
    name='magicfile',
    description='File type identification using libmagic',
    author='Adam Hupp',
    author_email='adam@hupp.org',
    url="http://github.com/messense/magicfile",
    version='0.4.22',
    packages=find_packages(exclude=('test', 'test.*')),
    include_package_data=True,
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    install_requires=["cffi>=1.0.0"],
    setup_requires=['cffi>=1.0.0'],
    cffi_modules=["magicfile/_libmagic_build.py:ffi"],
    keywords="mime magic file",
    license="MIT",
    test_suite='test',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
