# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['private_pypi_bundles']

package_data = \
{'': ['*']}

install_requires = \
['private-pypi-core==0.1.3a2', 'private-pypi-github==0.1.1a2']

entry_points = \
{'console_scripts': ['private_pypi = private_pypi_bundles:run']}

setup_kwargs = {
    'name': 'private-pypi',
    'version': '0.1.0a0',
    'description': 'A private PyPI server powered by flexible backends.',
    'long_description': '# TODO',
    'author': 'huntzhan',
    'author_email': 'huntzhan.dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/private-pypi/private-pypi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
