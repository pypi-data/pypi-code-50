#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Console script for pykeymapper."""
import click
import sys

from pykeymapper import run_mapper
from pykeymapper import premade


@click.group()
def main(args=None):
    """
    PyKeyMapper - A tool to customise your keyboard

    """
    return 0


@main.command()
def backslash2shift(args=None):
    """
    Make backslash shift when pressed with another key

    """
    run_mapper(premade.BackSlash2Shift)
    return 0


@main.command()
def forwardslash2shift(args=None):
    """
    Make forward slash shift when pressed with another key

    """
    run_mapper(premade.ForwardSlash2Shift)
    return 0


@main.command()
def alt_brackets(args=None):
    """
    Turn alt key into "Bracket Button"

    """
    run_mapper(premade.AltBrackets)
    return 0


@main.command()
def special_space(args=None):
    """
    Turn space into "Special Character key"

    """
    run_mapper(premade.SpecialSpace)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
