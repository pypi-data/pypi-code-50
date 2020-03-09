#!/usr/bin/env python

"""Tests for `trial_project` package."""

from trial_project.calculator import *
import pytest
import unittest

from click.testing import CliRunner

from trial_project import trial_project
from trial_project import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'trial_project.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_add():
    # Arrange
    calculator = Calculator()

    # Act
    result = calculator.add(2, 3)

    # Assert
    assert result == 5


def test_add_weird_stuff():
    calculator = Calculator()

    with pytest.raises(CalculatorError):
        result = calculator.add("two", 3)


def test_add_weirder_stuff():
    calculator = Calculator()

    with pytest.raises(CalculatorError) as context:
        result = calculator.add("two", "three")

    # assert str(context.value) == "wronge"


def test_subtract():
    calculator = Calculator()

    result = calculator.subtract(9, 3)

    assert result == 6


def test_multiply():
    calculator = Calculator()

    result = calculator.multiply(9, 3)

    assert result == 27


def test_divide():
    calculator = Calculator()

    result = calculator.divide(9, 3)

    assert result == 3


def test_divide_by_zero():
    calculator = Calculator()

    with pytest.raises(CalculatorError):
        result = calculator.divide(9, 0)
