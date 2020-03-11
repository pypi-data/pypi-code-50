import base64
import os
import posixpath
import re
import shutil
from typing import List, Tuple, Union


def copy_folders(src: str, dest: str, ignore: Union[List[str], str] = "", overwrite: bool = False) -> None:
    if overwrite or not os.path.exists(dest):
        if ignore:
            if isinstance(ignore, str):
                ignore = [ignore]
            shutil.copytree(src, dest, ignore=shutil.ignore_patterns(*ignore))
        else:
            shutil.copytree(src, dest)


def prepare_rel_posix_path(path: str) -> str:
    """
        Prepare any path in posix format and remove first slash if present
    """
    split_path = re.split(r"\\{1,}|/{1,}", path)
    remove_empty_path = list(filter(None, split_path))
    posix_path = "/".join(remove_empty_path)

    return posix_path


def get_absolute_posix_path(prefix: str, suffix: str = "") -> str:
    prefix = prepare_rel_posix_path(prefix)
    prefix = posixpath.join(posixpath.sep, prefix)
    suffix = prepare_rel_posix_path(suffix)

    return posixpath.join(prefix, suffix)


def copy_files_and_replace_placeholders(src_dest_pairs: List[Tuple[str, str]], placeholder: str, replacement: str):
    for src, dest in src_dest_pairs:
        with open(src, "r") as f:
            content = f.read()

        content = content.replace(placeholder, replacement)
        with open(dest, "w") as f:
            f.write(content)


def get_base64_encoded_content(file_path: str) -> str:
    with open(file_path, "rb") as f:
        content = f.read()
        encoded_content = base64.b64encode(content).decode()

        return encoded_content
