# -*- coding: utf-8 -*-
import setuptools
from setuptools import setup
import os
"""
thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = [] # Examples: ["gunicorn", "docutils>=0.3", "lxml==0.5a7"]
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()
"""
setup(
    name='psc_api_pub',
    version='0.0.19',
    description='psc api for public',
    license='LGPL',
    packages=setuptools.find_packages(),
    author='AlarmChang',
    author_email='AlarmChang@moldex3d.com',
    keywords=['easyredmine'],
    url='http://www.alarmchang.com',
    #install_requires = install_requires
)