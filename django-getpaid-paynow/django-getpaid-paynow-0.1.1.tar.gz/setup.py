# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['getpaid_paynow']

package_data = \
{'': ['*']}

install_requires = \
['django-getpaid>=2.0.0-rc.4,<3.0.0',
 'requests>=2.23.0,<3.0.0',
 'swapper>=1.1.2,<2.0.0']

setup_kwargs = {
    'name': 'django-getpaid-paynow',
    'version': '0.1.1',
    'description': 'Django-GetPaid plugin for mBank payNow service.',
    'long_description': '# django-getpaid-paynow\nDjango-getpaid plugin for mBank payNow service\n',
    'author': 'Dominik Kozaczko',
    'author_email': 'dominik@kozaczko.info',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/django-getpaid/django-getpaid-paynow',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
