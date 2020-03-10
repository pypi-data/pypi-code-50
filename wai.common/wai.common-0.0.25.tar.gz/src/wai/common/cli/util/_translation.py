"""
Module for count-translation functionality for the CountOption class.
"""
from typing import Optional, Dict, Tuple

TranslationDict = Dict[int, int]
TranslationDictPair = Tuple[TranslationDict, TranslationDict]


def create_translation_pair(translation: Optional[TranslationDict]) -> Optional[TranslationDictPair]:
    """
    Creates a pair of translation tables from a single one.

    :param translation:     The forward translation table.
    :return:                The forward and reverse translation tables.
    """
    # Preserve optionality
    if translation is None:
        return None

    # Translation tables must be integers both ways
    for key, value in translation.items():
        if not isinstance(key, int) or not isinstance(value, int):
            raise TypeError(f"All values in translation table must be ints")

    # The forward translation space must be continuous integers starting from zero
    if set(translation.keys()) != set(range(len(translation))):
        raise ValueError("Translation keys must be continuous from 0")

    # The translation must be reversible
    if len(set(translation.values())) != len(translation):
        raise ValueError("Translation values are not unique")

    return translation, {value: key for key, value in translation.items()}


def translate_forward(value: int, translation_pair: Optional[TranslationDictPair]) -> int:
    """
    Performs the forward translation using a pair of translation tables.

    :param value:               The value to translate.
    :param translation_pair:    The pair of translation tables.
    :return:                    The translated value.
    """
    # If there are no translation tables, perform no translation
    if translation_pair is None:
        return value

    # Cap the value to the range of the forward translation
    value = min(max(0, value), len(translation_pair[0]) - 1)

    return translation_pair[0][value]


def translate_reverse(value: int, translation_pair: Optional[TranslationDictPair]) -> int:
    """
    Performs the reverse translation using a pair of translation tables.

    :param value:               The value to translate.
    :param translation_pair:    The pair of translation tables.
    :return:                    The translated value.
    """
    # If there are no translation tables, perform no translation
    if translation_pair is None:
        return value

    # Make sure the value is translatable
    if value not in translation_pair[1]:
        raise ValueError(f"Value not in translation table: {value}")

    return translation_pair[1][value]
