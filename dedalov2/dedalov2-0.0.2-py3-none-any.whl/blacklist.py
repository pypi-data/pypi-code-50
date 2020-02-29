
import os
import logging
from typing import Optional, Set

from .knowledge_graph import Predicate

LOG = logging.getLogger('dedalov2.blacklist')


class Blacklist:

    @staticmethod
    def fromFile(filename: Optional[str]) -> 'Blacklist':
        bl = Blacklist()
        if filename is not None:
            if not os.path.isfile(filename):
                raise ValueError("{} is not a file!".format(filename))
            with open(filename) as fin:
                lines = map(lambda line: line.strip(), fin.readline())
                for line in lines:
                    try:
                        bl.addToBlacklist(Predicate.fromString(line))
                    except ValueError as e:
                        LOG.warning(e)
        return bl

    def __init__(self):
        self.blacklisted_items: Set[Predicate] = set()

    def addToBlacklist(self, item: Predicate) -> None:
        self.blacklisted_items.add(item)

    def isBlacklisted(self, p: Predicate) -> bool:
        return p in self.blacklisted_items
