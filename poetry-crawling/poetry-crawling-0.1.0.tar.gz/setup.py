# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_crawling']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.8.2,<5.0.0',
 'bs4>=0.0.1,<0.0.2',
 'grpcio>=1.27.2,<2.0.0',
 'numpy>=1.18.1,<2.0.0',
 'protobuf>=3.11.3,<4.0.0',
 'selenium>=3.141.0,<4.0.0',
 'six>=1.14.0,<2.0.0',
 'soupsieve>=2.0,<3.0']

setup_kwargs = {
    'name': 'poetry-crawling',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'adi',
    'author_email': 'adi@cakeplabs.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
