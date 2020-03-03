# -*- coding: utf-8 -*-


from setuptools import setup, find_packages
from openstreemap import __version__

VERSION = __version__

setup(
    name='openstreetmap',
    version=VERSION,
    description='OpenStreetMap coordinates',
    long_description=open('README.rst').read(),
    license='',
    author='galen',
    author_email='mywayking@icloud.com',
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    url='https://github.com/Mywayking/openstreetmap.git',
    keywords='openstreetmap',
    packages=find_packages(),
    install_requires=[
        'lxml',
        'requests',
    ],
)
