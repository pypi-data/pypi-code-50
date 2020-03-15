# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['namanhelloworld']

package_data = \
{'': ['*'], 'namanhelloworld': ['mgorav_hellworld.egg-info/*']}

install_requires = \
['toml>=0.9.6,<0.10.0']

setup_kwargs = {
    'name': 'namanhelloworld',
    'version': '0.0.1',
    'description': 'Hello world Poetry',
    'long_description': None,
    'author': 'Gaurav Malhotra',
    'author_email': 'mgorav@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
