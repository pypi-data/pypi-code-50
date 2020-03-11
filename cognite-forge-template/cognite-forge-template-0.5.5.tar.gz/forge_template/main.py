import logging
import sys
from typing import Callable, Dict, List, Mapping, Type

import click
from ruamel.yaml.parser import ParserError
from ruamel.yaml.scanner import ScannerError

from forge_template.exception.exceptions import AccessDeniedException, ValidationException
from forge_template.exception.handler import (
    handle_access_denied_error,
    handle_file_not_found,
    handle_parser_error,
    handle_validation_error,
)
from forge_template.handler.azure_handler import AzureHandler
from forge_template.handler.databricks_handler import DatabricksHandler
from forge_template.handler.github_actions_handler import GithubActionsHandler
from forge_template.handler.handler import BaseHandler
from forge_template.handler.powerbi_handler import PowerBIHandler
from forge_template.util.config_generator import ConfigGenerator
from forge_template.util.user_interface import UserInterface
from forge_template.util.yaml_util import (
    AZURE_CONFIG_NAME,
    DATABRICKS_CONFIG_NAME,
    POWERBI_CONFIG_NAME,
    YAML_CONFIG_PATH,
    YAML_CONFIG_SCHEMA_PATH,
    YAML_SECRETS_PATH,
    YAML_SECRETS_SCHEMA_PATH,
    assert_same_services,
    assert_scope_matches,
    load_and_validate_yaml,
    merge_dictionaries,
)

HANDLER_CLASSES: Mapping[str, Type[BaseHandler]] = {
    DATABRICKS_CONFIG_NAME: DatabricksHandler,
    AZURE_CONFIG_NAME: AzureHandler,
    POWERBI_CONFIG_NAME: PowerBIHandler,
}
LOGGING_FILE = "logs.log"


def instantiate_config() -> Dict:
    # Parse configs & secrets:
    config = load_and_validate_yaml(YAML_CONFIG_PATH, YAML_CONFIG_SCHEMA_PATH)
    secrets = load_and_validate_yaml(YAML_SECRETS_PATH, YAML_SECRETS_SCHEMA_PATH)

    # Assert that config files have the same services defined
    assert_same_services(config, secrets)

    # Assert that scopes matches
    assert_scope_matches(config, secrets)

    # Merge config files:
    merge_dictionaries(config, secrets)

    return config


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    logging.basicConfig(filename="logs.log", level=logging.INFO)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    UserInterface.print_title("Forge Template")
    logging.info(
        "If you have any questions that cannot be answered by the readme, please contact magnus.moan@cognite.com\n"
    )

    if ctx.invoked_subcommand is None:
        show_main_menu()
        UserInterface.print_title("Good bye!")


@cli.command()
@click.option("--project-name", "-n", prompt=True, help="name of project")
@click.option("--tool", "-t", type=click.Choice(HANDLER_CLASSES.keys(), case_sensitive=False))
def generate(project_name: str = "", tool: str = "") -> None:
    """ Generate a new config file """
    run_generate(project_name, tool)


@cli.command()
@click.option("--tool", "-t", type=click.Choice(HANDLER_CLASSES.keys(), case_sensitive=False))
def deploy(tool: str) -> None:
    """ Deploy configuration """
    run_deploy(tool)


@cli.command()
@click.option("--tool", "-t", type=click.Choice(HANDLER_CLASSES.keys(), case_sensitive=False))
def delete(tool: str = "") -> None:
    """ Delete resources mentioned in configuration """
    run_delete(tool)


@cli.command()
def upload_config() -> None:
    """ Upload config.yaml to Databricks """
    run_upload_config()


@cli.command()
@click.option("--tool", "-t", type=click.Choice(HANDLER_CLASSES.keys(), case_sensitive=False))
def pipeline(tool: str) -> None:
    """ Set up pipelines for automatic deployment """
    run_create_pipeline(tool)


@cli.resultcallback()
def process_result(_, __):
    UserInterface.print_title("Good bye!")


def run_generate(project_name: str = "", tool: str = ""):
    generator = ConfigGenerator(project_name)

    def generate_action(chosen_tool: str) -> None:
        is_custom = click.confirm(
            f"Do you want to do a custom configuration of {chosen_tool} (only recommended in very special cases)?",
            default=False,
            show_default=True,
        )
        generator.generate(chosen_tool, is_custom=is_custom)
        generator.preview()
        logging.info("\n")
        if click.confirm("Do you want to save the preview?"):
            generator.save()

    show_sub_menu("generate config for", generate_action, tool)


def run_deploy(tool: str = "") -> None:
    def deploy_action(chosen_tool: str) -> None:
        config = instantiate_config()
        handler = HANDLER_CLASSES[chosen_tool](chosen_tool, config)
        handler.run_create_preview()
        handler.run_print_preview()
        if click.confirm("Do you want to proceed?", default=False):
            handler.run_setup()
            UserInterface.print_ok(f"Successfully deployed {chosen_tool}")

    show_sub_menu("deploy", deploy_action, tool)


def run_delete(tool: str = "") -> None:
    def delete_action(chosen_tool: str) -> None:
        config = instantiate_config()
        handler = HANDLER_CLASSES[chosen_tool](chosen_tool, config)
        handler.run_delete_all_resources()
        UserInterface.print_ok(f"Successfully deleted {chosen_tool}")

    show_sub_menu("delete", delete_action, tool)


def run_upload_config() -> None:
    def upload_config_action() -> None:
        config = instantiate_config()
        handler = DatabricksHandler(DATABRICKS_CONFIG_NAME, config)
        handler.upload_config()

    do_action(upload_config_action)
    show_main_menu()


def run_create_pipeline(tool: str = "") -> None:
    def create_pipeline_action(chosen_tool: str) -> None:
        handler = GithubActionsHandler(chosen_tool)
        handler.print_preview()
        if click.confirm("Do you want to proceed?", default=False):
            handler.run_setup()
            UserInterface.print_ok(
                f"Successfully set up pipeline (still needs to be pushed to git) for {chosen_tool}. "
                f"In order for the pipeline to work, the {chosen_tool.upper()}_TOKEN "
                f"needs to be set in the Github repository secrets"
            )

    show_sub_menu("set up a deployment pipeline for", create_pipeline_action, tool)


def show_main_menu():
    exit_cmd = "e"
    generate_cmd = "Generate config"
    deploy_cmd = "Deploy config"
    delete_cmd = "Delete resources"
    upload_cmd = "Upload config.yaml to Databricks"
    pipeline_cmd = "Setup deployment pipeline"

    choice_to_action = {
        generate_cmd: run_generate,
        deploy_cmd: run_deploy,
        delete_cmd: run_delete,
        upload_cmd: run_upload_config,
        pipeline_cmd: run_create_pipeline,
    }

    ui = UserInterface()
    prompt = "What do you want to do?"
    choice = ui.get_menu_selection(prompt, list(choice_to_action.keys()), is_top_level=True)
    if choice != exit_cmd:
        choice_to_action[choice]()


def prompt_for_option(action: str, options: List[str]) -> str:
    ui = UserInterface()
    prompt = f"Which tool do you want to {action}?"
    return ui.get_menu_selection(prompt, options)


def show_sub_menu(action_str: str, action_handler: Callable[[str], None], user_option: str = "") -> None:
    exit_command = "e"
    menu_command = "m"
    tools = list(map(lambda x: x.capitalize(), HANDLER_CLASSES.keys()))

    if not user_option:
        user_option = prompt_for_option(action_str, tools)
    if user_option not in [menu_command, exit_command]:
        do_action(lambda: action_handler(user_option.lower()))
    if user_option != exit_command:
        show_main_menu()


def do_action(action: Callable[[], None]) -> None:
    try:
        action()
    except FileNotFoundError as e:
        handle_file_not_found(e)
    except (ParserError, ScannerError) as e:
        handle_parser_error(e)
    except ValidationException as e:
        handle_validation_error(e)
    except AccessDeniedException as e:
        handle_access_denied_error(e)
