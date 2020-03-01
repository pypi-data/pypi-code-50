#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages


RELEASE_VERSION='0.1.9'

setup(name = 'rubix_cube',
      packages = find_packages(),
      version = RELEASE_VERSION,
      license='MIT',
      description = 'Python Rubix Cube GUI package',
      author = 'David Grethlein',
      author_email = '12dgrethlein@gmail.com',
      url = 'https://github.com/dgrethlein/RubixCube' ,
      download_url = f'https://github.com/dgrethlein/RubixCube/archive/v{RELEASE_VERSION}.tar.gz',
      keywords = ['Python', 'GUI', 'Rubix' , 'A*'],
      install_requires = ['numpy' , 'pandas' , 'matplotlib'],
      classifiers = ['Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Games/Entertainment :: Arcade',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
      ],
)