from .components import List, Card
from .error import TrellogyError
import requests


class Trellogy:
    def __init__(self, key, token, board_id, trash_id=None):
        self._key = key
        self._token = token
        self._board_id = board_id
        self._idTrash = trash_id

    def create_list(self, title: str, pos='bottom') -> List:
        response = requests.post(
            'https://api.trello.com/1/boards/' +
            '{BOARD_ID}/lists?name={TITLE}&pos={POSITION}&key={KEY}&token={TOKEN}'.format(
                BOARD_ID=self._board_id,
                TITLE=title, POSITION=pos,
                KEY=self._key, TOKEN=self._token,
            )
        )
        if response.status_code != 200:
            raise TrellogyError(response.json()['message'])

        new_list = response.json()
        return List(key=self._key,
                    token=self._token,
                    idTrash=self._idTrash,
                    **new_list)

    def get_lists(self) -> list:
        response = requests.get(
            'https://api.trello.com/1/boards/' +
            '{BOARD_ID}/lists?key={KEY}&token={TOKEN}'.format(
                BOARD_ID=self._board_id, KEY=self._key, TOKEN=self._token
            ))
        if response.status_code != 200:
            raise TrellogyError(response.text)

        lists = []
        for list_item in response.json():
            lists.append(
                List(key=self._key,
                     token=self._token,
                     idTrash=self._idTrash,
                     **list_item))
        return lists

    def get_list(self, list_id: str) -> List:
        url = 'https://api.trello.com/1/lists' + \
            '/{LIST_ID}?key={KEY}&token={TOKEN}'.format(
                BOARD_ID=self._board_id, KEY=self._key, TOKEN=self._token,
                LIST_ID=list_id
            )
        response = requests.get(url)

        if response.status_code != 200:
            raise TrellogyError(response.text)

        return List(key=self._key,
                    token=self._token,
                    idTrash=self._idTrash,
                    **response.json())
