import os
import re
import sys
from typing import Any, Callable, Dict, List, Union

import click
from cerberus import Validator
from ruamel.yaml import YAML

from forge_template.util.user_interface import UserInterface
from forge_template.util.yaml_util import (
    YAML_CONFIG_PATH,
    YAML_CONFIG_SCHEMA_PATH,
    YAML_SECRETS_PATH,
    YAML_SECRETS_SCHEMA_PATH,
    load_yaml,
)


class ConfigGenerator:
    def __init__(self, project_name: str = ""):
        while not re.match(r"^[-\w_]+$", project_name):
            print("\nPlease enter a project name (string containing only letters, numbers, '_' and '-')")
            project_name = click.prompt("Project name", type=click.STRING)

        self.project_name = project_name
        self.ui = UserInterface()
        self.config: Dict[str, Any] = {}
        self.secrets: Dict[str, Any] = {}
        self.config_schema = load_yaml(YAML_CONFIG_SCHEMA_PATH)
        self.secrets_schema = load_yaml(YAML_SECRETS_SCHEMA_PATH)

        if os.path.exists(YAML_CONFIG_PATH):
            self.config = load_yaml(YAML_CONFIG_PATH)

        if os.path.exists(YAML_SECRETS_PATH):
            self.secrets = load_yaml(YAML_SECRETS_PATH)

    def generate(self, tool: str, is_custom: bool = False) -> None:
        self.config[tool] = self.__generate_config(tool, self.config_schema[tool], is_custom=is_custom)
        self.secrets[tool] = self.__generate_config(tool, self.secrets_schema[tool], is_custom=is_custom)

    def preview(self) -> None:
        yaml = YAML()
        print()
        self.ui.print_ok("Preview: config.yaml")
        yaml.dump(self.config, sys.stdout)

        print()
        self.ui.print_ok("Preview: secrets.yaml")
        yaml.dump(self.secrets, sys.stdout)

    def save(self) -> None:
        yaml = YAML()
        print()
        with open(YAML_CONFIG_PATH, "w") as f:
            yaml.dump(self.config, f)
            self.ui.print_ok("Saved config.yaml")

        with open(YAML_SECRETS_PATH, "w") as f:
            yaml.dump(self.secrets, f)
            self.ui.print_ok("Saved secrets.yaml")

    @staticmethod
    def __get_current_tool_config(tool: str, config: Dict[str, Any]) -> Dict[str, Any]:
        return config[tool] if tool in config.keys() else {}

    def __generate_config(
        self, key: str, schema: Dict[str, Any], is_custom: bool = False
    ) -> Union[Dict[str, Any], str, List[str]]:
        config = {}

        if type(schema) is dict:
            if schema["type"] == "dict":
                for key, values in schema["schema"].items():
                    config[key] = self.__generate_config(key, values, is_custom)

            elif schema["type"] == "list" and schema["schema"]["type"] == "dict":
                keys = list(dict(schema["schema"]["schema"]).keys())
                return self.ui.get_input_list_of_dicts(
                    schema["meta"]["prompt"],
                    validators=self.__get_list_of_dict_validators(schema["schema"]["schema"]),
                    keys=keys,
                )
            else:
                default_value = self.__get_default_value(key, schema, self.project_name)
                if not is_custom and default_value is not None:
                    return default_value
                else:
                    transform = self.__get_transformer(schema)
                    user_input = self.ui.get_input(
                        schema["meta"]["prompt"],
                        default=default_value if default_value else "",
                        validate=self.__validate(key, schema, transform),
                    )
                    return transform(user_input)

        return config

    def __validate(
        self, key: str, schema: Dict[str, Any], transform: Callable[[str], Any] = None
    ) -> Callable[[str], bool]:
        v = Validator({key: schema})

        def check_regex(input_value: str) -> bool:
            if transform:
                input_value = transform(input_value)
            is_valid = v.validate({key: input_value})
            if not is_valid:
                if "meta" in schema and "help" in schema["meta"]:
                    self.ui.print_warning(f"Explanation: {schema['meta']['help']}")
                self.ui.print_warning(f"Error message: {v.errors}")
            return is_valid

        return check_regex

    def __get_transformer(self, schema: Dict[str, Any]) -> Callable[[str], Any]:
        if schema["type"] == "list":
            return self.__transform_list
        else:
            return self.__base_transform

    def __get_list_of_dict_validators(self, schema: Dict[str, Any]) -> Dict[str, Callable[[str], bool]]:
        validators = {}
        for key in schema:
            validators[key] = self.__validate(key, schema[key])

        return validators

    @staticmethod
    def __transform_list(input_value: str) -> List[str]:
        return list(map(lambda x: x.strip(), input_value.split(",")))

    @staticmethod
    def __base_transform(input_value: str) -> str:
        return input_value.strip()

    @staticmethod
    def __get_default_value(key: str, schema: Dict[str, Any], project_name: str) -> Union[str, None]:
        if "default" in schema:
            value = schema["default"]
            if "<PROJECT_NAME>" in value:
                default_value = value.replace("<PROJECT_NAME>", project_name)
                if key == "database_name":
                    default_value = default_value.replace("-", "_").replace(" ", "_")
                return default_value
            return value
        return None
