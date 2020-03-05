import click

from .aws.commands.aws import aws as aws
from .gcp.commands.gcp import gcp as gcp

version = '0.0.0'


@click.group()
@click.version_option(version)
@click.pass_context
def cli(ctx):
    pass


cli.add_command(aws)
cli.add_command(gcp)
