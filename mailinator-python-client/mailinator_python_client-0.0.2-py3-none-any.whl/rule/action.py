from dataclasses import dataclass
from dataclasses_json import dataclass_json
from enum import Enum


class ActionType(Enum):
	WEBHOOK = 'WEBHOOK'
	DROP = 'DROP'


@dataclass_json
@dataclass
class ActionData(object):
	url: str


@dataclass_json
@dataclass
class Action(object):	
	action: ActionType
	action_data: ActionData
	destination: str
