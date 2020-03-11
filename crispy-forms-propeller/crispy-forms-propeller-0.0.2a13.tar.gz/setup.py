# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['crispy_forms_propeller',
 'crispy_forms_propeller.layout',
 'crispy_forms_propeller.templatetags']

package_data = \
{'': ['*'],
 'crispy_forms_propeller': ['locale/de/LC_MESSAGES/*',
                            'locale/fr/LC_MESSAGES/*',
                            'static/js/crispy_forms_foundation/*',
                            'templates/propeller/*',
                            'templates/propeller/layout/*']}

install_requires = \
['django>=3,<4', 'django_crispy_forms>=1.8.1,<2.0.0']

setup_kwargs = {
    'name': 'crispy-forms-propeller',
    'version': '0.0.2a13',
    'description': "Django application to add 'django-crispy-forms' layout objects for 'Propeller.in'",
    'long_description': None,
    'author': 'Adam Radestock',
    'author_email': 'raddishiow@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
