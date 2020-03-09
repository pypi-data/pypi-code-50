import itertools

from argparse import ArgumentParser, Namespace
from typing import Iterable
from lhc.binf.genomic_coordinate import GenomicInterval
from lhc.io.loci import open_loci_file


def get_loci_sizes(loci: Iterable[GenomicInterval]):
    for locus in loci:
        yield locus.stop - locus.start


def get_insert_sizes(loci: Iterable[GenomicInterval]):
    ends = {}
    for locus in loci:
        gene_id = locus.data['transcript_id']
        if gene_id in ends:
            yield gene_id, locus.start - ends[gene_id]
        ends[gene_id] = locus.stop


def main():
    args = get_parser().parse_args()
    args.func(args)


def get_parser() -> ArgumentParser:
    return define_parser(ArgumentParser())


def define_parser(parser: ArgumentParser) -> ArgumentParser:
    parser.add_argument('input', nargs='?')
    parser.set_defaults(func=init_stat)
    return parser


def init_stat(args: Namespace):
    #with open_loci_file(args.input) as loci:
    #    mn = 0
    #    mx = 0
    #    for k, v in get_insert_sizes(loci):
    #        if v < mn:
    #            mn = v
    #        elif v > mx:
    #            mx = v
    #    print('{}\t{}'.format(mn, mx))

    with open_loci_file(args.input) as loci:
        for_min, for_max = itertools.tee(get_loci_sizes(loci))
        print(min(for_min), max(for_max))


if __name__ == '__main__':
    main()
