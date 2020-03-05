"""Command-line interface of `glosm`."""

import glosm
import glosm.core
from enum import Enum
from sys import argv
from json import dumps
from typing import Any


class Commands(Enum):
    """Legal glosm commands."""

    delete = "del"
    get = "get"
    help = "help"
    set = "set"


HELP = f"""glosm {glosm.__version__} (default secrets path: {glosm.core.DEFAULT_PATH_SECRETS_FILE})

    Usage:
        glosm del KEY [KEY, ...]
        glosm get [KEY...]
        glosm set KEY [KEY, ...] SECRET
        glosm help

    Examples:

        glosm del key1 key2
            Delete key2 and its secret inside key1.

        glosm get
            Print all secrets.

        glosm get aws 4334433453 "joe the plumber" aws_access_key_id
            Get a specific secret.

        glosm set foo bar
            Sets secret stored under key `foo` to `bar`.

        glosm set foo bar baz
            Sets secret stored in key `bar` inside secret under key `foo` to `baz`.

        glosm help
            Print these help instructions.
    """


def formatted(secret: Any) -> str:
    """Format secret for stdout.

    We want list, tuples, and dicts to be formatted as valid JSON strings. The rest does not need to be valid JSON,
    because we assume it is already formatted properly as a secret.

    If we pass all secrets to `json.dumps`, then strings, and possibly other types, will be printed to stdout with
    surrounding double quotes, which we don't want to happen. We want `some_value` string to appear as `some_value`
    in stdout and not `"some_value"`. This will ensure shell commands like `PASSWORD=$(glosm get aws root)` work
    properly.
    """
    if isinstance(secret, (list, tuple, dict)):
        return dumps(secret, indent=2)
    return str(secret)


def execute() -> None:
    """Run a glosm command.

    The `argv` variable is assumed to contain: glosm [GLOSM_COMMAND [glosm_args...]].
    """
    if len(argv) == 1:
        print(HELP)
        return

    glosm_command = argv[1]
    glosm_args = argv[2:]

    if glosm_command == Commands.get.value:
        print(formatted(glosm.core.get(*glosm_args)))

    elif glosm_command == Commands.set.value:
        glosm.core.set_secret(glosm_args[-1], *glosm_args[:-1])

    elif glosm_command == Commands.delete.value:
        glosm.core.delete(*glosm_args)

    elif glosm_command == Commands.help.value:
        print(HELP)

    else:
        raise ValueError(f"No such command {glosm_command}")
