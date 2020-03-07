# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aioimport']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'aioimport',
    'version': '0.1.0',
    'description': 'Asynchronous module import for asyncio',
    'long_description': '# aioimport\nAsynchronous module import for asyncio\n',
    'author': 'rndr',
    'author_email': 'rndr@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rndr/aioimport',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
