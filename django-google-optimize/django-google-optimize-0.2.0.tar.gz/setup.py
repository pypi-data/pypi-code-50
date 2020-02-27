# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_google_optimize', 'django_google_optimize.migrations']

package_data = \
{'': ['*']}

install_requires = \
['factory-boy>=2.12.0,<3.0.0']

setup_kwargs = {
    'name': 'django-google-optimize',
    'version': '0.2.0',
    'description': 'Django-google-optimize is a reusable Django application designed to make running server side Google Optimize A/B test easy.',
    'long_description': '# Django-google-optimize\n\n![Lint](https://github.com/adinhodovic/django-google-optimize/workflows/Test/badge.svg)\n![Test](https://github.com/adinhodovic/django-google-optimize/workflows/Lint/badge.svg)\n[![Coverage](https://codecov.io/gh/adinhodovic/django-google-optimize/branch/master/graphs/badge.svg)](https://codecov.io/gh/adinhodovic/django-google-optimize/branch/master)\n[![Supported Python versions](https://img.shields.io/pypi/pyversions/django-google-optimize.svg)](https://pypi.org/project/django-google-optimize/)\n[![PyPI Version](https://img.shields.io/pypi/v/django-google-optimize.svg?style=flat)](https://pypi.org/project/django-google-optimize/)\n\nDjango-google-optimize is a Django application designed to make running Google Optimize A/B tests easy.\n\n## Installation\n\nInstall django-google-optimize with pip:\n\n`pip install django-google-optimize`\n\nAdd the application to installed Django applications:\n\n```py\nDJANGO_APPS = [\n    ...\n    "django_google_optimize",\n    ...\n]\n```\n\nAdd the middleware:\n\n```py\nMIDDLEWARE = [\n    ...\n    "django_google_optimize.middleware.google_optimize",\n    ...\n]\n```\n\n## Getting started\n\nHead over to the Django admin and add a new Google Optimize experiment. Add an experiment variant with the index 1 and the alias "new_design". Set the experiment cookie\'s active variant index to 1. Now the active variant index for that experiment is 1 which is the experiment variant with the alias "new_design" that you created.\n\nNow you can access the experiment in templates by the experiment alias and the variant alias:\n\n```django\n{% if request.google_optimize.redesign == "new_design" %}\n{% include "jobs/jobposting_list_new.html" %}\n{% else %}\n{% include "jobs/jobposting_list_old.html" %}\n{% endif %}\n```\n\nOr use it inline:\n\n```django\n<nav class="navbar navbar-expand-lg navbar-dark\n{% if request.google_optimize.redesign == "new_design" %} navbar-redesign{% endif %}">\n```\n\nNote: The experiment cookie only works in DEBUG mode and is used to avoid interacting with the session to add the `_gaexp` cookie making it possible to test the experiment variants through the Django admin.\n\nFull documentation [can be found here.](https://django-google-optimize.readthedocs.io/en/latest/)\n\n## Documentation and Support\n\nMore documentation can be found in the docs directory or read [online](https://django-google-optimize.readthedocs.io/en/latest/). Open a Github issue for support.\n',
    'author': 'Adin Hodovic',
    'author_email': 'hodovicadin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/adinhodovic/django-google-optimize',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
