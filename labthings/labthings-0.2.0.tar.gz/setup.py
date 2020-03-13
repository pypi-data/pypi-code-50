# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['labthings',
 'labthings.consumer',
 'labthings.core',
 'labthings.core.tasks',
 'labthings.server',
 'labthings.server.sockets',
 'labthings.server.spec',
 'labthings.server.views',
 'labthings.server.views.docs',
 'labthings.server.wsgi']

package_data = \
{'': ['*'],
 'labthings.server': ['views/docs/static/*', 'views/docs/templates/*']}

install_requires = \
['Flask>=1.1.1,<2.0.0',
 'apispec>=3.2.0,<4.0.0',
 'flask-cors>=3.0.8,<4.0.0',
 'gevent-websocket>=0.10.1,<0.11.0',
 'gevent>=1.4.0,<2.0.0',
 'marshmallow>=3.4.0,<4.0.0',
 'webargs>=5.5.3,<6.0.0']

setup_kwargs = {
    'name': 'labthings',
    'version': '0.2.0',
    'description': 'Python implementation of LabThings, based on the Flask microframework',
    'long_description': None,
    'author': 'jtc42',
    'author_email': 'jtc9242@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
