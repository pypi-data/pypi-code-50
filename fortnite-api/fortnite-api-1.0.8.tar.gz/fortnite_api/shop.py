from datetime import datetime

from fortnite_api.cosmetics import BrCosmetic


class BrShop:
    """Represents a Battle Royale shop.

    Attributes
    -----------
    hash: :class:`str`
        The hash of the shop.
    date: :class:`datetime.datetime`
        The timestamp of the .
    featured: Optional[List[:class:`BrShopEntry`]]
        A list of all featured entries.
    daily: Optional[List[:class:`BrShopEntry`]]
        A list of all daily entries.
    votes: Optional[List[:class:`BrShopEntry`]]
        A list of all vote entries.
    vote_winners: Optional[List[:class:`BrShopEntry`]]
        A list of all vote winner.
    raw_data: :class:`dict`
        The raw data from request. Can be used for saving and re-creating the class.
    """

    def __init__(self, data):
        self.hash = data.get('hash')
        try:
            self.date = datetime.strptime(data.get('date'), '%Y-%m-%dT%H:%M:%S%z')
        except ValueError:
            self.date = None
        self.featured = [BrShopEntry(item_data) for item_data in data.get('featured')] if data.get('featured') else None
        self.daily = [BrShopEntry(item_data) for item_data in data.get('daily')] if data.get('daily') else None
        self.votes = [BrShopEntry(item_data) for item_data in data.get('votes')] if data.get('votes') else None
        self.vote_winners = [BrShopEntry(item_data) for item_data in data.get('voteWinners')] \
            if data.get('voteWinners') else None
        self.raw_data = data


class BrShopEntry:
    """Represents a Battle Royale shop entry.

    Attributes
    -----------
    regular_price: :class:`int`
        The internal price.
    final_price: :class:`int`
        The price which is shown in-game.
    discount: :class:`int`
        The discount on the item.
    giftable: :class:`bool`
        Whether the item is giftable.
    refundable: :class:`bool`
        Whether the item is refundable.
    panel: :class:`int`
        The id of the panel in the featured section. -1 if the item is in no panel.
    sort_priority: :class:`int`
        The sort priority in the featured panels.
    banner: Optional[:class:`str`]
        The text of the banner. This text is shown in a arrow in-game.
    items: List[:class:`BrCosmetic`]
        A list of all cosmetics you get when you buy.
    raw_data: :class:`dict`
        The raw data from request. Can be used for saving and re-creating the class.
    """

    def __init__(self, data):
        self.regular_price = data.get('regularPrice')
        self.final_price = data.get('finalPrice')
        self.discount = self.regular_price - self.final_price
        self.is_bundle = data.get('isBundle')
        self.is_special = data.get('isSpecial')
        self.refundable = data.get('refundable')
        self.giftable = data.get('giftable')
        self.panel = data.get('panel')
        self.sort_priority = data.get('sortPriority')
        self.banner = data.get('banner')
        self.items = [BrCosmetic(item_data) for item_data in data.get('items')]
        self.raw_data = data
