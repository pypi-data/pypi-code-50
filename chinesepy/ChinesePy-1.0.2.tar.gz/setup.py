from setuptools import setup

with open('README.md', encoding = 'UTF-8') as fh:
	long_description = fh.read()

setup(name = 'ChinesePy',
version = '1.0.2',
author = 'pythonnlgs',
long_description = long_description,
description = '中文函数，适合初学菜鸟……',
packages = ['ChinesePy'])