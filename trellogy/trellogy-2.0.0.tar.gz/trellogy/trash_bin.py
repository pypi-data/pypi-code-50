from .error import TrellogyError, NotEnoughParamsError
from .component import Component
from .card import Card
from .label import Label
from .list import List


class TrashBin(Component):
    def __init__(self, **kwargs):
        """
        [Description]:
            Implementation of Trello Board
        [Params]:
            -------------------------------------------------------------------
            PARAMETER  | TYPE  | DESCRIPTION
            -------------------------------------------------------------------
            key        | <str> | API key
            token      | <str> | API token
            id         | <str> | Board ID
            -------------------------------------------------------------------
        [Available Methods]:
            -------------------------------------------------------------------
            METHOD         | DESCRIPTION
            -------------------------------------------------------------------
            name           | Name of this board.
            -------------------------------------------------------------------
        """
        _attributes = []
        super().__init__(**kwargs, _attributes=_attributes)

    def add(self, TrellogyComponent):
        """
        [Description]:
            Move a Trellogy Component to this board.
        [Params]:
            -------------------------------------------------------------------
            PARAMETER         | TYPE    | DESCRIPTION
            -------------------------------------------------------------------
            TrellogyComponent | <class> | Trellogy List, or Trellogy Card.
            -------------------------------------------------------------------
        """
        if type(TrellogyComponent) in [List, Card]:
            return TrellogyComponent.update(board_id=self._id)

        raise TrellogyError('TrashBin can only add List or Card component.')

    @property
    def name(self):
        """
        [Description]: Name of this board.
        """
        path = '/boards/{BOARD_ID}/name'.format(BOARD_ID=self._id)
        response = self.req('GET', path)
        return response['_value']
