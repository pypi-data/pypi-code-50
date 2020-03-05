from setuptools import setup
import os

__version__ = "0.3"
_here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(_here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='easytimer',
    py_modules=["easytimer"],
    version=__version__,
    description=('A module for easily timing sections of code.'),
    long_description_content_type='text/markdown',
    long_description=long_description,
    author='Adam Rose',
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3'],
)
