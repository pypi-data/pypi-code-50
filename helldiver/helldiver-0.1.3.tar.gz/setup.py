# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['helldiver']

package_data = \
{'': ['*']}

install_requires = \
['argparse>=1.4.0,<2.0.0',
 'beautifulsoup4>=4.8.2,<5.0.0',
 'markdown2>=2.3.8,<3.0.0']

setup_kwargs = {
    'name': 'helldiver',
    'version': '0.1.3',
    'description': 'A lightweight markdown to blog-aware HTML converter.',
    'long_description': None,
    'author': 'Rohan Bansal',
    'author_email': 'rohanarunbansal@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
