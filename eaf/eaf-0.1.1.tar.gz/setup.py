# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eaf']

package_data = \
{'': ['*']}

install_requires = \
['tornado>=6.0.4,<7.0.0']

setup_kwargs = {
    'name': 'eaf',
    'version': '0.1.1',
    'description': 'Enterprise Application Framework',
    'long_description': "|PyPI| |Build Status| |codecov.io|\n\n===\nEAF\n===\n\nEnterprise Application Framework.\n\nThis framework contains all the pieces you need to create feature-rich\nenterprise-grade distributed and distributedn't applications.\n\nAlso means Extensible As Fuck.\n\nRequirements\n============\n\n* >=python-3.7\n* >=tornado-6.0\n\nInstallation\n============\n\n.. code-block:: console\n\n\t$ pip install eaf\n\n\nDevelopment\n===========\n\nInstallation\n------------\n\n.. code-block:: console\n\n   $ poetry install\n\nTesting\n-------\n\n.. code-block:: console\n\n   $ poetry run pytest -s -v tests/  # run all tests\n   $ poetry run pytest --cov=eaf -s -v tests/  # run all tests with coverage\n\n\nDocumentation\n-------------\n\n* **To be added**\n\n.. |PyPI| image:: https://badge.fury.io/py/eaf.svg\n   :target: https://badge.fury.io/py/eaf\n.. |Build Status| image:: https://github.com/pkulev/eaf/workflows/CI/badge.svg\n.. |codecov.io| image:: http://codecov.io/github/pkulev/eaf/coverage.svg?branch=master\n   :target: http://codecov.io/github/pkulev/eaf?branch=master\n",
    'author': 'Pavel Kulyov',
    'author_email': 'kulyov.pavel@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pkulev/eaf',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
