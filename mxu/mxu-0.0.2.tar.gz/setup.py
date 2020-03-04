# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mxu']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'mxu',
    'version': '0.0.2',
    'description': 'A collection of utilities and helpers for writing Python programs.',
    'long_description': 'MX Python Utilities\n===================\n\nA collection of utilities and helpers for writing Python programs.\n',
    'author': 'Maximilian Köhl',
    'author_email': 'mkoehl@cs.uni-saarland.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/koehlma/mx-python-utils',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
