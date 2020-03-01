# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['upload_path_pyramid']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'upload-path-pyramid',
    'version': '0.1.0',
    'description': 'A small utility function to create path of a uploaded file.',
    'long_description': None,
    'author': 'Surya Teja',
    'author_email': '94suryateja@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/suryasr007/upload-path-pyramid',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<3.9',
}


setup(**setup_kwargs)
