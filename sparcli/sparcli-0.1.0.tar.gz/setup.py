# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sparcli']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.18.1,<2.0.0']

setup_kwargs = {
    'name': 'sparcli',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Alex Fraser',
    'author_email': 'alex.d.fraser@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/z0u/sparcli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
