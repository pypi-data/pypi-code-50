"""
Utility functions to transform YAML output.
"""
usage = """

Sanity saving data re-formatter.

See https://www.biostarhandbook.com for further details.

"""
import sys
import csv
import plac
import argparse
from pprint import pprint

GENBANK, SRA = "GENBANK", "SRA"

def print_metadata():
    """
    Prints metadata from an NCBI YAML output.
    """
    data = parse_yaml()
    rows = data['genbank-sequences']

    # Fix up country and state
    for row in rows:

        # Simplify the needlessly obtuse and verbose column headers.
        row['country'] = row['locality'].get('country', '')
        row['state'] = row['locality'].get('state', '')
        row['region'] = row['gene-region']
        row['date'] = row['collection-date']

        # Replace the accession with refseq id if exists.
        row['accession'] = row.get('refseq-accession', row['accession'])

        # Remove of unused fields
        for key in ('locality', 'gene-region', 'refseq-accession', 'collection-date'):
            row.pop(key, None)

    # Print the Genbank table
    fieldnames = ['accession', 'region', 'date', 'country', 'state']
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames, delimiter="\t")
    # writer.writeheader()
    writer.writerows(rows)


def print_sra():
    """
    Prints SRA metadata from an NCBI YAML output.
    """
    # Fix up SRA
    data = parse_yaml()
    rows = data['sra-accessions']

    # Print the SRA run table.
    fieldnames = ['sra-run', 'bioproject', 'sra-experiment', 'sra-study', 'sra-sample', 'biosample']
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames, delimiter="\t")
    # writer.writeheader()
    writer.writerows(rows)


def parse_yaml(stream=sys.stdin):
    """
    Parses a YAML stream.
    """
    try:
        # Don't make yaml a universal dependency.
        import yaml
    except ImportError as exc:
        print("*** This program requires pyyaml: conda install pyyaml", file=sys.stderr)
        sys.exit(1)

    # Parse the document
    data = yaml.load(stream, Loader=yaml.BaseLoader)

    # Uncomment to understand the structure of the data
    # pprint(data)

    if not data:
        sys.exit("*** error: empty stream")

    return data

@plac.annotations(
    acc=("print Genbank accession numbers", "flag", "a"),
    sra=("print SRA metadata", "flag", "s")
)
def run(acc=False,  sra=False,):
    "Reformats NCBI yaml data into tabular form."
    if sra:
        print_sra()
    else:
        print_metadata()

def main():
    """
    Entry point for the script.
    """
    plac.call(run)

if __name__ == '__main__':
    main()


