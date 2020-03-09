import argparse

from typing import Iterator
from lhc.binf.genomic_coordinate import GenomicInterval
from lhc.io.fasta import iter_fasta
from lhc.io.file import open_file
from lhc.io.loci import open_loci_file


def generate_from_fasta(sequences) -> Iterator[GenomicInterval]:
    pass


def main():
    args = get_parser().parse_args()
    args.func(args)


def get_parser() -> argparse.ArgumentParser:
    return define_parser(argparse.ArgumentParser())


def define_parser(parser) -> argparse.ArgumentParser:
    parser.add_argument('input', nargs='?',
                        help='input to generate from (default: stdin).')
    parser.add_argument('output', nargs='?',
                        help='loci file to extract loci to (default: stdout).')
    parser.add_argument('-o', '--output-format',
                        help='file format of output file (useful for writing to stdout).')
    parser.set_defaults(func=init_generate)
    return parser


def init_generate(args):
    with open_file(args.input) as input,\
            open_loci_file(args.output, 'w', format=args.output_format) as output:
        for header, sequence in iter_fasta(input):
            output.write(GenomicInterval(0, len(sequence), chromosome=header, data={'gene_id': header}))


if __name__ == '__main__':
    main()
