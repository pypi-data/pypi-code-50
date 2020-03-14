#!/usr/bin/env python
# # coding: utf-8

from setuptools import setup
from ddt2 import __version__

setup(
    name='ddt2',
    description='Data-Driven/Decorated Tests',
    long_description='A library to multiply test cases',
    version=__version__,
    author='Carles Barrobés, Juewuer',
    author_email='lihechao@gmail.com',
    url='https://github.com/juewuer/ddt2',
    py_modules=['ddt2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Testing',
    ],
)
