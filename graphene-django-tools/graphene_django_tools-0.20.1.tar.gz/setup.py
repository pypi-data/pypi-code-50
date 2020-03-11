# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['graphene_django_tools', 'graphene_django_tools.dataloader']

package_data = \
{'': ['*']}

install_requires = \
['graphene-resolver>=0.1.8,<0.2.0',
 'graphene>=2.1,<3.0',
 'isodate>=0.6,<0.7',
 'lazy-object-proxy>=1.4,<2.0']

setup_kwargs = {
    'name': 'graphene-django-tools',
    'version': '0.20.1',
    'description': 'Tools for use [`graphene-django`](https://github.com/graphql-python/graphene-django)',
    'long_description': '# Graphene django tools\n\n[![build status](https://github.com/NateScarlet/graphene-django-tools/workflows/Python%20package/badge.svg)](https://github.com/NateScarlet/graphene-django-tools/actions)\n[![version](https://img.shields.io/pypi/v/graphene-django-tools)](https://pypi.org/project/graphene-django-tools/)\n![python version](https://img.shields.io/pypi/pyversions/graphene-django-tools)\n![django version](https://img.shields.io/pypi/djversions/graphene-django-tools)\n![wheel](https://img.shields.io/pypi/wheel/graphene-django-tools)\n![maintenance](https://img.shields.io/maintenance/yes/2020)\n[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)\n\nTools for use [`graphene`](https://github.com/graphql-python/graphene) with django.\nUse a explicit schema definition approach that different from `graphene-django`.\n\nDocumentation is placed in [docs folder](./docs).\n\n## Install\n\n`pip install graphene-django-tools`\n\n## Features\n\n- django integration for [graphene-resolver](https://github.com/NateScarlet/graphene-resolver).\n- optimize queryset with django `only`,`selected_related`,`prefetch_related` to only select fields that used in query.\n- data loader graphene middleware.\n\n## Development\n\ntest: `make test`\n',
    'author': 'NateScarlet',
    'author_email': 'NateScarlet@Gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/NateScarlet/graphene-django-tools',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
