from typing import Union
from core import load_config, logger
import requests


class Trello:
    def __init__(self, config: dict) -> None:
        self._key = config['TRELLO_API_KEY']
        self._token = config['TRELLO_API_TOKEN']
        self._board_id = config['BOARD_ID']
        self._trash_board_id = config['TRASH_BOARD_ID']

    def _handle_position(self, position):
        if type(position) == str:
            if position.lower() not in ['top', 'bottom']:
                logger(
                    'ERROR', '`position` argument for the method `create_list`' +
                    'should be either top, bottom, or positive number.')
            position = position.lower()

        elif type(position) == int:
            if position <= 0:
                logger(
                    'ERROR', '`position` argument for the method `create_list`' +
                    'should be either top, bottom, or positive number.')

        return position

    def create_list(self, title: str, position: Union[str, int]) -> None:
        position = self._handle_position(position)

        response = requests.post(
            'https://api.trello.com/1/boards/' +
            '{BOARD_ID}/lists?name={TITLE}&pos={POSITION}&key={KEY}&token={TOKEN}'.format(
                BOARD_ID=self._board_id,
                TITLE=title, POSITION=position,
                KEY=self._key, TOKEN=self._token,

            )
        )
        if response.status_code != 200:
            logger('ERROR', 'Failed on creating list: "{}"}'.format(
                response.text
            ))
        return response.json()

    def get_list(self):

        response = requests.get(
            'https://api.trello.com/1/boards/' +
            '{BOARD_ID}/lists?key={KEY}&token={TOKEN}'.format(
                BOARD_ID=self._board_id, KEY=self._key, TOKEN=self._token
            ))
        if response.status_code != 200:
            logger('ERROR', 'Failed at getting the lists.')

        return response.json()

    def archive_list(self, list_id: str):
        response = requests.put(
            'https://api.trello.com/1/lists/{LIST_ID}/closed?value=true&key={KEY}&token={TOKEN}'.format(
                LIST_ID=list_id, KEY=self._key, TOKEN=self._token
            )
        )

        if response.status_code != 200:
            logger('ERROR', 'Failed at archiving the list `{}`.'.format(list_id))

    def update_list(self, list_id: str,
                    title: str = None, closed: bool = None,
                    idBoard: str = None,
                    position: Union[str, int] = None):

        params = ['key={}'.format(self._key),
                  'token={}'.format(self._token)]
        if title:
            params.append('name={}'.format(title))
        if type(closed) == bool:
            params.append('closed={}'.format(closed))
        if idBoard:
            params.append('idBoard={}'.format(idBoard))
        if position:
            position = self._handle_position(position)
            params.append('pos={}'.format(position))

        response = requests.put(
            'https://api.trello.com/1/lists/{}?'.format(list_id) +
            "&".join(params)
        )

        if response.status_code != 200:
            logger('ERROR', 'Failed at deleting the list `{}`({}).'.format(
                list_id, response.text))

    def delete_list(self, list_id: str):
        self.update_list(list_id=list_id, idBoard=self._trash_board_id)

    def get_cards(self, list_id: str):
        url = 'https://api.trello.com/1/lists/' + \
            '{LIST_ID}/cards?fields=all&key={KEY}&token={TOKEN}'
        response = requests.get(url.format(
            LIST_ID=list_id, KEY=self._key, TOKEN=self._token
        ))

        if response.status_code != 200:
            logger('ERROR', 'Failed at fetching the card `{}` ().'.format(
                list_id, response.text))

        return response.json()

    def get_card(self, card_id: str):
        response = requests.get('https://api.trello.com/1/cards/' +
                                '{CARD_ID}?key={KEY}&token={TOKEN}'.format(
                                    CARD_ID=card_id, KEY=self._key, TOKEN=self._token
                                ))

        if response.status_code != 200:
            logger('ERROR', 'Failed at fetching the card `{}` ().'.format(
                card_id, response.text))

        return response.json()


class APIHandler:
    def __init__(self, config):
        self.trello = Trello(config)
