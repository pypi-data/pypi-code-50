from setuptools import setup

setup(name = 'write_composition',
version = '1.1',
data_files = [('Lib\\site-packages\\wc_data', ['data.json'])],
author='pythonnlgs',
py_modules = ['write_composition']
)