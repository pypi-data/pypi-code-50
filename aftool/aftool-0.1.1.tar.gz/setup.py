# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aftool']

package_data = \
{'': ['*']}

install_requires = \
['joblib>=0.14.1,<0.15.0',
 'numpy>=1.18.0,<2.0.0',
 'pandas>=0.25.3,<0.26.0',
 'psutil>=5.6,<6.0',
 'pyecharts>=1.6.2,<2.0.0',
 'pytest>=5.3.5,<6.0.0',
 'snapshot_selenium>=0.0.2,<0.0.3',
 'tqdm>=4.41,<5.0']

setup_kwargs = {
    'name': 'aftool',
    'version': '0.1.1',
    'description': "Asdil Fibrizo's tool",
    'long_description': "# aftool \n[![](https://travis-ci.com/Asdil/aftool.svg?branch=master)](https://travis-ci.com/Asdil/aftool)\n\nAsdil's tool\n",
    'author': 'Asdil Fibrizo',
    'author_email': 'jpl4job@126.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Asdil/aftool',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
