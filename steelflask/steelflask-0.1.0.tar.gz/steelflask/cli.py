import click
from .actions import app_actions
import os


@click.group()
def steelflask():
    pass


@steelflask.command()
@click.argument('name', default=None, required=False)
@click.option('--basic', is_flag=True,
              help=('It creates structure for basic python project.'))
def init(basic, name):
    if name is None:
        name = os.path.basename(os.getcwd())
    venv_folder = f'{name}_venv'
    venv_folder = click.prompt(f'What is the virtual env folder name?', type=str, default=venv_folder)
    app_actions.generate_app(name, basic, venv_folder)
