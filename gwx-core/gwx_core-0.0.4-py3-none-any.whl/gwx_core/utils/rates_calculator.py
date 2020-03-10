"""
Rates Calculator Utility
========================

This utility will handle computations for specific rates
with different use cases.

"""


def calculate_supplier_service_rate(
        markup: float or int,
        supplier_service_price: float or int,
        is_int=False
) -> float or int:
    """Return the calculated sum of the markup and supplier service price,
    return value type might be int or float.

    :param is_int: bool value that decides if return value should be strictly int or possibly float
    :param markup: the float or int value of markup
    :param supplier_service_price: the float or int supplied service price.
    :return: float or int computed value
    """
    result = ((markup / 100) * supplier_service_price) + supplier_service_price
    if is_int:
        return int(result)

    return result
