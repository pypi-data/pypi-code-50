import collections
import os
import re
from typing import Dict, Optional, Tuple

from cerberus import Validator
from ruamel.yaml import YAML

from forge_template.exception.exceptions import ValidationException

SCHEMA_FOLDER = os.path.join(os.path.dirname(__file__), "..", "schema")
YAML_CONFIG_PATH = "config.yaml"
YAML_SECRETS_PATH = "secrets.yaml"
YAML_CONFIG_SCHEMA_PATH = os.path.join(SCHEMA_FOLDER, "config_schema.yaml")
YAML_SECRETS_SCHEMA_PATH = os.path.join(SCHEMA_FOLDER, "secrets_schema.yaml")

PIPELINES_PATH = "pipelines"

DATABRICKS_CONFIG_NAME = "databricks"
GITHUB_CONFIG_NAME = "github"
AZURE_CONFIG_NAME = "azure"
POWERBI_CONFIG_NAME = "powerbi"


def load_yaml(path: str) -> dict:
    yaml_reader = YAML(typ="safe")

    with open(path, encoding="utf-8") as f:
        dct = yaml_reader.load(f)
        assert isinstance(dct, dict), f"YAML malformatted, couldn't load into dict (got {type(dct)})"
        return dct


def validate_yaml(schema_path: str, document: Dict) -> Tuple[bool, Optional[Dict]]:
    schema = load_yaml(schema_path)
    validator = Validator(schema)
    return validator.validate(document), validator.errors or None


def load_and_validate_yaml(path: str, schema_path: str) -> Dict:
    loaded_yaml = load_yaml(path)
    is_valid, errors = validate_yaml(schema_path, loaded_yaml)
    if not is_valid:
        raise ValidationException(f"Validation of {path} failed.\n{errors}")
    return loaded_yaml


def assert_same_services(config: Dict, secrets: Dict) -> None:
    config_set = set(config.keys())
    secrets_set = set(secrets.keys())
    is_valid = config_set == secrets_set
    diff = {}
    if len(config_set - secrets_set) != 0:
        diff["secret.yaml is missing"] = config_set - secrets_set
    if len(secrets_set - config_set) != 0:
        diff["config.yaml is missing"] = secrets_set - config_set

    assert is_valid, f"YAML files don't contain the same services defined. Differences:\n{diff}"


def merge_dictionaries(dict_a: Dict, dict_b: Dict) -> None:
    for k, v in dict_b.items():
        if k in dict_a and isinstance(dict_a[k], dict) and isinstance(dict_b[k], collections.Mapping):
            merge_dictionaries(dict_a[k], dict_b[k])
        else:
            dict_a[k] = dict_b[k]


def assert_is_email(s: str) -> bool:
    regex = re.compile(r"^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$")
    return re.search(regex, s) is not None


def assert_scope_matches(config: Dict, secrets: Dict) -> None:
    if "databricks" in config and "databricks" in secrets:
        for stage in ["production", "development"]:
            name_in_config = config["databricks"][stage]["scope"]["name"]
            name_in_secrets = secrets["databricks"][stage]["scope"]["name"]
            assert name_in_config == name_in_secrets is not None, (
                f"Mismatch between scope name in '{YAML_CONFIG_PATH}' ({name_in_config}) and "
                f"'{YAML_SECRETS_PATH}' ({name_in_secrets})."
            )
