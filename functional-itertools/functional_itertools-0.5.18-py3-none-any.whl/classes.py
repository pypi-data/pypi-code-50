from functools import reduce
from itertools import accumulate
from itertools import chain
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import compress
from itertools import count
from itertools import cycle
from itertools import dropwhile
from itertools import filterfalse
from itertools import groupby
from itertools import islice
from itertools import permutations
from itertools import product
from itertools import repeat
from itertools import starmap
from itertools import takewhile
from itertools import tee
from itertools import zip_longest
from operator import add
from pathlib import Path
from sys import maxsize
from typing import Any
from typing import Callable
from typing import Dict
from typing import FrozenSet
from typing import Iterable
from typing import Iterator
from typing import List
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Set
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union
from warnings import warn

from more_itertools.recipes import all_equal
from more_itertools.recipes import consume
from more_itertools.recipes import dotproduct
from more_itertools.recipes import first_true
from more_itertools.recipes import flatten
from more_itertools.recipes import grouper
from more_itertools.recipes import iter_except
from more_itertools.recipes import ncycles
from more_itertools.recipes import nth
from more_itertools.recipes import nth_combination
from more_itertools.recipes import padnone
from more_itertools.recipes import pairwise
from more_itertools.recipes import partition
from more_itertools.recipes import powerset
from more_itertools.recipes import prepend
from more_itertools.recipes import quantify
from more_itertools.recipes import random_combination
from more_itertools.recipes import random_combination_with_replacement
from more_itertools.recipes import random_permutation
from more_itertools.recipes import random_product
from more_itertools.recipes import repeatfunc
from more_itertools.recipes import roundrobin
from more_itertools.recipes import tabulate
from more_itertools.recipes import tail
from more_itertools.recipes import take
from more_itertools.recipes import unique_everseen
from more_itertools.recipes import unique_justseen

from functional_itertools.compat import MAX_MIN_KEY_ANNOTATION
from functional_itertools.compat import MAX_MIN_KEY_DEFAULT
from functional_itertools.errors import EmptyIterableError
from functional_itertools.errors import MultipleElementsError
from functional_itertools.errors import UnsupportVersionError
from functional_itertools.utilities import drop_sentinel
from functional_itertools.utilities import filter_items_helper
from functional_itertools.utilities import filter_keys_helper
from functional_itertools.utilities import filter_values_helper
from functional_itertools.utilities import last_helper
from functional_itertools.utilities import map_items_helper
from functional_itertools.utilities import map_keys_helper
from functional_itertools.utilities import map_values_helper
from functional_itertools.utilities import Sentinel
from functional_itertools.utilities import sentinel
from functional_itertools.utilities import VERSION
from functional_itertools.utilities import Version


_T = TypeVar("_T")
_U = TypeVar("_U")
_V = TypeVar("_V")
_W = TypeVar("_W")


if VERSION in {Version.py36, Version.py37}:

    def _accumulate_citerable(
        self: "CIterable[_T]", func: Callable[[_T, _U], _U] = add,
    ) -> "CIterable[_T]":
        return CIterable(accumulate(self._iterable, func))

    def _accumulate_clist(
        self: "CList[_T]", func: Callable[[_T, _T], _T] = add,
    ) -> "CList[_T]":
        return self.iter().accumulate(func=func).list()


elif VERSION is Version.py38:

    def _accumulate_citerable(  # type: ignore
        self: "CIterable[_T]",
        func: Callable[[_T, _U], _U] = add,
        *,
        initial: Optional[_U] = None,
    ) -> "CIterable[Union[_T, _U]]":
        return CIterable(accumulate(self._iterable, func, initial=initial))

    def _accumulate_clist(  # type: ignore
        self: "CList[_T]",
        func: Callable[[_T, _U], _U] = add,
        *,
        initial: Optional[_U] = None,
    ) -> "CList[Union[_T, _U]]":
        return self.iter().accumulate(func=func, initial=initial).list()


else:
    raise UnsupportVersionError(VERSION)  # pragma: no cover


class CIterable(Iterable[_T]):
    __slots__ = ("_iterable",)

    def __init__(self: "CIterable[_T]", iterable: Iterable[_T]) -> None:
        try:
            iter(iterable)
        except TypeError as error:
            (msg,) = error.args
            raise TypeError(
                f"{type(self).__name__} expected an iterable, but {msg}",
            )
        else:
            self._iterable = iterable

    def __eq__(self: "CIterable[Any]", other: Any) -> bool:
        try:
            iter(other)
        except TypeError:
            return False
        else:
            return self.list() == list(other)

    @overload  # noqa: U100
    def __getitem__(self: "CIterable[_T]", item: int) -> _T:
        ...  # pragma: no cover

    @overload  # noqa: F811,U100
    def __getitem__(self: "CIterable[_T]", item: slice) -> "CIterable[_T]":
        ...  # pragma: no cover

    def __getitem__(  # noqa: F811
        self: "CIterable[_T]", item: Union[int, slice],
    ) -> Union[_T, "CIterable[_T]"]:
        if isinstance(item, int):
            if item < 0:
                raise IndexError(f"Expected a non-negative index; got {item}")
            elif item > maxsize:
                raise IndexError(
                    f"Expected an index at most {maxsize}; got {item}",
                )
            else:
                slice_ = islice(self._iterable, item, item + 1)
                try:
                    return next(slice_)
                except StopIteration:
                    raise IndexError(
                        f"{type(self).__name__} index out of range",
                    )
        elif isinstance(item, slice):
            return self.islice(item.start, item.stop, item.step)
        else:
            raise TypeError(
                f"Expected an int or slice; got a(n) {type(item).__name__}",
            )

    def __iter__(self: "CIterable[_T]") -> Iterator[_T]:
        yield from self._iterable

    def __repr__(self: "CIterable[Any]") -> str:
        return f"{type(self).__name__}({self._iterable!r})"

    def __str__(self: "CIterable[Any]") -> str:
        return f"{type(self).__name__}({self._iterable})"

    # built-in

    def all(self: "CIterable[Any]") -> bool:
        return all(self._iterable)

    def any(self: "CIterable[Any]") -> bool:
        return any(self._iterable)

    def dict(self: "CIterable[Tuple[_T,_U]]") -> "CDict[_T, _U]":
        return CDict(dict(self._iterable))

    def enumerate(
        self: "CIterable[_T]", start: int = 0,
    ) -> "CIterable[Tuple[int, _T]]":
        return CIterable(enumerate(self._iterable, start=start))

    def filter(
        self: "CIterable[_T]", func: Optional[Callable[[_T], bool]],
    ) -> "CIterable[_T]":
        return CIterable(filter(func, self._iterable))

    def frozenset(self: "CIterable[_T]") -> "CFrozenSet[_T]":
        return CFrozenSet(self._iterable)

    def iter(self: "CList[_T]") -> "CIterable[_T]":
        return CIterable(self._iterable)

    def list(self: "CIterable[_T]") -> "CList[_T]":
        return CList(self._iterable)

    def map(
        self: "CIterable[_T]", func: Callable[..., _U], *iterables: Iterable,
    ) -> "CIterable[_U]":
        return CIterable(map(func, self._iterable, *iterables))

    def max(
        self: "CIterable[_T]",
        *,
        key: MAX_MIN_KEY_ANNOTATION = MAX_MIN_KEY_DEFAULT,
        default: Union[_T, Sentinel] = sentinel,
    ) -> _T:
        _, kwargs = drop_sentinel(key=key, default=default)
        return max(self._iterable, **kwargs)

    def min(
        self: "CIterable[_T]",
        *,
        key: MAX_MIN_KEY_ANNOTATION = MAX_MIN_KEY_DEFAULT,
        default: Union[_T, Sentinel] = sentinel,
    ) -> _T:
        _, kwargs = drop_sentinel(key=key, default=default)
        return min(self._iterable, **kwargs)

    @classmethod
    def range(
        cls: Type["CIterable"],
        start: int,
        stop: Union[int, Sentinel] = sentinel,
        step: Union[int, Sentinel] = sentinel,
    ) -> "CIterable[int]":
        args, _ = drop_sentinel(stop, step)
        return cls(range(start, *args))

    def set(self: "CIterable[_T]") -> "CSet[_T]":
        return CSet(self._iterable)

    def sorted(
        self: "CIterable[_T]",
        *,
        key: Optional[Callable[[_T], Any]] = None,
        reverse: bool = False,
    ) -> "CList[_T]":
        return CList(sorted(self._iterable, key=key, reverse=reverse))

    def sum(self: "CIterable[_T]", start: Union[_T, int] = 0) -> Union[_T, int]:
        args, _ = drop_sentinel(start)
        return sum(self._iterable, *args)

    def tuple(self: "CIterable[_T]") -> Tuple[_T, ...]:
        return tuple(self._iterable)

    def zip(
        self: "CIterable[_T]", *iterables: Iterable[_U],
    ) -> "CIterable[Tuple[Union[_T, _U]]]":
        return CIterable(zip(self._iterable, *iterables))

    # extra public methods

    def first(self: "CIterable[_T]") -> _T:
        try:
            return next(iter(self._iterable))
        except StopIteration:
            raise EmptyIterableError from None

    def last(self: "CIterable[_T]") -> _T:
        return self.reduce(last_helper)

    def one(self: "CIterable[_T]") -> _T:
        head: CList[_T] = self.islice(2).list()
        if head:
            try:
                (x,) = head
            except ValueError:
                x, y = head
                raise MultipleElementsError(f"{x}, {y}")
            else:
                return x
        else:
            raise EmptyIterableError

    def pipe(
        self: "CIterable[_T]",
        func: Callable[..., Iterable[_U]],
        *args: Any,
        index: int = 0,
        **kwargs: Any,
    ) -> "CIterable[_U]":
        new_args = chain(
            islice(args, index), [self._iterable], islice(args, index, None),
        )
        return CIterable(func(*new_args, **kwargs))

    # itertools

    @classmethod
    def count(
        cls: Type["CIterable"], start: int = 0, step: int = 1,
    ) -> "CIterable[int]":
        return cls(count(start=start, step=step))

    def cycle(self: "CIterable[_T]") -> "CIterable[_T]":
        return CIterable(cycle(self._iterable))

    @classmethod
    def repeat(
        cls: Type["CIterable[_T]"], x: _T, times: Optional[int] = None,
    ) -> "CIterable[_T]":
        return cls(repeat(x, times=times))

    accumulate = _accumulate_citerable

    def chain(
        self: "CIterable[_T]", *iterables: Iterable[_U],
    ) -> "CIterable[Union[_T, _U]]":
        return CIterable(chain(self._iterable, *iterables))

    def compress(
        self: "CIterable[_T]", selectors: Iterable[Any],
    ) -> "CIterable[_T]":
        return CIterable(compress(self._iterable, selectors))

    def dropwhile(
        self: "CIterable[_T]", func: Callable[[_T], bool],
    ) -> "CIterable[_T]":
        return CIterable(dropwhile(func, self._iterable))

    def filterfalse(
        self: "CIterable[_T]", func: Callable[[_T], bool],
    ) -> "CIterable[_T]":
        return CIterable(filterfalse(func, self._iterable))

    def groupby(
        self: "CIterable[_T]", key: Optional[Callable[[_T], _U]] = None,
    ) -> "CIterable[Tuple[_U, Iterator[_T]]]":
        return CIterable(groupby(self._iterable, key=key))

    def islice(
        self: "CIterable[_T]",
        start: int,
        stop: Union[int, Sentinel] = sentinel,
        step: Union[int, Sentinel] = sentinel,
    ) -> "CIterable[_T]":
        args, _ = drop_sentinel(stop, step)
        return CIterable(islice(self._iterable, start, *args))

    def starmap(
        self: "CIterable[Iterable[_T]]", func: Callable[[Tuple[_T, ...]], _U],
    ) -> "CIterable[_U]":
        return CIterable(starmap(func, self._iterable))

    def takewhile(
        self: "CIterable[_T]", func: Callable[[_T], bool],
    ) -> "CIterable[_T]":
        return CIterable(takewhile(func, self._iterable))

    def tee(self: "CIterable[_T]", n: int = 2) -> "CIterable[Iterator[_T]]":
        return CIterable(tee(self._iterable, n=n))

    def zip_longest(
        self: "CIterable[_T]", *iterables: Iterable[_U], fillvalue: _V = None,
    ) -> "CIterable[Tuple[Union[_T, _U, _V]]]":
        return CIterable(
            zip_longest(self._iterable, *iterables, fillvalue=fillvalue),
        )

    def product(
        self: "CIterable[_T]", *iterables: Iterable[_U], repeat: int = 1,
    ) -> "CIterable[Tuple[Union[_T, _U], ...]]":
        return CIterable(product(self._iterable, *iterables, repeat=repeat))

    def permutations(
        self: "CIterable[_T]", r: Optional[int] = None,
    ) -> "CIterable[Tuple[_T, ...]]":
        return CIterable(permutations(self._iterable, r=r))

    def combinations(
        self: "CIterable[_T]", r: int,
    ) -> "CIterable[Tuple[_T, ...]]":
        return CIterable(combinations(self._iterable, r))

    def combinations_with_replacement(
        self: "CIterable[_T]", r: int,
    ) -> "CIterable[Tuple[_T, ...]]":
        return CIterable(combinations_with_replacement(self._iterable, r))

    # itertools-recipes

    def take(self: "CIterable[_T]", n: int) -> "CIterable[_T]":
        return CIterable(take(n, self._iterable))

    def prepend(self: "CIterable[_T]", value: _U) -> "CIterable[Union[_T, _U]]":
        return CIterable(prepend(value, self._iterable))

    @classmethod
    def tabulate(
        cls: Type["CIterable"], func: Callable[[int], _T], start: int = 0,
    ) -> "CIterable[_T]":
        return cls(tabulate(func, start=start))

    def tail(self: "CIterable[_T]", n: int) -> "CIterable[_T]":
        return CIterable(tail(n, self._iterable))

    def consume(
        self: "CIterable[_T]", n: Optional[int] = None,
    ) -> "CIterable[_T]":
        consume(self._iterable, n=n)
        return self

    def nth(
        self: "CIterable[_T]", n: int, default: _U = None,
    ) -> Union[_T, _U]:
        return nth(self._iterable, n, default=default)

    def all_equal(self: "CIterable[Any]") -> bool:
        return all_equal(self._iterable)

    def quantify(
        self: "CIterable[_T]", pred: Callable[[_T], bool] = bool,
    ) -> int:
        return quantify(self._iterable, pred=pred)

    def padnone(self: "CIterable[_T]") -> "CIterable[Optional[_T]]":
        return CIterable(padnone(self._iterable))

    def ncycles(self: "CIterable[_T]", n: int) -> "CIterable[_T]":
        return CIterable(ncycles(self._iterable, n))

    def dotproduct(self: "CIterable[_T]", iterable: Iterable[_T]) -> _T:
        return dotproduct(self._iterable, iterable)

    def flatten(self: "CIterable[Iterable[_T]]") -> "CIterable[_T]":
        return CIterable(flatten(self._iterable))

    @classmethod
    def repeatfunc(
        cls: Type["CIterable"],
        func: Callable[..., _T],
        times: Optional[int] = None,
        *args: Any,
    ) -> "CIterable[_T]":
        return cls(repeatfunc(func, times=times, *args))  # type: ignore

    def pairwise(self: "CIterable[_T]") -> "CIterable[Tuple[_T, _T]]":
        return CIterable(pairwise(self._iterable))

    def grouper(
        self: "CIterable[_T]", n: int, fillvalue: _U = None,
    ) -> "CIterable[Tuple[Union[_T, _U],...]]":
        return CIterable(grouper(self._iterable, n, fillvalue=fillvalue))

    def partition(
        self: "CIterable[_T]", func: Callable[[_T], bool],
    ) -> Tuple["CIterable[_T]", "CIterable[_T]"]:
        return CIterable(partition(func, self._iterable)).map(CIterable).tuple()

    def powerset(self: "CIterable[_T]") -> "CIterable[Tuple[_T,...]]":
        return CIterable(powerset(self._iterable))

    def roundrobin(
        self: "CIterable[_T]", *iterables: Iterable[_U],
    ) -> "CIterable[Tuple[_T, _U]]":
        return CIterable(roundrobin(self._iterable, *iterables))

    def unique_everseen(
        self: "CIterable[_T]", key: Optional[Callable[[_T], Any]] = None,
    ) -> "CIterable[_T]":
        return CIterable(unique_everseen(self._iterable, key=key))

    def unique_justseen(
        self: "CIterable[_T]", key: Optional[Callable[[_T], Any]] = None,
    ) -> "CIterable[_T]":
        return CIterable(unique_justseen(self._iterable, key=key))

    @classmethod
    def iter_except(
        cls: Type["CIterable"],
        func: Callable[..., _T],
        exception: Type[Exception],
        first: Optional[Callable[..., _U]] = None,
    ) -> "CIterable[Union[_T, _U]]":
        return cls(iter_except(func, exception, first=first))

    def first_true(
        self: "CIterable[_T]",
        default: _U = False,
        pred: Optional[Callable[[_T], Any]] = None,
    ) -> Union[_T, _U]:
        return first_true(self._iterable, default=default, pred=pred)

    def random_product(
        self: "CIterable[_T]", *iterables: Iterable[_U], repeat: int = 1,
    ) -> Tuple[Union[_T, _U], ...]:
        return random_product(self._iterable, *iterables, repeat=repeat)

    def random_permutation(
        self: "CIterable[_T]", r: Optional[int] = None,
    ) -> Tuple[Union[_T, _U], ...]:
        return random_permutation(self._iterable, r=r)

    def random_combination(self: "CIterable[_T]", r: int) -> Tuple[_T, ...]:
        return random_combination(self._iterable, r)

    def random_combination_with_replacement(
        self: "CIterable[_T]", r: int,
    ) -> Tuple[_T, ...]:
        return random_combination_with_replacement(self._iterable, r)

    def nth_combination(
        self: "CIterable[_T]", r: int, index: int,
    ) -> Tuple[_T, ...]:
        return nth_combination(self._iterable, r, index)

    # functools

    def reduce(
        self: "CIterable[_T]",
        func: Callable[[_T, _T], _T],
        initial: Union[_U, Sentinel] = sentinel,
    ) -> Any:
        args, _ = drop_sentinel(initial)
        try:
            return reduce(func, self._iterable, *args)
        except TypeError as error:
            (msg,) = error.args
            if msg == "reduce() of empty sequence with no initial value":
                raise EmptyIterableError from None
            else:
                raise error

    def reduce_as_iterable(
        self: "CIterable[_T]",
        func: Callable[[_T, _T], _T],
        initial: Union[_U, Sentinel] = sentinel,
    ) -> "CIterable[_T]":
        return CIterable(self.reduce(func, initial=initial))

    # pathlib

    @classmethod
    def iterdir(
        cls: Type["CIterable"], path: Union[Path, str],
    ) -> "CIterable[Path]":
        return cls(Path(path).iterdir())


class CList(List[_T]):
    """A list with chainable methods."""

    # built-in

    def all(self: "CList[Any]") -> bool:
        return self.iter().all()

    def any(self: "CList[Any]") -> bool:
        return self.iter().any()

    def dict(self: "CList[Tuple[_T, _U]]") -> "CDict[_T, _U]":
        return self.iter().dict()

    def enumerate(self: "CList[_T]", start: int = 0) -> "CList[Tuple[int, _T]]":
        return self.iter().enumerate(start=start).list()

    def filter(
        self: "CList[_T]", func: Optional[Callable[[_T], bool]],
    ) -> "CList[_T]":
        return self.iter().filter(func).list()

    def frozenset(self: "CList[_T]") -> "CFrozenSet[_T]":
        return self.iter().frozenset()

    def iter(self: "CList[_T]") -> "CIterable[_T]":
        return CIterable(self)

    def list(self: "CFrozenSet[_T]") -> "CList[_T]":
        return self.iter().list()

    def map(
        self: "CList[_T]", func: Callable[..., _U], *iterables: Iterable,
    ) -> "CList[_U]":
        return self.iter().map(func, *iterables).list()

    def max(
        self: "CList[_T]",
        *,
        key: MAX_MIN_KEY_ANNOTATION = MAX_MIN_KEY_DEFAULT,
        default: Union[_T, Sentinel] = sentinel,
    ) -> _T:
        return self.iter().max(key=key, default=default)

    def min(
        self: "CList[_T]",
        *,
        key: MAX_MIN_KEY_ANNOTATION = MAX_MIN_KEY_DEFAULT,
        default: Union[_T, Sentinel] = sentinel,
    ) -> _T:
        return self.iter().min(key=key, default=default)

    def reversed(self: "CList[_T]") -> "CList[_T]":
        return CList(reversed(self))

    def set(self: "CList[_T]") -> "CSet[_T]":
        return self.iter().set()

    def sort(
        self: "CList[_T]",
        *,
        key: Optional[Callable[[_T], Any]] = None,
        reverse: bool = False,
    ) -> "CList[_T]":
        warn("Use the 'sorted' method instead of 'sort'")
        return self.sorted(key=key, reverse=reverse)

    def sorted(
        self: "CList[_T]",
        *,
        key: Optional[Callable[[_T], Any]] = None,
        reverse: bool = False,
    ) -> "CList[_T]":
        return CList(sorted(self, key=key, reverse=reverse))

    def sum(self: "CList[_T]", start: Union[_T, int] = 0) -> Union[_T, int]:
        return self.iter().sum(start=start)

    def tuple(self: "CList[_T]") -> Tuple[_T, ...]:
        return self.iter().tuple()

    def zip(
        self: "CList[_T]", *iterables: Iterable[_U],
    ) -> "CList[Tuple[Union[_T, _U]]]":
        return self.iter().zip(*iterables).list()

    # extra public

    def one(self: "CList[_T]") -> _T:
        return self.iter().one()

    def pipe(
        self: "CList[_T]",
        func: Callable[..., Iterable[_U]],
        *args: Any,
        index: int = 0,
        **kwargs: Any,
    ) -> "CList[_U]":
        return self.iter().pipe(func, *args, index=index, **kwargs).list()

    # itertools

    @classmethod
    def repeat(cls: Type["CList"], x: _T, times: int) -> "CList[_T]":
        return CIterable.repeat(x, times=times).list()

    accumulate = _accumulate_clist

    def chain(
        self: "CList[_T]", *iterables: Iterable[_U],
    ) -> "CList[Union[_T, _U]]":
        return self.iter().chain(*iterables).list()

    def compress(self: "CList[_T]", selectors: List[Any]) -> "CList[_T]":
        return self.iter().compress(selectors).list()

    def dropwhile(
        self: "CList[_T]", func: Callable[[_T], bool],
    ) -> "CList[_T]":
        return self.iter().dropwhile(func).list()

    def filterfalse(
        self: "CList[_T]", func: Callable[[_T], bool],
    ) -> "CList[_T]":
        return self.iter().filterfalse(func).list()

    def groupby(
        self: "CList[_T]", key: Optional[Callable[[_T], _U]] = None,
    ) -> "CList[Tuple[_U, Iterator[_T]]]":
        return self.iter().groupby(key=key).list()

    def starmap(
        self: "CList[Iterable[_T]]", func: Callable[[Tuple[_T, ...]], _U],
    ) -> "CList[_U]":
        return self.iter().starmap(func).list()

    def takewhile(
        self: "CList[_T]", func: Callable[[_T], bool],
    ) -> "CList[_T]":
        return self.iter().takewhile(func).list()

    def tee(self: "CList[_T]", n: int = 2) -> "CList[Iterator[_T]]":
        return self.iter().tee(n=n).list()

    def zip_longest(
        self: "CList[_T]", *iterables: List, fillvalue: Any = None,
    ) -> "CList[Tuple[Union[_T, _U, _V]]]":
        return self.iter().zip_longest(*iterables, fillvalue=fillvalue).list()

    def product(
        self: "CList[_T]", *iterables: Iterable[_U], repeat: int = 1,
    ) -> "CList[Tuple[Union[_T, _U], ...]]":
        return self.iter().product(*iterables, repeat=repeat).list()

    def permutations(
        self: "CList[_T]", r: Optional[int] = None,
    ) -> "CList[Tuple[_T, ...]]":
        return self.iter().permutations(r=r).list()

    def combinations(self: "CList[_T]", r: int) -> "CList[Tuple[_T, ...]]":
        return self.iter().combinations(r).list()

    def combinations_with_replacement(
        self: "CList[_T]", r: int,
    ) -> "CList[Tuple[_T, ...]]":
        return self.iter().combinations_with_replacement(r).list()

    # itertools-recipes

    def take(self: "CList[_T]", n: int) -> "CList[_T]":
        return self.iter().take(n).list()

    def prepend(self: "CList[_T]", value: _U) -> "CList[Union[_T, _U]]":
        return self.iter().prepend(value).list()

    def tail(self: "CList[_T]", n: int) -> "CList[_T]":
        return self.iter().tail(n).list()

    def nth(self: "CList[_T]", n: int, default: _U = None) -> Union[_T, _U]:
        return self.iter().nth(n, default=default)

    def all_equal(self: "CList[Any]") -> bool:
        return self.iter().all_equal()

    def quantify(self: "CList[_T]", pred: Callable[[_T], bool] = bool) -> int:
        return self.iter().quantify(pred=pred)

    def ncycles(self: "CList[_T]", n: int) -> "CList[_T]":
        return self.iter().ncycles(n).list()

    def dotproduct(self: "CList[_T]", iterable: Iterable[_T]) -> _T:
        return self.iter().dotproduct(iterable)

    def flatten(self: "CList[Iterable[_T]]") -> "CList[_T]":
        return self.iter().flatten().list()

    @classmethod
    def repeatfunc(
        cls: Type["CList"], func: Callable[..., _T], times: int, *args: Any,
    ) -> "CList[_T]":
        return CIterable.repeatfunc(func, times=times, *args).list()  # type: ignore

    def pairwise(self: "CList[_T]") -> "CList[Tuple[_T, _T]]":
        return self.iter().pairwise().list()

    def grouper(
        self: "CList[_T]", n: int, fillvalue: Optional[_T] = None,
    ) -> "CList[Tuple[Union[_T, _U], ...]]":
        return self.iter().grouper(n, fillvalue=fillvalue).list()

    def partition(
        self: "CList[_T]", func: Callable[[_T], bool],
    ) -> Tuple["CList[_T]", "CList[_T]"]:
        return self.iter().partition(func).map(CList).tuple()

    def powerset(self: "CList[_T]") -> "CList[Tuple[_T,...]]":
        return self.iter().powerset().list()

    def roundrobin(
        self: "CList[_T]", *iterables: Iterable[_U],
    ) -> "CList[Tuple[_T, _U]]":
        return self.iter().roundrobin(*iterables).list()

    def unique_everseen(
        self: "CList[_T]", key: Optional[Callable[[_T], Any]] = None,
    ) -> "CList[_T]":
        return self.iter().unique_everseen(key=key).list()

    def unique_justseen(
        self: "CList[_T]", key: Optional[Callable[[_T], Any]] = None,
    ) -> "CList[_T]":
        return self.iter().unique_justseen(key=key).list()

    @classmethod
    def iter_except(
        cls: Type["CList"],
        func: Callable[..., _T],
        exception: Type[Exception],
        first: Optional[Callable[..., _U]] = None,
    ) -> "CList[Union[_T, _U]]":
        return CIterable.iter_except(func, exception, first=first).list()

    def first_true(
        self: "CList[_T]",
        default: _U = False,
        pred: Optional[Callable[[_T], Any]] = None,
    ) -> Union[_T, _U]:
        return self.iter().first_true(default=default, pred=pred).list()

    def random_product(
        self: "CList[_T]", *iterables: Iterable[_U], repeat: int = 1,
    ) -> Tuple[Union[_T, _U], ...]:
        return self.iter().random_product(*iterables, repeat=repeat)

    def random_permutation(
        self: "CList[_T]", r: Optional[int] = None,
    ) -> Tuple[_T, ...]:
        return self.iter().random_permutation(r=r)

    def random_combination(self: "CList[_T]", r: int) -> Tuple[_T, ...]:
        return self.iter().random_combination(r)

    def random_combination_with_replacement(
        self: "CList[_T]", r: int,
    ) -> Tuple[_T, ...]:
        return self.iter().random_combination_with_replacement(r)

    def nth_combination(
        self: "CList[_T]", r: int, index: int,
    ) -> Tuple[_T, ...]:
        return self.iter().nth_combination(r, index)

    # pathlib

    @classmethod
    def iterdir(cls: Type["CList"], path: Union[Path, str]) -> "CList[Path]":
        return CIterable.iterdir(path).list()


class CSet(Set[_T]):
    """A set with chainable methods."""

    # built-in

    def all(self: "CSet[Any]") -> bool:
        return self.iter().all()

    def any(self: "CSet[Any]") -> bool:
        return self.iter().any()

    def dict(self: "CSet[Tuple[_T, _U]]") -> "CDict[_T, _U]":
        return self.iter().dict()

    def filter(
        self: "CSet[_T]", func: Optional[Callable[[_T], bool]],
    ) -> "CSet[_T]":
        return self.iter().filter(func).set()

    def frozenset(self: "CSet[_T]") -> "CFrozenSet[_T]":
        return self.iter().frozenset()

    def iter(self: "CSet[_T]") -> "CIterable[_T]":
        return CIterable(self)

    def list(self: "CSet[_T]") -> "CList[_T]":
        return self.iter().list()

    def map(
        self: "CSet[_T]", func: Callable[..., _U], *iterables: Iterable,
    ) -> "CSet[_U]":
        return self.iter().map(func, *iterables).set()

    def set(self: "CSet[_T]") -> "CSet[_T]":
        return self.iter().set()

    # set & frozenset methods

    def union(self: "CSet[_T]", *others: Iterable[_U]) -> "CSet[Union[_T, _U]]":
        return CSet(super().union(*others))

    def intersection(
        self: "CSet[_T]", *others: Iterable[_U],
    ) -> "CSet[Union[_T, _U]]":
        return CSet(super().intersection(*others))

    def difference(
        self: "CSet[_T]", *others: Iterable[_U],
    ) -> "CSet[Union[_T, _U]]":
        return CSet(super().difference(*others))

    def symmetric_difference(
        self: "CSet[_T]", other: Iterable[_U],
    ) -> "CSet[Union[_T, _U]]":
        return CSet(super().symmetric_difference(other))

    def copy(self: "CSet[_T]") -> "CSet[_T]":
        return CSet(super().copy())

    # set methods

    def update(self: "CSet[_T]") -> NoReturn:
        raise RuntimeError("Use the 'union' method instead of 'update'")

    def intersection_update(self: "CSet[_T]") -> NoReturn:
        raise RuntimeError(
            "Use the 'intersection' method instead of 'intersection_update'",
        )

    def difference_update(self: "CSet[_T]") -> NoReturn:
        raise RuntimeError(
            "Use the 'difference' method instead of 'difference_update'",
        )

    def symmetric_difference_update(self: "CSet[_T]") -> NoReturn:
        raise RuntimeError(
            "Use the 'symmetric_difference' method instead of "
            "'symmetric_difference_update'",
        )

    def add(self: "CSet[_T]", element: _T) -> "CSet[_T]":
        super().add(element)
        return self

    def remove(self: "CSet[_T]", element: _T) -> "CSet[_T]":
        super().remove(element)
        return self

    def discard(self: "CSet[_T]", element: _T) -> "CSet[_T]":
        super().discard(element)
        return self

    def pop(self: "CSet[_T]") -> "CSet[_T]":
        super().pop()
        return self

    def clear(self: "CSet[_T]") -> "CSet[_T]":
        super().clear()
        return self

    # extra public

    def one(self: "CSet[_T]") -> _T:
        return self.iter().one()

    def pipe(
        self: "CSet[_T]",
        func: Callable[..., Iterable[_U]],
        *args: Any,
        index: int = 0,
        **kwargs: Any,
    ) -> "CSet[_U]":
        return self.iter().pipe(func, *args, index=index, **kwargs).set()

    # pathlib

    @classmethod
    def iterdir(cls: Type["CSet"], path: Union[Path, str]) -> "CSet[Path]":
        return CIterable.iterdir(path).set()


class CFrozenSet(FrozenSet[_T]):
    """A frozenset with chainable methods."""

    # built-in

    def all(self: "CFrozenSet[Any]") -> bool:
        return self.iter().all()

    def any(self: "CFrozenSet[Any]") -> bool:
        return self.iter().any()

    def dict(self: "CFrozenSet[Tuple[_T, _U]]") -> "CDict[_T, _U]":
        return self.iter().dict()

    def filter(
        self: "CFrozenSet[_T]", func: Optional[Callable[[_T], bool]],
    ) -> "CFrozenSet[_T]":
        return self.iter().filter(func).frozenset()

    def frozenset(self: "CFrozenSet[_T]") -> "CFrozenSet[_T]":
        return self.iter().frozenset()

    def iter(self: "CFrozenSet[_T]") -> "CIterable[_T]":
        return CIterable(self)

    def list(self: "CFrozenSet[_T]") -> "CList[_T]":
        return self.iter().list()

    def map(
        self: "CFrozenSet[_T]", func: Callable[..., _U], *iterables: Iterable,
    ) -> "CFrozenSet[_U]":
        return self.iter().map(func, *iterables).frozenset()

    def set(self: "CFrozenSet[_T]") -> "CSet[_T]":
        return self.iter().set()

    # set & frozenset methods

    def union(
        self: "CFrozenSet[_T]", *others: Iterable[_U],
    ) -> "CFrozenSet[Union[_T, _U]]":
        return CFrozenSet(super().union(*others))

    def intersection(
        self: "CFrozenSet[_T]", *others: Iterable[_U],
    ) -> "CFrozenSet[Union[_T, _U]]":
        return CFrozenSet(super().intersection(*others))

    def difference(
        self: "CFrozenSet[_T]", *others: Iterable[_U],
    ) -> "CFrozenSet[Union[_T, _U]]":
        return CFrozenSet(super().difference(*others))

    def symmetric_difference(
        self: "CFrozenSet[_T]", other: Iterable[_U],
    ) -> "CFrozenSet[Union[_T, _U]]":
        return CFrozenSet(super().symmetric_difference(other))

    def copy(self: "CFrozenSet[_T]") -> "CFrozenSet[_T]":
        return CFrozenSet(super().copy())

    # extra public

    def one(self: "CFrozenSet[_T]") -> _T:
        return self.iter().one()

    def pipe(
        self: "CFrozenSet[_T]",
        func: Callable[..., Iterable[_U]],
        *args: Any,
        index: int = 0,
        **kwargs: Any,
    ) -> "CFrozenSet[_U]":
        return self.iter().pipe(func, *args, index=index, **kwargs).frozenset()

    # pathlib

    @classmethod
    def iterdir(
        cls: Type["CFrozenset"], path: Union[Path, str],
    ) -> "CFrozenSet[Path]":
        return CIterable.iterdir(path).frozenset()


class CDict(Dict[_T, _U]):
    """A dictionary with chainable methods."""

    def keys(self: "CDict[_T, Any]") -> CIterable[_T]:
        return CIterable(super().keys())

    def values(self: "CDict[Any, _U]") -> CIterable[_U]:
        return CIterable(super().values())

    def items(self: "CDict[_T, _U]") -> CIterable[Tuple[_T, _U]]:
        return CIterable(super().items())

    # built-in

    def all_keys(self: "CDict[Any, Any]") -> bool:
        return self.keys().all()

    def all_values(self: "CDict[Any, Any]") -> bool:
        return self.values().all()

    def all_items(self: "CDict[Any, Any]") -> bool:
        return self.items().all()

    def any_keys(self: "CDict[Any, Any]") -> bool:
        return self.keys().any()

    def any_values(self: "CDict[Any, Any]") -> bool:
        return self.values().any()

    def any_items(self: "CDict[Any, Any]") -> bool:
        return self.items().any()

    def filter_keys(
        self: "CDict[_T, _U]", func: Callable[[_T], bool],
    ) -> "CDict[_T, _U]":
        return self.items().filter(filter_keys_helper(func)).dict()

    def filter_values(
        self: "CDict[_T, _U]", func: Callable[[_U], bool],
    ) -> "CDict[_T, _U]":
        return self.items().filter(filter_values_helper(func)).dict()

    def filter_items(
        self: "CDict[_T, _U]", func: Callable[[_T, _U], bool],
    ) -> "CDict[_T, _U]":
        return self.items().filter(filter_items_helper(func)).dict()

    def frozenset_keys(self: "CDict[_T, Any]") -> "CFrozenSet[_T]":
        return self.keys().frozenset()

    def frozenset_values(self: "CDict[_T, Any]") -> "CFrozenSet[_U]":
        return self.values().frozenset()

    def frozenset_items(self: "CDict[_T, Any]") -> "CFrozenSet[Tuple[_T, _U]]":
        return self.items().frozenset()

    def list_keys(self: "CDict[_T, Any]") -> "CList[_T]":
        return self.keys().list()

    def list_values(self: "CDict[Any, _U]") -> "CList[_U]":
        return self.values().list()

    def list_items(self: "CDict[_T, _U]") -> "CList[Tuple[_T, _U]]":
        return self.items().list()

    def map_keys(
        self: "CDict[_T, _U]", func: Callable[[_T], _V],
    ) -> "CDict[_V, _U]":
        return self.items().map(map_keys_helper(func)).dict()

    def map_values(
        self: "CDict[_T, _U]", func: Callable[[_U], _V],
    ) -> "CDict[_T, _V]":
        return self.items().map(map_values_helper(func)).dict()

    def map_items(
        self: "CDict[_T, _U]", func: Callable[[_T, _U], Tuple[_V, _W]],
    ) -> "CDict[_V, _W]":
        return self.items().map(map_items_helper(func)).dict()

    def max_keys(
        self: "CDict[_T, _U]",
        *,
        key: MAX_MIN_KEY_ANNOTATION = MAX_MIN_KEY_DEFAULT,
        default: Union[_T, Sentinel] = sentinel,
    ) -> _T:
        return self.keys().max(key=key, default=default)

    def max_values(
        self: "CDict[_T, _U]",
        *,
        key: MAX_MIN_KEY_ANNOTATION = MAX_MIN_KEY_DEFAULT,
        default: Union[_U, Sentinel] = sentinel,
    ) -> _U:
        return self.values().max(key=key, default=default)

    def max_items(
        self: "CDict[_T, _U]",
        *,
        key: MAX_MIN_KEY_ANNOTATION = MAX_MIN_KEY_DEFAULT,
        default: Union[_T, Sentinel] = sentinel,
    ) -> _T:
        _, kwargs = drop_sentinel(key=key, default=default)
        return max(self.items(), **kwargs)

    def set_keys(self: "CDict[_T, _U]") -> "CSet[_T]":
        return self.keys().set()

    def set_values(self: "CDict[_T, _U]") -> "CSet[_U]":
        return self.values().set()

    def set_items(self: "CDict[_T, _U]") -> "CSet[Tuple[_T, _U]]":
        return self.items().set()
