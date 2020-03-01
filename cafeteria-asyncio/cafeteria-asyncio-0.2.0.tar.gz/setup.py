# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cafeteria', 'cafeteria.asyncio', 'cafeteria.asyncio.patterns']

package_data = \
{'': ['*']}

install_requires = \
['cafeteria>=0,<1']

setup_kwargs = {
    'name': 'cafeteria-asyncio',
    'version': '0.2.0',
    'description': 'An extension to the cafeteria package to enable asyncio specific patterns for python 3.7 and above applications/libraries.',
    'long_description': '[![](https://github.com/abn/aiven-monitor-http/workflows/Test%20Suite/badge.svg)](https://github.com/abn/cafeteria-asyncio/actions?query=workflow%3A%22Test+Suite%22)\n[![image](https://img.shields.io/pypi/v/cafeteria-asyncio.svg)](https://pypi.org/project/cafeteria-asyncio/)\n[![image](https://img.shields.io/pypi/l/cafeteria-asyncio.svg)](https://pypi.org/project/cafeteria-asyncio/)\n[![image](https://img.shields.io/pypi/pyversions/cafeteria-asyncio.svg)](https://pypi.org/project/cafeteria-asyncio/)\n[![image](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n[![Dependabot Status](https://api.dependabot.com/badges/status?host=github&repo=abn/cafeteria-asyncio)](https://dependabot.com)\n\n# Asyncio Patterns and Utilities\nAn extension to the cafeteria package to enable asyncio specific patterns for python 3.7 and above applications/libraries.\n\n## Installation\n`pip install cafeteria-asyncio`\n',
    'author': 'Arun Babu Neelicattu',
    'author_email': 'arun.neelicattu@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/abn/cafeteria-asyncio',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
