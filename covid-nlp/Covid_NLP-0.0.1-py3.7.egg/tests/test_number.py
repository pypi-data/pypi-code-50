import sys
import pytest
from typing import Dict, List
from covid_nlp import number


def test_get_country():
    country = number.get_unique_country()

    assert isinstance(country, List) # error if false
    assert len(country) > 0


def test_get_confirmed_country():
    country = number.get_confirmed_country()

    assert isinstance(country, Dict)

