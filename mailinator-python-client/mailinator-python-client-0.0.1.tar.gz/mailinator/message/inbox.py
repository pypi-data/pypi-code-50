from enum import Enum
from typing import List

from dataclasses import dataclass
from dataclasses_json import dataclass_json

from .message import Message


class Sort(Enum):
    ASC = 'ascending'
    DESC = 'descending'


@dataclass_json
@dataclass
class Inbox(object):

    domain: str
    to: str
    msgs: List[Message]
