# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chatbase_track', 'chatbase_track.backend', 'chatbase_track.types']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.4,<2.0']

extras_require = \
{'aiogram': ['aiogram>=2.6.1,<3.0.0'],
 'aiohttp': ['aiohttp>=3.6.2,<4.0.0'],
 'httpx': ['httpx>=0.11.1,<0.12.0'],
 'requests': ['requests>=2.22.0,<3.0.0']}

setup_kwargs = {
    'name': 'chatbase-track',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Alex Root Junior',
    'author_email': 'jroot.junior@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
