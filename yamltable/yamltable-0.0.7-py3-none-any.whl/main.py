"""Command line interface for YamlTable."""


import enum
import pathlib
import pprint
from typing import List, Optional, Tuple

import typer

import yamltable
from yamltable.typing import Row, Schema


FileArg = typer.Argument(..., dir_okay=False, exists=True, file_okay=True, resolve_path=True)


app = typer.Typer(
    help="Utility for working with YAML files organized similar to a relational database table."
)


class Code(enum.Enum):
    """Exit code statuses."""

    SUCCESS = 0
    INVALID = 1
    ERROR = 2


class Msg(enum.Enum):
    """Colors for message types."""

    EMPTY = typer.colors.YELLOW
    ERROR = typer.colors.RED
    SUCCESS = typer.colors.BRIGHT_GREEN


@app.command(name="index")
def index_(index: int, file_path: pathlib.Path = FileArg) -> None:
    """Get row at INDEX in FILE_PATH."""

    rows, _ = load_data(file_path)
    try:
        typer.echo(rows[index])
    except IndexError:
        typer.secho(f"error: {index} is out of bounds", fg=Msg.ERROR.value)
        typer.Exit(code=Code.ERROR.value)


@app.command(name="list")
def list_(key: str, file_path: pathlib.Path = FileArg) -> None:
    """List all dictionary KEY values in FILE_PATH."""

    rows, _ = load_data(file_path)
    for idx, row in enumerate(rows):
        try:
            typer.echo(row[key])
        except KeyError:
            typer.secho(f"error: row {idx} does not have key {key}", fg=Msg.ERROR.value)
            typer.Exit(code=Code.ERROR.value)
            break


def load_data(file_path: pathlib.Path) -> Tuple[List[Row], Optional[Schema]]:
    """Attempt to load data from YAML file.

    Args:
        file_path: YAML file path

    Return:
        YAML row data, YAML schema
    """

    try:
        return yamltable.read(file_path)
    except (FileNotFoundError, TypeError) as xcpt:
        typer.secho(str(xcpt), fg=Msg.ERROR.value)
        raise typer.Exit(code=Code.ERROR.value)


@app.command()
def search(key: str, value: str, file_path: pathlib.Path = FileArg) -> None:
    """Search for all dictionaries in FILE_PATH with matching KEY and VALUE pairs."""

    rows, _ = load_data(file_path)

    count = 0
    for match in yamltable.search(key, value, rows):
        count += 1
        typer.echo(pprint.pformat(match, indent=2))

    if count == 0:
        typer.secho(
            f"no dictionaries found with (key={key}, value={value}) pair", fg=Msg.EMPTY.value
        )


@app.command()
def sort(key: str, file_path: pathlib.Path = FileArg) -> None:
    """Sort dictionaries in FILE_PATH by KEY values."""

    rows, schema = load_data(file_path)
    try:
        sorted_rows = yamltable.sort(key, rows)
    except TypeError as xcpt:
        typer.secho(f"error: {xcpt}", fg=Msg.ERROR.value)
        typer.Exit(code=Code.ERROR.value)
    else:
        yamltable.write(file_path, sorted_rows, schema)


@app.command()
def validate(file_path: pathlib.Path = FileArg) -> None:
    """Check that every dictionary in FILE_PATH has conforms to its schema."""

    rows, schema = load_data(file_path)
    valid, row, msg = yamltable.validate(rows, schema)
    if valid:
        typer.secho("YAML file rows conform to its schema", fg=Msg.SUCCESS.value)
    elif row == -1:
        typer.secho(f"invalid schema: {msg}", fg=Msg.ERROR.value)
        typer.Exit(code=Code.ERROR.value)
    else:
        typer.secho(f"invalid row {row}: {msg}", fg=Msg.ERROR.value)
        typer.Exit(code=Code.INVALID.value)


if __name__ == "__main__":
    app()
