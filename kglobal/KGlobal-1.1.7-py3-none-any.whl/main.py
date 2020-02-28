from getopt import GetoptError, getopt
import sys
import logging

logger = logging.getLogger(__name__)


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    try:
        opts, args = getopt(args, 'h:create_master_salt')
    except GetoptError as exc:
        sys.stderr.write("ERROR: %s" % exc)
        sys.stderr.write(os.linesep)
        return 1

    for cmd, arg in opts:
        if cmd == '-h':
            print('KGlobal -create_master_salt')
        elif cmd == '-create_master_salt':
            try:
                print('Creating Master Salt Key....')
                from . import create_master_salt_key
                create_master_salt_key()
                print('Master Salt Key has been successfully created')
            except Exception as exc:
                sys.stderr.write("ERROR: %s" % exc)
                sys.stderr.write(os.linesep)
                return 1

    return 0
