#!/usr/bin/env python

from setuptools import setup
import sys

with open("README.md") as f:
    long_description = f.read()

setup(
    name="torloc",
    version='1.0.0',
    description="A Python tool for running multiple Tor services on local ports",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrgyber/torloc",
    license="MIT",
    author="Nikita Kudryavtsev",
    author_email="mrgyber@mail.ru",
    keywords=["tor", "proxy"],
    python_requires='>=3.4',
    packages=['torloc'],
    package_data={'torloc': ['tor_linux.zip', 'tor_win32.zip', 'tor_darwin.zip']},
    data_files=[('', ['README.md', 'LICENSE'])],
    install_requires=['PySocks'],
    zip_safe=False,
)
