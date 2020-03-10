# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jsomark']

package_data = \
{'': ['*']}

install_requires = \
['lxml>=4.5.0,<5.0.0', 'pytest>=5.3.5,<6.0.0']

setup_kwargs = {
    'name': 'jsomark',
    'version': '0.2.0',
    'description': 'json <-> xml composing and parsing convention.',
    'long_description': None,
    'author': 'Knowark',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
