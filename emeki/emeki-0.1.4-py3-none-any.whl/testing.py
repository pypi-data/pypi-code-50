"""This module provides some additional testing functionality.

"""
import builtins
from typing import List, Union


class AssertPrints:
    """Checks if `print` is called with the specified arguments.

    Does not capture stdout output."""

    print_list: List[str] = []
    exp_print: List[str]
    old_print = None
    no_output: bool

    def __init__(self, s: Union[str, List[str]], no_output: bool = False):
        self.exp_print = s if isinstance(s, list) else [s]
        self.no_output = no_output

    def new_print(self, *args):
        self.print_list += [args[0] if len(args) == 1 else args]
        if not self.no_output:
            self.old_print(*args)

    def __enter__(self):
        self.old_print = builtins.print
        builtins.print = self.new_print

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            assert len(self.exp_print) == len(self.print_list)
            for e, p in zip(self.exp_print, self.print_list):
                assert e == p, f"{e} != {p}"
        finally:
            builtins.print = self.old_print

    pass
