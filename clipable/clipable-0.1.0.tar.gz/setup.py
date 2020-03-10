# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['clipable']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.0,<2.0', 'pyperclip>=1.7,<2.0', 'tabulate>=0.8.6,<0.9.0']

entry_points = \
{'console_scripts': ['clipable = clipable.cli:main']}

setup_kwargs = {
    'name': 'clipable',
    'version': '0.1.0',
    'description': 'Your clipboard(Excel or Google spreadsheet) change to markdown clipboard',
    'long_description': None,
    'author': 'yujikawa',
    'author_email': 'windbell0404@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.6,<4.0.0',
}


setup(**setup_kwargs)
