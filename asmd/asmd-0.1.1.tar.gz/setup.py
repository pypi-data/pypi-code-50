# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asmd']

package_data = \
{'': ['*'], 'asmd': ['definitions/*', 'my_scores/*']}

install_requires = \
['alive-progress>=1.3.3,<2.0.0',
 'beautifulsoup4>=4.8.2,<5.0.0',
 'decorator>=4.4.1,<5.0.0',
 'essentia>=2.1b6.dev184,<3.0',
 'mega.py>=1.0.6,<2.0.0',
 'numpy>=1.18.1,<2.0.0',
 'plotly>=4.4.1,<5.0.0',
 'pretty_midi>=0.2.8,<0.3.0',
 'prompt_toolkit>=3.0.3,<4.0.0',
 'pyfiglet>=0.8.post1,<0.9',
 'requests>=2.22.0,<3.0.0',
 'scikit_learn>=0.22.1,<0.23.0',
 'setuptools>=45.2.0,<46.0.0']

setup_kwargs = {
    'name': 'asmd',
    'version': '0.1.1',
    'description': 'Audio-Score Meta-Dataset',
    'long_description': 'Audio-Score Meta-Dataset\n========================\n\nThis is the repository for paper [. . .] \n\nRead more in the docs_.\n\n.. _docs: https://asmd.readthedocs.org\n\nCite us\n=======\n\n[. . .]\n\nFederico Simonetta \n\n#. https://federicosimonetta.eu.org\n#. https://lim.di.unimi.it\n\n',
    'author': 'Federico Simonetta',
    'author_email': 'federico.simonetta@unimi.it',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://asmd.readthedocs.org',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.9,<4.0.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
