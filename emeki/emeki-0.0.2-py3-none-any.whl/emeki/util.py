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
    if v.lower() in ('yes', 'true', 't', 'y', '1', '1.0'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0', '0.0'):
        return False
    else:
        raise ValueError(f"Boolean value expected, got {v}")
