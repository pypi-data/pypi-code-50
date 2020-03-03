import os
import os.path
import tarfile
import tempfile
from typing import IO, List

import click
import requests
from halo import Halo  # type: ignore
from humanfriendly import format_size, parse_size  # type: ignore
from timeago import format as timeago_format  # type: ignore

from treebeard.cli_helper import validate_notebook_directory, get_treebeard_config
from treebeard.conf import secrets_endpoint
from treebeard.helper import get_treebeard_env

treebeard_env = get_treebeard_env()


@click.group()
def secrets():
    pass


@secrets.command()
@click.argument("files", type=click.File("r"), nargs=-1)
def push(files: List[IO]):
    """Uploads json document of secrets to Treebeard's servers. These will be available in your notebook directory at runtime"""
    click.echo(f"🌲 Pushing Secrets for project {treebeard_env['project_id']}")

    treebeard_config = get_treebeard_config()

    if treebeard_config:
        files += tuple((open(path, "r") for path in treebeard_config.secret))

    validate_notebook_directory()
    for f in files:
        is_in_project = os.path.realpath(f.name).startswith(os.getcwd())
        if not is_in_project:
            click.echo(
                click.style(
                    f"ERROR: {f.name} is not in the notebook directory. All secrets must be located in the notebook directory",
                    fg="red",
                )
            )

    with tempfile.NamedTemporaryFile(
        "wb", suffix=".tar.gz", delete=False
    ) as secrets_archive:
        with tarfile.open(
            fileobj=secrets_archive, mode="w:gz", dereference=True
        ) as tar:
            for f in files:
                click.echo(f"Including {f.name}")
                tar.add(f.name)
    response = requests.post(
        secrets_endpoint,
        files={"secrets": open(secrets_archive.name, "rb")},
        headers=treebeard_env,
    )
    if response.status_code != 200:
        click.echo(
            f"Error: service failure pushing secrets, {response.status_code}: {response.text}"
        )
        return

    click.echo("🔐  done!")
