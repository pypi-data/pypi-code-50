import re
import click
import inquirer

from alfa_cli.lib.initializer import generate_specification, generate_files


@click.command()
def init ():
    """Create the file structure for a new algorithm"""
    specification = generate_specification()
    generate_files(specification)
