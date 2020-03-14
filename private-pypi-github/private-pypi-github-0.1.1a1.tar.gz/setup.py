# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['private_pypi_backends', 'private_pypi_backends.github']

package_data = \
{'': ['*']}

install_requires = \
['PyGithub>=1.46,<2.0', 'private-pypi-core==0.1.3a1', 'requests>=2.23.0,<3.0.0']

entry_points = \
{'console_scripts': ['private_pypi_github_create_package_repo = '
                     'private_pypi_backends.github.impl:github_create_package_repo_cli']}

setup_kwargs = {
    'name': 'private-pypi-github',
    'version': '0.1.1a1',
    'description': '',
    'long_description': '# todo',
    'author': 'huntzhan',
    'author_email': 'huntzhan.dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/private-pypi/private-pypi-github',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
