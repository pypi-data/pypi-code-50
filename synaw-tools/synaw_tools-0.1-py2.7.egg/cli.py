"""
CLI wrapper for SYNAW tools.
"""
import argparse


def main():
    parser = argparse.ArgumentParser(description='Python tooling for SYNAW.')
    subparsers = parser.add_subparsers(title='subcommands',
                                       description='available subcommands',
                                       help='additional help')

    ciphers_parser = subparsers.add_parser('ciphers')

    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
