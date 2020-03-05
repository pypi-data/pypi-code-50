import setuptools
from setuptools import setup

setup(
    name='congruous',
    version='0.1.0',
    author='Mahesh Kumaran T',
    author_email='maheshtkumaran@gmail.com',
    description='A python command-line tool to compare and generate accuracy reports for OCR data',
    packages=setuptools.find_packages(),
    py_modules=['congruous'],
    install_requires=[
        'Click', 'matplotlib', 'fuzzywuzzy[speedup]'
    ],
    entry_points='''
        [console_scripts]
        congruous=congruous:cli
    ''',
)