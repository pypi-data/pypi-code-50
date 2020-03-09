import argparse

from typing import Iterable, Iterator, Optional
from lhc.binf.genomic_coordinate import GenomicInterval
from lhc.io.loci import open_loci_file
from lhc.itertools.merge_sorted import merge_sorted


def closest(loci: Iterable[GenomicInterval], query: Iterable[GenomicInterval], tolerance: Optional[int] = None) -> Iterator[GenomicInterval]:
    previous = None
    unmatched = None
    for loci in merge_sorted(iter(loci), iter(query)):
        left = next(iter(loci[0]), None)
        right = next(iter(loci[1]), None)
        if left:
            if right:
                yield left, right, 0
            else:
                unmatched = loci[0][0]

            if previous and left.chromosome != previous.chromosome:
                previous = None
        if right:
            if unmatched:
                if previous:
                    if unmatched.chromosome == previous.chromosome and right.chromosome == unmatched.chromosome and unmatched.start - previous.start < right.start - unmatched.start:
                        if tolerance and unmatched.start - previous.start > tolerance:
                            yield unmatched, None, None
                        else:
                            yield unmatched, previous, unmatched.start - previous.start
                    else:
                        if tolerance and right.chromosome == unmatched.chromosome and right.start - unmatched.start > tolerance or right.chromosome != unmatched.chromosome:
                            yield unmatched, None, None
                        else:
                            yield unmatched, right, right.start - unmatched.start
                else:
                    if tolerance and right.start - unmatched.start > tolerance:
                        yield unmatched, None, None
                    else:
                        yield unmatched, right, right.start - unmatched.start
                unmatched = None
            previous = right


def main():
    args = get_parser().parse_args()
    args.func(args)


def get_parser() -> argparse.ArgumentParser:
    return define_parser(argparse.ArgumentParser())


def define_parser(parser) -> argparse.ArgumentParser:
    parser.add_argument('input', nargs='?',
                        help='input loci to filter (default: stdin).')
    parser.add_argument('output', nargs='?',
                        help='loci file to extract loci to (default: stdout).')
    parser.add_argument('-d', '--direction', default='both', choices=('left', 'right', 'both'),
                        help='which loci to return')
    parser.add_argument('-l', '--loci', required=True,
                        help='loci to find intersections with')
    parser.add_argument('-i', '--input-format',
                        help='file format of input file (useful for reading from stdin).')
    parser.add_argument('-o', '--output-format',
                        help='file format of output file (useful for writing to stdout).')
    parser.add_argument('-t', '--tolerance', type=int,
                        help='limit the farthest detected loci to tolerance.')
    parser.add_argument('--loci-format')
    parser.add_argument('--input-index', default=1, type=int)
    parser.add_argument('--output-index', default=1, type=int)
    parser.add_argument('--loci-index', default=1, type=int)
    parser.set_defaults(func=init_closest)
    return parser


def init_closest(args):
    import sys

    with open_loci_file(args.input, format=args.input_format, index=args.input_index) as input,\
            open_loci_file(args.output, 'w', format=args.output_format, index=args.output_index) as output,\
            open_loci_file(args.loci, format=args.loci_format, index=args.loci_index) as loci:
        for left, right, distance in closest(input, loci, args.tolerance):
            if args.direction == 'both':
                right_id = right.data['gene_id'] if right is not None else None
                sys.stderr.write(str((left.data['gene_id'], left, right_id, right, distance)))
                sys.stderr.write('\n')
            else:
                locus = left if args.direction == 'left' else right
                if distance is not None:
                    output.write(locus)


if __name__ == '__main__':
    main()
