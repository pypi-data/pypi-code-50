#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='santodigital-bigquery',
    version='1.0.1',
    license='Apache-2.0',
    description='Santo Digital Custom packages to work with BigQuery Python SDK',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.MD')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='Lucas Magalhães',
    author_email='lucas.magalhaes@santodigital.com.br',
    # url='https://gitlab.com/lucasmagalhaes/',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    setup_requires=[
        'cython>=0.x',
    ],
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
    ],
    # project_urls={
    #     'Changelog': 'https://gitlab.com/lucasmagalhaes/paralelocs_beam/blob/master/CHANGELOG.rst',
    #     'Issue Tracker': 'https://gitlab.com/lucasmagalhaes/paralelocs_beam/issues',
    # },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
        'bigquery'
    ],
    python_requires='>=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    install_requires=[
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
        'google-cloud-bigquery>=1.23.1'

    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    }
    # entry_points={
    #     'console_scripts': [
    #         'paralelocs-beam = paralelocs_beam.cli:main',
    #     ]
    # },
    )