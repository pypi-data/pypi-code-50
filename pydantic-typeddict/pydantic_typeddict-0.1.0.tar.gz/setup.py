# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['pydantic_typeddict']
install_requires = \
['pydantic>=1.4,<2.0']

setup_kwargs = {
    'name': 'pydantic-typeddict',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'asduj',
    'author_email': 'asduj@ya.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
