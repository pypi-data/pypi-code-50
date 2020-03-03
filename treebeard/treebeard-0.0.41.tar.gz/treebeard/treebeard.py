import treebeard.sentry_setup  # type: ignore isort:skip

import warnings
from typing import Any

import click
from halo import Halo  # type: ignore
from humanfriendly import format_size, parse_size  # type: ignore
from timeago import format as timeago_format  # type: ignore

from treebeard.cli_helper import check_for_updates, get_service_status_message
from treebeard.conf import service_status_endpoint
from treebeard.helper import get_config_path, get_treebeard_env
from treebeard.notebooks.commands import cancel, run, status
from treebeard.other.commands import configure, info, version
from treebeard.secrets.commands import secrets

config_path = get_config_path()

treebeard_env = get_treebeard_env()

msg = get_service_status_message(service_status_endpoint)
if msg:
    click.echo(click.style(msg, fg="red"), err=True)

project_id = treebeard_env["project_id"]
notebook_id = treebeard_env["notebook_id"]

warnings.filterwarnings(
    "ignore", "Your application has authenticated using end user credentials"
)


@click.group()
def cli():
    pass


@cli.resultcallback()
def process_result(*args: Any, **kwargs: Any):
    check_for_updates()


cli.add_command(configure)
cli.add_command(status)
cli.add_command(run)
cli.add_command(cancel)
cli.add_command(secrets)
cli.add_command(info)
cli.add_command(version)
