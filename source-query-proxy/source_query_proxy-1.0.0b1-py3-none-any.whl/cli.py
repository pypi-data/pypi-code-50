import click


@click.group()
def sqproxy():
    """Basic entrypoint"""


@sqproxy.command()
def run():
    """Run SQProxy process"""
    from .runner import run

    run()
