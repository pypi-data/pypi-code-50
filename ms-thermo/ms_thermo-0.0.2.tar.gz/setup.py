#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
    AVBP API

"""

from glob import glob
from os.path import basename
#from os.path import dirname
#from os.path import join
from os.path import splitext
from setuptools import find_packages, setup

NAME = "ms_thermo"
VERSION = "0.0.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools


with open("README.md", "r") as fin:
    readme = fin.read()

setup(
    name=NAME,
    version=VERSION,
    description="MS THERMO API",
    author_email="coop@cerfacs.fr",
    url="",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords=["MS THERMO API"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=[
        "setuptools",
        "numpy",
        "scipy>=1.2",
        "h5py",
        "click",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "tadia_table = ms_thermo.cli:tadia_table_cli",
            "tadia_cantera = ms_thermo.cli:tadia_cantera_cli",
            "yk_from_phi = ms_thermo.cli:yk_from_phi_cli",
            "fresh_gas = ms_thermo.cli:fresh_gas_cli"
        ]
    },
)
