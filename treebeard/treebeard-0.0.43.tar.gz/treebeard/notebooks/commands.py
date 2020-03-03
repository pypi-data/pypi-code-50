import glob
import json
import os
import os.path
import sys
import tarfile
import tempfile
import time
from datetime import datetime
from typing import Any, List

import click
import requests
from dateutil import parser
from halo import Halo  # type: ignore
from humanfriendly import format_size, parse_size  # type: ignore
from timeago import format as timeago_format  # type: ignore

from treebeard.conf import notebooks_endpoint
from treebeard.helper import (
    get_config_path,
    get_treebeard_env,
    get_time,
    validate_notebook_directory,
    get_treebeard_config,
)

config_path = get_config_path()

treebeard_env = get_treebeard_env()
notebook_id = treebeard_env["notebook_id"]


@click.command()
@click.option("t", "--hourly", flag_value="hourly", help="Run notebook hourly")
@click.option("t", "--daily", flag_value="daily", help="Run notebook daily")
@click.option("t", "--weekly", flag_value="weekly", help="Run notebook weekly")
@click.option(
    "t", "--quarter-hourly", flag_value="quarter-hourly", help="Run quarter-hourly"
)
@click.option(
    "watch", "--watch", is_flag=True, help="Run and check completed build status"
)
@click.option(
    "-i",
    "--ignore",
    help="Don't submit unneeded virtual envs and large files",
    multiple=True,
)
def run(t: str, watch: bool, ignore: List[str]):
    """
    Run a notebook and optionally schedule it to run periodically
    """

    validate_notebook_directory()

    params = {}
    if t:
        params["schedule"] = t

    spinner: Any = Halo(text="🌲  zipping directory\n", spinner="dots")
    spinner.start()

    treebeard_config = get_treebeard_config()
    if treebeard_config:
        ignore += treebeard_config.ignore + treebeard_config.secret

    # Create a temporary file for the compressed directory
    # compressed file accessible at f.name
    # git_files: Set[str] = set(
    #     subprocess.check_output(
    #         "git ls-files || exit 0", shell=True, stderr=subprocess.DEVNULL
    #     )
    #     .decode()
    #     .splitlines()
    # )

    with tempfile.NamedTemporaryFile("wb", suffix=".tar.gz", delete=False) as f:
        with tarfile.open(fileobj=f, mode="w:gz") as tar:

            def zip_filter(info: tarfile.TarInfo):
                for ignored in ignore:
                    if info.name in glob.glob(ignored):
                        return None

                # if len(git_files) > 0 and info.name not in git_files:
                #     return None
                click.echo(f"Including {info.name}")
                return info

            tar.add(
                os.getcwd(), arcname=os.path.basename(os.path.sep), filter=zip_filter
            )
            tar.add(config_path, arcname=os.path.basename(config_path))
    spinner.text = "🌲  submitting notebook to runner\n"
    size = os.path.getsize(f.name)
    max_upload_size = "100MB"
    if size > parse_size(max_upload_size):
        click.echo(
            click.style(
                (
                    f"ERROR: Compressed notebook directory is {format_size(size)},"
                    f" max upload size is {max_upload_size}. \nPlease ensure you ignore any virtualenv subdirectory"
                    " using `treebeard run --ignore venv`"
                ),
                fg="red",
            )
        )
        quit(1)

    response = requests.post(
        notebooks_endpoint,
        files={"repo": open(f.name, "rb")},
        params=params,
        headers=treebeard_env,
    )

    if response.status_code != 200:
        raise click.ClickException(f"Request failed: {response.text}")

    spinner.stop()
    try:
        json_data = json.loads(response.text)
        click.echo(f"✨  Run has been accepted! {json_data['admin_url']}")
    except:
        click.echo("❗  Request to run failed")
        click.echo(sys.exc_info())

    if watch:
        # spinner = Halo(text='watching build', spinner='dots')
        # spinner.start()
        build_result = None
        while not build_result:
            time.sleep(5)
            response = requests.get(notebooks_endpoint, headers=treebeard_env)
            json_data = json.loads(response.text)
            status = json_data["runs"][-1]["status"]
            click.echo(f"{get_time()} Build status: {status}")
            if status == "SUCCESS":
                build_result = status
                # spinner.stop()
                click.echo(f"Build result: {build_result}")
            elif status in ["FAILURE", "TIMEOUT", "INTERNAL_ERROR", "CANCELLED"]:
                click.echo(f"Build failed")
                build_result = status
                sys.exit(1)


@click.command()
def cancel():
    """Cancels the current notebook build and schedule"""
    validate_notebook_directory()
    spinner: Any = Halo(text="cancelling", spinner="dots")
    click.echo(f"🌲  Cancelling {notebook_id}")
    spinner.start()
    requests.delete(notebooks_endpoint, headers=treebeard_env)  # type: ignore
    spinner.stop()
    click.echo(f"🛑 Done!")


@click.command()
def status():
    """Show the status of the current notebook"""
    validate_notebook_directory()
    response = requests.get(notebooks_endpoint, headers=treebeard_env)
    if response.status_code != 200:
        raise click.ClickException(f"Request failed: {response.text}")

    json_data = json.loads(response.text)
    if len(json_data) == 0:
        click.echo(
            "This notebook has not been run. Try running it with `treebeard run`"
        )
        quit(1)
    click.echo("🌲  Recent runs:\n")

    max_results = 10
    status_emoji = {
        "SUCCESS": "✅",
        "QUEUED": "💤",
        "WORKING": "⏳",
        "FAILURE": "❌",
        "TIMEOUT": "⏰",
        "CANCELLED": "🛑",
    }

    for run in json_data["runs"][-max_results:]:
        now = parser.isoparse(datetime.utcnow().isoformat() + "Z")
        start_time = parser.isoparse(run["start_time"])
        time_string: str = timeago_format(start_time, now=now)
        click.echo(f"{status_emoji[run['status']]}  {time_string} {run['url']}")

    if "schedule" in json_data:
        click.echo(f"\n📅  Schedule: {json_data['schedule']}")
