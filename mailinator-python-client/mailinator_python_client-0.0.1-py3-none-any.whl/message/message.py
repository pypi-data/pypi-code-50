from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import List, Dict, Any, Optional

from mailinator.rule import Rule
from .part import Part


@dataclass_json
@dataclass
class Message(object):
    domain: str
    subject: str
    to: str
    time: int
    seconds_ago: int
    msg_from: str = field(metadata=config(field_name='from'))
    msg_id: str = field(metadata=config(field_name='id'))

    size: Optional[int] = None
    stream: Optional[str] = None
    msg_type: Optional[str] = None
    source: Optional[str] = None
    text: Optional[str] = None
    mrid: Optional[str] = None
    parts: List[Part] = field(default_factory=list)
    headers: Dict[str, Any] = field(default_factory=dict)
    from_full: Optional[str] = field(default=None, metadata=config(field_name='fromfull'))
    orig_from: Optional[str] = field(default=None, metadata=config(field_name='origfrom'))


@dataclass_json
@dataclass
class DeletedMessages(object):
    status: str
    count: int


@dataclass_json
@dataclass
class MessageToPost(object):
    subject: str
    msg_from: str = field(metadata=config(field_name='from'))
    text: str


@dataclass_json
@dataclass
class PostedMessage(object):
    status: str
    id: str
    rules_fired: List[Rule]
