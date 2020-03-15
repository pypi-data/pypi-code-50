from urllib.request import quote
from .error import TrellogyError, NotEnoughParamsError
from .component import Component
from .attachment import Attachment
import requests


class Card(Component):
    def __init__(self, **kwargs):
        """
        [Description]:
            Implementation of <Trello Card>
        [Params]:
            -------------------------------------------------------------------
            PARAMETER  | TYPE   | DESCRIPTION
            -------------------------------------------------------------------
            key        | <str>  | API key
            token      | <str>  | API token
            id         | <str>  | Board ID
            name       | <str>  | Name of this card
            desc       | <str>  | Description of this card
            labels     | <list> | A List of labels that belong to this card
            -------------------------------------------------------------------

        [Available Methods]:
            -------------------------------------------------------------------
            METHOD          | DESCRIPTION
            -------------------------------------------------------------------
            add_attachment  | Add a Trello Attachment to this card. 
            get_attachments | Get a list of Trello Cards.
            update          | Update this card.
            archive         | Archive this card.
            unarchive       | Unarchive this card.
            -------------------------------------------------------------------

        [Available Properties]:
            -------------------------------------------------------------------
            PROPERTY       | DESCRIPTION
            -------------------------------------------------------------------
            key            | API key
            token          | API token
            id             | ID of this card
            board_id       | ID of the parent board
            name           | Name of this card
            desc           | Description of this card
            closed         | Whether the card is archived
            labels         | Position of this card
            -------------------------------------------------------------------            
        """

        _attributes = ['id', 'closed', 'name', 'desc', 'labels']
        super().__init__(**kwargs, _attributes=_attributes)

    def update(self, name=None, closed=None, desc=None, labels=None, board_id=None):
        """
        [Description]:
            Update attributes of this card.

        [Params]:
            -------------------------------------------------------------------
            PARAMETER  | TYPE   | DESCRIPTION
            -------------------------------------------------------------------
            name       | <str>  | New name of the card
            closed     | <str>  | Whether to archive or unarchive this card
            desc       | <str>  | New description of the card
            board_id   | <str>  | ID of the parent board
            labels     | <list> | New list of Trello Labels for this card
            -------------------------------------------------------------------

        [Returns]:
            None
        """

        name = self._name if name is None else name
        closed = self._closed if closed is None else closed
        desc = self._desc if desc is None else desc
        labels = self._labels if labels is None else labels
        board_id = self._board_id if board_id is None else board_id

        # Update labels
        labels_id = ",".join([label.id for label in labels])
        self.req('PUT', '/cards/{}'.format(self._id),
                 name=name, closed=self.bool_to_str[closed],
                 desc=quote(desc), idLabels=labels_id, idBoard=board_id)

    def archive(self):
        """
        [Description]:
            Archive this card.

        [Params]:
            None

        [Returns]:
            None
        """
        self.update(closed=True)

    def unarchive(self):
        """
        [Description]:
            Archive this card.

        [Params]:
            None

        [Returns]:
            None
        """
        self.update(closed=False)

    def add_attachment(self, filepath):
        """
        [Description]:
            Add attachment to this card.

        [Params]:
            -------------------------------------------------------------------
            PARAMETER  | TYPE  | DESCRIPTION
            -------------------------------------------------------------------
            filepath   | <str> | Local path of the attachment file
            -------------------------------------------------------------------

        [Returns]:
            None
        """
        params = (
            ('key', self._key),
            ('token', self._token),
        )

        files = {
            'file': (filepath, open(filepath, 'rb')),
        }

        response = requests.post(
            'https://api.trello.com/1/cards/{}/attachments'.format(self._id),
            params=params, files=files)

        return Attachment(key=self._key, token=self._token,
                          card_id=self._id,
                          id=response.data['id'],
                          size=response.data['bytes'],
                          name=response.data['name'],
                          url=response.data['url'])

    def get_attachments(self):
        """
        [Description]:
            Get Trello Attachments that belong to this card.

        [Params]:
            None

        [Returns]:
            A list of <Trellogy.Attachment>
        """
        path = '/cards/{CARD_ID}/attachments'.format(CARD_ID=self._id)
        response = self.req('GET', path)

        attachments = []
        for attachment in response:
            attachments.append(Attachment(key=self._key, token=self._token,
                                          card_id=self._id,
                                          id=attachment['id'],
                                          size=attachment['bytes'],
                                          name=attachment['name'],
                                          url=attachment['url']))
        return attachments
