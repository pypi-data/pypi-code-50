# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['floxcore', 'floxcore.utils']

package_data = \
{'': ['*']}

install_requires = \
['anyconfig>=0.9.0,<0.10.0',
 'python-box>=4.0,<5.0',
 'tqdm>=4.43.0,<5.0.0',
 'wasabi>=0.6.0,<0.7.0']

setup_kwargs = {
    'name': 'flox-core',
    'version': '0.1.0',
    'description': 'Core library for flox',
    'long_description': None,
    'author': 'Michal Przytulski',
    'author_email': 'michal@przytulski.pl',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
