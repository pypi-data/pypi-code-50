from __future__ import annotations

from gramat.errors import GramatError


class Location:

    def __init__(self, source: 'Source', position: int):
        self.source = source
        self.position = position

    def area(self, end: Location) -> Area:
        return Area(self, end)

    def error(self, message: str) -> GramatError:
        return GramatError(f'{self}: {message}')

    def __str__(self):
        line, column = self.source.get_coordinates(self.position)
        return (
            f'{self.source.src}:'
            f' Line {line + 1},'
            f' Column {column + 1}')

    @property
    def short_desc(self) -> str:
        line, column = self.source.get_coordinates(self.position)
        return f'L:{line + 1}, C:{column + 1}'


class Area:

    def __init__(self, begin: Location, end: Location):
        self.begin = begin
        self.end = end

    def error(self, message: str) -> GramatError:
        # TODO improve message
        return GramatError(f'{self.begin} - {self.end}: {message}')
