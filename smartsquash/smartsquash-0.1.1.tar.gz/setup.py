# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['smartsquash']

package_data = \
{'': ['*']}

install_requires = \
['gitpython>=3.0.5,<4.0.0', 'loguru>=0.4.1,<0.5.0']

entry_points = \
{'console_scripts': ['sq = smartsquash.__main__:main']}

setup_kwargs = {
    'name': 'smartsquash',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Max Wittig',
    'author_email': 'max.wittig95@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
