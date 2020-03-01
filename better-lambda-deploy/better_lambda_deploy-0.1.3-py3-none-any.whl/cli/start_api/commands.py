from ...deployer import Deployer
import click


@click.command()
@click.option("--name", default="local", help="The name of the project to run.")
@click.option("--dir", default="./", help="The directory to deploy as a BLD project.")
def start_api(name, dir):
    deployer = Deployer(name, dir)
    deployer.start_api()
