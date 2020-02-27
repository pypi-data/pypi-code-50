#!/usr/bin/env python
import ast
import codecs
import os.path
import re
import sys
from codecs import open

from setuptools import find_packages, setup

ROOT = os.path.realpath(os.path.dirname(__file__))
init = os.path.join(ROOT, 'src', 'etools_offline', '__init__.py')
_version_re = re.compile(r'__version__\s+=\s+(.*)')
_name_re = re.compile(r'NAME\s+=\s+(.*)')

sys.path.insert(0, os.path.join(ROOT, 'src'))

with open(init, 'rb') as f:
    content = f.read().decode('utf-8')
    VERSION = str(ast.literal_eval(_version_re.search(content).group(1)))
    NAME = str(ast.literal_eval(_name_re.search(content).group(1)))


setup(
    name=NAME,
    version=VERSION,
    url='https://github.com/unicef/etools-offline-collect',
    author='UNICEF',
    author_email='dev@unicef.org',
    license="UNICEF",
    description='eTools Offline Collect application',
    long_description=codecs.open("README.rst").read(),
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    include_package_data=True,
    install_requires=[
        'djangorestframework',
        'django',
        'requests',
        'unicef_attachments',
    ],
    extras_require={
        'test': [
            'django-celery',
            'coverage',
            'factory-boy',
            'faker',
            'flake8',
            'isort',
            'pytest',
            'pytest-cov',
            'pytest-django',
            'pytest-echo',
            'pytest-pythonpath',
            'psycopg2-binary',
            'responses',
        ],
    },
    platforms=['linux'],
    classifiers=[
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers'
    ],
    scripts=[]
)
