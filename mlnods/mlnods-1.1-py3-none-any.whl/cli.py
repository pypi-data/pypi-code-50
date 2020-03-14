import sys
import argparse
from pathlib import Path
from .helpers import _globals
from . import run, __version__, __releasedate__

pkgpath = Path(__file__).absolute().parent

def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="mlnods",
        description='''\
This is a script that will create independent sets of data

Version: %s [%s]''' % (__version__, __releasedate__),
        epilog='''\
If an ID is present in the instance file, but not in the table file the ID is considered to not be linked to anything else
If an ID is present in the table file but not in the instance file, it is ignored

mlnods was developed by Yana Bromberg and refactored by Maximilian Miller.

Feel free to contact us for support at services@bromberglab.org.
This software is licensed under [NPOSL-3.0](http://opensource.org/licenses/NPOSL-3.0)''',
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument('-s', '--splits', type=int, required=True,
                        help="number of splits required")
    parser.add_argument('-c', '--cutoff', type=int, required=True,
                        help="similarity cutoff in the units of link scores")
    parser.add_argument('-l', '--limit', type=int, default=0,
                        help="limit on the number of links for each node (default=0, infinity)")
    parser.add_argument('-e', '--edges', type=Path, required=True, dest='edges_file', 
                        help="file containing a table of instances with link scores for each pair")
    parser.add_argument('-f', '--format', type=str, dest='edges_format',
                        help='''\
format of the table file

blast     : takes a list of -m 9 formated blast files and builds a table based on seqID
hssp      : takes a list of -m 9 formated blast files, runs HSSP scoring script and builds an HSSP distance table
self<int> : space/tab separated table file, similarity score in column <int>
            eg \"ID1 ID2 similarity_score\" will be addressed as self3 (default=self5)'''
                        )
    parser.add_argument('-n', '--nodes', type=Path, required=True, dest='nodes_file',
                        help='''\
instance file containing IDs of all instances being considered

IDs are case-independent (eg ABC = abc)
IDs are always preceeded by \">\" and followed by a white space.
No white spaces are allowed in an ID.
If score is provided for an ID, it should be surrounded by spaces and directly follow the ID
(eg. >abl1_human 10 gene associated with ....)
Everything between two IDs is printed in the junction files, but not considered in evaluation'''
                        )
    parser.add_argument('-a', '--abundance', action='store_true',
                        help='''\
the option to score

false : score retrieved from instance file, range [0-100], default=50 when missing
true  : score approximated by actual number of times an ID appears in the instance file'''
                        )
    parser.add_argument('-r', '--random', type=int, default=None,
                        help="set a fixed random seed to generate consistent partitions")
    parser.add_argument('-o', '--outfolder', type=Path,
                        help="path to output folder (default=<current directory>")
    parser.add_argument('-v', '--verbose', action='count', default=0,
                        help="set verbosity level")
    parser.add_argument('-q', '--quiet', action='store_true',
                        help="no logging to stdout")
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__} ({__releasedate__})')

    return parser.parse_known_args()


def init():
    namespace, args = parse_arguments()
    _globals('verbose', namespace.verbose)
    del namespace.verbose
    _globals('quiet', namespace.quiet)
    del namespace.quiet
    run.main(namespace, args)


if __name__ == "__main__":
    init()
