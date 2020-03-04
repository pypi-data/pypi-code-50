# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['agilicus', 'agilicus.api', 'agilicus.models']

package_data = \
{'': ['*']}

install_requires = \
['certifi>=14.05.14', 'python_dateutil>2.5.3', 'six>1.10', 'urllib3>1.15.1']

setup_kwargs = {
    'name': 'agilicus',
    'version': '1.4.1',
    'description': 'Agilicus SDK',
    'long_description': '## Agilicus SDK (Python)\n\n[generated](agilicus_README.md)\n',
    'author': 'Don Bowman',
    'author_email': 'don@agilicus.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
