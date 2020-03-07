# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['renet']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'renet',
    'version': '0.113',
    'description': 'Renet, reliable udp',
    'long_description': 'Reliable UDP network for games in pure Python. A light-weight manager of connections for sending and recving data over UDP sockets. \n\nIt works but still very much a WIP.\n\n# Installation\n\n`pip install renet`',
    'author': 'Solid Smoke Software',
    'author_email': 'solid.smoke.software@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/solidsmokesoftware/renet.py',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6.9,<4.0.0',
}


setup(**setup_kwargs)
