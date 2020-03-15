# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['demo_poetry']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.23.0,<3.0.0']

setup_kwargs = {
    'name': 'demo-poetry',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'gmalho',
    'author_email': 'gaurav.malhotra@nike.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
