# -*- coding: utf-8 -*-

import setuptools

with open("README.md", 'r') as fh:
  long_description = fh.read()

setuptools.setup(
    name='picdetect',
    version='0.1',
    author='Ning',
    author_email='admin@163.com',
    description='Picture Detect.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Zening-Li/picdetect',
    packages=setuptools.find_packages(),
    classifiers=('Programming Language :: Python :: 3',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent',
                 ),
)
