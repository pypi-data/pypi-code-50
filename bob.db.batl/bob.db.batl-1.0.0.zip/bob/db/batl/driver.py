#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

import os
import sys
import argparse
import pkg_resources

from itertools import chain

from bob.db.base.driver import Interface as BaseInterface
from bob.db.base.utils import null

from .create import add_command as create_command
from .query import Database
from .generate_metadata import FILES_PATH, DIR_PATH

class Interface(BaseInterface):

  DB = Database()

  def name(self):
    return 'batl'

  def version(self):
    return pkg_resources.require('bob.db.%s' % self.name())[0].version

  def files(self):
      with open(FILES_PATH, 'r') as f:
        return [os.path.join(DIR_PATH, line.strip()) for line in f]

  def type(self):
    return 'sqlite'

  def add_commands(self, parser):


    subparsers = self.setup_parser(parser,
        "BATL database", __doc__)

    # example: get the "create" action from a submodule
    create_command(subparsers)


    # example: get the "dumplist" action from a submodule
    parser = subparsers.add_parser('dumplist', help=dumplist.__doc__)
    parser.add_argument('-d', '--directory', default='',   help="if given, this path will be added to every entry returned.")
    parser.add_argument('-e', '--extension', default='',   help="if given, this extension will be appended to every entry returned.")
    parser.add_argument('-p', '--protocol',
                        help="if given, limits the dump to a particular subset of the data that corresponds to the given protocol.",
                        choices=self.DB.protocol_names() if self.DB.is_valid() else ())
    parser.add_argument('-u', '--purpose',   help="if given, this value will limit the output files to those designed for the given purposes.",
                        choices=self.DB.purposes() if self.DB.is_valid() else ())
    parser.add_argument('-g', '--group',   help="if given, this value will limit the output files to those designed for the given group.",
                        choices=self.DB.groups() if self.DB.is_valid() else ())
    parser.add_argument('-s', '--session', type=int,
                        help="if given, this value will limit the output files to those acquired in a particular session.",
                        choices=self.DB.file_sessions() if self.DB.is_valid() else ())

    parser.add_argument('--self-test', dest="selftest", action='store_true', help=argparse.SUPPRESS)
    parser.set_defaults(func=dumplist) #action

    # the "checkfiles" action
    parser = subparsers.add_parser('checkfiles', help=checkfiles.__doc__)
    parser.add_argument('-d', '--directory', default='/idiap/project/batl/datasets/database-batl-idiap', help="if given, this path will be prepended to every entry returned.")
    parser.add_argument('-e', '--extension', default='.png', help="if given, this extension will be appended to every entry returned.")
    parser.add_argument('--self-test', dest="selftest", action='store_true', help=argparse.SUPPRESS)
    parser.set_defaults(func=checkfiles) #action

    # adds the "reverse" command
    parser = subparsers.add_parser('reverse', help=reverse.__doc__)
    parser.add_argument('path', nargs='+', type=str, help="one or more path stems to look up. If you provide more than one, files which cannot be reversed will be omitted from the output.")
    parser.add_argument('--self-test', dest="selftest", action='store_true', help=argparse.SUPPRESS)
    parser.set_defaults(func=reverse) #action

    # adds the "path" command
    parser = subparsers.add_parser('path', help=path.__doc__)
    parser.add_argument('-d', '--directory', default='/idiap/project/batl/datasets/database-batl-idiap/', help="if given, this path will be added to every entry returned.")
    parser.add_argument('-e', '--extension', default='.h5', help="if given, this extension will be appended to every entry returned.")
    parser.add_argument('id', nargs='+', type=int, help="one or more file ids to look up. If you provide more than one, files which cannot be found will be omitted from the output. If you provide a single id to lookup, an error message will be printed if the id does not exist in the database. The exit status will be non-zero in such case.")
    parser.add_argument('--self-test', dest="selftest", action='store_true', help=argparse.SUPPRESS)
    parser.set_defaults(func=path) #action

def dumplist(args):
  """Dumps lists of files based on your criteria"""

  db = Database()
  print (args)

  r = db.objects(
            protocol      = args.protocol,
            groups        = args.group,
            purposes      = args.purpose,
            sessions      = args.session)
  output = sys.stdout

  if args.selftest:
    output = null()

  for f in r:
    output.write('%s\n' % (f.make_path(args.directory, args.extension),))

  return 0

def checkfiles(args):
  """Checks existence of files based on your criteria"""

  db = Database()

  r = db.objects()

  # go through all files, check if they are available on the file system
  good = []
  bad = []
  for f in r:
    if os.path.exists(f.make_path(args.directory, args.extension)):
      good.append(f)
    else:
      bad.append(f)

  # report
  output = sys.stdout
  if args.selftest:
    output = null()

  if bad:
    for f in bad:
      output.write('Cannot find file "%s"\n' % (f.make_path(args.directory, args.extension),))
    output.write('%d files (out of %d) were not found at "%s"\n' % \
      (len(bad), len(r), args.directory))

  return 0

def reverse(args):
  """Returns a list of file database identifiers given the path stems"""

  db = Database()

  output = sys.stdout
  if args.selftest:
    output = null()
  try:
      r = db.reverse(args.path)
  except KeyError as err:
    raise DatabaseError("One or more of the input paths wasn't found - original error message:\nKeyError: {}".format(err))

  for f in r: output.write('%d\n' % f.id)

  if not r: return 1

  return 0

def path(args):
  """Returns a list of fully formed paths or stems given some file id"""

  db = Database()

  output = sys.stdout
  if args.selftest:
    output = null()

  r = db.paths(args.id, prefix=args.directory, suffix=args.extension)
  for path in r: output.write('%s\n' % path)

  if not r: return 1

  return 0


