# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_hello_world']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['poetry-hello-world = poetry_hello_world.main:main']}

setup_kwargs = {
    'name': 'poetry-hello-world',
    'version': '0.1.0',
    'description': 'Hello World',
    'long_description': None,
    'author': 'hideaki murotani',
    'author_email': 'munroyello@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
