# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lrrr']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'lrrr',
    'version': '0.0.3',
    'description': 'orbital dynamics',
    'long_description': '![](pics/lrrr.png)\n',
    'author': 'walchko',
    'author_email': 'walchko@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/lrrr/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
