from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from frater.data_type import DataType


@dataclass
class Experiment(DataType):
    name: str = ''
    experiment_id: str = field(default_factory=lambda: str(uuid4()))
    created: datetime = field(default_factory=datetime.now)
