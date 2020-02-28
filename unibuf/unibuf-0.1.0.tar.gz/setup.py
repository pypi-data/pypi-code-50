# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['unibuf']

package_data = \
{'': ['*']}

install_requires = \
['hypothesis>=5.5.4,<6.0.0', 'pytest>=5.3.5,<6.0.0']

setup_kwargs = {
    'name': 'unibuf',
    'version': '0.1.0',
    'description': 'An implementation of the buffer protocol for unicode strings.',
    'long_description': 'Python Unicode Buffer\n=====================\n',
    'author': 'Maximilian Köhl',
    'author_email': 'mkoehl@cs.uni-saarland.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://dgit.cs.uni-saarland.de/koehlma/python-unicode-buffer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
