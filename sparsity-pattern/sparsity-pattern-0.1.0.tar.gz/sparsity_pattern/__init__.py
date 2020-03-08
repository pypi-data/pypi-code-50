from itertools import combinations
from typing import List


def get(sp: str, *args, **kwargs) -> List[List[int]]:
    if sp in ("diag"):
        arr = diag(*args, **kwargs)
    elif sp in ("dense"):
        if (len(args) + len(kwargs)) == 1:
            arr = dense_quadratic(*args, **kwargs)
        else:
            arr = dense_pythonic(*args, **kwargs)
    elif sp in ("nodiag"):
        if (len(args) + len(kwargs)) == 1:
            arr = nodiag_quadratic(*args, **kwargs)
        else:
            arr = nodiag_pythonic(*args, **kwargs)
    elif sp in ("block"):
        arr = blockflex(*args, **kwargs)
    elif sp in ("circle"):
        arr = circledet(*args, **kwargs)
    # remove duplicates
    arr = list(set(arr))
    # sort by row, col indices
    arr.sort(key=lambda x: (x[0], x[1]))
    return arr


def diag(n: int) -> List[List[int]]:
    """Diagonal Matrix. Req.: Quadratic Matrix"""
    arr = [(i, i) for i in range(n)]
    return arr


def dense_quadratic(n: int) -> List[List[int]]:
    """A Dense matrix. Quadratic"""
    arr1 = list(combinations(range(n), 2))  # all combinations (only triag)
    arr2 = [(j, i) for i, j in arr1]  # copy flipped indices
    arr3 = [(i, i) for i in range(n)]
    return arr1 + arr2 + arr3


def dense_pythonic(r: int, c: int = None) -> List[List[int]]:
    """A Dense matrix"""
    if c is None:
        c = r
    arr = [(i, j) for j in range(c) for i in range(r)]
    return arr


def nodiag_quadratic(n: int) -> List[List[int]]:
    """Almost Dense matrix without diagonal elements. Quadratic"""
    arr1 = list(combinations(range(n), 2))  # all combinations (only triag)
    arr2 = [(j, i) for i, j in arr1]  # copy flipped indices
    return arr1 + arr2


def nodiag_pythonic(r: int, c: int = None) -> List[List[int]]:
    """Almost Dense matrix without diagonal elements"""
    if c is None:
        c = r
    arr = [(i, j) for j in range(c) for i in range(r) if i != j]
    return arr


def blockflex(n: int, block_sizes=List[int]) -> List[List[int]]:
    """Block Diagonal Matrix with different sized blocks"""
    if isinstance(block_sizes, int):
        block_sizes = [block_sizes]
    arr = []
    flag = True
    i = 0
    n_blocks = len(block_sizes)
    idx_block_end = 0
    # loop over blocks
    while flag:
        # get the start index of the next block
        h = i % n_blocks
        idx_block_start = idx_block_end
        idx_block_end = min(n, idx_block_start + block_sizes[h])
        indices = range(idx_block_start, idx_block_end)
        # enumerate all index pairs
        arr.extend([(j, k) for k in indices for j in indices])
        # set flag to false
        if idx_block_end >= n:
            flag = False
        i += 1
    return arr


def circledet(n: int, offsets: List[int] = [1]) -> List[List[int]]:
    """"""
    arr = []
    off = set(offsets)
    off = [k for k in off if k < n]
    for k in off:
        arr.extend(
            [(i, (i - k) if (i - k) >= 0 else (n + i - k)) for i in range(n)])
    return arr
