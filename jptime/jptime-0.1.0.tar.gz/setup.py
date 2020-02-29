# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['jptime']
install_requires = \
['japanese-numbers-python>=0.2.0,<0.3.0', 'python-dateutil>=2.8.1,<3.0.0']

setup_kwargs = {
    'name': 'jptime',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'kitagawa-hr',
    'author_email': 'kitagawa@cancerscan.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
