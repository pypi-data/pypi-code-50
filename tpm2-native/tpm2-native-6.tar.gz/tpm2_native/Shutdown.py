import struct
import sys
from tpm2_native.common import *


def _shutdown(sessions, clear):
    info0('<<< Command >>>')
    su = TPM_SU['CLEAR' if clear else 'STATE']
    info0('shutdownType', (su, TPM_SUrev.get(su, 'UNKNOWN')))
    req = struct.pack('!HIH',
            TPM_ST['SESSIONS'] if sessions else TPM_ST['NO_SESSIONS'],
            TPM_CC['Shutdown'],
            su)
    tpm2_xmit(req)


def main():
    parser = argparse.ArgumentParser()
    add_tpm_st(parser)
    parser.add_argument('--shutdown-type', choices=['clear', 'state'], required=True)
    args = run(parser)
    _shutdown(args.sessions == 'yes', args.shutdown_type == 'clear')
