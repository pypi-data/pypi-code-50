"""Core API."""

import os
import json
import warnings

from typing import Dict, Union, List, Tuple, NoReturn
from functools import lru_cache


DEFAULT_PATH_SECRETS_FILE = "~/.glosm.json"


SecretsKey = Union[int, float, str]
SecretsValue = Union["SecretsDict", str, int, float, List[Union["SecretsDict", str, int, float]]]


class CustomJsonDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    @staticmethod
    def object_hook(obj):
        if isinstance(obj, dict):
            return SecretsDict(obj)
        return obj


class SecretsDict(dict):
    """A data structure representing secrets dictionary.

    We need custom data structure to allow us to get and set values deep into the dictionary, for an any
    sequence of keys. Using standard dictionary would be possible but would lead to boilerplate.

    When setting a secret for some sequence say ["a", "b", "c"] we automatically create any missing keys. For example
    if our secrets are: {"a": "aa", "d": "dd"} and then we set secrets["a", "b", "c"] = "cc", our secrets will become
    {"a": {"b": {"c": "cc"}}, "d": "dd}. So we overwrote the existing value in "a" and created two nested dictionaries.
    """

    def __getitem__(self, keys) -> SecretsValue:
        """Returns object located at secrets_dict[keys[0]][keys[1]][...].

        When multiple keys are supplied inside square brackets this method will receive them in a tuple. When single key
        is passed, then this method receives just this key. For example, when you run `secrets_dict["a", "b", "c"]`,
        the `keys` parameter this method received will be `("a", "b", "c")` tuple. When you run `secrets_dict["foo"],
        the `keys` will be `"foo"` string.
        """

        keys = (keys,) if not isinstance(keys, tuple) else keys  # Convert or we end up iterating over a string.
        secret = self
        for key in keys:

            if not isinstance(secret, dict):
                raise TypeError(f"Cannot get key `{key}`. Secret is not a dict, but `{type(secret)}`")

            if key not in secret:
                raise KeyError(f"Key `{key}` is not present in object `{secret}` of type `{type(secret)}`.")

            secret = dict.__getitem__(secret, key)

        return secret

    def __setitem__(self, keys, value) -> NoReturn:
        """Sets a specific part of the SecretsDict to the supplied value.

        When multiple keys are supplied inside square brackets this method will receive them in a tuple. When single key
        is passed, then this method receives just this key. For example, when you run
        `secrets_dict["a", "b", "c"] = 123`, the `keys` parameter this method received will be `("a", "b", "c")` tuple.
        When you run `secrets_dict["foo"] = 123, the `keys` will be `"foo"` string.
        """

        if not keys:
            raise RuntimeError("You must provide keys when setting a secret.")

        keys = (keys,) if not isinstance(keys, tuple) else keys  # Convert or we end up iterating over a string.

        secret = self
        for key in keys[:-1]:

            if key not in secret:
                secret[key] = dict()

            secret = secret[key]

        dict.__setitem__(secret, keys[-1], value)

    def __delitem__(self, keys):
        """Deletes the secret located at specified keys. The keys parameter is same as described in `__getitem__()`."""

        if not keys:
            raise RuntimeError("You must provide keys when deleting a secret.")

        keys = (keys,) if not isinstance(keys, tuple) else keys  # Convert or we end up iterating over a string.

        secret = self
        for key in keys[:-1]:

            if key not in secret:
                secret[key] = dict()

            secret = secret[key]

        if not isinstance(secret, dict):
            raise TypeError(f"Unable to delete key `{keys[-1]}` inside object that is not dict but `{type(secret)}`.")
        dict.__delitem__(secret, keys[-1])


@lru_cache(maxsize=128)
def _secrets(path_secrets_file: str = None) -> SecretsDict:

    with open(os.path.expanduser(path_secrets_file or DEFAULT_PATH_SECRETS_FILE), "r") as f:
        return SecretsDict(json.load(f, cls=CustomJsonDecoder))


def _dereferenced(secrets: SecretsValue, secrets_path: List[SecretsKey] = None) -> SecretsValue:
    """Returns dereferenced secrets.

    A reference to a glosm secret is a list of two or more elements, with first element being the sentinel, representing
    the root of glosm. For example, if sentinel value is "$glosm" then a valid glosm reference is
    `["$glosm", "accounts", "joe"]` and it will be dereferenced by calling `get("accounts", "joe"). Dereferenced values
    may themselves contain glosm references, e.g. turtles all the way down.

    Glosm references help avoid repetition.

    Secrets are dereferenced recursively. Circular references are possible because we do not check for their presence
    because they are meaningless and we assume users will not make this mistake. Dereferencing circular values will
    crash glosm with `RunTimeError`.

    Glosm may also crash with deeply nested references because this function is recursive and Python limits recursion
    depth.
    """
    secrets_path = secrets_path or []

    legacy_glosm_path_sentinel = "$glosm"
    glosm_path_sentinel = "_glosm_root_"

    if isinstance(secrets, SecretsDict) and len(secrets) > 0:
        for k in secrets:
            secrets[k] = _dereferenced(secrets=secrets[k], secrets_path=secrets_path + [k])

    if isinstance(secrets, list) and len(secrets) > 0:

        if secrets[0] == legacy_glosm_path_sentinel:
            warnings.warn(
                "Sentinel value `$glosm` will be replaced by `_glosm_root_` in version 1.0.0.", DeprecationWarning
            )

        if secrets[0] in {legacy_glosm_path_sentinel, glosm_path_sentinel}:
            referenced_path = secrets[1:]

            if referenced_path == secrets_path[0 : len(referenced_path)]:
                # reference_path may not be ancestor of secrets_path and it may not be same as secrets_path
                raise ValueError(
                    (
                        f"Detected circular reference: secret in path {secrets_path} ",
                        "references secret in {referenced_path}.",
                    )
                )

            secrets = get(*referenced_path)
            secrets = _dereferenced(secrets=secrets, secrets_path=secrets_path)
        else:
            secrets = [_dereferenced(secrets=s, secrets_path=secrets_path) for s in secrets]

    return secrets


def get(*path: str) -> SecretsValue:
    """Get a secret, specified by one or more keys. Without any keys, return all secrets.

    The keys are traversed recursively. If `get()` returns `{1: {2: {3: 4}}}` then `get(1, 2, 3)` will return `4`.
    """
    if not path:
        return _secrets()

    secrets = _secrets()[path]
    secrets = _dereferenced(secrets=secrets, secrets_path=list(path))
    return secrets


def _save_to_file(path_secrets_file: str, secrets: Union[SecretsDict, dict]):
    with open(os.path.expanduser(path_secrets_file), "w") as f:
        json.dump(secrets, f, indent=4)


def set_secret(secret, *path):

    updated_secrets = _secrets()
    updated_secrets.__setitem__(keys=path, value=secret)

    if not path and not isinstance(secret, dict):
        TypeError("Secret must be a dict when writing it to root level.")

    _save_to_file(path_secrets_file=DEFAULT_PATH_SECRETS_FILE, secrets=updated_secrets)


def delete(*path):
    updated_secrets = _secrets()
    updated_secrets.__delitem__(path)
    _save_to_file(path_secrets_file=DEFAULT_PATH_SECRETS_FILE, secrets=updated_secrets)
