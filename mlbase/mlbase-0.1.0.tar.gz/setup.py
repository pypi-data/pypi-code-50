# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mlbase']

package_data = \
{'': ['*']}

install_requires = \
['ipython>=7.13.0,<8.0.0',
 'matplotlib>=3.1.3,<4.0.0',
 'numpy>=1.18.1,<2.0.0',
 'pandas>=1.0.1,<2.0.0',
 'seaborn>=0.10.0,<0.11.0',
 'sklearn>=0.0,<0.1']

setup_kwargs = {
    'name': 'mlbase',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Zhen Zhang',
    'author_email': 'git@zhen-zhang.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
