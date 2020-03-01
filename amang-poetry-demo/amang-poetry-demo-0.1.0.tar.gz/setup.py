# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['amang_poetry_demo']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'amang-poetry-demo',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'aikmeng',
    'author_email': 'aikmeng80@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
