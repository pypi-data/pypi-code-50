from .offer_list import _html_to_soup, _get_offer_list, _find_offers


#Constants
BASE_MARKET_URL = "https://www.urban-rivals.com/market/?"


def _clean_input(id):
    """Cleans the char id"""
    if type(id) is int:
        id = abs(id)
    return id


def get_market_offers(session, ids, base_market_url=BASE_MARKET_URL):
    """\nMain function for interaction with this library.
    \nProvided a sequence of Character Ids, returns a dictionary of offers for each. \
    Requires a session which has already authenticated with Urban Rivals.
    \nOptional: provide a base market URL for proxy. Must end with a "?" \
    Ex: "http://example.com?"


    >>>get_market_offers(session, [1400, 1423, 1764])

    {1400: Offer, 1423: Offer, 1764: Offer}


    >>>get_market_offers(session, ["1301", "1543"])

    {"1301": Offer, "1543": Offer}

    """
    if len(ids) < 1:
        raise ValueError("Ids cannot be empty")
    if not base_market_url.endswith("?"):
        raise ValueError("URL must end with a question mark")
    market = {
        char_id:
        _html_to_soup(
            session.get(
                _get_offer_list(char_id, base_market_url)
        ))
        for char_id in map(_clean_input, ids)
    }
    return {char_id :_find_offers(market[char_id])
            for char_id in map(_clean_input, ids) }