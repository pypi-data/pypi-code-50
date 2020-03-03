import sys
import click
import s1crets


@click.group()
def main():
    pass


@main.command()
@click.option('--provider', help='Secrets provider', default='aws.sm',
              show_default=True, type=click.Choice(['aws.sm', 'aws.ps']))
@click.argument('path', nargs=1, required=True)
@click.argument('keypath', nargs=-1, type=click.UNPROCESSED)
def get(provider, path, keypath):
    click.echo(s1crets.get(provider, path, keypath=keypath))


@main.command()
@click.option('--provider', help='Secrets provider', default='aws.sm',
              show_default=True, type=click.Choice(['aws.sm', 'aws.ps']))
@click.argument('path', nargs=1, required=True)
@click.argument('keypath', nargs=-1, type=click.UNPROCESSED)
def exists(provider, path, keypath):
    if not s1crets.path_exists(provider, path, keypath=keypath):
        sys.exit(1)


@main.command()
@click.option('--provider', help='Secrets provider', default='aws.sm',
              show_default=True, type=click.Choice(['aws.sm', 'aws.ps']))
@click.argument('path', nargs=1, required=True)
def get_by_path(provider, path):
    for k, v in s1crets.get_by_path(provider, path).items():
        print(k, v)


@main.command()
@click.option('--provider', help='Secrets provider', default='aws.sm',
              show_default=True, type=click.Choice(['aws.sm', 'aws.ps']))
@click.argument('path', nargs=1, required=True)
@click.argument('value', nargs=1, required=True)
def update(provider, path, value):
    s1crets.update(provider, path, value)
