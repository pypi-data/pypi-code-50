#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['confdaora']

package_data = \
{'': ['*'], 'confdaora': ['tests/*']}

install_requires = \
['jsondaora']

extras_require = \
{'doc': ['mkdocs', 'mkdocs-material', 'markdown-include'],
 'test': ['black',
          'bumpversion',
          'flake8',
          'isort',
          'ipython',
          'mypy',
          'pytest-cov',
          'pytest-mock',
          'pytest>=5.1.1',
          'tox']}

setup(name='confdaora',
      version='0.2.1',
      description='confdaora',
      author='Diogo Dutra',
      author_email='diogodutradamata@gmai.com',
      url='https://github.com/dutradda/confdaora',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      extras_require=extras_require,
      python_requires='>=3.7',
     )
