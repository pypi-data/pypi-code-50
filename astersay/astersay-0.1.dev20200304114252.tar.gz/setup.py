#
# Copyright (c) 2019, Grigoriy Kramarenko
# All rights reserved.
# This file is distributed under the same license as the current project.
#
from setuptools import setup

# Dynamically calculate the version based on astersay.VERSION.
version = __import__('astersay').get_version()

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='astersay',
    version=version,
    description=(
        'This is a Python library for Asterisk to work with Yandex and '
        'Google voice models.'
    ),
    long_description=long_description,
    author='Grigoriy Kramarenko',
    author_email='root@rosix.ru',
    url='https://gitlab.com/avantelecom/asterisk-dialogs/',
    license='BSD License',
    platforms='any',
    zip_safe=False,
    packages=['astersay'],
    include_package_data=True,
    install_requires=[
    ],
    classifiers=[
        # List of Classifiers: https://pypi.org/classifiers/
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: Russian',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Topic :: Communications :: Internet Phone',
        'Topic :: Communications :: Telephony',
    ],
)
