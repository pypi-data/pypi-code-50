#!/usr/bin/env python3

"""Main module for etna-cli."""

import click

from etna_cli import config
from etna_cli import conversation
from etna_cli import etna_gitlab
from etna_cli import event
from etna_cli import project
from etna_cli import student
from etna_cli import rank
from etna_cli import task

__version__ = '0.1.0'


@click.group(invoke_without_command=True)
@click.pass_context
@click.option("-v", "--version", is_flag=True, help="print version")
def main(ctx, version):
    """main function."""
    if version:
        print("Etna utility version %s" % __version__)
    elif ctx.invoked_subcommand is None:
        click.echo(main.get_help(ctx))


main.add_command(config.main)
main.add_command(conversation.main)
main.add_command(event.main)
main.add_command(project.main)
main.add_command(etna_gitlab.main)
main.add_command(student.main)
main.add_command(rank.main)
main.add_command(task.main)
if __name__ == '__main__':
    main()
