# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyrs990']

package_data = \
{'': ['*']}

install_requires = \
['defusedxml>=0.6.0,<0.7.0', 'requests>=2.23.0,<3.0.0']

setup_kwargs = {
    'name': 'pyrs990',
    'version': '0.1.0',
    'description': 'A tool for fetching and filtering IRS 990 data.',
    'long_description': None,
    'author': 'George Lesica',
    'author_email': 'george@lesica.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
