# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hootsweet']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.23.0,<3.0.0']

setup_kwargs = {
    'name': 'hootsweet',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Ciaran McCormick',
    'author_email': 'ciaran.mccormick@itoworld.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
