# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mobi']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'mobi',
    'version': '0.1.0',
    'description': 'unpack mobi files',
    'long_description': '# mobi - lib for unpacking mobi files\n\nwork in progress ...\n',
    'author': 'Titusz Pan',
    'author_email': 'tp@py7.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github/iscc/mobi',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
