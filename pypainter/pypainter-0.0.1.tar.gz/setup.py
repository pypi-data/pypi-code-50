from setuptools import setup


with open('README.md', encoding = 'UTF-8') as fh:
	long_description = fh.read()

setup(name = 'pypainter',
version = '0.0.1',
description = 'tkinter_painter',
author='pythonnlgs',
long_description = long_description,
long_description_content_type = 'text/markdown',
py_modules = ['painter']
)