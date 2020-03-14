import os
import re
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'jsondiff', '__init__.py')) as f:
    version = re.compile(r".*__version__ = '(.*?)'", re.S).match(f.read()).group(1)

setup(
    name='jsondiff2',
    packages=find_packages(exclude=['tests']),
    version=version,
    description='Diff JSON and JSON-like structures in Python',
    author='Javier Martinez',
    author_email='edoreld@gmail.com',
    url='https://github.com/edoreld/jsondiff',
    keywords=['json', 'diff', 'diffing', 'difference', 'patch', 'delta', 'dict', 'LCS'],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'jsondiff=jsondiff.cli:main_deprecated',
            'jdiff=jsondiff.cli:main'
        ]
    }
)
