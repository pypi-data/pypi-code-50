#!/usr/bin/env python
from setuptools import setup
setup(
  name = 'cs.upd',
  description = 'Single line status updates with minimal update sequences.',
  author = 'Cameron Simpson',
  author_email = 'cs@cskk.id.au',
  version = '20200229',
  url = 'https://bitbucket.org/cameron_simpson/css/commits/all',
  classifiers = ['Programming Language :: Python', 'Programming Language :: Python :: 2', 'Programming Language :: Python :: 3', 'Development Status :: 4 - Beta', 'Intended Audience :: Developers', 'Operating System :: OS Independent', 'Topic :: Software Development :: Libraries :: Python Modules', 'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'],
  include_package_data = True,
  install_requires = ['cs.lex', 'cs.tty'],
  keywords = ['python2', 'python3'],
  license = 'GNU General Public License v3 or later (GPLv3+)',
  long_description = '*Latest release 20200229*:\nUpd: can now be used as a context manager, clearing the line on exit.\nUpd.without is now a context manager, returning the older state, and accepting an optional inner state (default "").\nUpd is now a singleton factory, obsoleting upd_for.\nUpd.nl: use "insert line above" mode if supported.\n\nSingle line status updates with minimal update sequences.\n\nThis is available as an output mode in `cs.logutils`.\n\nExample:\n\n    with Upd() as U:\n        for filename in filenames:\n            U.out(filename)\n            ... process filename ...\n            upd.nl(\'an informational line\')\n\n## Function `cleanupAtExit()`\n\nCleanup function called at programme exit to clear the status line.\n\n## Function `Upd(stream)`\n\nFactory for `Upd` singletons keyed by the id of their backend.\n\n## Function `upd_for(stream)`\n\nFactory for `Upd` singletons keyed by the id of their backend.\n\n\n\n# Release Log\n\n*Release 20200229*:\nUpd: can now be used as a context manager, clearing the line on exit.\nUpd.without is now a context manager, returning the older state, and accepting an optional inner state (default "").\nUpd is now a singleton factory, obsoleting upd_for.\nUpd.nl: use "insert line above" mode if supported.\n\n*Release 20181108*:\nDocumentation improvements.\n\n*Release 20170903*:\nNew function upd_for(stream) returning singleton Upds.\nDrop noStrip keyword argument/mode - always strip trailing whitespace.\n\n*Release 20160828*:\nUse "install_requires" instead of "requires" in DISTINFO.\nAdd Upd.flush method.\nUpd.out: fix longstanding trailing text erasure bug.\nUpd.nl,out: accept optional positional parameters, use with %-formatting if supplied, just like logging.\n\n*Release 20150118*:\nmetadata fix\n\n*Release 20150116*:\nInitial PyPI release.',
  long_description_content_type = 'text/markdown',
  package_dir = {'': 'lib/python'},
  py_modules = ['cs.upd'],
)
