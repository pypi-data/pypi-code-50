#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup(
    author="dem4ply",
    author_email='dem4ply@gmail.com',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="python client for use the open api of gobmx",
    entry_points={
        'console_scripts': [
            'chibi_gob_mx=chibi_gob_mx.cli:main',
        ],
    },
    install_requires=requirements,
    license="WTFPL",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='chibi_gob_mx',
    name='chibi_gob_mx',
    packages=find_packages(include=['chibi_gob_mx', 'chibi_gob_mx.*']),
    url='https://github.com/dem4ply/chibi_gob_mx',
    version='0.0.1',
    zip_safe=False,
)
