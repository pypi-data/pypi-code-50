# -*- coding: utf-8 -*-
import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())

setup(
    name="paczekfiller",
    version="0.1.1",
    url="https://github.com/kr1surb4n/paczekfiller",
    license='MIT',

    author="Kris Urbanski",
    author_email="kris@whereibend.space",

    description="Pączek filler - simple script for filling out single template files",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",

    packages=find_packages(exclude=('tests', 'docs', 'htmlcov',)),

    install_requires=['Click', 'Jinja2'],
    extras_require={
        'fzf':  ["fzf"],
    },
    scripts=['bin/paczek'],
    entry_points={'console_scripts': [
        'paczekfiller = paczekfiller.cli:main',
    ]},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
