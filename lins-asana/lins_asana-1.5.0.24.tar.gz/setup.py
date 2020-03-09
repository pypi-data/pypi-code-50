#!/usr/bin/env python

import os
import sys
from distutils.core import setup
from setuptools import find_packages


def get_version():
    return open('version.txt', 'r').read().strip()


setup(
    author='Guilherme Severo',
    author_email='guilherme@lojaspompeia.com.br',
    description='Classe para uso da API Asana.',
    license='MIT',
    name='lins_asana',
    packages=find_packages(),
    url='https://bitbucket.org/grupolinsferrao/pypck-lins_asana/',
    version=get_version()
)
