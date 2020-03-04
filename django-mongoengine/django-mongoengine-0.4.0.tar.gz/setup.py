# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_mongoengine',
 'django_mongoengine.fields',
 'django_mongoengine.forms',
 'django_mongoengine.mongo_admin',
 'django_mongoengine.mongo_admin.management',
 'django_mongoengine.mongo_admin.management.commands',
 'django_mongoengine.mongo_admin.templatetags',
 'django_mongoengine.mongo_auth',
 'django_mongoengine.utils',
 'django_mongoengine.views']

package_data = \
{'': ['*'],
 'django_mongoengine.mongo_admin': ['static/*',
                                    'templates/admin/*',
                                    'templates/mongo_admin/*'],
 'django_mongoengine.views': ['templates/*']}

install_requires = \
['django>1.11', 'mongoengine>=0.14']

setup_kwargs = {
    'name': 'django-mongoengine',
    'version': '0.4.0',
    'description': 'Django support for MongoDB via MongoEngine',
    'long_description': None,
    'author': 'Ross Lawley',
    'author_email': 'ross.lawley@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=2.7',
}


setup(**setup_kwargs)
