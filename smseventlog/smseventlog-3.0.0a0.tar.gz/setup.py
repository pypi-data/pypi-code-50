import sys
import os

from setuptools import find_packages, setup, Command

# TODO: just manually cleanup the files without janitor
try:
   from setupext_janitor import janitor
   CleanCommand = janitor.CleanCommand
except ImportError:
   CleanCommand = None

cmd_classes = {}
if CleanCommand is not None:
   cmd_classes['clean'] = CleanCommand

VERSION = '3.0.0a0'

# Names of required packages
requires = [
    'bs4 >= 0.0.1',
    'pandas >= 1.0.1',
    'pyodbc == 4.0.28',
    'pypika >= 0.35.21',
    'pyqt5 >= 5.14.1',
    'pyyaml >= 5.3',
    'sqlalchemy >= 1.3.13',
    'xlrd >= 1.2.0',
    'xlwings >= 0.18.0']

setup(
    name='smseventlog', 
    version=VERSION,
    packages=find_packages(),
    install_requires=requires,
    package_data={'smseventlog': ['data/images/*', 'data/config.yaml', 'data/db_secret.txt']}, 
    author='Jayme Gordon',
    author_email='',
    description='SMS Event Log',
    long_description='',
    long_description_content_type='text/markdown',
    url='https://github.com/jaymegordo/SMSEventLog',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    cmdclass=cmd_classes
)
