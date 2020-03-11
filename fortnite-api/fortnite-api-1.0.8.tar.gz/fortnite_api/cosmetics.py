from datetime import datetime

from fortnite_api.enums import BrCosmeticType, BrCosmeticRarity


class BrCosmetic:
    """Represents a Battle Royale Cosmetic.

    Attributes
    -----------
    id: :class:`str`
        The id of the cosmetic.
    type: :class:`BrCosmeticType`
        The type of the cosmetic.
    backend_type: :class:`str`
        The internal type of the cosmetic.
    rarity: :class:`BrCosmeticRarity`
        The rarity of the cosmetic.
    backend_rarity: :class:`str`
        The internal rarity of the cosmetic.
    name: :class:`str`
        The name of the cosmetic in the chosen language.
    short_description: Optional[:class:`str`]
        The short description of the cosmetic in the chosen language.
    description: :class:`str`
        The description of the cosmetic in the chosen language.
    set: Optional[:class:`str`]
        The set of the cosmetic in the chosen language.
    set_text: Optional[:class:`str`]
        The text of the set of the cosmetic in the chosen language.
    series: Optional[:class:`str`]
        The series of the cosmetic in the chosen language.
    backend_series: Optional[:class:`str`]
        The internal series of the cosmetic.
    small_icon: :class:`BrCosmeticImage`
        The icon image in 128x128 resolution of the cosmetic.
    icon: Optional[:class:`BrCosmeticImage`]
        The icon image in 512x512 resolution of the cosmetic.
    featured: Optional[:class:`BrCosmeticImage`]
        The featured image in 1024x1024 resolution of the cosmetic.
    background: Optional[:class:`BrCosmeticImage`]
        The background image in 2048x1024 resolution of a loading screen.
    cover_art: Optional[:class:`BrCosmeticImage`]
        The cover art image in 512x512 resolution of a music pack.
    decal: Optional[:class:`BrCosmeticImage`]
        The decal in 512x512 resolution of a spray.
    variants: Optional[List[:class:`BrCosmeticVariant`]]
        A :class:`list` of :class:`BrCosmeticVariant` of the cosmetic.
    gameplay_tags: Optional[List[:class:`str`]]
        A :class:`list` of gameplay tags of the cosmetics.
    display_asset_path: Optional[:class:`str`]
        The path of the display asset.
    definition: Optional[:class:`str`]
        The definition of the cosmetic.
    required_item_id: Optional[:class:`str`]
        The id of the cosmetic which is required to get this cosmetic.
    built_in_emote_id: Optional[:class:`str`]
        The id of the emote which is built-in into the cosmetic.
    path: :class:`str`
        The path of the asset.
    last_update: :class:`datetime.datetime`
        The timestamp of the last update of the cosmetic.
    added: :class:`datetime.datetime`
        The timestamp when the item was added to the Fortnite-API.com database.
    raw_data: :class:`dict`
        The raw data from request. Can be used for saving and recreating the class.
    """

    def __init__(self, data):
        self.id = data.get('id')
        self.type = BrCosmeticType(data.get('type'))
        self.backend_type = data.get('backendType')
        self.rarity = BrCosmeticRarity(data.get('rarity'))
        self.display_rarity = data.get('displayRarity')
        self.backend_rarity = data.get('backendRarity')
        self.name = data.get('name')
        self.short_description = data.get('shortDescription')
        self.description = data.get('description')
        self.set = data.get('set')
        self.set_text = data.get('setText')
        self.series = data.get('series')
        self.backend_series = data.get('backendSeries')
        images = data.get('images', {})
        self.small_icon = BrCosmeticImage(images.get('smallIcon')) if images.get('smallIcon') is not None else None
        self.icon = BrCosmeticImage(images.get('icon')) if images.get('icon') is not None else None
        self.featured = BrCosmeticImage(images.get('featured')) if images.get('featured') is not None else None
        self.background = BrCosmeticImage(images.get('background')) if images.get('background') is not None else None
        self.cover_art = BrCosmeticImage(images.get('coverArt')) if images.get('coverArt') is not None else None
        self.decal = BrCosmeticImage(images.get('decal')) if images.get('decal') is not None else None
        self.variants = [BrCosmeticVariant(variant) for variant in data.get('variants')] \
            if data.get('variants') is not None else None
        self.gameplay_tags = [gameplay_tag for gameplay_tag in data.get('gameplayTags')] \
            if data.get('gameplayTags') is not None else None
        self.display_asset_path = data.get('displayAssetPath')
        self.definition = data.get('definition')
        self.required_item_id = data.get('requiredItemId')
        self.built_in_emote_id = data.get('builtInEmoteId')
        self.path = data.get('path')
        try:
            self.last_update = datetime.strptime(data.get('lastUpdate'), '%Y-%m-%dT%H:%M:%S%z')
        except ValueError:
            self.last_update = None
        try:
            self.added = datetime.strptime(data.get('added'), '%Y-%m-%dT%H:%M:%S%z')
        except ValueError:
            self.added = None
        self.raw_data = data


class BrCosmeticImage:
    """Represents a Battle Royale cosmetic image.

    Attributes
    -----------
    hash: :class:`str`
        The hash of the image.
    url: :class:`str`
        The hash of the image.
    raw_data: :class:`dict`
        The raw data from request. Can be used for saving and re-creating the class.
    """

    def __init__(self, data):
        self.hash = data.get('hash')
        self.url = data.get('url')
        self.raw_data = data


class BrCosmeticVariant:
    """Represents a Battle Royale cosmetic image.

    Attributes
    -----------
    channel: :class:`str`
        The channel of the variant.
    type: Optional[:class:`str`]
        The type of the variant in the chosen language.
    options: List[:class:`BrCosmeticVariantOption`]
        A :class:`list` of :class:`BrCosmeticVariantOption` of the variant.
    raw_data: :class:`dict`
        The raw data from request. Can be used for saving and re-creating the class.
    """

    def __init__(self, data):
        self.channel = data.get('channel')
        self.type = data.get('type')
        self.options = None
        self.raw_data = data

        if data.get('options'):
            self.options = []
            for variant in data.get('options'):
                self.options.append(variant)


class BrCosmeticVariantOption:
    """Represents a Battle Royale cosmetic image.

    Attributes
    -----------
    tag: :class:`str`
        The tag of the option.
    name: :class:`str`
        The name of the option in the chosen language.
    image: :class:`BrCosmeticImage`
        A image of the option.
    raw_data: :class:`dict`
        The raw data from request. Can be used for saving and re-creating the class.
    """

    def __init__(self, data):
        self.tag = data.get('tag')
        self.name = data.get('name')
        self.image = BrCosmeticImage(data.get('image'))
        self.raw_data = data
