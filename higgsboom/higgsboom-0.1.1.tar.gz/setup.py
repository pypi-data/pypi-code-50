# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
	name = 'higgsboom',
	version = '0.1.1',
	description = 'Higgs Asset Management Boom Strategy Platform API',
	author = 'Veidt',
	author_email = 'veidt1988@live.com',
	url = 'https://github.com/veidt1988/higgs-boom-master',
	python_requires = '>=3.5',
	packages = find_packages(),
	install_requires=['sqlalchemy', 'mysqlclient', 'numpy', 'pandas',],
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License',
		],
)
