# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['cfg-cli']
install_requires = \
['better-exceptions>=0.2.2,<0.3.0',
 'boto3>=1.12.17,<2.0.0',
 'fire>=0.2.1,<0.3.0',
 'pandas==1.0.1',
 'requests>=2.23.0,<3.0.0']

setup_kwargs = {
    'name': 'cfg-cli',
    'version': '0.1.0',
    'description': "Command-line tool for Cofactor Genomics' products and services.",
    'long_description': None,
    'author': 'Alex Bode',
    'author_email': 'alex_bode@cofactorgenomics.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
