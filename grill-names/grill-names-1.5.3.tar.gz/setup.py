#!/usr/bin/env python
from setuptools import setup, find_namespace_packages

_VERSION = '1.5.3'
setup(
    name='grill-names',
    version=_VERSION,
    packages=find_namespace_packages(
        exclude=("*.tests", "*.tests.*", "tests.*", "tests", "*.docs", "*.docs.*", "docs.*", "docs")),
    package_data={
        'grill.tokens.ids': ['*.cfg'],
    },
    description='Name objects for digital content creation.',
    author='Christian López Barrón',
    author_email='chris.gfz@gmail.com',
    url='https://github.com/thegrill/grill-names',
    download_url=f'https://github.com/thegrill/grill-names/releases/tag/{_VERSION}',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    extras_require={'docs': ['sphinx_autodoc_typehints', 'sphinx_rtd_theme']},
    install_requires=['naming>=0.5'],
    namespace_packages=['grill']
)
