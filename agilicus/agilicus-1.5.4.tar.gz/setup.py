# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['agilicus',
 'agilicus.agilicus_api',
 'agilicus.agilicus_api.api',
 'agilicus.agilicus_api.models',
 'agilicus.agilicus_api.test']

package_data = \
{'': ['*'],
 'agilicus': ['.openapi-generator/*'],
 'agilicus.agilicus_api': ['docs/*']}

install_requires = \
['PyJWT>=1.5.3,<1.6.0',
 'arrow>=0.13.1,<0.14.0',
 'certifi>=14.05.14',
 'click-shell>=2.0,<3.0',
 'connexion>=2.2.0,<2.3.0',
 'oauth2client>=4.1.3,<4.2.0',
 'prettytable>=0.7.2,<0.8.0',
 'python_dateutil>2.5.3',
 'requests>=2.21.0,<2.30.0',
 'six>1.10',
 'urllib3>1.15.1']

entry_points = \
{'console_scripts': ['agilicus-cli = agilicus.main:main']}

setup_kwargs = {
    'name': 'agilicus',
    'version': '1.5.4',
    'description': 'Agilicus SDK',
    'long_description': "## Agilicus SDK (Python)\n\nThe overall API is [documented](https://www.agilicus.com/api).\n\nA subset of this code (that which accesses the above API)\nis [generated](agilicus/agilicus_api_README.md)\n\n## Build\n\n(first generate the api access, 'cd ..; ./local-build')\n\n```\npoetry install\npoetry run pytest\n```\n\nTo run the CLI from the development venv:\ngene\n\n`poetry run python -m agilicus.main`\n\nTo format & lint:\n\n```\npoetry run black .\npoetry run flake8\n```\n\n## CLI Usage\n\nCredentials are cached in ~/.config/agilicus, per issuer.\n\n```\nagilicus-cli --client_id admin-portal --issuer https://auth.cloud.egov.city list-applications\n```\n",
    'author': 'Agilicus Devs',
    'author_email': 'dev@agilicus.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
