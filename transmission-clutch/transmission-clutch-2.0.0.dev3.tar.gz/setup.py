# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clutch',
 'clutch.method',
 'clutch.method.convert',
 'clutch.method.convert.argument',
 'clutch.method.convert.response',
 'clutch.method.typing',
 'clutch.method.typing.session',
 'clutch.method.typing.torrent',
 'clutch.network',
 'clutch.network.rpc']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.22.0,<3.0.0']

setup_kwargs = {
    'name': 'transmission-clutch',
    'version': '2.0.0.dev3',
    'description': 'An RPC client library for the Transmission bittorrent client',
    'long_description': None,
    'author': 'mhadam',
    'author_email': 'michael@hadam.us',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
