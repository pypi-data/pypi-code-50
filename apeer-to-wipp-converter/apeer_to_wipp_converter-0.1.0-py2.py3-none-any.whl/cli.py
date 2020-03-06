"""Console script for apeer_to_wipp_converter."""
import sys
import click

import apeer_to_wipp_converter.apeer_to_wipp_converter as converter


@click.command()
@click.argument('filename')
def main(filename):
    """Console script for apeer_to_wipp_converter."""
    click.echo("Replace this message by putting your code into "
               "apeer_to_wipp_converter.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    click.echo(filename)

    converter.convert(filename)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
