#!/usr/bin/python

import sys
from os import path
from setuptools import setup

# Scripts
scripts = []

# Local hack
if len(sys.argv) == 2 and sys.argv[1] == '--list-scripts':
    print(' '.join(scripts))
    sys.exit(0)

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

name = 'sails'
version = '1.0'
release = '1.0.0'

setup(
    name=name,

    version=release,

    description='Spectral Analysis In Linear Systems',

    # this becomes the PyPI landing page
    long_description=long_description,
    long_description_content_type='text/x-rst',

    # Author details
    author='Andrew Quinn <andrew.quinn@psych.ox.ac.uk>, '
           'Mark Hymers <mark.hymers@ynic.york.ac.uk>',
    author_email='sails-devel@ynic.york.ac.uk',

    # Choose your license
    license='GPL-2+',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
      'Development Status :: 4 - Beta',

      # Indicate who your project is intended for
      'Intended Audience :: Science/Research',
      'Topic :: Scientific/Engineering :: Bio-Informatics',
      'Topic :: Scientific/Engineering :: Information Analysis',
      'Topic :: Scientific/Engineering :: Mathematics',

      # Pick your license as you wish (should match "license" above)
      'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',

      # Specify the Python versions you support here. In particular, ensure
      # that you indicate whether you support Python 2, Python 3 or both.
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
    ],

    keywords='multivariate autoregressive models spectral',

    packages=['sails', 'sails.tests'],

    install_requires=['numpy',
                      'scipy',
                      'matplotlib',
                      'h5py',
                      'sphinx_rtd_theme'],

    extras_require={
        'test': ['coverage'],
    },

    command_options={
            'build_sphinx': {
                'project': ('setup.py', name),
                'version': ('setup.py', name),
                'release': ('setup.py', name)}},

    package_data={'sails': ['support/*.csv']},
)
