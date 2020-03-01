#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(*file_paths):
    """Retrieves the version from djmypypi/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


version = get_version("djmypypi", "__init__.py") # pylint: disable=invalid-name


if sys.argv[-1] == 'publish':
    try:
        import wheel
        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read() # pylint: disable=invalid-name
history = open('HISTORY.rst').read().replace('.. :changelog:', '') # pylint: disable=invalid-name

setup(
    name='dj-mypypi',
    version=version,
    description="""This package provides a private python package index based on django""",
    long_description=readme + '\n\n' + history,
    author='Karel Antonio Verdecia Ortiz',
    author_email='kverdecia@gmail.com',
    url='https://github.com/kverdecia/dj-mypypi',
    packages=[
        'djmypypi',
    ],
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    keywords='dj-mypypi',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
