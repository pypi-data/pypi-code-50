# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hootsweet']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.23,<3.0']

setup_kwargs = {
    'name': 'hootsweet',
    'version': '0.2.0',
    'description': 'A python library for the HootSuite REST API.',
    'long_description': None,
    'author': 'Ciaran McCormick',
    'author_email': 'ciaran@ciaranmccormick.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
