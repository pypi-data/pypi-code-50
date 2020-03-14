# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nayvy',
 'nayvy.console',
 'nayvy.function',
 'nayvy.importing',
 'nayvy.projects',
 'nayvy.projects.modules',
 'nayvy.testing']

package_data = \
{'': ['*']}

install_requires = \
['click-help-colors>=0.7,<0.8', 'click>=7.1.1,<8.0.0']

entry_points = \
{'console_scripts': ['nayvy = nayvy.console:main']}

setup_kwargs = {
    'name': 'nayvy',
    'version': '0.0.1',
    'description': 'Enhancing python code editting environment',
    'long_description': None,
    'author': 'Hiroki Konishi',
    'author_email': 'relastle@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
