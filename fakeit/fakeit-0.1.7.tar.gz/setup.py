# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fakeit',
 'fakeit.advanced',
 'fakeit.advanced.person',
 'fakeit.basics',
 'fakeit.basics.boolean',
 'fakeit.basics.bytes',
 'fakeit.basics.geo',
 'fakeit.basics.hashes',
 'fakeit.basics.ip',
 'fakeit.basics.numerics',
 'fakeit.basics.personal',
 'fakeit.basics.strings',
 'fakeit.basics.texts',
 'fakeit.basics.uuids',
 'fakeit.constance',
 'fakeit.constance.email',
 'fakeit.constance.tld',
 'fakeit.extras',
 'fakeit.extras.alchemy',
 'fakeit.extras.django']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'fakeit',
    'version': '0.1.7',
    'description': 'Generate fake data',
    'long_description': None,
    'author': 'Ruslan Samoylov',
    'author_email': 'ruslan.v.samoylov@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
