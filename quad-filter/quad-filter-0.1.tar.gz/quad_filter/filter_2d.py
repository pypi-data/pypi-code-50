"""A filter function for 2D domains

Given a rectangle (x0, y0, x1, y1), a filter function and a cell size,
quickly find the cell size-sized squares for which the filter function
returns True.

This is done by bisecting the rectangle into squares repeatedly, and it
is meant to be useful in cases where we only have a function indicates
whether or not an area contain the things we're looking for.

This works for intensive variables.
"""

import math
from typing import Callable, Generator, Tuple


# This is an upright rectangle: (x0, y0, x1, y1)
Box = Tuple[float, float, float, float]


def filter_rectangle(
        filter_func: Callable[[Box], bool],
        rectangle: Box,
        cell_size: float) -> Generator[Box, None, None]:
    """Given a rectangle, return a stream of small squares from the
    rectangle for which filter_func returns True

    :param filter_func: a filter function
    :param rectangle: the rectangle (x0, y0, x1, y1)
    :param cell_size: size of the tiles to be returned
    :return: a stream of squares (x, y, x+cell_size, y+cell_size)
        for which filter_func(x, y, x+step, y+step) == True

    """
    x0, y0, x1, y1 = rectangle

    if not (x0 < x1 and y0 < y1):
        raise ValueError(
            f"Incorrect rectangle specification.  "
            f"Expected x0 < x1 and y0 < y1, "
            f"got x0={x0} x1={x1} y0={y0} y1={y1}"
        )
    elif cell_size <= 0:
        raise ValueError(
            f"Expected cell size > 0, "
            f"got cell size={cell_size}")

    max_side_length = max(x1 - x0, y1 - y0)
    nb_cells_in_side = max_side_length / cell_size

    tree_depth = math.ceil(
        math.log2(nb_cells_in_side)
    )

    square_size = cell_size * 2**tree_depth

    yield from _filter_square(filter_func, x0, y0, square_size, tree_depth)


def _filter_square(
        filter_func,
        x0: float, y0: float,
        side_length: float, tree_depth: int):

    if filter_func(x0, y0, x0 + side_length, y0 + side_length):
        if tree_depth <= 1:
            # The filter is true and this is the smallest square,
            # return it.
            yield x0, y0, x0 + side_length, y0 + side_length
        else:
            # This is not the smallest square yet, cut it in 4 smaller
            # squares and test those.
            half_length = side_length / 2
            for step_i in range(2):
                small_x = x0 + step_i * half_length
                for step_j in range(2):
                    small_y = y0 + step_j * half_length
                    yield from _filter_square(
                        filter_func, small_x, small_y,
                        half_length, tree_depth-1)
