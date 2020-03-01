# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ohmyxdu',
 'ohmyxdu.auth',
 'ohmyxdu.builtins',
 'ohmyxdu.plugins',
 'ohmyxdu.security',
 'ohmyxdu.security.chacha20poly1305',
 'ohmyxdu.utils']

package_data = \
{'': ['*']}

install_requires = \
['defopt>=5.1.0,<6.0.0',
 'icalendar>=4.0.4,<5.0.0',
 'loguru>=0.4.1,<0.5.0',
 'parsel>=1.5.2,<2.0.0',
 'requests>=2.23.0,<3.0.0',
 'toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['omx = ohmyxdu.console:main']}

setup_kwargs = {
    'name': 'oh-my-xdu',
    'version': '0.1.0',
    'description': 'Useful tools for XDU students',
    'long_description': None,
    'author': 'zkonge',
    'author_email': 'zkonge@outlook.com',
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
