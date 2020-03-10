from typing import Optional, Any

from ..constants import SHORT_FLAG_PREFIX
from ..util import is_short_flag, \
    TranslationDict, TranslationDictPair, create_translation_pair, translate_forward, translate_reverse
from .._typing import OptionsList
from ._Option import Option


class CountOption(Option):
    """
    Option which counts the number of times its flag appears.

    Can optionally supply a translation table to translate from
    actual count values to some other set of integers (e.g. from
    counts to verbosity values).
    """
    def __init__(self,
                 *flags: str,
                 translation: Optional[TranslationDict] = None,
                 help: str = ...):
        super().__init__(*flags,
                         action="count",
                         default=0,
                         help=help)

        self._update_kwargs_repr("translation", translation, translation is not None)
        self._update_kwargs_repr("help", help, help is not ...)

        self._translations: Optional[TranslationDictPair] = create_translation_pair(translation)

    def _validate_value(self, value: Any) -> int:
        # Value must be an integer
        if not isinstance(value, int):
            raise TypeError(f"Count options take integer values, not {value}")

        # Make sure the value is reverse-translatable
        translate_reverse(value, self._translations)

        return value

    def _options_list_from_current_value(self, value: int) -> OptionsList:
        # Get the count from the current value
        count = translate_reverse(value, self._translations)

        # If count is 0, return no options
        if count == 0:
            return []

        # Try to use a short flag if available, otherwise just the first flag
        selected_flag = self.flags[0]
        short_flag = is_short_flag(selected_flag)
        if len(self.flags) == 2 and not short_flag:
            selected_flag = self.flags[1]
            short_flag = True

        # Iterate the flag count times
        if short_flag:
            return [SHORT_FLAG_PREFIX + selected_flag[1] * count]
        else:
            return [selected_flag] * count

    def _parse_raw_namespace_value(self, value: int) -> int:
        # Apply the translation if provided
        return translate_forward(value, self._translations)
