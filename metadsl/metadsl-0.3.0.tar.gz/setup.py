#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['metadsl']

package_data = \
{'': ['*']}

install_requires = \
['typing_extensions', 'typing_inspect', 'python-igraph>=0.8.0']

extras_require = \
{'dev': ['jupyterlab>=1.0.0', 'nbconvert', 'pudb', 'beni'],
 'doc': ['sphinx',
         'sphinx-autodoc-typehints',
         'sphinx_rtd_theme',
         'recommonmark',
         'nbsphinx',
         'ipykernel',
         'IPython',
         'sphinx-autobuild'],
 'test': ['pytest>=3.6.0',
          'pytest-cov',
          'pytest-mypy',
          'pytest-randomly',
          'pytest-xdist',
          'pytest-pudb',
          'mypy']}

setup(name='metadsl',
      version='0.3.0',
      description='Library to help create DSLs in Python.',
      author='Saul Shanabrook',
      author_email='s.shanabrook@gmail.com',
      url='https://github.com/Quansight-Labs/metadsl',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      extras_require=extras_require,
      python_requires='>=3.8',
     )
