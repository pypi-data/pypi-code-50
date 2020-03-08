# coding:utf-8
"""
description: 
author: jiangyx3915
date: 2020-03-08
"""
from setuptools import setup
import sys

if sys.version_info[0] < 3:
    with open('README.md') as f:
        long_description = f.read()
else:
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='oh-my-email',
    version='0.1.0',
    description='simple send email in python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Jiang Yi Xin',
    author_email='15221613915@163.com',
    url='https://github.com/jiangyx3915/oh-my-email',
    license='MPL-2.0',
    packages=['oh_my_email'],
    install_requires=[
        'requests~=2.22.0',
        'beautifulsoup4~=4.8.2',
        'lxml~=4.5.0',
    ],
    scripts=[],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
)
