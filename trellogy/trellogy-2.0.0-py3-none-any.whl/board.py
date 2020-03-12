from .error import TrellogyError, NotEnoughParamsError
from .component import Component
from .label import Label
from .list import List
from .card import Card


class Board(Component):
    def __init__(self, **kwargs):
        """
        [Description]:
            Implementation of <Trello Board>
        [Params]:
            -------------------------------------------------------------------
            PARAMETER  | TYPE  | DESCRIPTION
            -------------------------------------------------------------------
            key        | <str> | API key
            token      | <str> | API token
            id         | <str> | ID of this board
            -------------------------------------------------------------------

        [Available Methods]:
            -------------------------------------------------------------------
            METHOD         | DESCRIPTION
            -------------------------------------------------------------------
            create_label   | Create a Trello Label.
            create_list    | Create a Trello List.
            update         | Update attributes of this board.
            -------------------------------------------------------------------

        [Available Properties]:
            -------------------------------------------------------------------
            PROPERTY       | DESCRIPTION
            -------------------------------------------------------------------
            key            | API key
            token          | API token
            id             | ID of this board
            name           | Name of this board.
            labels         | A list of Trello Lists available on this board.
            lists          | A list of Trello Labels available on this board.
            archived_cards | A list of archived Trello Cards on this board.
            archived_lists | A list of archived Trello Lists on this board.
            -------------------------------------------------------------------            
        """
        _attributes = []
        super().__init__(**kwargs, _attributes=_attributes)

    def create_label(self, name=None, color=None):
        """
        [Description]:
            Create a Trello Label.

        [Params]:
            -------------------------------------------------------------------
            PARAMETER  | TYPE  | DESCRIPTION
            -------------------------------------------------------------------
            name       | <str> | Name of the label
            color      | <str> | Color of the label
            -------------------------------------------------------------------

        [Note]:
            parameter `color` should be one of the followings: yellow, purple,
            blue, red, green, orange, black, sky, pink, lime, null.

        [Returns]:
            <Trellogy.Label> of the new Trello Label.
        """
        if name is None:
            raise NotEnoughParamsError('name')
        if color is None:
            raise NotEnoughParamsError('color')

        colors = ['yellow', 'purple', 'blue', 'red', 'green', 'orange',
                  'black', 'sky', 'pink', 'lime', 'null']
        if color.lower() not in colors:
            raise TrellogyError('`color` should be one of the followings: ' +
                                '[yellow, purple, blue, red, green, ' +
                                'orange, black, sky, pink, lime, null].')

        response = self.req('POST', '/labels',
                            name=name, color=color.lower(), idBoard=self._id)

        return Label(key=self._key,
                     token=self._token,
                     id=response['id'],
                     board_id=response['idBoard'],
                     name=response['name'],
                     color=response['color'])

    def create_list(self, name, position='bottom'):
        """
        [Description]:
            Create a Trello List.

        [Params]:
            -------------------------------------------------------------------
            PARAMETER  | TYPE  | DESCRIPTION
            -------------------------------------------------------------------
            name       | <str> | Name of the list
            position   | <str> | Position of the list
            -------------------------------------------------------------------

        [Note]:
            Parameter `position` should be one of the followings:
            'bottom', 'top', or floating number.

        [Returns]:
            <Trellogy.List> of the new Trello List.
        """
        if name is None:
            raise NotEnoughParamsError('name')

        response = self.req('POST', '/boards/{}/lists'.format(self._id),
                            name=name, pos=position)

        return List(key=self._key, token=self._token, id=response['id'],
                    position=response['pos'], closed=response['closed'])

    def update(self, name=None):
        """
        [Description]:
            Update attributes of this board.

        [Params]:
            -------------------------------------------------------------------
            PARAMETER  | TYPE  | DESCRIPTION
            -------------------------------------------------------------------
            name       | <str> | New name of the board
            -------------------------------------------------------------------

        [Returns]:
            None
        """
        name = self._name if name is None else name
        self.req('PUT', '/boards/{}'.format(self._id), name=name)

    @property
    def name(self):
        """
        [Description]: Name of this board
        """
        path = '/boards/{BOARD_ID}/name'.format(BOARD_ID=self._id)
        response = self.req('GET', path)
        return response['_value']

    @property
    def labels(self):
        """
        [Description]: A list of Trello Labels available on this board.
        """
        path = '/boards/{BOARD_ID}/labels'.format(BOARD_ID=self._id)
        response = self.req('GET', path)
        labels = []
        for label in response:
            labels.append(Label(key=self._key,
                                token=self._token,
                                id=label['id'],
                                board_id=label['idBoard'],
                                name=label['name'],
                                color=label['color']))
        return labels

    @property
    def lists(self):
        """
        [Description]: A list of Trello Lists available on this board.
        """
        path = '/boards/{BOARD_ID}/lists'.format(BOARD_ID=self._id)
        response = self.req('GET', path)
        t_lists = []
        for t_list in response:
            t_lists.append(List(key=self._key,
                                token=self._token,
                                id=t_list['id'],
                                board_id=t_list['idBoard'],
                                name=t_list['name'],
                                position=t_list['pos'],
                                closed=t_list['closed']))
        return t_lists

    @property
    def archived_cards(self):
        """
        [Description]: A list of archived Trello Cards on this board.
        """
        path = '/boards/{BOARD_ID}/cards'.format(BOARD_ID=self._id)
        response = self.req('GET', path, fields='all', filter='closed')

        cards = []
        for card in response:
            labels = []
            for label in card['labels']:
                labels.append(Label(key=self._key,
                                    token=self._token,
                                    board_id=self._id,
                                    id=label['id'],
                                    color=label['color'],
                                    name=label['name']
                                    ))

            cards.append(Card(key=self._key, token=self._token,
                              board_id=self._id,
                              list_id=card['idList'],
                              id=card['id'],
                              closed=card['closed'],
                              name=card['name'],
                              desc=card['desc'],
                              labels=labels
                              ))
        return cards

    @property
    def archived_lists(self):
        """
        [Description]: A list of archived Trello Lists on this board.
        """
        path = '/boards/{BOARD_ID}/lists'.format(BOARD_ID=self._id)
        response = self.req('GET', path, filter='closed')
        t_lists = []
        for t_list in response:
            t_lists.append(List(key=self._key,
                                token=self._token,
                                id=t_list['id'],
                                board_id=t_list['idBoard'],
                                name=t_list['name'],
                                position=t_list['pos'],
                                closed=t_list['closed']))
        return t_lists
