# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shishakai']

package_data = \
{'': ['*']}

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1.5.0,<2.0.0']}

setup_kwargs = {
    'name': 'shishakai',
    'version': '0.0.1',
    'description': 'Gather schedules for movie preview events',
    'long_description': '# shishakai\n\nshishakai is a Python library that gathers schedules for movie preview events. The "shishakai" (試写会) is a movie preview in Japanese.\n',
    'author': 'Takahiro Yano',
    'author_email': 'speg03@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/speg03/shishakai',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
