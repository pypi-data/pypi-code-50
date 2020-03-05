from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from typing import List, Dict, Any


@dataclass_json
@dataclass
class Part(object):
    headers: Dict[str, Any]
    body: str
