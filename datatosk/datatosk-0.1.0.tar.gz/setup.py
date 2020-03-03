# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datatosk']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'datatosk',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Miłosz Bednarzak',
    'author_email': 'milosz.bednarzak@bethink.pl',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
