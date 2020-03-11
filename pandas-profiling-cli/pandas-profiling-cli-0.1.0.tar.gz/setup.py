# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pandas_profiling_cli']

package_data = \
{'': ['*']}

install_requires = \
['japanize-matplotlib>=1.0.5,<2.0.0',
 'pandas-profiling>=2.5.0,<3.0.0',
 'xlrd>=1.2.0,<2.0.0']

entry_points = \
{'console_scripts': ['pandas-profiling = pandas_profiling_cli.main:main']}

setup_kwargs = {
    'name': 'pandas-profiling-cli',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'fuyutarow',
    'author_email': 'fuyutarow@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
