import math
from unittest import mock

import pytest

from running_stats.running_stats import RunningStats


@pytest.fixture
def rs_empty():
    return RunningStats()


@pytest.fixture
def rs_one_value(rs_empty):
    rs_empty.push(4.0)
    return rs_empty


@pytest.fixture
def rs_two_values(rs_one_value):
    rs_one_value.push(6.0)
    return rs_one_value


@pytest.fixture
def rs_three_values(rs_two_values):
    rs_two_values.push(2.0)
    return rs_two_values


@pytest.fixture
def value_list():
    values = [2.0, 1.0, -3.0, -1.0]
    return values


def test_initial_values(rs_empty):
    assert rs_empty.n == 0
    assert rs_empty.mean() == 0.0
    assert rs_empty.variance() == 0.0
    assert rs_empty.standard_deviation() == 0.0


@pytest.mark.parametrize("var", [0.0, 2.0, 4.0, 5.0])
def test_standard_deviation(var):
    rs = RunningStats()
    rs.variance = mock.Mock()
    rs.variance.return_value = var
    assert rs.standard_deviation() == math.sqrt(var)


def test_n_one_value(rs_one_value):
    assert rs_one_value.n == 1


def test_mean_one_value(rs_one_value):
    assert rs_one_value.mean() == 4.0


def test_variance_one_value(rs_one_value):
    assert rs_one_value.variance() == 0.0


def test_n_two_values(rs_two_values):
    assert rs_two_values.n == 2


def test_mean_two_values(rs_two_values):
    assert rs_two_values.mean() == 5.0


def test_variance_two_values(rs_two_values):
    assert rs_two_values.variance() == 2.0


def test_mean_three_values(rs_three_values):
    assert rs_three_values.n == 3
    assert rs_three_values.mean() == 4.0


def test_variance_three_values(rs_three_values):
    assert rs_three_values.variance() == 4.0


def test_push_iter_with_list(value_list):
    rs = RunningStats()
    rs.push_iter(value_list)
    assert rs.n == len(value_list)
    assert rs.mean() == -0.25
    assert rs.variance() == 4.916666666666667


def test_add_two_running_stats():
    a = RunningStats()
    a.n = 3
    a.M1 = 2.0
    a.M2 = 7.8

    b = RunningStats()
    b.n = 6
    b.M1 = 6.0
    b.M2 = 3.4

    c = a + b
    assert c.n == a.n + b.n
    assert c.M1 == 42.0/9
    assert c.M2 == 43.2


def test_iadd_two_running_stats():
    a = RunningStats()
    a.n = 3
    a.M1 = 2.0
    a.M2 = 0.8

    b = RunningStats()
    b.n = 8
    b.M1 = -3.0
    b.M2 = 4.4

    a += b
    assert a.n == 11
    assert a.M1 == -18.0/11
    assert a.M2 == 5.2 + 25.0 * 24 / 11
