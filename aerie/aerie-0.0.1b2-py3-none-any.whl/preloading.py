from typing import TypeVar

from .fields import Relation
from .schemas import Schema

E = TypeVar('E', bound=Schema)


class Preload:
    def __init__(self, relation: Relation):
        self.relation = relation
