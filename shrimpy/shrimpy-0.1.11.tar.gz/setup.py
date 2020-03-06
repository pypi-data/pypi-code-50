# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shrimpy']

package_data = \
{'': ['*']}

install_requires = \
['fire>=0.2.1,<0.3.0', 'jsonschema>=3.2.0,<4.0.0']

entry_points = \
{'console_scripts': ['shrimpy = shrimpy:run']}

setup_kwargs = {
    'name': 'shrimpy',
    'version': '0.1.11',
    'description': 'A minimal engine for choose-your-own-adventure games.',
    'long_description': None,
    'author': 'Yosoi',
    'author_email': 'yosoi@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
