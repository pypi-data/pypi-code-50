# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fsorg']

package_data = \
{'': ['*']}

install_requires = \
['pyfiglet>=0.8.post1,<0.9', 'rm>=2019.4.13,<2020.0.0']

entry_points = \
{'console_scripts': ['fsorg = fsorg.entry:main']}

setup_kwargs = {
    'name': 'fsorg',
    'version': '1.0.1',
    'description': 'Create a directory structure by describing it',
    'long_description': None,
    'author': 'ewen-lbh',
    'author_email': 'ewen.lebihan7@gmail.com',
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
