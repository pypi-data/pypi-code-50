# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['colossal', 'colossal.examples', 'colossal.macros']

package_data = \
{'': ['*']}

install_requires = \
['astor>=0.8.1,<0.9.0', 'jinja2>=2.11.1,<3.0.0']

setup_kwargs = {
    'name': 'colossal',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'd1618033',
    'author_email': 'd1618033@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
