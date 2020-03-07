# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['adbc', 'adbc.commands']

package_data = \
{'': ['*']}

install_requires = \
['asyncpg>=0.18.3,<0.19.0',
 'cached_property>=1.5.1,<2.0.0',
 'cleo>=0.7.5,<0.8.0',
 'ipython>=7.6.1,<8.0.0',
 'jsondiff>=1.2.0,<2.0.0',
 'pyaml>=19.12.0,<20.0.0',
 'pyyaml>=5.3,<6.0',
 'uvloop>=0.12.2,<0.13.0']

entry_points = \
{'console_scripts': ['adbc = adbc.cli:main']}

setup_kwargs = {
    'name': 'adbc',
    'version': '0.0.1',
    'description': '',
    'long_description': None,
    'author': 'aleontiev',
    'author_email': 'alonetiev@gmail.com',
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
