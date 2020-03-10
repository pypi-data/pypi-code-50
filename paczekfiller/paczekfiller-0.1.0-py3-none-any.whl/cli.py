# -*- coding: utf-8 -*-
"""Command line function."""
import sys
import click

from paczekfiller.paczekfiller import main as fry


def write(filename, contents):
    with open(filename, 'w') as file:
        file.write(contents)


@click.command()
@click.argument('paczek')
@click.argument('output_file')
def main(output_file, paczek):
    """Console script for Pączek filler."""

    write(output_file, fry(paczek))


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
