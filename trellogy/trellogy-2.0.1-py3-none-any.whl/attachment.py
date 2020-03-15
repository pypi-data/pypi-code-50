from .error import TrellogyError, NotEnoughParamsError
from .component import Component


class Attachment(Component):
    def __init__(self, **kwargs):
        """
        [Description]:
            Implementation of <Trello Attachment>
        [Params]:
            -------------------------------------------------------------------
            PARAMETER  | TYPE  | DESCRIPTION
            -------------------------------------------------------------------
            id         | <str> | Attachment ID
            card_id    | <str> | ID of the parent Card Component
            name       | <str> | Name of the parent Card Component
            url        | <str> | Downloadable URL link of the attachment
            -------------------------------------------------------------------
        """
        _attributes = ['id', 'card_id', 'size', 'name', 'url']
        super().__init__(**kwargs, _attributes=_attributes)

    def delete(self):
        """
        [Description]:
            Remove this attachment from the card.
        [Params]:
            None
        [Returns]:
            None
        """
        path = '/cards/{CARD_ID}/attachments/{ATTACHMENT_ID}'\
            .format(CARD_ID=self._card_id, ATTACHMENT_ID=self._id)
        self.req('DELETE', path)
