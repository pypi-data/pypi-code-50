"""Console script for cy_data_access."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for cy_data_access."""
    click.echo("Replace this message by putting your code into "
               "cy_data_access.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
