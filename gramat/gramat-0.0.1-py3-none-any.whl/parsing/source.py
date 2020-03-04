from __future__ import annotations

from io import StringIO
from typing import Optional, List, Tuple

from gramat.parsing.location import Location


class Source:

    def __init__(self, text: str, src: Optional[str] = None):
        self.text = text
        self.length = len(text)
        self.src = src
        self.position = 0

    def substring(self, begin: int, end: int) -> str:
        # TODO validate indexes
        return self.text[begin:end]

    @staticmethod
    def from_file(file_path):
        with open(file_path) as f:
            text = f.read()

        return Source(text, file_path)

    @property
    def location(self) -> Location:
        return Location(self, self.position)

    def peek(self) -> Optional[str]:
        if self.position < self.length:
            return self.text[self.position]

        return None

    def move_next(self) -> bool:
        if self.position < self.length:
            self.position += 1
            return True
        return False

    def try_move(self, delta=1) -> int:
        if delta > 0:
            count = 0

            for i in range(delta):
                if self.move_next():
                    count += 1
                else:
                    break

            return count
        else:
            raise NotImplementedError()

    def test_any(self, tokens: List[str]) -> bool:
        for token in tokens:
            if self.test(token):
                return True
        return False

    def test(self, token: Optional[str]) -> bool:
        if token is None:
            return False

        pos0 = self.position

        for expected_char in token:
            actual_char = self.peek()

            if actual_char is None or actual_char != expected_char:
                self.position = pos0
                return False

            self.move_next()

        self.position = pos0
        return True

    def pull_any(self, tokens: List[str]) -> Optional[str]:
        for token in tokens:
            if self.pull(token):
                return token
        return None

    def pull(self, token: str) -> bool:
        pos0 = self.position

        for expected_char in token:
            actual_char = self.peek()

            if actual_char is None or actual_char != expected_char:
                self.position = pos0
                return False

            self.move_next()

        return True

    def extract(self, length: int) -> str:
        out = StringIO()

        for i in range(length):
            c = self.peek()

            if c is None:
                raise self.error('Unexpected EOF.')

            out.write(c)
            self.move_next()

        return out.getvalue()

    def error(self, message: str):
        return self.location.error(message)

    def error_expected_symbols(self, *symbols: str):
        # TODO convert to a method for parsing
        return self.error(f'Expected symbols: {", ".join(symbols)}')

    def get_coordinates(self, some_position: int) -> Tuple[int, int]:
        line = 0
        column = 0

        for index, c in enumerate(self.text):
            if c == '\n':
                line += 1
                column = 0
            else:
                column += 1

            if index >= some_position:
                break

        return line, column
