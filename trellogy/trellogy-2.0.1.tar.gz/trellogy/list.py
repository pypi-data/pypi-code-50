from .error import TrellogyError, NotEnoughParamsError
from .component import Component
from .card import Card
from .label import Label


class List(Component):
    def __init__(self, **kwargs):
        """
        [Description]:
            Implementation of <Trello List>
        [Params]:
            -------------------------------------------------------------------
            PARAMETER  | TYPE   | DESCRIPTION
            -------------------------------------------------------------------
            key        | <str>  | API key
            token      | <str>  | API token
            id         | <str>  | Board ID
            name       | <str>  | Name of this list
            closed     | <bool> | Whether this list is closed or not.
            position   | <int>  | Position of this list
            -------------------------------------------------------------------

        [Available Methods]:
            -------------------------------------------------------------------
            METHOD         | DESCRIPTION
            -------------------------------------------------------------------
            create_card    | Create a Trello Card that belongs to this list.
            get_cards      | Get a list of Trello Cards.
            update         | Update this list.
            archive        | Archive this list.
            unarchive      | Unarchive this list.
            -------------------------------------------------------------------

        [Available Properties]:
            -------------------------------------------------------------------
            PROPERTY       | DESCRIPTION
            -------------------------------------------------------------------
            key            | API key
            token          | API token
            id             | ID of this list
            board_id       | ID of the parent board
            name           | Name of this list
            closed         | Whether the board is archived
            position       | Position of this list
            -------------------------------------------------------------------            
        """
        _attributes = ['id', 'board_id', 'name', 'closed', 'position']
        super().__init__(**kwargs, _attributes=_attributes)

    def create_card(self, name, position='bottom'):
        """
        [Description]:
            Create a Trello Card.

        [Params]:
            -------------------------------------------------------------------
            PARAMETER  | TYPE  | DESCRIPTION
            -------------------------------------------------------------------
            name       | <str> | Name of the card
            position   | <str> | Position of the card
            -------------------------------------------------------------------

        [Note]:
            Parameter `position` should be one of the followings:
            'bottom', 'top', or floating number.

        [Returns]:
            <Trellogy.Card> of the new Trello List.
        """
        if name is None:
            raise NotEnoughParamsError('name')

        response = self.req('POST', '/lists/{}/cards'.format(self._id),
                            name=name, pos=position)

        return Card(key=self._key, token=self._token,
                    board_id=self._board_id,
                    list_id=self._id,
                    id=response['id'],
                    closed=response['closed'],
                    name=response['name'],
                    desc=response['desc'],
                    labels=[]
                    )

    def update(self, name=None, closed=None, board_id=None, position=None):
        """
        [Description]:
            Update attributes of this list.

        [Params]:
            -------------------------------------------------------------------
            PARAMETER  | TYPE  | DESCRIPTION
            -------------------------------------------------------------------
            name       | <str> | New name of the list
            closed     | <str> | Whether to archive or unarchive this list
            board_id   | <str> | ID of the parent board
            position   | <str> | New position of the list
            -------------------------------------------------------------------

        [Returns]:
            None
        """
        if name is None and closed is None and \
                board_id is None and position is None:
            raise TrellogyError(
                'Need to give at least one parameter of the followings: ' +
                'name, closed, board_id, position')

        name = self._name if not name else name
        closed = self._closed if not closed else closed
        board_id = self._board_id if not board_id else board_id
        position = self._position if not position else position

        self.req('PUT', '/lists/{}'.format(self._id),
                 name=name, closed=self.bool_to_str[closed],
                 idBoard=board_id, pos=position)

    def archive(self):
        """
        [Description]:
            Archive this list.

        [Params]:
            None

        [Returns]:
            None
        """

        self.update(closed=True)

    def unarchive(self):
        """
        [Description]:
            Archive this list.

        [Params]:
            None

        [Returns]:
            None
        """

        self.update(closed=False)

    def get_cards(self):
        """
        [Description]:
            Get Trello Cards that belong to this list.

        [Params]:
            None

        [Returns]:
            A list of <Trellogy.Card>
        """
        path = '/lists/{LIST_ID}/cards'.format(LIST_ID=self._id)
        response = self.req('GET', path, fields='all')

        cards = []
        for card in response:
            labels = []
            for label in card['labels']:
                labels.append(Label(key=self._key,
                                    token=self._token,
                                    board_id=self._board_id,
                                    id=label['id'],
                                    color=label['color'],
                                    name=label['name']
                                    ))

            cards.append(Card(key=self._key, token=self._token,
                              board_id=self._board_id,
                              list_id=self._id,
                              id=card['id'],
                              closed=card['closed'],
                              name=card['name'],
                              desc=card['desc'],
                              labels=labels
                              ))
        return cards
