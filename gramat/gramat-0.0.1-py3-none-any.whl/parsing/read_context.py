from typing import List

from gramat.errors import GramatError
from gramat.parsing.source import Source


class ReadContext:

    def __init__(self, source: Source):
        self.source = source
        self.stop_marks: List[str] = []

    def error(self, message: str) -> GramatError:
        return self.source.error(message)

    # TODO implement literal and char predicate caching
