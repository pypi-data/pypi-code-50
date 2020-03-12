#!/usr/bin/env python
from setuptools import setup, find_packages
import os

cwd = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(cwd, 'requirements.txt')) as requirements_file:
    requirements = requirements_file.read().splitlines()

setup(
    name='schmecko',
    version='0.0.1',
    author='Ryan Fitzpatrick',
    author_email='rmfitzpatrick@gmail.com',
    url='http://github.com/rmfitzpatrick/schmecko',
    download_url='http://github.com/rmfitzpatrick/schmecko/tarball/master',
    description='Debugging http server',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    install_requires=requirements,
    entry_points=dict(
        console_scripts=[
            'schmecko = schmecko.echo_server:run',
        ]
    ),
)
