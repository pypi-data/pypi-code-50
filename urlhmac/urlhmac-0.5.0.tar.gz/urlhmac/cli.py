"""Console script for urlhmac."""
import sys

import click
import lumberpy.click


@click.command()
@lumberpy.click.options()
def main(lumberpy_config_path, verbose):
    """Console script for urlhmac."""
    lumberpy.setup(lumberpy_config_path, verbose)
    click.echo(
        "Replace this message by putting your code into  urlhmac.cli.main"
    )
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
