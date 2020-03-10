from argparse import Namespace
from typing import Union

from .util import to_cli_string, from_cli_string
from ._CLIRepresentable import CLIRepresentable, cli_repr, from_cli_repr
from ._OptionValueHandler import OptionValueHandler
from ._typing import OptionsList


class CLIInstantiable(CLIRepresentable, OptionValueHandler):
    """
    Base class for types that can be instantiated from the
    command-line.
    """
    def __init__(self, namespace: Union[Namespace, OptionsList, None] = None):
        self._namespace: Namespace = self._ensure_namespace(namespace)

    @property
    def namespace(self) -> Namespace:
        return self._namespace

    def _cli_repr(self) -> str:
        return to_cli_string([cli_repr(type(self))] + self.to_options_list())

    @classmethod
    def _from_cli_repr(cls, cli_string: str) -> 'CLIInstantiable':
        # Split into class and option parts
        options_list = from_cli_string(cli_string)

        # Parse the class
        klass = from_cli_repr(type, options_list[0])

        # Make sure it is a sub-class of our type
        if not issubclass(klass, cls):
            raise TypeError(f"{options_list[0]} is not a sub-class of {cli_repr(cls)}")

        options_list = options_list[1:]

        return klass(options_list)
