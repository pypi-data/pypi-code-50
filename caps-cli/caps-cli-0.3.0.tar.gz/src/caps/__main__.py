import configparser
import logging
import os
import sys
from pathlib import Path
import json

import click

import semver

import caps
from caps import _utils, _metadata_schema, _transform_data, _initialize, _push, _validate

__DEFAULT_CAPS_CLI_CREDENTIALS_FILE__ = "~/.caps-cli/credentials"
__DEFAULT_MINT_API_CREDENTIALS_FILE__ = "~/.mint_api/credentials"


@click.group()
@click.option("--verbose", "-v", default=0, count=True)
def cli(verbose):
    _utils.init_logger()
    lv = ".".join(_utils.get_latest_version().split(".")[:3])
    cv = ".".join(caps.__version__.split(".")[:3])

    if semver.compare(lv, cv) > 0:
        click.secho(
            f"""WARNING: You are using caps-cli version {caps.__version__}, however version {lv} is available.
You should consider upgrading via the 'pip install --upgrade caps' command.""",
            fg="yellow",
        )


@cli.command(short_help="Show caps-cli version.")
def version(debug=False):
    click.echo(f"{Path(sys.argv[0]).name} v{caps.__version__}")


@cli.command(help="Configure Model Catalog API credentials")
@click.option(
    "--profile",
    "-p",
    envvar="CAPS_PROFILE",
    type=str,
    default="default",
    metavar="<profile-name>",
)
def configure(profile="default"):
    api_username = click.prompt("Model Catalog API Username")
    api_password = click.prompt("Model Catalog API Password", hide_input=True)

    credentials_file = Path(
        os.getenv("MINT_API_CREDENTIALS_FILE", __DEFAULT_MINT_API_CREDENTIALS_FILE__)
    ).expanduser()
    os.makedirs(str(credentials_file.parent), exist_ok=True)

    credentials = configparser.ConfigParser()
    credentials.optionxform = str

    if credentials_file.exists():
        credentials.read(credentials_file)

    credentials[profile] = {
        "api_username": api_username,
        "api_password": api_password
    }

    with credentials_file.open("w") as fh:
        credentials_file.parent.chmod(0o700)
        credentials_file.chmod(0o600)
        credentials.write(fh)
        click.secho(f"Success", fg="green")


@cli.command(short_help="Create an empty JSON template to fill the data to be inserted in Model Catalog")
@click.option(
    "--inputs",
    "-i",
    type=int,
    default=0,
)
@click.option(
    "--outputs",
    "-o",
    type=int,
    default=0,
)
@click.option(
    "--parameters",
    "-p",
    type=int,
    default=0,
)
@click.option(
    "--directory",
    "-d",
    type=str,
    default="",
    help="Specify folder to generate new component in. Entering a filename will initialize the yaml with that name"
)
@click.option(
    "--force",
    "-f",
    is_flag=True,
    help="Force file creation. This will override a file with the same name. Use with caution"
)
def initialize(inputs=0, outputs=0, parameters=0, directory="", force=False):

    logging.info("Initializing YAML")
    _initialize.initialize(inputs, outputs, parameters, directory, force)
    click.secho(f"Success", fg="green")


@cli.command(short_help="Transform the input YAML into a Valid JSON for posting the file to Model Catalog")
@click.option(
    "--profile",
    "-m",
    envvar="MINT_API_PROFILE",
    type=str,
    default="default",
    metavar="<profile-name>",
)
@click.argument("is_setup", default="false", type=str)
@click.argument("yaml_file_path", default=None, type=str)
def push(is_setup, yaml_file_path,  profile="default"):
    logging.info("Pushing yaml")
    _push.push(is_setup, yaml_file_path, profile=profile)
    click.secho(f"Success", fg="green")


@cli.command(short_help="Validate the JSON obtained after creating one")
@click.argument("metadata_file_path", default=None, type=str)
def validate(metadata_file_path):
    logging.info("Validating metadata")
    _validate.validate(metadata_file_path)
    click.secho(f"Success", fg="green")


