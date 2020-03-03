import click

from treebeard.helper import env, get_treebeard_env

if env == "development":
    click.echo("WARNING: RUNNING IN LOCAL MODE")
    url = "http://localhost:8080"
    treebeard_web_url = "http://localhost:8000"
else:
    url = "https://scheduler-cvee2224cq-ew.a.run.app"
    treebeard_web_url = "https://treebeard.io"


treebeard_env = get_treebeard_env()
project_id = treebeard_env["project_id"]
notebook_id = treebeard_env["notebook_id"]
secrets_endpoint = f"{url}/projects/{project_id}/notebooks/{notebook_id}/secrets"
notebooks_endpoint = f"{url}/notebooks/{notebook_id}"
signup_endpoint = f"{url}/cli_signup"
service_status_endpoint = f"{url}/service_status"
