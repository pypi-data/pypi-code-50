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
    'version': '0.1.4',
    'description': 'Your clipboard(Excel or Google spreadsheet) change to markdown clipboard',
    'long_description': '# clipable\nWhen we copy cells from spreadsheet or excel, clipboard change to markdown format using clipable.\n\n![clipable](https://user-images.githubusercontent.com/14313351/76307902-0baf8b80-630d-11ea-9d01-337d8da9b448.gif)\n\n# How to install\n\n```\n$ pip install clipable\n```\n\n# How to use\n1. Copy table from spreadsheet, csv etc.\n2. Open terminal, then run clipable.(if you will copy csv, run clipable -f csv)\n3. Paste to textarea.\n\n# LICENSE\nApache 2.0',
    'author': 'yujikawa',
    'author_email': 'windbell0404@gmail.com',
    'url': 'https://github.com/yujikawa/clipable',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
