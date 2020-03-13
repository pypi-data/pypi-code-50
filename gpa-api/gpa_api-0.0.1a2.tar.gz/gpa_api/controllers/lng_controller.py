import connexion
import six

from gpa_api.models.calculation import Calculation  # noqa: E501
from gpa_api.models.calculation_body import CalculationBody  # noqa: E501
from gpa_api.models.ship import Ship  # noqa: E501
from gpa_api import util


def calculate(calculation_body):  # noqa: E501
    """Calculate LNG Ageing

     # noqa: E501

    :param calculation_body: Object containing all info for a calculation
    :type calculation_body: dict | bytes

    :rtype: Calculation
    """
    if connexion.request.is_json:
        calculation_body = CalculationBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_calculation(calculation_id):  # noqa: E501
    """Get LNG Ageing calculation

     # noqa: E501

    :param calculation_id: The ID of the calculation
    :type calculation_id: str

    :rtype: Calculation
    """
    return 'do some magic!'


def get_calculations():  # noqa: E501
    """Get a list of LNG Ageing calculations

     # noqa: E501


    :rtype: List[Calculation]
    """
    return 'do some magic!'


def get_ships():  # noqa: E501
    """Get a list of ships.

     # noqa: E501


    :rtype: List[Ship]
    """
    return 'do some magic!'
