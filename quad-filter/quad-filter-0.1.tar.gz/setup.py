#!/usr/bin/env python

from distutils.core import setup

setup(name='quad-filter',
      version='0.1',
      description='Filtering tools for quad trees',
      author='JB Robertson',
      author_email='jbr@freeshell.org',
      url='https://www.gitlab.com/jbrobertson/quad-filter/',
      packages=['quad_filter'],
      python_requires='>=3.6',
      classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ])
