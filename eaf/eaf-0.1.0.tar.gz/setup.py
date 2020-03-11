# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eaf']

package_data = \
{'': ['*']}

install_requires = \
['tornado>=6.0.4,<7.0.0']

setup_kwargs = {
    'name': 'eaf',
    'version': '0.1.0',
    'description': 'Enterprise Application Framework',
    'long_description': None,
    'author': 'Pavel Kulyov',
    'author_email': 'kulyov.pavel@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
