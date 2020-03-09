#!/usr/bin/env python
"""The setup script."""

from setuptools import setup, find_packages

# Package meta-data.
VERSION = __import__("obfuscator").__version__
NAME = 'django-db-obfuscator'
DESCRIPTION = 'Django app to obfuscate text data.'
URL = 'https://github.com/oesah/django-db-obfuscator'
EMAIL = 'os@oesah.ch'
AUTHOR = 'Oezer Sahin'

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'setuptools-git >= 1.2',
]

setup_requirements = [
    'pytest-runner',
]

test_requirements = [
    'pytest>=3',
]

setup(
    author=AUTHOR,
    author_email=EMAIL,
    python_requires='>=3.6',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.2',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description=DESCRIPTION,
    entry_points={
        'console_scripts': [
            'obfuscator=obfuscator.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='obfuscator',
    name=NAME,
    packages=find_packages(include=['obfuscator', 'obfuscator.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url=URL,
    version=VERSION,
    zip_safe=False,
)
