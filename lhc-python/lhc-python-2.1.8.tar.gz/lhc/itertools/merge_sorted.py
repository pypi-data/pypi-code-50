from itertools import chain
from typing import Any, Iterator, List, Tuple


def merge_sorted(*iterators: Iterator[Any], key=lambda x: x, flatten=False) -> Iterator[List[List[Any]]]:
    tops = [next(iterator, None) for iterator in iterators]  # type: List[Any]
    smallest_indices = get_smallest_indices(tops, key)
    while len(smallest_indices) > 0:
        smallest = get_at_indices(tops, smallest_indices, iterators, key)
        yield list(chain.from_iterable(smallest)) if flatten else smallest
        smallest_indices = get_smallest_indices(tops, key)


def get_smallest_indices(tops: List[Any], key=lambda x: x) -> List[int]:
    smallest = []  # type: List[int]
    for i, item in enumerate(tops):
        if item is None:
            continue

        if len(smallest) == 0 or key(item) < key(tops[smallest[0]]):
            smallest = [i]
        elif key(item) == key(tops[smallest[0]]):
            smallest.append(i)
    return smallest


def get_at_indices(tops, indices: List[int], iterators: Tuple[Iterator[Any]], key: lambda x: x) -> List[List[Any]]:
    result = [[] for i in range(len(iterators))]  # type: List[List[Any]]
    for index in indices:
        result[index].append(tops[index])
        tops[index] = next(iterators[index], None)
        while tops[index] is not None and key(tops[index]) == key(result[index][0]):
            result[index].append(tops[index])
            tops[index] = next(iterators[index], None)
    return result
