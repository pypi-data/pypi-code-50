# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['resp3']
setup_kwargs = {
    'name': 'resp3',
    'version': '0.1.0',
    'description': 'A python implementation of RESP3.',
    'long_description': None,
    'author': 'laixintao',
    'author_email': 'laixintaoo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
