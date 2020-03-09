# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zygoat',
 'zygoat.components',
 'zygoat.components.backend',
 'zygoat.components.backend.resources',
 'zygoat.components.backend.settings',
 'zygoat.components.frontend',
 'zygoat.components.frontend.cypress',
 'zygoat.components.frontend.cypress.resources',
 'zygoat.components.frontend.eslint',
 'zygoat.components.frontend.eslint.resources',
 'zygoat.components.frontend.prettier',
 'zygoat.components.frontend.prettier.resources',
 'zygoat.components.frontend.resources',
 'zygoat.components.resources',
 'zygoat.utils']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0',
 'colorama>=0.4.3,<0.5.0',
 'python-box>=4.0,<5.0',
 'redbaron>=0.9.2,<0.10.0',
 'requests>=2.23.0,<3.0.0',
 'ruamel.yaml>=0.16.10,<0.17.0',
 'virtualenv>=20.0,<21.0']

entry_points = \
{'console_scripts': ['zg = zygoat.cli:cli']}

setup_kwargs = {
    'name': 'zygoat',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Bequest, Inc.',
    'author_email': 'oss@willing.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
