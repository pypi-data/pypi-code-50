"""Library functions for YamlTable."""


import pathlib
from typing import Any, Iterable, List, Optional, Tuple

import fastjsonschema
import yaml
from yamltable.typing import Row, Schema


def read(file_path: pathlib.Path) -> Tuple[List[Row], Optional[Schema]]:
    """Read data from YAML file.

    Args:
        file_path: YAML file path

    Raises:
        FileNotFoundError: if unable to find file path
        TypeError: if file is not organized as a list

    Return:
        YAML data
    """

    try:
        with open(file_path, "r") as handle:
            data = yaml.safe_load(handle)
    except (yaml.scanner.ScannerError, yaml.parser.ParserError) as xcpt:
        raise TypeError(f"invalid YAML file: {xcpt}")

    if isinstance(data, list):
        return data, None
    elif isinstance(data, dict):
        try:
            return data["rows"], data["schema"]
        except KeyError:
            raise TypeError("YAML file does not have a schema and rows organization")
    else:
        raise TypeError("YAML file is not organized in a tabular format")


def search(key: str, val: Any, rows: Iterable[Row]) -> List[Row]:
    """Search dictionaries by key and value.

    Args:
        key: search key
        val: key comparison value
        rows: dictionaries to search

    Return:
        matching dictionaries
    """

    return [row for row in rows if key in row and row[key] == val]


def sort(key: str, rows: Iterable[Row]) -> List[Row]:
    """Sort dictionaries based on value for supplied key name.

    Args:
        key: search key
        rows: dictionaries to sort

    Return:
        list of sorted dictionaries
    """

    return sorted(rows, key=lambda row: row[key])


def validate(rows: Iterable[Row], schema: Optional[Schema]) -> Tuple[bool, int, str]:
    """Check that each row satisfies the schema.

    Args:
        rows: dictionaries to validate
        schema: JSON schema for validation

    Return:
        whether all rows are valid, invalid row index or -1, invalid error message
    """

    try:
        validator = fastjsonschema.compile(schema)
    except (fastjsonschema.JsonSchemaDefinitionException, TypeError) as xcpt:
        return False, -1, f"invalid schema: {xcpt}"

    for idx, row in enumerate(rows):
        try:
            validator(row)
        except fastjsonschema.JsonSchemaException as xcpt:
            return False, idx, xcpt.message

    return True, -1, ""


def write(
    file_path: pathlib.Path,
    rows: List[Row],
    schema: Optional[Schema] = None,
    sort_keys: bool = False,
) -> None:
    """Write data to YAML file.

    Args:
        file_path: YAML file path
        rows: list of dictionaries to write
        schema: JSON schema dictionary
        sort_keys: whether to sort row keys
    """

    if schema is None:
        with open(file_path, "w") as handle:
            yaml.dump(rows, handle, sort_keys=sort_keys)
    else:
        data = {"schema": schema, "rows": rows}
        with open(file_path, "w") as handle:
            yaml.dump(data, handle, sort_keys=sort_keys)
