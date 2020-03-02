"""Console script for johnstondechazal."""
import sys
import click

from johnstondechazal.data import download_data, PKG_DIR

@click.command()
@click.argument('dest', default=PKG_DIR)
def main(dest):
    """Console script for johnstondechazal."""
    download_data(dest)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
