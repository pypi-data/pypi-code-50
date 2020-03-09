# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['onelearn']

package_data = \
{'': ['*']}

install_requires = \
['bokeh>=1.3.4,<2.0.0',
 'colorcet>=2.0.2,<3.0.0',
 'matplotlib>=3.1,<4.0',
 'numba>=0.48,<0.49',
 'numpy>=1.17.4,<2.0.0',
 'scikit-learn>=0.22,<0.23',
 'scipy>=1.3.2,<2.0.0',
 'streamlit>=0.49.0,<0.50.0',
 'tqdm>=4.36,<5.0']

setup_kwargs = {
    'name': 'onelearn',
    'version': '0.1.1',
    'description': 'Machine learning algorithms for online learning',
    'long_description': None,
    'author': 'Stéphane Gaïffas',
    'author_email': 'stephane.gaiffas@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
