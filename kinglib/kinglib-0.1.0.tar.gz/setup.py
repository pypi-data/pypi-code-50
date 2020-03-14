#!/usr/bin/python
# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

setup(
    name='kinglib',
    version='0.1.0',
    keywords=('setup', 'kinglib'),
    description='setup kinglib',
    long_description='', # open('README.md').read()
    license='MIT',
    install_requires=[
        'openpyxl>=3.0.3',
        'xlrd>=1.2.0',
        'xlwt>=1.3.0'
    ],
    author='Guozhi Hu',
    author_email='guozhi.hu@qq.com',
    packages=find_packages(),
    platforms='any',
    url='',
    include_package_data = True,
    entry_points={
        'console_scripts':[
            'kinglib=kinglib.run:main' 
        ]
    },
    zip_safe=False
)