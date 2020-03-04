from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config


@dataclass_json
@dataclass
class Attachment(object):
    filename: str
    content_disposition: str = field(metadata=config(field_name='content-disposition'))
    content_transfer_encoding: str = field(metadata=config(field_name='content-transfer-encoding'))
    content_type: str = field(metadata=config(field_name='content-type'))
    attachment_id: str = field(metadata=config(field_name='attachment-id'))
