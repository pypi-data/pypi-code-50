from .error import TrellogyError, NotEnoughParamsError
from .component import Component


class Label(Component):
    def __init__(self, **kwargs):
        """
        [Description]:
            Implementation of <Trello Label>
        [Params]:
            -------------------------------------------------------------------
            PARAMETER  | TYPE   | DESCRIPTION
            -------------------------------------------------------------------
            key        | <str>  | API key
            token      | <str>  | API token
            id         | <str>  | Board ID
            name       | <str>  | Name of this label
            color      | <str>  | Color of this label
            -------------------------------------------------------------------

        [Available Methods]:
            -------------------------------------------------------------------
            METHOD         | DESCRIPTION
            -------------------------------------------------------------------
            update         | Update this label.
            delete         | Delete this label.
            -------------------------------------------------------------------

        [Available Properties]:
            -------------------------------------------------------------------
            PROPERTY       | DESCRIPTION
            -------------------------------------------------------------------
            key            | API key
            token          | API token
            board_id       | Board ID of this label
            id             | ID of this label
            name           | Name of this label
            color          | Color of this label
            -------------------------------------------------------------------            
        """
        _attributes = ['id', 'board_id', 'name', 'color']
        super().__init__(**kwargs, _attributes=_attributes)

    def update(self, name=None, color=None):
        """
        [Description]:
            Update attributes of this list.

        [Params]:
            -------------------------------------------------------------------
            PARAMETER  | TYPE  | DESCRIPTION
            -------------------------------------------------------------------
            name       | <str> | New name of the label
            color      | <str> | New color of the label 
            -------------------------------------------------------------------

        [Returns]:
            None
        """
        if name is None and color is None:
            raise TrellogyError('Need to give either name or color value.')

        if not name:
            name = self._name
        if not color:
            color = self._color

        colors = ['yellow', 'purple', 'blue', 'red', 'green', 'orange',
                  'black', 'sky', 'pink', 'lime', 'null']
        if color.lower() not in colors:
            raise TrellogyError('`color` should be one of the followings: ' +
                                '[yellow, purple, blue, red, green, ' +
                                'orange, black, sky, pink, lime, null].')

        self.req('PUT', '/labels/{}'.format(self._id),
                 name=name, color=color)

    def delete(self):
        """
        [Description]:
            Remove this label from the board.

        [Params]:
            None

        [Returns]:
            None
        """
        self.req('DELETE', '/labels/{}'.format(self._id))
