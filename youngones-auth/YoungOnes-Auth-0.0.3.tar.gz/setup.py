# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['youngones']

package_data = \
{'': ['*']}

install_requires = \
['build>=1.0.2,<2.0.0', 'pyyaml>=5.3,<6.0', 'requests>=2.23.0,<3.0.0']

setup_kwargs = {
    'name': 'youngones-auth',
    'version': '0.0.3',
    'description': 'Python Auth Adapter for YoungOnes Authentication',
    'long_description': None,
    'author': 'Alex Pedersen',
    'author_email': 'alex@youngones.works',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
