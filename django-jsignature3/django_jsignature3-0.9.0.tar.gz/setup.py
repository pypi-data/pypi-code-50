# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jsignature', 'jsignature.tests']

package_data = \
{'': ['*'],
 'jsignature': ['locale/es/LC_MESSAGES/*',
                'locale/fr/LC_MESSAGES/*',
                'static/js/*',
                'templates/jsignature/*']}

install_requires = \
['django>3.0.1', 'pillow>5.0.0', 'pyquery>1.0']

setup_kwargs = {
    'name': 'django-jsignature3',
    'version': '0.9.0',
    'description': 'Provides a simple way to handle jSignature jQuery plugin through a django form.',
    'long_description': None,
    'author': 'Florent Lebreton',
    'author_email': 'lebreton.florent@wanadoo.fr',
    'maintainer': 'Adremides',
    'maintainer_email': 'adremides@gmail.com',
    'url': 'https://gitlab.com/adremides/django_jsignature3/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>3.6',
}


setup(**setup_kwargs)
