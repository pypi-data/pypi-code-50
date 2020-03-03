#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import, print_function

import io
import re
from glob import glob
from os.path import basename, dirname, join, splitext

from setuptools import find_packages, setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='py3helpers',
    version='0.4.0',
    license='BSD-3-Clause',
    description='Python utility functions.',
    long_description_content_type="text/x-rst",
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='Andrew Dewey Bailey IV',
    author_email='bailey.andrew4@gmail.com',
    url='https://github.com/adbailey4/py3helpers',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities',
    ],
    project_urls={
        'Documentation': 'https://py3helpers.readthedocs.io/',
        'Changelog': 'https://py3helpers.readthedocs.io/en/latest/changelog.html',
        'Issue Tracker': 'https://github.com/adbailey4/py3helpers/issues',
    },
    keywords=['utility', 'python3', 'functions'],
    python_requires='>=3.5',
    install_requires=[
        'numpy>=1.14.2',
        'pandas>=0.23.4',
        'scikit-learn>=0.19.0',
        'matplotlib>=2.0.2',
        'boto3>=1.9',
        'moto>=1.3.14'],
    scripts=["src/py3helpers/scripts/merge_methyl_bed_files.py"],
    extras_require={'seq_tools': ['Cython>=0.29.12', 'pysam>=0.15', 'biopython>=1.73',
                                  'mappy==2.17; python_version>="3.6"',
                                  'mappy==2.16; python_version<="3.6"']},
    entry_points={
        'console_scripts': [
            'py3helpers = py3helpers.cli:main',
        ]
    },
)
