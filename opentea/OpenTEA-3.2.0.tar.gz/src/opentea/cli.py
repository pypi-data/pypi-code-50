#!/usr/bin/env python
"""
cli.py

Command line interface for tools in pyavbp
"""

import click

from opentea.noob.check_schema import (
    nob_check_schema,
    read_serialized_data)

@click.command()
@click.argument("schema_f")
# @click.option(
#     "--schema_f",
#     "-f",
#     type=str,
#     multiple=False,
#     help="Files to join")
def test_schema(schema_f):
    """Test a yaml file for schema."""
    schema = read_serialized_data(schema_f)
    nob_check_schema(schema)
    print("** Congratulations! **")
    print(schema_f + " SCHEMA structure is valid\nfor opentea requirements.")
