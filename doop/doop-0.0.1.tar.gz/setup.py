# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['doop']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'doop',
    'version': '0.0.1',
    'description': 'orbital dynamics',
    'long_description': '![](pics/lrrr.png)\n',
    'author': 'walchko',
    'author_email': 'walchko@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/doop/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
