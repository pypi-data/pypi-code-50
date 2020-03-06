# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['query_diet']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.0.1,<2.0.0', 'shortuuid>=0.5.0,<0.6.0']

setup_kwargs = {
    'name': 'query-diet',
    'version': '0.1.1',
    'description': 'A diet for losing query fats.',
    'long_description': None,
    'author': 'Mohamed Seleem',
    'author_email': 'hi@mselee.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mselee/query_diet',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
