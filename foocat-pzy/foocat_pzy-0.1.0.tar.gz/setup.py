# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['foocat_pzy']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.0.1,<2.0.0']

setup_kwargs = {
    'name': 'foocat-pzy',
    'version': '0.1.0',
    'description': 'python package test',
    'long_description': None,
    'author': 'zhypan',
    'author_email': 'apeggy123@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
