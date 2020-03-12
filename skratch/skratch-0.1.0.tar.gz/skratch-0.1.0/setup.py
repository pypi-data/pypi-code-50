# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['skratch']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'skratch',
    'version': '0.1.0',
    'description': 'Machine learning algorithms implemented from scratch',
    'long_description': None,
    'author': 'Valentin Calomme',
    'author_email': 'info@valentincalomme.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
