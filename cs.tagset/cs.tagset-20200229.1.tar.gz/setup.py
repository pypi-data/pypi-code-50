#!/usr/bin/env python
from setuptools import setup
setup(
  name = 'cs.tagset',
  description = 'Tags and sets of tags.',
  author = 'Cameron Simpson',
  author_email = 'cs@cskk.id.au',
  version = '20200229.1',
  url = 'https://bitbucket.org/cameron_simpson/css/commits/all',
  classifiers = ['Programming Language :: Python', 'Programming Language :: Python :: 3', 'Development Status :: 4 - Beta', 'Intended Audience :: Developers', 'Operating System :: OS Independent', 'Topic :: Software Development :: Libraries :: Python Modules', 'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'],
  include_package_data = True,
  install_requires = ['cs.lex', 'cs.logutils', 'cs.pfx'],
  keywords = ['python3'],
  license = 'GNU General Public License v3 or later (GPLv3+)',
  long_description = '*Latest release 20200229.1*:\nInitial release: pull TagSet, Tag, TagChoice from cs.fstags for independent use.\n\nTags and sets of tags.\n\n## Class `Tag(Tag,builtins.tuple)`\n\nA Tag has a `.name` (`str`) and a `.value`.\n\nThe `name` must be a dotted identifier.\n\nA "bare" `Tag` has a `value` of `None`.\n\n## Class `TagChoice(TagChoice,builtins.tuple)`\n\nA "tag choice", an apply/reject flag and a `Tag`,\nused to apply changes to a `TagSet`\nor as a criterion for a tag search.\n\nAttributes:\n* `spec`: the source text from which this choice was parsed,\n  possibly `None`\n* `choice`: the apply/reject flag\n* `tag`: the `Tag` representing the criterion\n\n## Class `TagSet`\n\nA setlike class associating a set of tag names with values.\n\n### Method `TagSet.__init__(self, *, defaults=None)`\n\nInitialise the `TagSet`.\n\nParameters:\n* `defaults`: a mapping of name->`TagSet` to provide default values.\n\n\n\n# Release Log\n\n*Release 20200229.1*:\nInitial release: pull TagSet, Tag, TagChoice from cs.fstags for independent use.',
  long_description_content_type = 'text/markdown',
  package_dir = {'': 'lib/python'},
  py_modules = ['cs.tagset'],
)
