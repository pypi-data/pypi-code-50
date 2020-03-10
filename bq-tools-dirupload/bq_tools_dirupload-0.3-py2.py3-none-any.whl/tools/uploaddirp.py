#!/usr/bin/env python
from __future__ import unicode_literals
from __future__ import print_function
from builtins import input
from builtins import range
from future import standard_library
standard_library.install_aliases()

import os
import sys
import signal
import re
import csv
import fnmatch
import argparse
import logging
import random

import string
import urllib3
import configparser
import time
import traceback
import posixpath
from itertools import zip_longest
from collections import OrderedDict

try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree

import bqapi
from .pool import ProcessManager

# def bisque_session(args):
#     "Get a bisque session"
#     user = None
#     password = None
#     root = None
#     if args.bisque_host:
#         root = args.bisque_host
#     if args.credentials:
#         user,password = args.credentials.split(':')
#     elif os.path.exists (os.path.expanduser(args.config)):
#         parser = configparser.ConfigParser ()
#         parser.read (os.path.expanduser(args.config))
#         if root is None:
#             root = parser.get (args.profile, 'host')
#         user = parser.get (args.profile, 'user')
#         password = parser.get (args.profile, 'password')
#     if not (root and user and password):
#         config = configparser.RawConfigParser()
#         print ("Please configure how to connect to bisque")
#         root = input("BisQue URL e.g. https://data.viqi.org/: ")
#         user = input("username: ")
#         password = input("password: ")
#         config_file = os.path.expanduser (args.config)
#         os.makedirs(os.path.dirname(config_file))
#         with open (config_file, 'wb') as conf:
#             config.add_section (args.profile)
#             config.set(args.profile, 'host', root)
#             config.set(args.profile, 'user', user)
#             config.set(args.profile, 'password', password)
#             config.write (conf)
#             print ("configuration has been saved to", args.config)

#     if root and user and password:
#         session =   bqapi.BQSession()
#         urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#         session.c.verify = False
#         session = session.init_local(bisque_root=root,  user = user, pwd=password, create_mex=False)
#         if not args.quiet:
#             print  ("Sending uploads to ", root, " for user ", user)
#         return session
#     print ("Could not create bisque session with root={} user={} pass={}".format(root, user, password))
#     return None

def send_image_to_bisque(session, args, image_path, tagmap=None, tagtable=None):
    "Send one image to bisque"

    # Strip off top level dirs .. except user given root
    filename = os.path.basename (image_path)
    original_image_path = image_path
    image_path = image_path[len(posixpath.dirname(args.directory))+1:]

    ################
    # Skip pre-existing resources with same filename
    if args.skip:
        data_service   = session.service('data_service')
        response = data_service.get(params={ 'name': filename }, render='xml')
        if len(response) and  response[0].get ('name') == filename:
            args.log.info ("skipping %s", filename)
            return None
    ###################
    # build argument tags into upload xml
    tags  = etree.Element ('image', name=image_path)
    tagdict = {}
    # add any fixed arguments
    for tag,value in [ x.split(':') for x in args.tag ]:
            etree.SubElement (tags, 'tag', name=tag, value = value)
    # path elements can be made tags (only match directory portion)
    if args.path_tags:
        for tag,value in zip_longest (args.path_tags, image_path.split ('/')[-1]):
            if tag  and value :
                #etree.SubElement (tags, 'tag', name=tagmap.get(tag, tag), value = tagmap.get(value, value))
                tagdict [tag] =  value
                #tagdict [tagmap.get(tag, tag)] =  tagmap.get(value, value)
    ###################
    # RE over the filename
    if args.re_tags:
        matches = args.re_tags.match (filename)
        if matches:
            for tag, value in matches.groupdict().items():
                if tag  and value :
                    #etree.SubElement (tags, 'tag', name=tagmap.get (tag, tag), value = tagmap.get (value, value))
                    #tagdict [tagmap.get(tag, tag)] =  tagmap.get(value, value)
                    tagdict [tag] =  value
        elif args.re_only:
            args.log.info ("Skipping %s: does not match re_tags", filename)
            return None
        else:
            args.log.warn ("RE did not match %s", filename)
    ######################
    # Add fixed tags based on associated tagtable
    if tagtable:
        #  tag
        key = None
        if args.tagkey == 'filename':
            key = filename
        if args.tagkey == 'image_path':
            key = image_path
        if args.tagkey in tagdict:
            key = tagdict[args.tagkey]
        args.log.debug ("tagtable %s", key)
        if key is not None:
            if key not in tagtable:
                args.log.warn ("Key %s : %s was not present in tagtable", args.tagkey, key)
            else:
                for tag,value in tagtable[key].items():
                    tagdict[tag]=value
    # Special geotag processing
    geo = {}
    for tag,value in tagdict.items():
        if tag in ('lat', 'latitude'):
            geo['latitude'] = value
            del tagdict[tag]
        if tag in ('alt', 'altitude'):
            geo['altitude'] = value
            del tagdict[tag]
        if tag in ('long', 'longitude'):
            geo['longitude'] = value
            del tagdict[tag]
    if geo:
        geotags = etree.SubElement (tags, 'tag', name='Geo')
        coords  = etree.SubElement (geotags, 'tag', name = 'Coordinates')
        center  = etree.SubElement (coords, 'tag', name = 'center')
        for tag,val in geo.items():
            etree.SubElement(center, 'tag', name=tag, value = val)
    #######
    # fold duplicates and move tags to xml
    tagdict = { tagmap.get(tag,tag):tagmap.get(value,value) for tag,value in tagdict.items() }
    for tag,value in tagdict.items():
        if tag and value:
            etree.SubElement (tags, 'tag', name=tagmap.get (tag, tag), value = tagmap.get (value, value))
    xml = etree.tostring(tags)

    ################
    # Prepare to upload
    if args.debug:
        args.log.debug ("upload %s with xml %s ", image_path, xml)

    import_service = session.service('import')
    if not args.dry_run :
        with open (original_image_path, 'rb') as fileobj:
            response = import_service.transfer(image_path, fileobj = fileobj, xml = xml, render='xml')
    else:
        # Return a dry_run response
        response = etree.Element ('resource')
        etree.SubElement (response, 'image', name=image_path,
                          resource_uniq = '00-%s' % ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)),
                          value = image_path)
    if not args.quiet:
        args.log.info ("Uploaded %s with %s", image_path, tagdict)
    return response



SUCCESS=[]
ERROR = []
SKIPPED = []
UNIQS = []

def append_result_list (request):
    SUCCESS.append (request)
    resource = request['return_value']
    UNIQS.append (resource[0].get ('resource_uniq'))


def append_error_list (request):
    ERROR.append (request)
    if request.get ('return_value') is None:
        SKIPPED.append (request)
        return
    args = request['args'][1]
    if request.get ('return_value'):
        args.log.error ("return value %s", etree.tostring (request['return_value']))



DEFAULT_CONFIG='~/bisque/config' if os.name == 'nt' else "~/.bisque/config"



DOC_EPILOG="""
bq-dirupload -n  --threads 1 --re-tags "(?P<photo_site_code>\w+)_(?P<target_assemblage>\D+)(?P<plot>\d+)_(?P<season>\D+)(?P<year>\d+).+\.JPG" --dataset upload --tagmap @speciesmap.csv --tagmap @locationmap.csv --tagmap fa=fall --tagmap 15=2015 --tagtable photo_code_reference_2019_0912.csv --tagkey photo_site_code

 Magic decoder ring:
    -n : dry run
    --threads 1: one thread for debugging
    --retags :   use filename to create tags: photo_site_code, target_assemblage, season and year.
    --dataset : create a dataset "upload"
    --tagmap @speciesmap.csv: use value ins speciesmap.csv to rename tag/values for target_assemblage
    --tagmap @locationmap: Use location map to rename tag/value from phto_site_code
    --tagmap fa=fall : rename season 'fa' to 'fall'
    --tagmap 15=2015 : remame year from '15' to 2015
    --tagtable photo_code... :   table of fixed tag data keyed by --tagkey
    --tagkey   photo_site_code:  use photo_site_code to key into tagtable to read extra tags

"""

def main():
    parser = bqapi.cmd.bisque_argument_parser ("Upload files to bisque", formatter_class=argparse.RawDescriptionHelpFormatter, epilog = DOC_EPILOG)
    parser.add_argument('--tag', help="fixed name:value pair. Any number allow", action="append", default=[])
    parser.add_argument('--path-tags', help='tag names for a parsible path i.e. /project/date/subject/', default="")
    parser.add_argument('--re-tags', help=r're expressions for tags i.e. (?P<location>\w+)--(?P<date>[\d-]+)')
    parser.add_argument('--re-only', help=r'Accept files only if match re-tags', default = False, action="store_true")
    parser.add_argument('--include', help='shell expression for files to include. Can be repeated', action="append", default=[])
    parser.add_argument('--exclude', help='shell expression for files to exclude. Can be repeated', action="append", default=[])
    parser.add_argument('--dataset', help='create dataset and add files to it', default=None)
    parser.add_argument('--threads', help='set number of uploader threads', default=8)
    parser.add_argument("-s", '--skip', help="Skip upload if there is file with the same name already present on the server", action='store_true')
    parser.add_argument("--tagmap", action="append", default=[], help="Supply a map tag/value -> tag/value found in tag path and re decoder.  carp=carpenteria or @tagmap.csv")
    parser.add_argument("--tagtable", help="Table of fixed tags to add to resource: First column is key ")
    parser.add_argument("--tagkey", help="Used with tagtable can be filename, image_path or any extracted tag", default='filename')
    parser.add_argument('directories', help='director(ies) to upload', default=[], nargs='*' )

    session, args = bqapi.cmd.bisque_session(parser=parser)
    if session is None:
        print("Failed to create session.. check credentials")
        sys.exit(1)

    args.log = logging.getLogger("bq.uploader")
    args.log.debug (args)
    args.path_tags = args.path_tags.split ('/')
    if args.re_tags:
        args.re_tags = re.compile (args.re_tags, flags = re.IGNORECASE)
    tagtable = {}
    if args.tagtable and args.tagtable.endswith('.csv'):
        with open (args.tagtable, 'rb') as csvfile:
            reader = csv.reader (csvfile)
            fieldnames = next(reader)
            keyfield = fieldnames[0]
            fieldnames = fieldnames[1:]
            for row in  reader:
                # grab value of first columner and use as key for the rest of the values.
                tagtable[row[0]] = OrderedDict (zip_longest (fieldnames, row[1:]))

    # load tag map items (mapping certain values from filename/path to full values)
    tagitems = {}
    for entry in args.tagmap:
        if entry.startswith('@'):
            with open (entry[1:], 'rb') as csvfile:
                tagitems.update ( (row[0].strip(), row[1].strip()) for row in csv.reader(csvfile))
            continue
        tagitems.update (  [ entry.split('=') ] )

    # Start workers with default arguments
    manager = ProcessManager(limit=int(args.threads), workfun = send_image_to_bisque,
                              is_success = lambda r: r is not None and r[0].get ('name'),
                              on_success = append_result_list,
                              on_fail    = append_error_list)
    # helper function to add a list of paths
    def add_files(files):
        for f1 in files:
            if args.include and not any (fnmatch.fnmatch (f1, include) for include in args.include):
                args.log.info ("Skipping %s: not included", f1)
                continue
            if args.exclude and any (fnmatch.fnmatch (f1, exclude) for exclude in args.exclude):
                args.log.info ("Skipping %s: excluded", f1)
                continue
            manager.schedule ( args = (session, args, f1, tagitems, tagtable))

    # Add files to work queue
    try:
        for directory in args.directories:
            args.directory = os.path.abspath(os.path.expanduser (directory))
            #args.directory = os.path.normpath(os.path.expanduser (directory))
            if os.path.isdir(args.directory):
                for root, dirs, files in os.walk (args.directory):
                    root = root.replace ('\\', '/')
                    #print ("In ", root, dirs, files, " Prefix DIR ", args.directory)
                    add_files (os.path.join (root, f1) for f1 in files)
            elif os.path.isfile (args.directory):
                 add_files ([args.directory])
            else:
                args.log.error ("argument %s was neither directory or file",args.directory)

        # wait for all workers to stop
        while manager.isbusy(): # wait while queue has work
            time.sleep(1)
        manager.stop() # wait for worker to finish

    except (KeyboardInterrupt, SystemExit) as e:
        print ("TRANSFER INTERRUPT")
        manager.kill()
        #manager.stop()

    # Store output dataset
    if args.dataset and UNIQS:
        datasets = session.service('dataset_service')
        if args.debug:
            args.log.debug ('create dataset %s with %s', args.dataset, UNIQS)
        if not args.dry_run:
            dataset = datasets.create (args.dataset, UNIQS)
            if args.debug:
                args.log.debug ('created dataset %s', etree.tostring(dataset) )
    if args.debug:
        for S in SUCCESS:
            args.log.debug ('success %s', S)
        for E in ERROR:
            args.log.debug ('failed %s', E)
            if 'with_exception' in E:
                traceback.print_exception (E['with_exc_type'], E['with_exc_val'], E['with_exc_tb'])
    if not args.quiet:
        print ("Successful uploads: ", len (SUCCESS))
        print ("Failed uploads:", len (ERROR))
        print ("Skipped uploads:", len (SKIPPED))

if __name__ == "__main__":
    main()
