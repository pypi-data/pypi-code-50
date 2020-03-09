"""
Filters taxonomical information
"""
import argparse
import csv
import re

import plac


def run_filter(inp, tgt, keep='', remove=None):

    if keep:
        patt1 = re.compile(keep, re.IGNORECASE)
        # Any elements matches
        keeper = lambda x: any(map(patt1.search, x))
    else:
        # Default is to keep all.
        keeper = lambda x: True

    if remove:
        patt2 = re.compile(remove, re.IGNORECASE)
        remover = lambda x: not any(map(patt2.search, x))
    else:
        # Default is to remove nothing.
        remover = lambda x: True

    # Open stream to lineage.
    stream_tgt = csv.reader(tgt, delimiter="\t")

    # Filter for more than a single column.
    stream_tgt = filter(lambda x: len(x) > 1, stream_tgt)

    # Filter patterns to keep
    stream_tgt = filter(keeper, stream_tgt)

    # Filter patterns to remove
    stream_tgt = filter(remover, stream_tgt)

    # The taxids that match the words
    ids1 = map(lambda x: x[0], stream_tgt)

    # The valid accession numbers
    valid = set(ids1)

    # Open stream to lineage.
    stream_inp = csv.reader(inp, delimiter=" ")

    # Remoter
    stream_inp = filter(remover, stream_inp)

    # Filter for more than a single column.
    stream_inp = filter(lambda x: len(x) > 2, stream_inp)

    # Filter for second element matching the pattern.
    stream_inp = filter(lambda x: x[1] in valid, stream_inp)

    for row in stream_inp:
        print(" ".join(row))


@plac.annotations(
    inp=("Input file, first column is accession", "option", "i", argparse.FileType("rt")),
    tgt=("Target file, first column is accession", "option", "t", argparse.FileType("rt")),
    k=("keep lines that match regular expression", "option", ),
    r=("remove lines that match regular expression", "option",),
)
def run(inp, tgt, k='', r=''):
    "Filters rows in one file based on content in another file"
    run_filter(inp=inp, tgt=tgt, keep=k, remove=r)


def main():
    plac.call(run)


if __name__ == '__main__':
    main()
