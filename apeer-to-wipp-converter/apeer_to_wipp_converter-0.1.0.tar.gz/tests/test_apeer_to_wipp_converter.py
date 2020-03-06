#!/usr/bin/env python

"""Tests for `apeer_to_wipp_converter` package."""


import unittest
from click.testing import CliRunner

from apeer_to_wipp_converter import apeer_to_wipp_converter
from apeer_to_wipp_converter import cli


class TestApeer_to_wipp_converter(unittest.TestCase):
    """Tests for `apeer_to_wipp_converter` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'apeer_to_wipp_converter.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
