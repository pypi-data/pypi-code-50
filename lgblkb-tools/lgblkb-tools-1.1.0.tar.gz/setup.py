# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lgblkb_tools', 'lgblkb_tools.common', 'lgblkb_tools.db']

package_data = \
{'': ['*']}

install_requires = \
['checksumdir>=1.1.7,<2.0.0',
 'colorlog>=4.1.0,<5.0.0',
 'geojson>=2.5.0,<3.0.0',
 'matplotlib>=3.1.3,<4.0.0',
 'more-itertools>=8.2.0,<9.0.0',
 'numpy>=1.18.1,<2.0.0',
 'pandas>=1.0.1,<2.0.0',
 'pyproj>=2.5.0,<3.0.0',
 'python-box>=4.2.0,<5.0.0',
 'python-log-indenter>=0.9,<0.10',
 'python-telegram-bot>=12.4.2,<13.0.0',
 'requests>=2.23.0,<3.0.0',
 'shapely>=1.7.0,<2.0.0',
 'wrapt>=1.12.0,<2.0.0']

entry_points = \
{'console_scripts': ['bump = lgblkb_tools.dev_script:export_reqs',
                     'export_reqs = lgblkb_tools.dev_script:export_reqs']}

setup_kwargs = {
    'name': 'lgblkb-tools',
    'version': '1.1.0',
    'description': 'Tools to make life easier',
    'long_description': None,
    'author': 'lgblkb',
    'author_email': 'dbakhtiyarov@nu.edu.kz',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.9,<4.0.0',
}


setup(**setup_kwargs)
