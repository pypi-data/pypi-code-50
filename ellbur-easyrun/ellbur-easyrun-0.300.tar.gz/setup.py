#!/usr/bin/python

from setuptools import setup

setup(
    name       = 'ellbur-easyrun',
    version    = '0.300',
    py_modules = ['ellbureasyrun'],
    install_requires = [
        'quickfiles',
        'quickstructures'
    ]
)

