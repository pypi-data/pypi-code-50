#!/usr/bin/env python
from __future__ import absolute_import, division, print_function

from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object, map, zip)

__author__ = 'Carlo Ferrigno'

from setuptools import setup, find_packages
import  glob

#packs=find_packages()
#print ('packs',packs)

include_package_data=True

setup(name='optimalgrouping',
      scripts=["optimal_binning.py"],
      version="1.0.0",
      description='Performs optimal grouping of spectra using Kaastra & Bleeker (2016)',
      author='Carlo Ferrigno',
      author_email='carlo.ferrigno@unige.ch',
      packages=['optimalgrouping'],
      install_requires=["argparse",
                        "astropy",
                        "numpy"
                    ],
      url="https://gitlab.astro.unige.ch/ferrigno/optimalgrouping",
      python_requires='>=3.0',
      license='MIT'
      )



