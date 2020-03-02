# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['onig', 'onig._onig_cffi']

package_data = \
{'': ['*']}

install_requires = \
['cffi>=1.14.0,<2.0.0']

extras_require = \
{':implementation_name == "cpython"': ['unibuf>=0.1.1,<0.2.0']}

setup_kwargs = {
    'name': 'onig',
    'version': '0.0.6',
    'description': 'A Python wrapper around the Oniguruma regular expression library.',
    'long_description': 'Python Onig\n===========\n\nPython bindings for the Oniguruma regular expression library.\n',
    'author': 'Maximilian Köhl',
    'author_email': 'mkoehl@cs.uni-saarland.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://dgit.cs.uni-saarland.de/koehlma/onig',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
