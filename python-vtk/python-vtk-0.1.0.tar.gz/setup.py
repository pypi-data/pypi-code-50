# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['python_vtk']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=19.1,<20.0', 'numpy>=1.15,<2.0', 'vtk>=8.1,<9.0']

setup_kwargs = {
    'name': 'python-vtk',
    'version': '0.1.0',
    'description': 'Pythonic API for VTK.',
    'long_description': None,
    'author': 'Dominik Steinberger',
    'author_email': 'dominik.steinberger@imfd.tu-freiberg.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
