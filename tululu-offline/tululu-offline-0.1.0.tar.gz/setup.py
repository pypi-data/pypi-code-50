# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tululu_offline']

package_data = \
{'': ['*']}

install_requires = \
['BeautifulSoup4>=4.8.2,<5.0.0',
 'lxml>=4.5.0,<5.0.0',
 'pathvalidate>=2.2.0,<3.0.0',
 'requests>=2.23.0,<3.0.0',
 'tqdm>=4.43.0,<5.0.0']

entry_points = \
{'console_scripts': ['tululu-offline = tululu_offline.app:main']}

setup_kwargs = {
    'name': 'tululu-offline',
    'version': '0.1.0',
    'description': 'Read it tululu.org without Internet',
    'long_description': '# Books library restyle\n\n<p align="center">\n  <a href="https://link_to_docs">\n    <img width="500"\n         src="http://omsklib.ru/files/news/2017/predvarit-zakaz/166513214-1.jpg"\n         alt="Books library restyle" />\n  </a>\n</p>\n\n![Platform](https://img.shields.io/badge/platform-linux-brightgreen)\n![Python_versions](https://img.shields.io/badge/3.7%20%7C%203.8-blue)\n![GitHub](https://img.shields.io/github/license/velivir/books-library-restyle)\n[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)\n',
    'author': 'Vitaliy Antonov',
    'author_email': 'vitaliyantonoff@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/wemake-services/wemake-python-styleguide',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
