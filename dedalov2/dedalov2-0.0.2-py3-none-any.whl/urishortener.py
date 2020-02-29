
import os
from typing import Dict, Optional

prefix_map: Dict[str, str] = {}


def setPrefixMapFromFile(filename: Optional[str]) -> None:
    prefixes: Dict[str, str] = {}
    if filename is not None:
        if not os.path.isfile(filename):
            raise ValueError("File {} not found!".format(filename))
        with open(filename) as fin:
            no_empty_lines = filter(lambda line: len(line) > 0, fin.readlines())
            no_commented_lines = filter(lambda line: line[0] != "#", no_empty_lines)
            stripped_lines = map(lambda line: line.strip(), no_commented_lines)
            for line in stripped_lines:
                abbr, prefix = line.split()
                prefixes[prefix] = abbr
    setPrefixMap(prefixes)


def setPrefixMap(pm: Dict[str, str]) -> None:
    global prefix_map
    prefix_map = pm


def shorten(uri: str) -> str:
    if prefix_map is None or len(prefix_map) == 0:
        return uri
    else:
        replaced = __replace_prefix(uri, "#")
        if replaced != uri:
            return replaced
        else:
            return __replace_prefix(uri, "/")


def __replace_prefix(uri: str, sep: str) -> str:
    try:
        protocol, rest = uri.split("//", maxsplit=1)
        parts = rest.split(sep)
        for i in reversed(range(1, len(parts))):
            pref = "{}//{}{}".format(protocol, sep.join(parts[:i]), sep)
            if pref in prefix_map:
                return uri.replace(pref, "{}:".format(prefix_map[pref]), 1)
    except IndexError:
        pass
    return uri
