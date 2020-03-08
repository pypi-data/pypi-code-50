import argparse
import logging
import os
import sys

import coloredlogs
import ruamel.yaml

from efitness_sniper.efitness import Client


def load_config(config_path: str) -> dict:
    yaml = ruamel.yaml.YAML(typ="safe")
    config = yaml.load(os.path.expanduser(os.path.expandvars(config_path)))
    with open(config) as stream:
        return yaml.load(stream)


def main() -> None:
    # Create a logger object.
    logger = logging.getLogger(__name__)
    coloredlogs.install(level="INFO")
    logger.info("eFitness Booking Sniper - Marek Wajdzik 2020 <marek@wajdzik.eu>")
    # Setup argument parser
    parser = argparse.ArgumentParser(
        description="eFitness Booking Sniper - Marek Wajdzik 2020 <marek@wajdzik.eu>"
    )
    parser.add_argument(
        "-c",
        "--config",
        type=str,
        help="eFitness sniper config file",
        required=False,
        default="~/.efitness.yml",
    )
    app_args = parser.parse_args()
    # Try to load app configuration
    try:
        config = load_config(app_args.config)
    except FileNotFoundError:
        logger.info("Cannot load configuration.")
        sys.exit(1)
    # Setup eFitness client class
    efitness = Client(
        club_subdomain=config["login_data"]["subdomain"],
        user=config["login_data"]["user"],
        password=config["login_data"]["password"],
    )
    # Try login
    efitness.login()
    # Execute sniper rules
    efitness.check_and_book(config["sniper_rules"])
