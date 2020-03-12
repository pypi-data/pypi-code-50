# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['didtoday']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['didtoday = didtoday.main:main']}

setup_kwargs = {
    'name': 'didtoday',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'David Riff',
    'author_email': 'davidriff@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
