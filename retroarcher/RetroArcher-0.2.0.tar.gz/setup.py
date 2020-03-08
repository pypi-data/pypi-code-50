# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['retroarcher']

package_data = \
{'': ['*']}

install_requires = \
['typing-extensions>=3.7.4,<4.0.0']

entry_points = \
{'console_scripts': ['retroarcher = retroarcher.main:main']}

setup_kwargs = {
    'name': 'retroarcher',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'Tim Simpson',
    'author_email': 'timsimpson4@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
