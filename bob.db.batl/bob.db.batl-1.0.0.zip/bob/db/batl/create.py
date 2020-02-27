from __future__ import print_function
from glob import iglob
from sys import stderr
from os import path, makedirs, unlink
from json import load
from itertools import product

from sqlalchemy import or_, and_, not_

from bob.db.base.utils import session_try_nolock, create_engine_try_nolock

from .models import Base, ProtocolPurpose, Protocol, Client, VideoFile, RppgFile
from .batl_config import FILE_SPEC as FS, TYPE_LOOKUP as TL
from .generate_metadata import METADATA_PATH

def add_clients(session, data, verbose):
    client_set = set()
    filter_set = set()
    for fileinfo in data['files']:
        is_presenter = fileinfo[FS['type_id']]==0
        client_set.add((fileinfo[FS['client_id']], is_presenter))
        if is_presenter:
            filter_set.add((fileinfo[FS['client_id']], False))
    client_set.difference_update(filter_set)
    for client_info in client_set:
        client = Client(*client_info)
        if verbose > 0:
            print('adding {}'.format(client))
        session.add(client)
    
def add_files(session, data, verbose):
    """Add files to the database."""
    for fileinfo in data['files']:
        videofile = VideoFile(fileinfo[FS['path']], *fileinfo[:-2])
        if verbose > 0:
            print('adding {}'.format(videofile))
        rppg_path = fileinfo[FS['rppg_path']]
        if rppg_path != '':
            rppgfile = RppgFile(rppg_path)
            if verbose > 1:
                print('    with {}'.format(rppgfile))
            session.add(rppgfile)
            videofile.rppgfile = rppgfile
        session.add(videofile)

def add_protocols(session, data, verbose):
    def get_files(field, selector, is_real, exclude):
        def parse_exclusion_criteria(exclude):
            filter_exclude = []
            for (criteria, values) in exclude:
                if isinstance(values[0], list):
                    crit = parse_exclusion_criteria(values)
                else:
                    crit = getattr(VideoFile, values[0]).in_(values[1])
                filter_exclude.append(not_(and_(getattr(VideoFile, criteria[0]) == criteria[1], crit)))
            return or_(*filter_exclude)
        is_real_filter = VideoFile.type_id == TL['Bona Fide']
        is_real_filter = is_real_filter if is_real else not_(is_real_filter)
        flt = parse_exclusion_criteria(exclude)
        files = session.query(VideoFile)\
                       .filter(getattr(VideoFile, field).in_(selector))\
                       .filter(flt)\
                       .filter(is_real_filter)
        return files

    purposes = ProtocolPurpose.PURPOSES
    groups = ProtocolPurpose.GROUPS
    for protocol_name, protocol_description in data['protocols'].items():
        split_criteria = protocol_description['field']
        files = {group: {purpose: 
                         get_files(split_criteria, protocol_description[group], purpose == 'real',
                                   protocol_description['exclude'])
                         for purpose in purposes}
                 for group in groups}
        protocol = Protocol(protocol_name)
        session.add(protocol)
        if verbose > 0:
            print('adding {}'.format(protocol))
        for group, purpose in product(groups, purposes):
            protocol_purpose = ProtocolPurpose(group, purpose)
            protocol_purpose.protocol = protocol
            if verbose > 0:
                print('    with {}'.format(protocol_purpose))
            for f in files[group][purpose]:
                if verbose > 1:
                    print('        with {}'.format(f))
                protocol_purpose.files.append(f)
            session.add(protocol_purpose)

def create_tables(args):
    """Creates all necessary tables (only to be used at the first time)"""
    engine = create_engine_try_nolock(args.type, args.files[0], echo=(args.verbose > 2))
    Base.metadata.create_all(engine)

def create(args):
    """Creates or re-creates this database"""
    dbfile = args.files[0]

    if path.exists(dbfile):
        if args.recreate:
            if args.verbose > 0:
                print('unlinking %s...' % dbfile)
            unlink(dbfile)
    else:
        makedirs(path.dirname(dbfile), exist_ok=True)

# ALL THE WORK:
#----------------------------------------------------------------------------
    create_tables(args)
    s = session_try_nolock(args.type, dbfile, echo=(args.verbose > 2))
    with open(METADATA_PATH, 'r') as mf:
        metadata = load(mf)
    add_clients(s, metadata, args.verbose)
    add_files(s, metadata, args.verbose)
    add_protocols(s, metadata, args.verbose)
    s.commit()
    s.close()

def add_command(subparsers):
    """Add specific subcommands that the action "create" can use"""

    parser = subparsers.add_parser('create', help=create.__doc__)

    parser.add_argument('-R', '--recreate', action='store_true', help="If set, I'll first erase the current database")
    parser.add_argument('-v', '--verbose', action='count', default=0, help="Do SQL operations in a verbose way?")
    parser.add_argument('-D', '--datadir', metavar='DIR',
                        default='/idiap/project/batl/datasets/database-batl-idiap',
                        help="Change the relative path to the directory containing the images of the batl database.")
    parser.set_defaults(func=create) #action
