# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cambak', 'cambak.cameras']

package_data = \
{'': ['*']}

install_requires = \
['pyyaml>=5.3,<6.0']

setup_kwargs = {
    'name': 'cambak',
    'version': '0.1.0',
    'description': 'Camera Backup script',
    'long_description': None,
    'author': 'Michael Vieira',
    'author_email': 'contact@mvieira.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
