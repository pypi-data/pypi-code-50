# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['orex']

package_data = \
{'': ['*']}

install_requires = \
['mxu>=0.0.5,<0.0.6']

setup_kwargs = {
    'name': 'orex',
    'version': '0.0.1',
    'description': 'An object-oriented approach to regular expressions.',
    'long_description': 'Orex: Object-Oriented Regular Expressions\n=========================================\n\nAn object-oriented approach to regular expressions.\n',
    'author': 'Maximilian Köhl',
    'author_email': 'mkoehl@cs.uni-saarland.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://dgit.cs.uni-saarland.de/koehlma/python-orex',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
