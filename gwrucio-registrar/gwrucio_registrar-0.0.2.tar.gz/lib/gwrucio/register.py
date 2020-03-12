# Copyright (C) 2018  James Alexander Clark <james.clark@ligo.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""Methods and classes for data registration.
"""

# Native
import copy
import os
import sys
import logging
import time
import requests
import gfal2

# Rucio
from rucio.client.client import Client
from rucio.client.uploadclient import UploadClient
from rucio.common.config import config_get
from rucio.common.exception import (DataIdentifierAlreadyExists,
                                    FileAlreadyExists, RSEBlacklisted,
                                    InputValidationError)
from rucio.common.utils import generate_uuid
import rucio.rse.rsemanager as rsemgr
from rucio.rse.protocols.protocol import RSEDeterministicTranslation

SUCCESS = 0
FAILURE = 1


def gfal_md5(pfn):
    """
    Compute the MD5 checksum of a file using GFAL2.

    :param pfn: Physical filename, including protocol and hostname
    :type pfn: str
    :returns: str. The MD5 checksum
    """
    ctxt = gfal2.creat_context()
    return ctxt.checksum(pfn, 'MD5')


def gfal_adler32(pfn):
    """
    Compute the Adler32 checksum of a file using GFAL2.

    :param pfn: Physical filename, including protocol and hostname
    :type pfn: str
    :returns: str. The adler32 checksum
    """
    ctxt = gfal2.creat_context()
    return ctxt.checksum(pfn, 'Adler32')


def gfal_stat(pfn):
    """
    Stat a file.

    :param pfn: Physical filename, including protocol and hostname
    :type pfn: str
    :returns: class gfal2.Stat. GFAL2 stat object.
    """
    ctxt = gfal2.creat_context()
    return ctxt.stat(pfn)


def gfal_bytes(pfn):
    """
    Compute the size in bytes of a file.

    :param pfn: Physical filename, including protocol and hostname
    :type pfn: str
    :returns: int. The size in bytes
    """
    return gfal_stat(pfn).st_size


def convert_file_for_api(filemd):
    """
    Creates a new dictionary that contains only the values that are needed
    for the upload with the correct keys (Taken from `uploadclient.py`)

    :param file: dictionary describing a file to upload

    :returns: dictionary containing not more then the needed values for the
    upload
    """
    replica = {}
    replica['scope'] = filemd['did_scope']
    replica['name'] = filemd['did_name']
    replica['bytes'] = filemd['bytes']
    replica['adler32'] = filemd['adler32']
    replica['md5'] = filemd['md5']
    replica['meta'] = filemd['meta']
    replica['state'] = filemd['state']
    pfn = filemd.get('pfn')
    if pfn:
        replica['pfn'] = pfn
    return replica


def get_rse_pfn(rse_info, scope, name):
    """
    Return the PFN at this RSE

    Parameters
    ----------
    rse_info : dict
        Protocol related RSE attributes.  See
        `rucio/lib/rucio/rse/rsemanager.py`.
    scope : str
        Scope for the DID
    name : str
        filename of the DID
    """

    protocol = rse_info['protocols'][0]
    schema = protocol['scheme']
    prefix = protocol['prefix']
    port = protocol['port']
    rucioserver = protocol['hostname']

    lfn2pfn_translator = RSEDeterministicTranslation(rse=rse_info['rse'])

    if schema == 'srm':
        prefix = protocol['extended_attributes']['web_service_path'] + prefix
    uri = schema + '://' + rucioserver
    if port != 0:
        uri += ':' + str(port)

    path = os.path.join(prefix, lfn2pfn_translator.path(scope=scope,
                                                        name=name))

    pfn = uri + path

    return pfn, path


class DataSetInjector:
    """
    General Class for injecting a LIGO dataset in rucio

    1) Load list of files for dataset from text file OR diskcache object
    2) Get their checksums
    2) Convert frame names to rucio DIDs
    3) Create Rucio dataset
    4) Register Rucio dataset

    data is a dictionary with a list of files to register
    """

    # pylint: disable=too-many-instance-attributes,too-many-arguments

    def __init__(self,
                 rse_info,
                 dataset_name,
                 data,
                 allow_uploads=False,
                 logger=None):

        if not logger:
            logger = logging.getLogger('%s.null' % __name__)
            logger.disabled = True
        self.logger = logger

        # Check rucio server connection
        try:
            requests.get(config_get('client', 'rucio_host'))
        except requests.exceptions.RequestException as exe:
            self.logger.error(exe)
            sys.exit(FAILURE)

        # Dataset configuration
        self.scope = data['scope']
        self.dataset_name = dataset_name
        try:
            self.lifetime = data['lifetime']
        except KeyError:
            self.lifetime = None

        self.rse_info = rse_info
        self.allow_uploads = allow_uploads
        self.client = Client(rucio_host=config_get('client', 'rucio_host'))

        # Read and attach list of file attributes:
        # (filename, adler32, md5, bytes)
        # If file is not found, continue to compute attributes on the fly
        try:
            self.fileinfos = data['fileinfos']
            self.logger.info("Using pre-computed file sizes and checksums")
        except KeyError:
            self.logger.info("Computing file sizes and checksums on the fly")

        # Support lists OR diskcache for files
        try:
            # Treat data as a diskcache, fall back to list on failure
            files = list(data['diskcache'].expand())
        except KeyError:
            files = data['filelist'][:]

        # Get dictionary of files and metadata to register
        self._enumerate_uploads(files)

    def _create_dataset(self):
        """
        Add a dataset object to contain the files we're registering
        """
        logger = self.logger
        try:
            # Add rule in here if DID does not exist
            logger.info("Trying to create dataset: %s", self.dataset_name)
            self.client.add_dataset(scope=self.scope,
                                    name=self.dataset_name,
                                    rules=[{
                                        'account': self.client.account,
                                        'copies': 1,
                                        'rse_expression': self.rse_info['rse'],
                                        'grouping': 'DATASET',
                                        'lifetime': self.lifetime
                                    }])
            logger.info('Created new dataset %s', self.dataset_name)
        except RSEBlacklisted:
            logger.warning(
                'RSE write blacklisted, not adding replication rule')
            self.client.add_dataset(scope=self.scope, name=self.dataset_name)
            logger.info('Created new dataset %s', self.dataset_name)
        except DataIdentifierAlreadyExists:
            logger.debug("Dataset %s already exists", self.dataset_name)

    def _check_replica(self, lfn):
        """
        Check if a replica of the given file at the site already exists in the
        catalog.

        :param lfn: Logical filename to check
        :type lfn: str
        :returns bool: True if file exists in catalog
        """
        logger = self.logger
        logger.debug("Checking catalog for replica %s:%s at %s", self.scope,
                     lfn, self.rse_info['rse'])
        replicas = list(
            self.client.list_replicas([{
                'scope': self.scope,
                'name': lfn
            }]))

        if replicas:
            replicas = replicas[0]
            if 'rses' in replicas:
                if self.rse_info['rse'] in replicas['rses']:
                    logger.debug("%s:%s already has a replica at %s",
                                 self.scope, lfn, self.rse_info['rse'])
                    return True

        return False

    def _enumerate_uploads(self, files):
        """
        Create a list of dictionaries which describe files to pass to the rucio
        UploadClient
        """
        logger = self.logger
        items = list()

        for filename in files:

            pfn, path = get_rse_pfn(self.rse_info, self.scope,
                                    os.path.basename(filename))

            dataset_did_str = ('%s:%s' % (self.scope, self.dataset_name))
            items.append({
                'path': path,
                'pfn': pfn,
                'rse': self.rse_info['rse'],
                'did_scope': self.scope,
                'did_name': os.path.basename(path),
                'dataset_scope': self.scope,
                'dataset_name': self.dataset_name,
                'dataset_did_str': dataset_did_str,
                'force_scheme': None,
                'no_register': False,
                'register_after_upload': True,
                'lifetime': self.lifetime,
                'transfer_timeout': None
            })

        # check given sources, resolve dirs into files, and collect meta infos
        logger.info("Checking file integrity")
        then = time.time()
        self.files = self._collect_and_validate_file_info(items)
        logger.info("File integrity check took %.2fs", (time.time() - then))

    def _collect_and_validate_file_info(self, items):
        """
        Checks if there are any inconsistencies within the given input options
        and stores the output of _add_metadata for every file (Adapted
        from `uploadclient.py`)

        :param filepath: list of dictionaries with all input files and options

        :returns: a list of dictionaries containing all descriptions of the
        files to upload

        :raises InputValidationError: if an input option has a wrong format
        """
        logger = self.logger
        files = []
        for item in items:

            path = item.get('path')
            pfn = item.get('pfn')

            if not self._check_replica(os.path.basename(path)):

                logger.debug('Getting metadata for: %s', pfn)

                # Is this required?
                if pfn:
                    item['force_scheme'] = pfn.split(':')[0]

                # Check file exists
                try:
                    gfal_stat(pfn)
                except gfal2.GError as gfalerr:
                    logger.critical(gfalerr)
                    logger.critical('Could not access file: %s', pfn)
                    sys.exit(FAILURE)

                filemd = self._add_metadata(item)
                files.append(filemd)

            if not files:
                raise InputValidationError('No valid input files given')

        return files

    def _add_metadata(self, item):
        """
        Collects infos (e.g. size, checksums, etc.) about the file and returns
        them as a dictionary (Adapted from `uploadclient.py`)

        :param item: input options for the given file
        :type item: dict

        :returns: a dictionary containing all collected info and the input
        options
        """
        logger = self.logger

        item['dirname'] = os.path.dirname(item.get('path'))
        item['basename'] = os.path.basename(item.get('path'))

        # Try getting file info from fileinfos dict
        try:
            # Try getting file info from fileinfos dict
            item['bytes'] = self.fileinfos[item['path']].get('bytes')
            item['adler32'] = self.fileinfos[item['path']].get('adler32')
            item['md5'] = self.fileinfos[item['path']].get('md5')
        except AttributeError:
            # Compute file infos on the fly
            item['bytes'] = gfal_bytes(item.get('pfn'))
            then = time.time()
            item['adler32'] = gfal_adler32(item.get('pfn'))
            duration = time.time() - then
            logger.debug('Adler32 checksum took %fs', duration)
            then = time.time()
            item['md5'] = gfal_md5(item.get('pfn'))
            duration = time.time() - then
            logger.debug('MD5 checksum took %fs', duration)
        item['meta'] = {'guid': generate_uuid()}
        item['state'] = 'A'

        return item

    def upload_file(self, filemd):
        """
        Upload file to RSE
        """
        # instantiate upload client for files not present
        upload_client = UploadClient(self.client, self.logger)

        #  Remove PFN so that `upload_client` registers file for us
        filemd_tmp = copy.deepcopy(filemd)
        filemd_tmp['pfn'] = None
        upload_client.upload([filemd_tmp])

    def add_files(self):
        """
        Add files replicas in rucio catalog

        """

        logger = self.logger
        then = time.time()

        # Create dataset
        self._create_dataset()

        # Register files and attach to dataset
        for filemd in self.files:
            logger.info("Adding %s to catalog", filemd['did_name'])

            if self.allow_uploads:
                # Test for file existence at end-point
                file_exists = rsemgr.exists(self.rse_info, filemd['pfn'])
            else:
                file_exists = True

            if not self._check_replica(filemd['did_name']) or not file_exists:
                # IF not in catalog OR doesn't exist on the RSE, test for
                # upload and re-catalog

                if not file_exists:
                    # File does not exist at RSE so upload it
                    logger.info("%s not found at %s, beginning upload",
                                self.rse_info['rse'], filemd['did_name'])
                    self.upload_file(filemd)

                else:
                    # Register replica
                    logger.debug("File %s already exits at RSE",
                                 filemd['did_name'])
                    replica_for_api = convert_file_for_api(filemd)

                    if self.client.add_replicas(rse=self.rse_info['rse'],
                                                files=[replica_for_api]):
                        logger.debug("File %s registered", filemd['did_name'])

                    # Attach to dataset
                    try:
                        logger.debug("Attaching file %s to dataset %s",
                                     filemd['did_name'], self.dataset_name)

                        self.client.attach_dids(scope=self.scope,
                                                name=self.dataset_name,
                                                dids=[{
                                                    'scope':
                                                    self.scope,
                                                    'name':
                                                    filemd['did_name']
                                                }])
                    except FileAlreadyExists:
                        logger.debug("File %s already exists in dataset %s",
                                     filemd['did_name'], self.dataset_name)

        if self.files:
            logger.info('File registration took %fs', (time.time() - then))
