#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='xtalpi-pandas',
    version='0.0.2',
    author='Wenzhi Ma',
    author_email='wenzhi.ma@xtalpi.com',
    description=u'XtalPi Pandas CMD',
    packages=['xpandas'],
    install_requires=['click', 'pandas'],
    entry_points={
        'console_scripts': ['xpandas=xpandas:run']
    }
)
