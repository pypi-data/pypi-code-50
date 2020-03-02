# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['single_instance']

package_data = \
{'': ['*']}

install_requires = \
['kanilog>=0.3.2,<0.4.0', 'logzero>=1.5.0,<2.0.0']

setup_kwargs = {
    'name': 'single-instance',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'fx_kirin',
    'author_email': 'fx.kirin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
