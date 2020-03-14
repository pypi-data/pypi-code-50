#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

setup_requirements = ['setuptools']

test_requirements = ['wheel', 'flake8', 'coverage', 'twine', 'pytest',
                     'pytest-runner', 'Faker', 'ipython', 'import-linter']

setup(
    author="Jonathan López",
    author_email='jlopez@fipasoft.com.mx',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="A persistent data plugin to store kakeibox data in SQLite 3.",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='kakeibox_database_sqlite3',
    name='kakeibox-database-sqlite3',
    packages=find_packages(),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://gitlab.com/kakeibox/plugins/database/kakeibox-database'
        '-sqlite3',
    version='0.0.5',
    zip_safe=False,
)
