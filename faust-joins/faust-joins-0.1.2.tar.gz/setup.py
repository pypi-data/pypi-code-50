# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['faust_joins']

package_data = \
{'': ['*']}

install_requires = \
['faust>=1.10.4,<2.0.0']

setup_kwargs = {
    'name': 'faust-joins',
    'version': '0.1.2',
    'description': 'Join Faust Streams',
    'long_description': None,
    'author': 'Brian Stearns',
    'author_email': 'brian.stearns@kensho.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/BWStearns/faust_joins',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
