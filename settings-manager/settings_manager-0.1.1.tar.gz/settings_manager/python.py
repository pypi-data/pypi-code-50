from typing import (
    Dict,
    Any
)

from importlib import import_module, reload
import re

CONFIG_VAR_RE  = re.compile(r"^[A-Z_]+[A-Z_0-9]*$")

def load_python_file_data(module_path: str) -> Dict[str, Any]:

    mod = import_module(module_path)
    mod_dict = mod.__dict__

    settings = {}

    for k in mod_dict.keys():
        if CONFIG_VAR_RE.match(k):
            settings[k] = mod_dict[k]

    return settings