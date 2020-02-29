#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module sets up the package for the lib_work_login"""

from setuptools import find_packages, setup

__author__ = "Justin Furuness"
__credits__ = ["Justin Furuness"]
__Lisence__ = "MIT"
__maintainer__ = "Justin Furuness"
__email__ = "jfuruness@gmail.com"
__status__ = "Development"

setup(
    name="lib_work_login",
    version="0.1.0",
    url="https://github.com/jfuruness/lib_work_login.git",
    download_url='https://github.com/jfuruness/lib_work_login.git',
    keywords=['Furuness', 'Login', 'login', 'terminal'],
    license="BSD",
    description="Logs you into work",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pynput'
    ],
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3'],
    entry_points={
        'console_scripts': [
            'login = lib_work_login.__main__:main',
            'configure = lib_work_login.__main__:configure',
        ]},
)
