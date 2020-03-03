#!/usr/bin/env python

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='quad-filter',
    version='0.2',
    description='Filtering tools for quad trees',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='JB Robertson',
    author_email='jbr@freeshell.org',
    url='https://www.gitlab.com/jbrobertson/quad-filter/',
    packages=['quad_filter'],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ])
