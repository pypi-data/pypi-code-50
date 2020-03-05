import click

from .aws.commands.aws import aws as aws
from .gcp.commands.gcp import gcp as gcp
from .azure.commands.azure import azure as azure

version = '0.1.1'


@click.group()
@click.version_option(version)
@click.pass_context
def cli(ctx):
    pass


cli.add_command(aws)
cli.add_command(gcp)
cli.add_command(azure)
