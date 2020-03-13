from typing import (Callable,
                    TypeVar)

try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol


class Sortable(Protocol):
    def __lt__(self, other: 'Sortable') -> bool:
        """
        Checks if the object is less than the other one.
        """


Domain = TypeVar('Domain')
OtherDomain = TypeVar('OtherDomain')
SortingKey = Callable[[Domain], Sortable]
