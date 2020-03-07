#!/usr/bin/env python
# coding: utf-8

import setuptools

setuptools.setup(
    name='melaxtool',  # pip3 install
    version='0.0.1',  #
    author='lj',  #
    author_email='soda.lj@gmail.com',
    url='https://github.com/sodalvjian/melax_nlp_lib.git',
    description='this is simple tool for melaxtech nlp',
    packages=setuptools.find_packages(),
    install_requires=['requests']

)
