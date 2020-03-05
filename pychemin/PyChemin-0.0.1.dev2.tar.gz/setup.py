# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pychemin']

package_data = \
{'': ['*']}

install_requires = \
['colr>=0.9.1,<0.10.0',
 'docopt>=0.6.2,<0.7.0',
 'fuzzywuzzy>=0.18.0,<0.19.0',
 'lark-parser>=0.8.1,<0.9.0',
 'python-levenshtein>=0.12.0,<0.13.0',
 'termcolor>=1.1.0,<2.0.0',
 'toml>=0.10.0,<0.11.0',
 'unidecode>=1.1.1,<2.0.0']

entry_points = \
{'console_scripts': ['pychemin = pychemin.cli:run']}

setup_kwargs = {
    'name': 'pychemin',
    'version': '0.0.1.dev2',
    'description': 'A minimal language to describe interactive, terminal-based text adventure games',
    'long_description': "# PyChemin\n\nI'm in the process of decoupling PyChemin from its inception's repository, [Hyperis](github.com/ewen-lbh/hyperis) -- a terminal-based adventure game.\n\nA proper README + GitHub page will soon be available.\n\nIn the meantime, if you can read french, you can [learn PyChemin's syntax](ewen-lbh.github.io/hyperis)\n",
    'author': 'ewen-lbh',
    'author_email': 'ewen.lebihan7@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ewen-lbh/pychemin',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
