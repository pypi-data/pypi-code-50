#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
    Nested object manipulations OPENTEA

"""

from glob import glob
from os.path import basename
#from os.path import dirname
#from os.path import join
from os.path import splitext
from setuptools import find_packages, setup

NAME = "OpenTEA"
VERSION = "3.2.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
setup(
    name=NAME,
    version=VERSION,
    description='Nested object manipulations',
    license="CeCILL-B",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    author_email="coop@cerfacs.fr",
    url="",
    entry_points={
        'console_scripts': [
            "opentea_test_schema = opentea.cli:test_schema",
            "gui_test_trivial = opentea.examples.trivial.startup:main",
            "gui_test_simple = opentea.examples.simple.startup:main",
            "gui_test_complex = opentea.examples.calculator.startup:main",
        ],
    },
    
    install_requires=[
        'numpy>=1.16.2',
        'h5py>=2.9.0',
        'jsonschema',
        'markdown',
        'Pillow>=5.4.1',
        'PyYAML>=3.13',
        'nob>=0.4.1',
        'click',
        'tiny_3d_engine'
    ],
)
