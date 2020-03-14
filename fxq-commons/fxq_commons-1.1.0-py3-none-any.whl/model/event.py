import logging
from enum import Enum


class Impact(Enum):
    NONE = 0, "None"
    LOW = 1, "Low"
    MEDIUM = 2, "Medium"
    HIGH = 3, "High"

    @property
    def id(self) -> int:
        """ID for the Impact, i.e. 0 for None"""
        return self.value[0]

    @property
    def name(self) -> str:
        """Name of the Impact Enum"""
        return self.value[1]

    def get_id(self) -> int:
        """
        Get the ID of the Enum

        :return: Returns the ID of the Enum
        """
        return self.id

    def get_name(self) -> str:
        """
        Return the Name of the Enum

        :return: Returns the Name as a String
        """
        return self.name

    @staticmethod
    def value_of(value: str or int):
        """
        Parses the provided value into an Impact Enum

        i.e.

        0 -> Impact.NONE
        2 -> Impact.MEDIUM

        :param value: Value to parse, String or Id
        :return: Returns the Impact Enum
        """
        try:
            try:
                return [e for e in Impact.__members__.values() if e.id == value][0]
            except IndexError as ie:
                logging.debug(
                    f"Failed to match the id of '{value}'")

            return [e for e in Impact.__members__.values() if e.name.lower() == value.lower()][0]

        except IndexError as ie:
            raise Exception(
                f"Failed to match value '{value}' as an id or name") from None


class Type(Enum):
    CENTRAL_BANKS = 1, "Central Banks"
    CONFIDENCE_INDICES = 2, "Confidence Indices"
    CONSUMPTION_AND_INFLATION = 3, "Consumption & Inflation"
    EMPLOYMENT = 4, "Employment"
    GOVERNMENT = 5, "Government"
    HOLIDAYS = 6, "Holidays"
    INDUSTRIAL_AND_NON_INDUSTRIAL_ACTIVITY = 7, "Industrial & Non-Industrial Activity"
    INTEREST_RATES = 9, "Interest Rates"
    LIQUIDITY_AND_BALANCE = 10, "Liquidity & Balance"

    @property
    def id(self) -> int:
        """ID for the Type, i.e. 1 for Central Banks"""
        return self.value[0]

    @property
    def name(self) -> str:
        """Name of the Type Enum"""
        return self.value[1]

    def get_id(self) -> int:
        """
        Get the ID of the Enum

        :return: Returns the ID of the Enum
        """
        return self.id

    def get_name(self) -> str:
        """
        Return the Name of the Enum

        :return: Returns the Name as a String
        """
        return self.name

    @staticmethod
    def value_of(value: str or int):
        """
        Parses the provided value into an Type Enum

        :param value: Value to parse, String or Id
        :return: Returns the Type Enum
        """
        try:
            try:
                return [e for e in Type.__members__.values() if e.id == value][0]
            except IndexError as ie:
                logging.debug(
                    f"Failed to match the id of '{value}'")

            return [e for e in Type.__members__.values() if e.name.lower() == value.lower()][0]

        except IndexError as ie:
            raise Exception(
                f"Failed to match value '{value}' as an id or name") from None
