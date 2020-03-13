# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['easy_tenants']

package_data = \
{'': ['*']}

install_requires = \
['django>=3.0.4,<4.0.0']

setup_kwargs = {
    'name': 'django-easy-tenants',
    'version': '0.1.0',
    'description': 'Easy to create applications that use tenants in django',
    'long_description': '# easy-tenants\n',
    'author': 'Cleiton Lima',
    'author_email': 'cleiton.limapin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/CleitonDeLima/django-easy-tenants',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
