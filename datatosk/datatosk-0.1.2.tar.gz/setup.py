# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datatosk', 'datatosk.consts']

package_data = \
{'': ['*']}

install_requires = \
['bottleneck>=1.3.2,<2.0.0',
 'google-cloud-bigquery>=1.24.0,<2.0.0',
 'mysqlclient>=1.4.6,<2.0.0',
 'numexpr>=2.7.1,<3.0.0',
 'pandas-gbq>=0.13.1,<0.14.0',
 'pandas>=1.0.1,<2.0.0',
 'sqlalchemy>=1.3.13,<2.0.0']

setup_kwargs = {
    'name': 'datatosk',
    'version': '0.1.2',
    'description': '',
    'long_description': None,
    'author': 'Miłosz Bednarzak',
    'author_email': 'milosz.bednarzak@bethink.pl',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
