# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hootsweet']

package_data = \
{'': ['*']}

install_requires = \
['cherrypy>=18.5.0,<19.0.0',
 'requests>=2.23,<3.0',
 'requests_oauthlib>=1.3.0,<2.0.0']

setup_kwargs = {
    'name': 'hootsweet',
    'version': '0.3.0',
    'description': 'A python library for the HootSuite REST API.',
    'long_description': None,
    'author': 'Ciaran McCormick',
    'author_email': 'ciaran@ciaranmccormick.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
