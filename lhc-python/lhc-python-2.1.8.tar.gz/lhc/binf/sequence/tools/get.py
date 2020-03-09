import argparse
import pysam
import sys

from textwrap import TextWrapper
from typing import Generator, Iterable, Set
from lhc.binf.genomic_coordinate import GenomicInterval
from lhc.binf.sequence.reverse_complement import reverse_complement
from lhc.io.file import open_file


def extract(loci: Iterable[GenomicInterval], sequences: pysam.FastaFile) -> Generator[str, None, Set[str]]:
    missing_chromosomes = set()
    for locus in loci:
        identifier = str(locus.chromosome)

        if identifier not in sequences.references:
            missing_chromosomes.add(identifier)
            continue

        sequence = locus.get_sub_seq(sequences)
        yield reverse_complement(sequence) if locus.strand == '-' else sequence
    sys.stderr.write('\n'.join(sorted(missing_chromosomes)))
    return missing_chromosomes


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
                        help='entries to extract (default: stdin).')
    parser.add_argument('output', nargs='?',
                        help='sequence file to extract sequences to (default: stdout).')
    parser.add_argument('-s', '--sequence', required=True,
                        help='sequence file to extract loci from')
    parser.set_defaults(func=init_extract)
    return parser


def init_extract(args):
    wrapper = TextWrapper()
    with open_file(args.input) as headers, open_file(args.output, 'w') as output:
        sequences = pysam.FastaFile(args.sequence)
        for header in headers:
            header = header.strip()
            output.write('>{}\n{}\n'.format(header, '\n'.join(wrapper.wrap(sequences.fetch(header)))))


if __name__ == '__main__':
    sys.exit(main())
