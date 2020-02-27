import time
import math

DEFAULT_FLOAT_DIFF = 0.00000000000001


def float_equal(a, b, diff=DEFAULT_FLOAT_DIFF):
    return math.fabs(a - b) < diff


def equal(a, b):
    return a == b


def location_equal(a, b, diff=DEFAULT_FLOAT_DIFF):
    if not float_equal(a.x, b.x, diff) or not float_equal(a.y, b.y, diff) or not float_equal(a.z, b.z, diff):
        return False

    return True


def assert_float_equal(a, b, diff=DEFAULT_FLOAT_DIFF):
    if not float_equal(a, b, diff):
        raise AssertionError(f'{a} does not equal {b}')

    return True


def assert_equal(a, b):
    if a != b:
        raise AssertionError(f'{a} does not equal {b}')

    return True


def assert_not_equal(a, b):
    if a == b:
        raise AssertionError(f'{a} does not equal {b}')

    return True


def assert_list_items_equal(list_a, list_b, recursive=True, is_equal=equal):
    if len(list_a) != len(list_b):
        raise AssertionError(f'list {list_a} does not equal {list_b}')

    for i in range(0, len(list_a)):
        if isinstance(list_a[i], list) and isinstance(list_b[i], list) and recursive:
            assert_list_items_equal(list_a[i], list_b[i], recursive=True, is_equal=is_equal)
        else:
            if not is_equal(list_a[i], list_b[i]):
                raise AssertionError(f'list {list_a} does not equal {list_b}')

    return True


def assert_vector_equal(a, b, diff=DEFAULT_FLOAT_DIFF):
    if not float_equal(a.x(), b.x(), diff) or not float_equal(a.y(), b.y(), diff) or not float_equal(a.z(), b.z(), diff):
        raise AssertionError(f'vector {a} does not equal {b}')

    return True


def assert_location_equal(a, b, diff=DEFAULT_FLOAT_DIFF):
    if not float_equal(a.x, b.x, diff) or not float_equal(a.y, b.y, diff) or not float_equal(a.z, b.z, diff):
        raise AssertionError(f'vector {a} does not equal {b}')

    return True


def assert_config_equal(a, b):
    if not float_equal(a.column, b.column) or not float_equal(a.link1, b.link1) or not float_equal(a.link2, b.link2) \
       or not float_equal(a.link3, b.link3):
        raise AssertionError(f'config {a} does not equal {b}')


def wait(delay: float=0.02):
    time.sleep(delay)