import click

from . import __version__


@click.group(help="A pygnn template project")
@click.version_option(version=__version__)
def _main() -> None:
    pass


@_main.command(name="echo", help="Echos a message")
@click.option("-m", "--message", required=True, type=str, help="the message to echo")
def _echo(message: str) -> None:
    print(message)


if __name__ == "__main__":
    _main(prog_name="pygnn")
