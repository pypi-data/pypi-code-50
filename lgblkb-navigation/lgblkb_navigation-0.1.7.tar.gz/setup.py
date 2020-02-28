# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lgblkb_navigation',
 'lgblkb_navigation.base_geometry',
 'lgblkb_navigation.field_geometry',
 'lgblkb_navigation.utils']

package_data = \
{'': ['*']}

install_requires = \
['dynaconf>=2.2.2,<3.0.0',
 'geoalchemy2>=0.6.3,<0.7.0',
 'geojson>=2.5.0,<3.0.0',
 'lgblkb-tools>=1.1.3,<2.0.0',
 'matplotlib>=3.1.3,<4.0.0',
 'more-itertools>=8.2.0,<9.0.0',
 'networkx>=2.4,<3.0',
 'numpy>=1.18.1,<2.0.0',
 'ortools>=7.5.7466,<8.0.0',
 'pandas>=1.0.1,<2.0.0',
 'pillow>=7.0.0,<8.0.0',
 'pyyaml>=5.3,<6.0',
 'requests>=2.23.0,<3.0.0',
 'ruamel.yaml>=0.16.10,<0.17.0',
 'scikit-learn>=0.22.1,<0.23.0',
 'scipy>=1.4.1,<2.0.0',
 'shapely>=1.7.0,<2.0.0',
 'sortedcontainers>=2.1.0,<3.0.0',
 'visilibity>=1.0.10,<2.0.0',
 'visvalingamwyatt>=0.1.2,<0.2.0']

setup_kwargs = {
    'name': 'lgblkb-navigation',
    'version': '0.1.7',
    'description': 'Tools to navigate easier)',
    'long_description': None,
    'author': 'lgblkb',
    'author_email': 'dbakhtiyarov@nu.edu.kz',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.9,<4.0.0',
}


setup(**setup_kwargs)
