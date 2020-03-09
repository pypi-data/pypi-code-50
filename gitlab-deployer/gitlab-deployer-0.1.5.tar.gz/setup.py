# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deployer']

package_data = \
{'': ['*']}

install_requires = \
['Click>=7.0,<8.0', 'python-gitlab>=1.15,<2.0', 'requests>=2.22,<3.0']

entry_points = \
{'console_scripts': ['deployer = deployer.main:cli']}

setup_kwargs = {
    'name': 'gitlab-deployer',
    'version': '0.1.5',
    'description': 'GitLab Deployer',
    'long_description': '# GitLab deployer\n\n\n## Installation\n\n```\npip install gitlab-deployer\n```\n\n\n## Usage \n\nComing Soon!\n\n\n',
    'author': 'Dmitry Vysochin',
    'author_email': 'dmitry.vysochin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/veryevilzed/gitlab-deployer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
