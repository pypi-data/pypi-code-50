#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Mon 16 Apr 08:18:08 2012 CEST

from setuptools import setup, find_packages, dist
dist.Distribution(dict(setup_requires = ['bob.extension']))

from bob.extension.utils import load_requirements
install_requires = load_requirements()

version = open("version.txt").read().rstrip()

# The only thing we do in this file is to call the setup() function with all
# parameters that define our package.
setup(

    # This is the basic information about your project. Modify all this
    # information before releasing code publicly.
    name = 'bob.db.batl',
    version=version,
    description = 'Implements a low-level database interface for the BATL database, which is designed for spoofing or presentation attack detection experiments in face biometrics.',
    url = 'https://gitlab.idiap.ch/bob/bob.db.batl',
    license = 'GPLv3',
    author = 'Salim Kayal',
    author_email = 'salim.kayal@idiap.ch',
    keywords = 'bob',
    long_description = open('README.rst').read(),

    # This line is required for any distutils based packaging.
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    install_requires = install_requires,

    entry_points = {
      # bob database declaration
      'bob.db': [
        'batl = bob.db.batl.driver:Interface',
      ],
    },

    # Classifiers are important if you plan to distribute this package through
    # PyPI. You can find the complete list of classifiers that are valid and
    # useful here (http://pypi.python.org/pypi?%3Aaction=list_classifiers).
    classifiers = [
      'Framework :: Bob',
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)
