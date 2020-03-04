from dataclasses import dataclass
from dataclasses_json import dataclass_json
from enum import Enum


class OperationType(Enum):
	EQUALS = 'EQUALS'
	PREFIX = 'PREFIX'


@dataclass_json
@dataclass
class Condition(object):
	operation: OperationType
	value: str
	field: str = 'to'
