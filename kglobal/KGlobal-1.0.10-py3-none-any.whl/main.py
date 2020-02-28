from getopt import GetoptError
import sys

if MYPY_CHECK_RUNNING:
    from typing import List, Optional

logger = logging.getLogger(__name__)


def main(args=None):
    # type: (Optional[List[str]]) -> int
    if args is None:
        args = sys.argv[1:]

    try:
        opts, args = parse_command(args)
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
        else:
            print('Please execute KGlobal -h')

    return 0
