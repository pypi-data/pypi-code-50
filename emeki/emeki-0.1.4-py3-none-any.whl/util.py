"""The util module.

This module provides some utility functionality.
"""


def str2bool(v) -> bool:
    """Converts a string to a boolean.

    Raises:
        ValueError: If it cannot be converted.
    """
    if isinstance(v, bool):
        return v
    elif isinstance(v, str):
        v_low = v.lower()
        if v_low in ("yes", "true", "t", "y", "1", "1.0"):
            return True
        elif v_low in ("no", "false", "f", "n", "0", "0.0"):
            return False
    raise ValueError(f"{v} is not convertible to boolean!")


def emeki_main():
    """The main function.

    It may be called directly from the command line when
    typing `emeki`."""
    print("Hoi! This is my personal python library.")
