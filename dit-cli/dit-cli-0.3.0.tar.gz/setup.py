# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dit_cli']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['dit = dit_cli.cli:main']}

setup_kwargs = {
    'name': 'dit-cli',
    'version': '0.3.0',
    'description': 'The CLI for dit',
    'long_description': 'This is the CLI for dit. Dit is a type of arbitrary container file. This\nCLI can interact with scripts in dit files, and do things like telling\nthem to validate themselves. See more at [DitaBase.io]\n\n  [DitaBase.io]: https://www.ditabase.io/',
    'author': 'Isaiah Shiner',
    'author_email': 'shiner.isaiah@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://www.ditabase.io/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
