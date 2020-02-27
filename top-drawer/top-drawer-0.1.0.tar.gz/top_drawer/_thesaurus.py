from typing import List
from urllib.parse import quote

import aiohttp

API_URL_TEMPLATE = 'https://words.bighugelabs.com/api/2/{api_key}/{word}/json'

NOUN = 'noun'
VERB = 'verb'
ADJECTIVE = 'adjective'

SYNONYM = 'syn'
ANTONYM = 'ant'
USR = 'usr'  # Not really sure what this is.
SIM = 'sim'
REL = 'rel'

WORD_TYPES = (
    NOUN,
    VERB,
    ADJECTIVE
)

THESAURUS_MODES = (
    SYNONYM,
    ANTONYM,
    USR,
    SIM,
    REL
)


async def thesaurus(session: aiohttp.ClientSession, api_key: str, word: str):
    url = API_URL_TEMPLATE.format(api_key=api_key, word=quote(word))
    data = {}
    async with session.get(url) as response:  # type: aiohttp.ClientResponse

        if response.status == 200:
            data = await response.json(content_type='text/javascript')
        elif response.status != 404:
            response.raise_for_status()

    return data


def reduce_thesaurus(
        data: dict,
        word_types: List[str],
        modes: List[str]
):
    thes = set()
    for category, word_data in data.items():
        if not word_types or category in word_types:
            for mode, mode_data in word_data.items():
                if not modes or mode in modes:
                    thes.update(mode_data)

    return thes
