from typing import TypeVar, Dict, Callable, Type, Tuple, Any, NoReturn

from ..meta import fully_qualified_name

# Generic type variable
T = TypeVar("T")

# The types of the '_cli_repr'/'_from_cli_repr' methods
_CLI_REPR_METHOD_TYPE = Callable[[T], str]
_FROM_CLI_REPR_METHOD_TYPE = Callable[[str], T]


# For use when honarary member methods aren't implemented (yet)
def NOT_IMPLEMENTED(method_name: str) -> Callable[[Any], NoReturn]:
    def method(*args, **kwargs):
        raise NotImplementedError(method_name)

    return method


def type_from_cli_repr(cli_string: str) -> type:
    """
    Imports a class from its CLI representation.
    TODO: Move to meta package

    :param cli_string:  The CLI representation of the class.
    :return:            The class.
    """
    locals_ = dict(locals())
    parts = cli_string.split(".")
    for i in range(len(parts) - 1, 0, -1):
        code = f"from {'.'.join(parts[:i])} import {parts[i]} as result"
        if i != len(parts) - 1:
            code += f"\nresult = result.{'.'.join(parts[i+1:])}"
        try:
            exec(code, globals(), locals_)
        except ImportError:
            pass
        else:
            return locals_["result"]

    raise ImportError(f"Couldn't import class '{cli_string}'")


# Honorary CLI-representable types and their '_cli_repr'/'_from_cli_repr' methods
HONORARY_MEMBERS: Dict[Type[T], Tuple[_CLI_REPR_METHOD_TYPE, _FROM_CLI_REPR_METHOD_TYPE]] = {
    type: (fully_qualified_name, type_from_cli_repr),
    int: (repr, int),
    str: (repr, lambda cli_string: cli_string),
    float: (repr, float)
}


class CLIRepresentable:
    """
    Interface for objects which can represent themselves
    as a value on the command-line.
    """
    def _cli_repr(self) -> str:
        """
        Gets the CLI representation of this object.

        :return:        The CLI string.
        """
        raise NotImplementedError(CLIRepresentable._cli_repr.__qualname__)

    @classmethod
    def _from_cli_repr(cls, cli_string: str) -> 'CLIRepresentable':
        """
        Gets an instance of the type from its CLI representation.

        :param cli_string:  The CLI representation.
        :return:            The instance.
        """
        raise NotImplementedError(CLIRepresentable._from_cli_repr.__qualname__)

    @staticmethod
    def type_check(type_: type) -> bool:
        """
        Checks if the given type is CLI-representable.

        :param type_:   The type to check.
        :return:        True if the type is CLI-representable.
        """
        return issubclass(type_, CLIRepresentable) or type_ in HONORARY_MEMBERS


def cli_repr(value) -> str:
    """
    Gets the CLI representation of a CLI-representable value.

    :param value:   The value.
    :return:        The CLI string.
    """
    # Get the type of the value
    type_ = type(value)

    # Make sure it is CLI-representable
    if not CLIRepresentable.type_check(type_):
        raise TypeError(f"Values of type '{type.__name__}' are not CLI-representable")

    # Handle honorary members
    if type_ in HONORARY_MEMBERS:
        return HONORARY_MEMBERS[type_][0](value)

    return value._cli_repr()


def from_cli_repr(type_: Type[T], cli_string: str) -> T:
    """
    Gets a value of a CLI-representable type from its CLI representation.

    :param type_:       The type of value to get.
    :param cli_string:  The CLI representation.
    :return:            The value.
    :raises TypeError:  If the type is not CLI-representable.
    """
    # Only works for CLI-representable types
    if not CLIRepresentable.type_check(type_):
        raise TypeError(f"Type '{type_.__name__}' are not CLI-representable")

    # Handle honorary members
    if type_ in HONORARY_MEMBERS:
        return HONORARY_MEMBERS[type_][1](cli_string)

    return type_._from_cli_repr(cli_string)
