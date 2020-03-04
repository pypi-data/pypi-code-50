import re
import os
import click
import inquirer
from alfa_cli.config import algorithm

FUNCTIONS = algorithm.initialization.functions
OPTIONS = algorithm.initialization.specification


def generate_specification():
    specification = {}

    specification["name"] = _prompt_field("Algorithm name", default=os.path.basename(os.getcwd()))
    specification["id"] = _prompt_field("Algorithm ID")
    specification["environment"] = _prompt_field("Environment name", default="production")
    specification["version"] = "0.0.1"
    specification["description"] = _prompt_field("Description")
    specification["functions"] = _generate_functions_specification()

    return specification


#


def _generate_functions_specification():
    functions_spec = []
    for function_type in FUNCTIONS.keys():
        to_generate = FUNCTIONS[function_type].required or _prompt_commit(
            f"Do you want to define a {_pprint_func(function_type)} function?"
        )
        if to_generate:
            spec = _generate_function_specification(function_type)
            functions_spec.append(spec)

    return functions_spec


def _generate_function_specification(function_type):
    provider_spec = {}
    provider_spec["architecture"] = _prompt_list(
        f"Architecture of the {_pprint_func(function_type)} function", OPTIONS.architectures.keys()
    )
    provider_spec["runtime"] = _prompt_list(
        f"Runtime of the {_pprint_func(function_type)} function", OPTIONS.runtimes
    )
    provider_spec["timeout"] = _round_timeout(
        _prompt_field(
            f"Timeout of the {_pprint_func(function_type)} function", type=int, default=900
        ),
        provider_spec["architecture"],
    )
    provider_spec["instance"] = _generate_instance_specification(
        function_type, provider_spec["architecture"]
    )

    function_spec = {"provider": provider_spec, "function": {"handler": "main.run"}}
    if provider_spec["runtime"] == "python":
        function_spec["package"] = {"exclude": ["*/venv/**"]}
    if provider_spec["runtime"] == "node":
        function_spec["package"] = {"exclude": ["*/node_modules/**"]}

    return {function_type: function_spec}


def _generate_instance_specification(function_type, architecture):
    instance_spec = {}
    for setting, values in OPTIONS.architectures[architecture].settings.items():
        if isinstance(values, dict):
            values = _get_setting_values(values, instance_spec)
        instance_spec[setting] = _prompt_list(
            f"{setting.title()} for the {function_type} function", values
        )

    return instance_spec


#


def _prompt_field(text, type=str, default=""):
    """Prompt the user to fill in the values in a field and return the value"""
    return click.prompt(text, type=type, default=default)


def _prompt_list(text, choices):
    """Prompt the user to select one item from a list of options and return the selected value"""
    return inquirer.prompt([inquirer.List("value", message=text, choices=choices)])["value"]


def _prompt_commit(text):
    return click.confirm(text)


#


def _round_timeout(timeout, architecture):
    return min(max(0, timeout), OPTIONS.architectures[architecture].timeout.max)


def _get_setting_values(settings, instance_spec):
    for setting, values in settings.items():
        key, value = setting.split("==")
        if str(instance_spec[key]) == value:
            return values

    raise ValueError("Invalid instance specification.")


#


def _pprint_func(function_type):
    return "-".join(re.sub(r"([A-Z])", r" \1", function_type).split()).lower()
