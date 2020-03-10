
import sys
import getopt
import os
import platform
import logging
import urllib.parse
import json
from operator import itemgetter
from datetime import datetime, timezone
from tempfile import mkstemp
from typing import Dict, List, Tuple, Union
import requests
import dateutil.parser
import spacepy.datamodel as spdm       # type: ignore
from cdasws import CdasWs, TimeInterval


ENDPOINT = 'https://cdaweb.sci.gsfc.nasa.gov/WS/cdasr/1/dataviews/sp_phys/'
#ENDPOINT = 'https://cdaweb-dev.sci.gsfc.nasa.gov/WS/cdasr/1/dataviews/sp_phys/'
#ENDPOINT = 'https://cdaweb-tmp.sci.gsfc.nasa.gov/WS/cdasr/1/dataviews/sp_phys/'
#ENDPOINT = 'https://cdaweb-su.sci.gsfc.nasa.gov/WS/cdasr/1/dataviews/sp_phys/'
#CA_CERTS = '/etc/pki/ca-trust/extracted/openssl/ca-bundle.trust.crt'


def print_usage(name: str) -> None:
    """
    Prints program usage information to stdout.

    Returns
    -------
    None
    """
    print('USAGE: %s [-e url][-c cacerts][-h]', name)
    print('WHERE: url = CDAS web service endpoint URL')
    print('       cacerts = CA certificate filename')


def example(argv: List[str]) -> None:
    """
    Example Coordinate Data Analysis System (CDAS) web service client.
    Includes example calls to most of the web services.

    Parameters
    ----------
    argv
        Command-line arguments.<br>
        -e url or --endpoint=url where url is the cdas web service endpoint
            URL to use.<br>
        -c url or --cacerts=filename where filename is the name of the file
            containing the CA certificates to use.<br>
        -h or --help prints help information.
    """

    try:
        opts = getopt.getopt(argv[1:], 'he:c:',
                             ['help', 'endpoint=', 'cacerts='])[0]
    except getopt.GetoptError:
        print('ERROR: invalid option')
        print_usage(argv[0])
        sys.exit(2)

#    logger = logging.getLogger(__name__)

    endpoint = ENDPOINT
    ca_certs = None

    for opt, arg in opts:
        if opt in ('-e', '--endpoint'):
            endpoint = arg
        elif opt in ('-c', '--cacerts'):
            ca_certs = arg
        elif opt in ('-h', '--help'):
            print_usage(argv[0])
            sys.exit()

    cdas = CdasWs(endpoint=endpoint, ca_certs=ca_certs)


    print(cdas.get_observatory_groups(
        instrumentType='Magnetic Fields (Balloon)'))
    print(cdas.get_instrument_types(observatory='AC'))
    print(cdas.get_instruments(observatory='AC'))
    print(cdas.get_observatories(
        instrumentType='Magnetic Fields (space)'))
    print(cdas.get_observatory_groups_and_instruments(\
                   instrumentType='Magnetic Fields (space)'))
    mms_brst_inventory = cdas.get_inventory('MMS1_FPI_BRST_L2_DES-MOMS',
                                            timeInterval=TimeInterval(
                                                '2018-08-30T08:09:53Z',
                                                '2018-08-30T08:52:00Z'))
    print('MMS1_FPI_BRST_L2_DES-MOMS inventory:')
    for interval in mms_brst_inventory:
        print('    ' + str(interval))

    variables = cdas.get_variables('AC_H0_MFI')
    if variables is not None:
        print('Variable Names:')
        for variable in variables:
            print('    ' + variable['Name'])

    status, data = \
        cdas.get_data('AC_H1_MFI', ['Magnitude', 'BGSEc'],
                      '2009-06-01T00:00:00Z', '2009-06-01T00:10:00Z'
                      #binData={
                      #    'interval': 60.0,
                      #    'interpolateMissingValues': True,
                      #    'sigmaMultiplier': 4
                      #}
                      )
#        cdas.get_data('10.21978/P8PG8V', ['BT'],
#                      '1987-09-24T00:00:00Z', '1987-09-24T01:00:00Z'

    if status['http']['status_code'] == 200:
        print(data)
    else:
        print('Request failed with status = ', status)

if __name__ == '__main__':
    example(sys.argv)
