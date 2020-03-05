from dataclasses import dataclass
from dataclasses_json import dataclass_json
from enum import Enum
from typing import List

from .action import Action
from .condition import Condition


class MatchType(Enum):
	ANY = 'ANY'
	ALL = 'ALL'
	ALWAYS_MATCH = 'ALWAYS_MATCH'


@dataclass_json
@dataclass
class Rule(object):
	_id: str 
	description: str 
	enabled: bool 
	match: MatchType 
	name: str
	conditions: List[Condition]
	actions: List[Action]


@dataclass_json
@dataclass
class RuleToCreate(object):
	description: str
	name: str
	priority: int
	conditions: List[Condition]
	actions: List[Action]
	enabled: bool = True
	match: MatchType = MatchType.ALL
