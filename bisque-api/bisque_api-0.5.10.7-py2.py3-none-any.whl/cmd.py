#!/usr/bin/env python
from __future__ import unicode_literals
from __future__ import print_function
from builtins import input
from future import standard_library
standard_library.install_aliases()

import os
import sys
import signal
import re
import fnmatch
import argparse
import logging
import random
import string
import urllib3
import configparser
import time


DEFAULT_CONFIG='~/bisque/config' if os.name == 'nt' else "~/.bisque/config"

def bisque_argument_parser(*args, **kw):
    parser = argparse.ArgumentParser(*args, **kw)
    parser.add_argument('-c', '--config', help='bisque config', default=DEFAULT_CONFIG)
    parser.add_argument('--profile', help="Profile to use in bisque config", default='default')
    parser.add_argument('-n', '--dry-run', action="store_true", help='report actions w/o changes', default=False)
    parser.add_argument('-d', '--debug',  nargs='?', help='set debug level: debug,info,warn,error' )
    parser.add_argument('-q', '--quiet', action="store_true", help='print actions ', default=False)
    parser.add_argument('-a', '--credentials', help= "A bisque login.. admin ", default=None)
    parser.add_argument('--bisque-host', help = "Default bisque server to connect to ")
    # Local arguments
    return parser

def bisque_session(parser=None, args=None, root_logger = None):
    """Get a bisque session for command line tools using arguments and ~/.bisque/config files

    Usage:
    parser = bisque_argument_parser ("MyCommand")
    parser.add_argument ('newarg', help='any specific argument')
    args = parser.parse_args()
    session = bisque_session(args)

    ~/.bisque/config:
    [default]
    host=
    user=
    password=

    [testing]
    host=
    user=
    password=
    """
    user =  password =  root =  config = None
    if parser is None:
        parser = bisque_argument_parser()
    pargs = parser.parse_args (args = args)
    config = configparser.SafeConfigParser ()
    if os.path.exists (os.path.expanduser(pargs.config)):
        config.read (os.path.expanduser(pargs.config))
        try:
            root = config.get (pargs.profile, 'host')
            user = config.get (pargs.profile, 'user')
            password = config.get (pargs.profile, 'password')
        except configparser.NoSectionError:
            pass
    if pargs.bisque_host:
        root = pargs.bisque_host
    if pargs.credentials:
        user,password = pargs.credentials.split(':')
    if not (root and user and password):
        print ("Please configure how to connect to bisque with profile {}".format (pargs.profile))
        root = input("BisQue URL [{}] ".format (root)) or root
        user = input("username[{}] ".format (user)) or user
        password = input("password[{}]: ".format(password)) or password
        config_file = os.path.expanduser (pargs.config)
        if not os.path.isdir (os.path.dirname(config_file)):
            os.makedirs(os.path.dirname(config_file))
        with open(config_file, 'wb') as conf:
            config.add_section (pargs.profile)
            config.set(pargs.profile, 'host', root)
            config.set(pargs.profile, 'user', user)
            config.set(pargs.profile, 'password', password)
            config.write(conf)
            print ("configuration has been saved to", pargs.config)

    if pargs.debug:
        logging.captureWarnings(True)
        if root_logger is None:
            logging.basicConfig(level=logging.DEBUG)
            root_logger = logging.getLogger()
        root_logger.setLevel ({'debug':logging.DEBUG, 'info':logging.INFO,'warn':logging.WARN,'error':logging.ERROR}.get (pargs.debug.lower(), logging.DEBUG))


    if root and user and password:
        import urllib3
        from .comm import BQSession
        session =   BQSession()
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        session.c.verify = False
        session = session.init_local(bisque_root=root,  user = user, pwd=password, create_mex=False)
        if not pargs.quiet:
            print  ("Session for  ", root, " for user ", user, " created")
        if session is None:
            print ("Could not create bisque session with root={} user={} pass={}".format(root, user, password))
    return session, pargs
