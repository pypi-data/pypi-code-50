#!/usr/bin/env python
from setuptools import setup
setup(
  name = 'cs.py3',
  description = 'Aids for code sharing between python2 and python3.',
  author = 'Cameron Simpson',
  author_email = 'cs@cskk.id.au',
  version = '20200229',
  url = 'https://bitbucket.org/cameron_simpson/css/commits/all',
  classifiers = ['Programming Language :: Python', 'Programming Language :: Python :: 2', 'Programming Language :: Python :: 3', 'Development Status :: 4 - Beta', 'Intended Audience :: Developers', 'Operating System :: OS Independent', 'Topic :: Software Development :: Libraries :: Python Modules', 'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'],
  include_package_data = True,
  install_requires = [],
  keywords = ['python2', 'python3'],
  license = 'GNU General Public License v3 or later (GPLv3+)',
  long_description = '*Latest release 20200229*:\nMinor fixes.\n\nAids for code sharing between python2 and python3.\n\nThis package presents various names in python 3 flavour for common use in\npython 2 and python 3.\n\n## Function `ustr(s, e=\'utf-8\', errors=\'strict\')`\n\nUpgrade string to unicode: no-op for python 3.\n\n\n\n# Release Log\n\n*Release 20200229*:\nMinor fixes.\n\n*Release 20190729*:\nAdd DEVNULL, which only arrived with 3.3.\n\n*Release 20190331*:\ncs.py3._for3.raise3: bugfix raise-with-traceback.\n\n*Release 20190108*:\nNew raise_from function to provide raise...from in py3 and plain raise in py2.\n\n*Release 20181108*:\nSmall import fix for pread.\n\n*Release 20180805*:\nImplement pread for systems lacking os.pread.\n\n*Release 20170903*:\nMake into a package subsuming cs.py3_for2 and cs.py3_for3.\nImplementation of struct.iter_unpack.\nMake bytes.__eq__ work with str for Python 2.\nNew name joinbytes for Python 2 and 3.\nBackports for Python 2.5.\n\n*Release 20160828*:\nUse "install_requires" instead of "requires" in DISTINFO.\n\n*Release 20160827*:\nMove python 2 and 3 specific code into cs.py3_for2 and cs.py3_for3.\nDo not bother with StringIO and BytesIO, modules can get them directly from the io module.\nRedo python 2 bytes class.\nPython3 compatible versions of struct.pack and struct.unpack.\n\n*Release 20150126*:\nbugfix py2 ustr()\n\n*Release 20150120*:\ncs.py3: add __contains__ to python 2 bytes type\n\n*Release 20150112*:\nRerelease with separate README.rst file.\n\n*Release 20150111*:\nustr: accept errors= parameter, default "strict"; update PyPI distinfo and arrangements\n\n*Release 20150103*:\ninitial release tag for cs.py3',
  long_description_content_type = 'text/markdown',
  package_dir = {'': 'lib/python'},
  packages = ['cs.py3'],
)
