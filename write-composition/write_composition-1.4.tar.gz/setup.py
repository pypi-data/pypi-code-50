from setuptools import setup

with open('README.md', encoding = 'UTF-8') as fh:
	long_description = fh.read()

setup(name = 'write_composition',
version = '1.4',
data_files = [('Lib\\site-packages\\wc_data', ['data.json'])],
author='pythonnlgs',
long_description = long_description,
long_description_content_type = 'text/markdown',
py_modules = ['write_composition']
)