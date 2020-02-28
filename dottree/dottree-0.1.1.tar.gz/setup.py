# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dottree']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dottree',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Jitender',
    'author_email': 'gitbackspacer@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=2.7,<3.0',
}


setup(**setup_kwargs)
