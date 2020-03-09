import argparse
import csv
import itertools

import plac

FILL_VALUE = ''


def process(file1, file2, delimiter, colidx, show):
    """
    Processes the files and prints the output
    """

    def parse(stream):
        """
        A generator in a clojure to processes each stream.
        Returns the value of a column at the column index.
        """
        # Skip comment lines
        stream = filter(lambda x: not x.startswith('#'), stream)

        # Ignore empty lines.
        stream = filter(lambda x: x.strip(), stream)

        # Format the stream.
        stream = csv.reader(stream, delimiter=delimiter)

        # Generate empty values on missing columns.
        for row in stream:
            try:
                yield (row[colidx], None)
            except IndexError as exc:
                yield ('', None)

    # Make dictionaries to maintain original item order.
    store1 = dict(parse(file1))
    store2 = dict(parse(file2))

    # Generate the various groupings.
    isect = [key for key in store1.keys() if key in store2]
    onlyA = [key for key in store1.keys() if key not in store2]
    onlyB = [key for key in store2.keys() if key not in store1]
    union = isect + onlyA + onlyB
    # Select output based on flags.
    if show == 1:
        output = onlyA
    elif show == 2:
        output = onlyB
    elif show == 3:
        output = isect
    elif show == 4:
        output = union
    else:
        output = itertools.zip_longest(onlyA, onlyB, isect, union, fillvalue=FILL_VALUE)
        output = map(lambda x: "\t".join(x), output)

    # Print the output
    for line in output:
        print(line)


@plac.annotations(
    fileA=("file A", "positional", None, argparse.FileType('rt')),
    fileB=("file B", "positional", None, argparse.FileType('rt')),
    c=("column index for values", "option"),
    show=("1: A-B, 2: B-A, 3: A and B, 4: A + B, 0: all columns", "option", 's', int),
    t=("input files are tab delimited", "flag"),
)
def run(fileA, fileB, t=False, c=1, show=0):
    "A better 'comm' command to find common values."
    delimiter = "\t" if t else ","

    colidx = c - 1

    process(file1=fileA, file2=fileB, delimiter=delimiter, colidx=colidx, show=show)


def main():
    """
    Entry point for the script.
    """

    plac.call(run)


if __name__ == '__main__':
    main()
