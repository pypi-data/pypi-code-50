from typing import List

from mailinator.client import ResourceInterface
from mailinator.constants import INBOX_URL, MESSAGE_URL, ATTACHMENTS_URL, ATTACHMENT_URL
from mailinator.message.inbox import Inbox, Message, Sort
from mailinator.message.attachment import Attachment


class InboxInterface(ResourceInterface):

    def __init__(self, domain_id: str, inbox_id: str):
        self.base_url = INBOX_URL.format(domain_id=domain_id, inbox_id=inbox_id)
        self.query_params = {}

    def skip(self, skip: int):
        self.query_params['skip'] = skip
        return self

    def sort(self, sort: Sort):
        self.query_params['sort'] = sort
        return self

    def limit(self, limit: int):
        self.query_params['limit'] = limit
        return self

    def decode_subject(self, decode_subject: bool):
        self.query_params['decode_subject'] = decode_subject
        return self

    def execute(self, session) -> Inbox:
        result = session.get(self.base_url, params=self.query_params)
        return Inbox.from_json(result.text)


class SmsInboxInterface(ResourceInterface):

    def __init__(self, domain_id: str, phone_number: str):
        self.base_url = INBOX_URL.format(domain_id=domain_id, inbox_id=phone_number)

    def execute(self, session) -> Inbox:
        result = session.get(self.base_url)
        return Inbox.from_json(result.text)


class MessageInterface(ResourceInterface):

    def __init__(self, domain_id: str, inbox_id: str, message_id: str):
        self.base_url = MESSAGE_URL.format(domain_id=domain_id, inbox_id=inbox_id, message_id=message_id)

    def execute(self, session) -> Message:
        result = session.get(self.base_url)
        return Message.from_json(result.text)


class AttachmentInterface(ResourceInterface):

    def __init__(self, domain_id: str, inbox_id: str, message_id: str, attachment_id: str):
        self.base_url = ATTACHMENT_URL.format(
            domain_id=domain_id,
            inbox_id=inbox_id,
            message_id=message_id,
            attachment_id=attachment_id
        )

    def execute(self, session) -> Attachment:
        result = session.get(self.base_url)
        return Attachment.from_json(result.text)


class AttachmentsInterface(ResourceInterface):

    def __init__(self, domain_id: str, inbox_id: str, message_id: str):
        self.base_url = ATTACHMENTS_URL.format(
            domain_id=domain_id,
            inbox_id=inbox_id,
            message_id=message_id
        )

    def execute(self, session) -> List[Attachment]:
        result = session.get(self.base_url)
        return Attachment.schema().loads(result.text, many=True)
