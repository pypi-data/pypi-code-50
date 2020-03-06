from pathlib import Path


def truncate_path(path: Path = None, base_path: Path = None) -> str:
    """
    Returns a shortened version of a given path string.
    Removes the base path string from the path to be truncated.
    Parameters:
        path (Path): Path to truncate
        base_path (Path): Base path to omit from the main path
    Returns:
        str: Shortened path string for the given path
    """
    if path is None:
        return ""
    path_str = str(path.absolute())
    if base_path is None:
        return path_str
    base_str = str(base_path.absolute())
    if path_str.startswith(base_str):
        return "..." + path_str[len(base_str):]
    return path_str


def print_paths(paths: list = None, base_path: Path = None):
    """
    Prints a list of pathlib paths.
    Parameters:
        paths (list): Paths to print
        base_path (Path): Base path used for truncating path strings
    """
    if paths is not None:
        for path in paths:
            print(truncate_path(path, base_path))
