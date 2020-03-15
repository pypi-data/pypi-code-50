import shutil
import os

from distutils.command.sdist import sdist as sdist_orig
from distutils.errors import DistutilsExecError

from setuptools import setup  

import setuptools.command.build_py

setup(
    name='pynetcon',
    version='0.1.10',
    url='https://github.com/TensorCon/PyNetcon',
    license='MIT',
    author='David Anekstein',
    author_email='aneksteind@gmail.com',
    packages=['pynetcon'],
    install_requires=[
        'oct2py==4.0.6'
    ],
    package_data={'pynetcon':['../netcon/netcon.m', '../netcon/netcon_nondisj_cpp.cpp']},
)