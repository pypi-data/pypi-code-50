# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['herja', 'herja.logging', 'herja.settings']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.8.2,<5.0.0', 'requests>=2.23.0,<3.0.0']

setup_kwargs = {
    'name': 'herja',
    'version': '0.1.0',
    'description': 'A python repository for quality of life purposes.',
    'long_description': None,
    'author': 'IanWernecke',
    'author_email': 'IanWernecke@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
