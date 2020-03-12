"""
Package for utility functions for working with command-line options.
"""
from ._cli_string import to_cli_string, from_cli_string
from ._flags import (
    is_flag,
    is_flag_reason,
    is_short_flag,
    is_short_flag_reason,
    is_long_flag,
    is_long_flag_reason,
    flag_from_name
)
from ._translation import TranslationTable
