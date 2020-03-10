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
    'version': '0.1.1',
    'description': 'Read it tululu.org without Internet',
    'long_description': '# Parser of books from the site tululu.org\n\n<p align="center">\n  <a href="https://link_to_docs">\n    <img width="500"\n         src="http://omsklib.ru/files/news/2017/predvarit-zakaz/166513214-1.jpg"\n         alt="Books library restyle" />\n  </a>\n</p>\n\n## Description\n[![Maintainability](https://api.codeclimate.com/v1/badges/c8ec73b47d297795daae/maintainability)](https://codeclimate.com/github/velivir/tululu-offline/maintainability)\n[![Build Status](https://travis-ci.com/velivir/tululu-offline.svg?branch=master)](https://travis-ci.com/velivir/tululu-offline)\n[![Coverage Status](https://coveralls.io/repos/github/velivir/tululu-offline/badge.png?branch=master)](https://coveralls.io/github/velivir/tululu-offline?branch=master)\n![Platform](https://img.shields.io/badge/platform-linux-brightgreen)\n![Python_versions](https://img.shields.io/badge/Python-3.7%7C3.8-brightgreen)\n![GitHub](https://img.shields.io/github/license/velivir/books-library-restyle)\n[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)\n\n\nThe program downloads from tululu.org books in text format and their covers. The following information is also downloaded to the json file:\n- title\n- author\n- image path\n- book path\n- comments\n- genres\n\n\n## How to install\n\nInstall using [pip](https://pypi.org/project/tululu-offline/):\n  ```bash\n  pip install tululu-offline\n  ```\n\n\n## How to use\n  ```bash\n  tululu-offline [OPTIONS]\n  ```\n\n\n## Options\n- [category_url] - the category url [tululu.org](http://tululu.org)\n- [--start_page] - which page to start downloading\n- [--end_page] - on which page to finish downloading\n- [--dest_folder] - path to the directory with parsing results: pictures, books, JSON.\n- [--skip_txt] - do not download books\n- [--skip_imgs] - do not download images\n- [--json_path] - specify your path to *.json file with results\n\n\n## License\n\nTululu-offline is licensed under the MIT License. See [LICENSE](https://github.com/velivir/tululu-offline/blob/master/LICENSE) for more information.\n\n\n## Project goal\nThe code is written for educational purposes in an online course for web developers [dvmn.org](https://dvmn.org).\n',
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
