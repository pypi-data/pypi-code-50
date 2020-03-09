import argparse

from textwrap import TextWrapper
from typing import Callable, Iterable, Iterator, Set
from lhc.binf.genomic_coordinate import GenomicInterval
from lhc.io.loci import open_loci_file
from lhc.io.fasta.iterator import iter_fasta, FastaEntry
from lhc.io.file import open_file


def filter(sequences: Iterable[FastaEntry], filters: Set[Callable], mode=all) -> Iterator[FastaEntry]:
    for sequence in sequences:
        if mode(filter_(sequence) for filter_ in filters):
            yield sequence


def filter_in_set(entry, entries):
    return entry.hdr in entries


def format_locus(format_string: str, locus: GenomicInterval) -> str:
    return format_string.format(chromosome=locus.chromosome,
                                start=locus.start.position,
                                end=locus.stop.position,
                                strand=locus.strand,
                                **locus.data)


def main():
    args = get_parser().parse_args()
    args.func(args)


def get_parser():
    return define_parser(argparse.ArgumentParser())


def define_parser(parser):
    parser.add_argument('input', nargs='?',
                        help='sequences to filter (default: stdin).')
    parser.add_argument('output', nargs='?',
                        help='sequence file to filtered sequences to (default: stdout).')
    parser.add_argument('-l', '--loci',
                        help='filter using given loci')
    parser.add_argument('--loci-format', default='{gene_id}',
                        help='format string to convert loci into fasta header')
    parser.add_argument('-m', '--mode', default='all', choices=['all', 'any'],
                        help='whether entry has to match all or any filter')
    parser.set_defaults(func=init_extract)
    return parser


def init_extract(args: argparse.Namespace):
    from functools import partial

    wrapper = TextWrapper()
    filters = set()

    if args.loci:
        with open_loci_file(args.loci) as loci:
            filters.add(partial(filter_in_set, entries={format_locus(args.loci_format, locus) for locus in loci}))

    with open_file(args.output, 'w') as output:
        sequences = iter_fasta(args.input)
        for sequence in filter(sequences, filters, mode={'all': all, 'any': any}[args.mode]):
            output.write('>{}\n{}\n'.format(sequence.hdr, '\n'.join(wrapper.wrap(sequence.seq))))


if __name__ == '__main__':
    import sys
    sys.exit(main())
