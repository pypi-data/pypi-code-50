# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['confgetti']

package_data = \
{'': ['*']}

install_requires = \
['python-consul>=1.1.0,<2.0.0', 'voluptuous>=0.11.7,<0.12.0']

setup_kwargs = {
    'name': 'confgetti',
    'version': '0.1.11',
    'description': 'Package for getting configuration variables from remote configuration server, json files and environment variables in a simple way',
    'long_description': None,
    'author': 'Styria Digital Development',
    'author_email': 'development@styria.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
