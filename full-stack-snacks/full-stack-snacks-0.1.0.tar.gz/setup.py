# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['full_stack_snacks']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'full-stack-snacks',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'JB',
    'author_email': 'jb.tellez@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
