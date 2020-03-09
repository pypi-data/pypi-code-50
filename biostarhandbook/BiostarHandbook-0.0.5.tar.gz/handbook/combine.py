#!/usr/bin/env python
"""
Combines Kallisto and Salmon abundance files.

Usage:

    cat SAMPLES | python combine.py WORKDIR 
    
Where:

- WORKDIR is a directory
- SAMPLES is a file with one SAMPLE_ID per line
 
For each SAMPLE_ID the program will attempt to read the file named located at:

    WORKDIR/SAMPLE_ID/abundances.tsv

Once loaded, the files will be combined into a tabular format printed to standard output. 
"""

import csv
import os
import sys
import plac
import argparse

def parse(workdir, sample):
    """
    Returns a generator over the file.
    """

    # The path to the abundnace file.
    path = os.path.join(workdir, sample, "abundance.tsv")

    # Stop on missing files.
    if not os.path.isfile(path):
        print("ERROR: unable to read file path: %s" % path)
        sys.exit()

    # Open the stream.
    stream = csv.DictReader(open(path), delimiter="\t")

    # Generate the data
    for row in stream:
        yield row


def run():
    "Processes and combines the tsv files resulting from kallisto runs."

    stream = sys.stdin

    # The samples in the work directory.
    samples = [line.strip() for line in stream]

    collect = {}
    for sample in samples:

        # Open the stream to the file
        stream = parse(sample)

        for row in stream:

            # Identify data of interest.
            target_id, length, eff_length = row['target_id'], row['length'], row['eff_length']

            # Create a list for each new target id.
            if target_id not in collect:
                collect[target_id] = [target_id, length, eff_length]

            # Append the estimated counts to each target id.
            collect[target_id].append(row['est_counts'])

    # Print the new headers
    header = ["target_id", "length", "eff_length"] + samples
    header = "\t".join(header)
    print(header)

    # Go over the collection and print each row.
    for key, values in collect.items():
        line = "\t".join(values)
        print(line)


def main():
    """
    Entry point for the script.
    """
    plac.call(run)

if __name__ == '__main__':
    main()
