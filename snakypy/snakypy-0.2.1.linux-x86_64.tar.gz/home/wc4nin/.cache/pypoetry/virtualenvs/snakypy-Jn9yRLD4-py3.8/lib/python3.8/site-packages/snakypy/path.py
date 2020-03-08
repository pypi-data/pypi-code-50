from pathlib import Path


def create(*args, multidir=()):
    """
    Function that creates single or multiple directories using
    the "multidir" parameter.
    The "multidir" parameter must receive a tuple with the paths
    of the directories to be created.
    """

    # Create directory single.
    if args:
        for directory in args:
            path = Path(directory)
            path.mkdir(parents=True, exist_ok=True)
    # Create multiple directory.
    if len(multidir) > 0:
        for directory in multidir:
            path = Path(directory)
            path.mkdir(parents=True, exist_ok=True)
