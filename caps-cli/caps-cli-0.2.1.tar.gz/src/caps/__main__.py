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
def initialize(inputs=0, outputs=0, parameters=0):

    logging.info("Initializing YAML")
    _initialize.initialize(inputs, outputs, parameters)
    click.secho(f"Success", fg="green")


@cli.command(short_help="Transform the input YAML into a Valid JSON for posting the file to Model Catalog")
@click.argument("yaml_file_path", default=None, type=str)
def push(yaml_file_path):
    logging.info("Pushing yaml")
    _push.push(yaml_file_path)
    click.secho(f"Success", fg="green")


@cli.command(short_help="Validate the JSON obtained after creating one")
@click.argument("metadata_file_path", default=None, type=str)
def validate(metadata_file_path):
    logging.info("Validating metadata")
    _validate.validate(metadata_file_path)
    click.secho(f"Success", fg="green")


