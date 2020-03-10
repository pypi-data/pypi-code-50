from typing import Any

from .._typing import OptionsList
from ._Option import Option


class FlagOption(Option):
    """
    Option which stores True or False based on if it is provided or not.
    """
    def __init__(self,
                 *flags: str,
                 invert: bool = False,
                 help: str = ...):
        super().__init__(*flags,
                         action="store_false" if invert else "store_true",
                         help=help)

        self._update_kwargs_repr("invert", invert, invert)
        self._update_kwargs_repr("help", help, help is not ...)

        self._invert: bool = invert

    def _validate_value(self, value: Any) -> bool:
        # Make sure the value is boolean
        if not isinstance(value, bool):
            raise TypeError(f"Flag options only take boolean values, not {value}")

        return value

    def _options_list_from_current_value(self, value: bool) -> OptionsList:
        # Flag should be present if value is True XOR invert is True
        return [self.flags[0]] if value != self._invert else []

    def _parse_raw_namespace_value(self, value: bool) -> bool:
        # raw namespace value is already correct
        return value
