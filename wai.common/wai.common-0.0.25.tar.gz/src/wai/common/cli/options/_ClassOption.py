from argparse import REMAINDER
from typing import Union, Any, Type, Iterable, Tuple, TypeVar, Optional, List

from ...meta import non_default_kwargs
from .._CLIRepresentable import CLIRepresentable, cli_repr, from_cli_repr
from .._typing import OptionsList
from ._Option import Option

# The type of class the option takes
ClassType = TypeVar("ClassType", bound=CLIRepresentable)

# The set of actions allowed with this type of option
ALLOWED_ACTIONS = {"store", "append"}


class ClassOption(Option):
    """
    An option which takes CLI-representable objects as values.
    """
    def __init__(self,
                 *flags: str,
                 type: Type[ClassType],
                 action: str = ...,
                 nargs: Union[int, str] = ...,
                 choices: Iterable[Union[str, ClassType]] = ...,
                 required: bool = ...,
                 help: str = ...,
                 metavar: Union[str, Tuple[str, ...]] = ...):
        # Check the type is CLI-representable
        if not CLIRepresentable.type_check(type):
            raise TypeError(f"Type {type.__qualname__} is not a CLI-representable type")
        self._type = type

        # Check the action is allowed
        if action is not ... and action not in ALLOWED_ACTIONS:
            raise ValueError(f"Action must be one of {ALLOWED_ACTIONS}")

        # Check the number of arguments is allowed
        if nargs == "?" or nargs == REMAINDER:
            raise ValueError(f"Disallowed nargs value {nargs}")

        # See if our values should be list-valued or not
        self._is_list_valued = action == "append" or nargs is not ...

        # Format choices as strings
        if choices is not ...:
            formatted_choices = []
            for choice in choices:
                # Convert CLI representations into actual objects
                if isinstance(choice, str):
                    choice = from_cli_repr(type, choice)

                # Make sure they are instances of the defined type
                if not isinstance(choice, type):
                    raise TypeError(f"Choice is not of the declared type")

                formatted_choices.append(cli_repr(choice))
            choices = formatted_choices

        # Extract the set of keyword arguments
        kwargs = non_default_kwargs(ClassOption.__init__, locals())

        super().__init__(*flags, default=[] if self._is_list_valued else None, **kwargs)

        self._update_kwargs_repr("type", type, True)
        for name, value in kwargs.items():
            self._update_kwargs_repr(name, value, True)

    @property
    def type(self) -> Type[ClassType]:
        """
        Gets the type of value this option takes.
        """
        return self._type

    def _validate_value(self, value: Any) -> Any:
        if self._is_list_valued:
            return self._validate_list_value(value)
        else:
            return self._validate_singular_value(value)

    def _validate_singular_value(self, value: Any) -> Optional[ClassType]:
        """
        Validate's the given value when trying to set the value
        of this option. Assumes the value should be a singular value.

        :param value:       The value attempting to be set.
        :return:            The actual value that should be set.
        :raises Exception:  If the value cannot be validated.
        """
        # Determine if None is allowed
        optional = self._kwargs.get("optional", True)

        # Make sure the value is of our type (or None if we're optional)
        if not optional or value is not None:
            if not isinstance(value, self._type):
                raise TypeError(f"Expected {self._type.__name__} but got {type(value).__name__}")

        return value

    def _validate_list_value(self, value: Any) -> List[ClassType]:
        """
        Validate's the given value when trying to set the value
        of this option. Assumes the value should be a list of values.

        :param value:       The value attempting to be set.
        :return:            The actual value that should be set.
        :raises Exception:  If the value cannot be validated.
        """
        # Make sure the value is a list
        if not isinstance(value, list):
            raise TypeError(f"Value must be a list")

        # Make sure the list has the correct number of values in it
        length = len(value)
        action = self._kwargs.get("action", "store")
        nargs = self._kwargs.get("nargs", None)
        optional = self._kwargs.get("optional", True)
        if optional and length == 0:
            pass
        elif isinstance(nargs, int):
            if action == "store":
                if length != nargs:
                    raise ValueError(f"Requires list of length {nargs}")
            else:
                if length % nargs != 0:
                    raise ValueError(f"Requires list of length a multiple of {nargs}")
        elif nargs == "+":
            if length == 0:
                raise ValueError(f"Requires at least one item")

        if any(not isinstance(element, self._type) for element in value):
            raise TypeError(f"All values must be of the declared type {self._type.__name__}")

        return value

    def _options_list_from_current_value(self, value: Any) -> OptionsList:
        optional = self._kwargs.get("optional", True)
        if self._is_list_valued:
            length = len(value)
            action = self._kwargs.get("action", "store")
            nargs = self._kwargs.get("nargs", 1)
            options_list = []
            if optional and length == 0:
                pass
            if action == "store" or isinstance(nargs, str):
                options_list.append(self._flags[0])
                for val in value:
                    options_list.append(cli_repr(val))
            else:
                for i in range(0, len(value), nargs):
                    options_list.append(self._flags[0])
                    for val in value[i:i + nargs]:
                        options_list.append(cli_repr(val))
            return options_list
        else:
            if optional and value is None:
                return []
            return [self._flags[0], cli_repr(value)]

    def _parse_raw_namespace_value(self, value: Any) -> Any:
        if isinstance(value, list):
            return [from_cli_repr(self._type, cli_string) for cli_string in value]
        elif isinstance(value, str):
            return from_cli_repr(self._type, value)
        else:
            return None
