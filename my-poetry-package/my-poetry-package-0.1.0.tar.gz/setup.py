# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['my_poetry_package']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'my-poetry-package',
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
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
