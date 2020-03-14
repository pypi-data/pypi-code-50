import logging
from enum import Enum


class Currency(Enum):
    AUSTRALIAN_DOLLAR = "AUD", "$",
    CANADIAN_DOLLAR = "CAD", "$",
    SWISS_FRANC = "CHF", "CHF",
    YUAN_RENMINBI = "CNY", "¥",
    EURO = "EUR", "€",
    POUND_STERLING = "GBP", "£",
    YEN = "JPY", "¥",
    MEXICAN_PESO = "MXN", "$"
    NORWEGIAN_KRONE = "NOK", "kr",
    NEW_ZEALAND_DOLLAR = "NZD", "$",
    SWEDISH_KRONA = "SEK", "kr",
    TURKISH_LIRA = "TRY", "TL",
    US_DOLLAR = "USD", "$",
    RAND = "ZAR", "R"

    @property
    def code(self):
        """Currency Code i.e. GBP"""
        return self.value[0]

    @property
    def symbol(self):
        """Symbol of the currency i.e £"""
        return self.value[1]

    def get_code(self):
        """
        Get the Code of the Currency

        :return: Returns the code as a string i.e. GBP
        """
        return self.code

    def get_symbol(self):
        """
        Get the Symbol of the Currency

        :return: Returns the symbol of the currency as a string
        """
        return self.symbol

    @staticmethod
    def value_of(code: str):
        """
        Parses the provided Code into the Currency enum

        i.e.

        "GBP" -> FxqCurrency.POUND_STERLING

        :param code: Currency Code, i.e. GBP
        :return: Returns the FxqCurrency Enum
        """
        try:
            try:
                return [e for e in Currency.__members__.values() if e.code == code][0]
            except IndexError as ie:
                logging.debug(
                    f"Failed to match the code of '{code}'")

            return [e for e in Currency.__members__.values() if e.symbol == code][0]

        except IndexError as ie:
            raise Exception(
                f"Failed to match '{code}' as a code or symbol") from None
