import configparser
import json
import os
import sys
import time
from pathlib import Path

import click
import requests
from datetime import datetime
from typing import Optional, Tuple
from pydantic import BaseModel
import yaml

from treebeard.version import get_version


if os.getenv("TREEBEARD_ENVIRONMENT") is None:
    env = "production"
else:
    env = os.getenv("TREEBEARD_ENVIRONMENT")


def get_config_path():
    home = str(Path.home())
    return f"{home}/.treebeard"


config_path = get_config_path()


def get_notebook_name():
    treebeard_config = get_treebeard_config()

    notebook = "main.ipynb"
    if treebeard_config:
        notebook = treebeard_config.notebook

    if not os.path.isfile(f"{os.getcwd()}/{notebook}"):
        return None
    return Path(os.getcwd()).name


def get_treebeard_env():
    """Reads variables from a local file, credentials.cfg"""
    config = configparser.RawConfigParser()
    treebeard_project_id = None
    run_id = None
    email = None
    api_key = None

    try:
        config.read(config_path)
        email = config.get("credentials", "TREEBEARD_EMAIL")
        treebeard_project_id = config.get("credentials", "TREEBEARD_PROJECT_ID")
        api_key = config.get("credentials", "TREEBEARD_API_KEY")

        run_id = os.getenv("TREEBEARD_RUN_ID")
        if run_id is None:
            run_id = f"local-{int(time.time())}"
    except:
        pass  # Default values indicate error occurred
    treebeard_env = {
        "notebook_id": get_notebook_name(),
        "project_id": treebeard_project_id,
        "run_id": run_id,
        "email": email,
        "api_key": api_key,
    }
    return treebeard_env


def set_credentials(email: str, key: str, signup_endpoint: str):
    """Create user credentials"""
    # key = secrets.token_urlsafe(16)
    config = configparser.RawConfigParser()
    config.add_section("credentials")
    config.set("credentials", "TREEBEARD_EMAIL", email)
    # Project id is last 10 numbers of hash of email

    click.echo(signup_endpoint)
    response = requests.post(signup_endpoint, headers={"api_key": key, "email": email},)

    if response.status_code != 200:
        raise click.ClickException(f"Request failed: {response.text}")

    try:
        json_data = json.loads(response.text)
        project_id = json_data["project_id"]
        # click.echo(f"✨  Run has been accepted! {json_data['admin_url']}")
    except:
        click.echo("❗  Request to configure failed")
        click.echo(sys.exc_info())
        if response:
            click.echo(response.text)
        return

    config.set("credentials", "TREEBEARD_PROJECT_ID", project_id)
    config.set("credentials", "TREEBEARD_API_KEY", key)
    with open(config_path, "w") as configfile:
        config.write(configfile)
    click.echo(f"🔑  Config saved in {config_path}")
    return project_id


def get_run_path():
    treebeard_env = get_treebeard_env()
    print(f"Treebeard env is {treebeard_env}")
    return f"{treebeard_env['project_id']}/{treebeard_env['notebook_id']}/{treebeard_env['run_id']}"


def get_time():
    return datetime.now().strftime("%H:%M:%S")


def validate_notebook_directory():
    treebeard_env = get_treebeard_env()
    if treebeard_env["project_id"] is None:
        click.echo(
            click.style(
                "This library will not function without credentials.\nPlease email alex@treebeard.io to obtain an API key then run `treebeard configure`",
                fg="red",
            )
        )
        sys.exit(1)
    if treebeard_env["notebook_id"] is None:
        click.echo(
            "Fatal: This command must be run in a directory containing a main.ipynb file or valid treebeard.yaml"
        )
        sys.exit(1)


def check_for_updates():
    version = get_version()

    pypi_data = requests.get("https://pypi.org/pypi/treebeard/json")
    latest_version = json.loads(pypi_data.text)["info"]["version"]

    if latest_version != version:
        click.echo(
            click.style(
                "🌲 Warning: you are not on the latest version of Treebeard, update with `pip install --upgrade treebeard`",
                fg="yellow",
            ),
            err=True,
        )


def get_service_status_message(service_status_url: str) -> Optional[str]:
    data = json.loads(requests.get(service_status_url).text)
    if "message" in data:
        return data["message"]
    return None


class TreebeardConfig(BaseModel):
    notebook: str = "main.ipynb"
    output_dirs: Tuple[str, ...] = tuple(["output"])
    ignore: Tuple[str, ...] = ()
    secret: Tuple[str, ...] = ()


def get_treebeard_config() -> Optional[TreebeardConfig]:
    config = "treebeard.yaml"
    if not os.path.exists(config):
        return None

    with open(config) as f:
        conf = yaml.load(f, Loader=yaml.FullLoader)
        return TreebeardConfig(**conf)
