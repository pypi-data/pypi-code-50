# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['deetly']

package_data = \
{'': ['*']}

install_requires = \
['altair>=4.0.1,<5.0.0',
 'click>=7.0,<8.0',
 'desert>=2020.1.6,<2021.0.0',
 'geopandas>=0.7.0,<0.8.0',
 'marshmallow>=3.3.0,<4.0.0',
 'pandas>=1.0.1,<2.0.0',
 'plotly>=4.5.1,<5.0.0',
 'pyarrow>=0.16.0,<0.17.0',
 'pydeck>=0.2.1,<0.3.0',
 'requests>=2.22.0,<3.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1.5.0,<2.0.0']}

entry_points = \
{'console_scripts': ['deetly = deetly.console:main']}

setup_kwargs = {
    'name': 'deetly',
    'version': '0.0.2',
    'description': 'toolkit for creating data packages',
    'long_description': None,
    'author': 'Paul Bencze',
    'author_email': 'paul@idelab.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
