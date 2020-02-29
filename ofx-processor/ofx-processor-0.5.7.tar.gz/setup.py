# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ofx_processor', 'ofx_processor.processors', 'ofx_processor.utils']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0',
 'dateparser>=0.7.2,<0.8.0',
 'ofxtools>=0.8.20,<0.9.0',
 'requests>=2.22.0,<3.0.0']

entry_points = \
{'console_scripts': ['ynab = ofx_processor.main:cli']}

setup_kwargs = {
    'name': 'ofx-processor',
    'version': '0.5.7',
    'description': 'Personal ofx processor',
    'long_description': '# ofx-processor\n\n[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Crocmagnon_ofx-processor&metric=bugs)](https://sonarcloud.io/dashboard?id=Crocmagnon_ofx-processor)\n[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Crocmagnon_ofx-processor&metric=code_smells)](https://sonarcloud.io/dashboard?id=Crocmagnon_ofx-processor)\n[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Crocmagnon_ofx-processor&metric=coverage)](https://sonarcloud.io/dashboard?id=Crocmagnon_ofx-processor)\n[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=Crocmagnon_ofx-processor&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=Crocmagnon_ofx-processor)\n[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Crocmagnon_ofx-processor&metric=ncloc)](https://sonarcloud.io/dashboard?id=Crocmagnon_ofx-processor)\n[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Crocmagnon_ofx-processor&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=Crocmagnon_ofx-processor)\n[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Crocmagnon_ofx-processor&metric=alert_status)](https://sonarcloud.io/dashboard?id=Crocmagnon_ofx-processor)\n[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Crocmagnon_ofx-processor&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=Crocmagnon_ofx-processor)\n[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Crocmagnon_ofx-processor&metric=security_rating)](https://sonarcloud.io/dashboard?id=Crocmagnon_ofx-processor)\n[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=Crocmagnon_ofx-processor&metric=sqale_index)](https://sonarcloud.io/dashboard?id=Crocmagnon_ofx-processor)\n    \n## Usage\n\n```shell script\nUsage: ynab [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  --version   Show the version and exit.\n  -h, --help  Show this message and exit.\n\nCommands:\n  bpvf     Process BPVF bank statement (OFX)\n  ce       Process CE bank statement (OFX)\n  config\n  revolut  Process Revolut bank statement (CSV)\n```\n\nAll transactions will be pushed to YNAB. If this is your first time using the script,\nit will open a generated config file for you to fill up.\n\nThe account and budget UUID are found in the YNAB url when using the web app.\n',
    'author': 'Gabriel Augendre',
    'author_email': 'gabriel@augendre.info',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
