# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gitsplit']

package_data = \
{'': ['*']}

install_requires = \
['python-ranges>=0.1.3,<0.2.0', 'toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['git-split = gitsplit.main:main']}

setup_kwargs = {
    'name': 'git-split',
    'version': '0.0.1',
    'description': 'A history-preserving file splitter for Git.',
    'long_description': None,
    'author': 'Eric Smith',
    'author_email': 'eric@esmithy.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
