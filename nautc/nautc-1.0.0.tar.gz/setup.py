# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['nautc']
install_requires = \
['wisepy2>=1.1.1,<2.0.0']

entry_points = \
{'console_scripts': ['nautc = nautc:main']}

setup_kwargs = {
    'name': 'nautc',
    'version': '1.0.0',
    'description': 'Convert plain text (letters, sometimes numbers, sometimes punctuation) to obscure but cool characters.',
    'long_description': None,
    'author': 'Nasy',
    'author_email': 'nasyxx+python@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
