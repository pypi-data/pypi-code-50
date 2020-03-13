# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyxbee']

package_data = \
{'': ['*']}

install_requires = \
['digi-xbee>=1.2.0,<2.0.0', 'ordered-set>=3.1.1,<4.0.0']

setup_kwargs = {
    'name': 'pyxbee',
    'version': '0.7.0',
    'description': 'Communication module for Marta (Policumbent)',
    'long_description': '# Pyxbee\n\n![Status](https://img.shields.io/badge/status-beta-yellow.svg)\n[![Version](https://img.shields.io/pypi/v/pyxbee)](https://pypi.python.org/pypi/pyxbee/)\n[![License](https://img.shields.io/github/license/gabelluardo/pyxbee?color=blue)](https://github.com/gabelluardo/pyxbee/blob/master/LICENSE)\n[![Python Version](https://img.shields.io/pypi/pyversions/pyxbee)](https://www.python.org/downloads/)\n\nModulo di comunicazione per [Marta](https://github.com/gabelluardo/marta)\n\nFornisce classi di alto livello per interfacciarsi col modulo [digi-xbee](https://github.com/digidotcom/xbee-python) e le antenne xbee\n\n\n## Installazione\n\n    pip install pyxbee\n\noppure clonando il repository (serve [poetry](https://python-poetry.org/)):\n\n    git clone https://github.com/gabelluardo/pyxbee\n    cd pyxbee/\n    poetry install\n\n## License\n\nLGPLv3\n',
    'author': 'Gabriele Bellaurdo',
    'author_email': 'gabriele.belluardo@outlook.it',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/gabelluardo/pyxbee',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
